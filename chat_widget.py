from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QScrollArea, QFrame, QSizePolicy, QApplication, QMenu
)
from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtGui import QFont, QColor, QPalette


class ChatBubble(QFrame):
    """
    Widget bóng chat đơn lẻ với style giống Messenger.
    """
    
    def __init__(self, message, sender, timestamp=None, message_id=None, parent=None):
        """
        Khởi tạo ChatBubble.
        
        Args:
            message (str): Nội dung tin nhắn
            sender (str): 'user' hoặc 'ai'
            timestamp (str, optional): Thời gian gửi
            message_id (int, optional): ID tin nhắn trong database
            parent: Parent widget
        """
        super().__init__(parent)
        
        self.message = message
        self.sender = sender
        self.timestamp = timestamp
        self.message_id = message_id
        
        self.setup_ui()
    
    def setup_ui(self):
        """
        Thiết lập giao diện cho bóng chat.
        """
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)
        
        # Tạo label chứa tin nhắn
        self.bubble = QLabel(self.message)
        self.bubble.setWordWrap(True)
        self.bubble.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.bubble.setMaximumWidth(400)
        self.bubble.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        
        # Font
        font = QFont()
        font.setPointSize(10)
        self.bubble.setFont(font)
        
        # Style dựa trên sender
        if self.sender == 'user':
            # User message: Bên phải, màu xanh
            self.bubble.setStyleSheet("""
                QLabel {
                    background-color: #0084FF;
                    color: white;
                    border-radius: 18px;
                    padding: 10px 15px;
                }
            """)
            layout.addStretch()
            layout.addWidget(self.bubble)
        else:
            # AI message: Bên trái, màu xám
            self.bubble.setStyleSheet("""
                QLabel {
                    background-color: #E4E6EB;
                    color: #050505;
                    border-radius: 18px;
                    padding: 10px 15px;
                }
            """)
            layout.addWidget(self.bubble)
            layout.addStretch()
        
        # Thêm timestamp nếu có
        if self.timestamp:
            try:
                from datetime import datetime
                dt = datetime.fromisoformat(self.timestamp)
                time_str = dt.strftime("%H:%M")
                
                time_label = QLabel(time_str)
                time_label.setStyleSheet("color: #65676B; font-size: 9px;")
                
                if self.sender == 'user':
                    layout.insertWidget(1, time_label)
                else:
                    layout.addWidget(time_label)
            except:
                pass
    
    def contextMenuEvent(self, event):
        """
        Hiển thị menu chuột phải.
        """
        menu = QMenu(self)
        
        copy_action = menu.addAction("📋 Copy")
        copy_action.triggered.connect(self.copy_message)
        
        menu.exec(event.globalPos())
    
    def copy_message(self):
        """
        Copy nội dung tin nhắn.
        """
        clipboard = QApplication.clipboard()
        clipboard.setText(self.message)


class ChatWidget(QScrollArea):
    """
    Widget chat với style giống Messenger.
    Hiển thị tin nhắn dạng bóng chat, user bên phải, AI bên trái.
    """
    
    # Signal để thông báo khi có tin nhắn mới
    message_added = Signal(str, str)  # sender, message
    
    def __init__(self, parent=None):
        """
        Khởi tạo ChatWidget.
        """
        super().__init__(parent)
        
        self.bubbles = []  # Danh sách các ChatBubble
        
        self.setup_ui()
    
    def setup_ui(self):
        """
        Thiết lập giao diện chat.
        """
        # Container widget
        self.container = QWidget()
        self.container_layout = QVBoxLayout(self.container)
        self.container_layout.setSpacing(2)
        self.container_layout.setContentsMargins(5, 5, 5, 5)
        
        # Thêm stretch ở đầu để tin nhắn đẩy xuống dưới
        self.container_layout.addStretch()
        
        # Setup scroll area
        self.setWidget(self.container)
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        
        # Style cho scroll area
        self.setStyleSheet("""
            QScrollArea {
                background-color: white;
                border: 1px solid #E4E6EB;
                border-radius: 8px;
            }
            QScrollBar:vertical {
                background: #F0F2F5;
                width: 8px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical {
                background: #BCC0C4;
                border-radius: 4px;
                min-height: 20px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)
    
    def add_message(self, message, sender, timestamp=None, message_id=None):
        """
        Thêm tin nhắn mới vào chat.
        
        Args:
            message (str): Nội dung tin nhắn
            sender (str): 'user' hoặc 'ai'
            timestamp (str, optional): Thời gian gửi
            message_id (int, optional): ID tin nhắn
        """
        bubble = ChatBubble(message, sender, timestamp, message_id, self.container)
        self.bubbles.append(bubble)
        self.container_layout.addWidget(bubble)
        
        # Scroll xuống cuối
        self.scroll_to_bottom()
        
        # Emit signal
        self.message_added.emit(sender, message)
    
    def add_user_message(self, message, timestamp=None, message_id=None):
        """
        Thêm tin nhắn của user.
        """
        self.add_message(message, 'user', timestamp, message_id)
    
    def add_ai_message(self, message, timestamp=None, message_id=None):
        """
        Thêm tin nhắn của AI.
        """
        self.add_message(message, 'ai', timestamp, message_id)
    
    def scroll_to_bottom(self):
        """
        Cuộn xuống cuối chat.
        """
        # Đợi layout cập nhật
        QApplication.processEvents()
        scrollbar = self.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
    
    def clear_chat(self):
        """
        Xóa tất cả tin nhắn.
        """
        for bubble in self.bubbles:
            bubble.deleteLater()
        self.bubbles.clear()
    
    def load_history(self, messages):
        """
        Load lịch sử chat.
        
        Args:
            messages (list): Danh sách tin nhắn từ database
                [{'sender': 'user'/'ai', 'message': str, 'timestamp': str, 'id': int}, ...]
        """
        self.clear_chat()
        
        for msg in messages:
            self.add_message(
                msg.get('message', ''),
                msg.get('sender', 'ai'),
                msg.get('timestamp'),
                msg.get('id')
            )
    
    def get_all_messages(self):
        """
        Lấy tất cả tin nhắn dạng text.
        
        Returns:
            list: Danh sách tuple (sender, message)
        """
        return [(bubble.sender, bubble.message) for bubble in self.bubbles]
    
    def copy_all_chat(self):
        """
        Copy tất cả nội dung chat.
        """
        all_text = []
        for bubble in self.bubbles:
            prefix = "👤 Bạn" if bubble.sender == 'user' else "🤖 AI"
            all_text.append(f"{prefix}: {bubble.message}")
        
        if all_text:
            clipboard = QApplication.clipboard()
            clipboard.setText("\n".join(all_text))
            return len(all_text)
        return 0


# Demo
if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)
    
    # Tạo window test
    window = QWidget()
    window.setWindowTitle("Chat Widget Demo")
    window.resize(500, 600)
    
    layout = QVBoxLayout(window)
    
    # Tạo chat widget
    chat = ChatWidget()
    layout.addWidget(chat)
    
    # Thêm một số tin nhắn test
    chat.add_user_message("Xin chào!")
    chat.add_ai_message("Chào bạn! Tôi có thể giúp gì cho bạn?")
    chat.add_user_message("Tạo lịch họp 10h sáng mai tại phòng 101")
    chat.add_ai_message("✅ Đã tạo sự kiện: Lịch họp\n📅 Thời gian: 05/12/2025 10:00\n📍 Địa điểm: phòng 101")
    chat.add_user_message("Cảm ơn!")
    chat.add_ai_message("Không có gì! Bạn có cần gì khác không?")
    
    window.show()
    sys.exit(app.exec())

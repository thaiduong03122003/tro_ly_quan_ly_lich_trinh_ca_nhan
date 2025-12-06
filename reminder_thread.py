import threading
from datetime import datetime
from PySide6.QtCore import QThread, Signal
from database_manager import DatabaseManager

class ReminderThread(QThread):
    """
    Luồng ngầm để kiểm tra định kỳ các sự kiện cần nhắc nhở.
    
    Kế thừa từ QThread và chạy độc lập với luồng giao diện chính.
    Sử dụng threading.Event để có thể dừng ngay lập tức khi đóng ứng dụng.
    """
    
    # Signal để gửi dữ liệu nhắc nhở về luồng chính
    reminder_signal = Signal(list)
    
    def __init__(self, parent=None):
        """
        Khởi tạo ReminderThread.
        
        Args:
            parent: Parent object (optional)
        """
        super().__init__(parent)
        self._running = True
        self._stop_event = threading.Event()  # Event để interrupt sleep ngay lập tức
        self.check_interval = 60  # Kiểm tra mỗi 60 giây
        
    
    def run(self):
        """
        Vòng lặp chính của luồng - chạy liên tục để kiểm tra reminders.
        Sử dụng Event.wait() thay vì time.sleep() để có thể dừng ngay lập tức.
        """
        while self._running and not self._stop_event.is_set():
            try:
                # Lấy thời điểm hiện tại
                current_time = datetime.now()
                current_time_iso = current_time.isoformat()
                
                # Khởi tạo DatabaseManager (cục bộ cho luồng này)
                db = DatabaseManager()
                
                # Lấy danh sách sự kiện cần nhắc nhở
                reminders = db.get_reminders_due(current_time_iso)
                
                # Nếu có reminders, gửi signal về luồng chính
                if reminders:
                    # Phát tín hiệu về luồng chính
                    self.reminder_signal.emit(reminders)
                    
                    # Đánh dấu các reminders đã được thông báo
                    for reminder in reminders:
                        db.mark_as_notified(reminder['id'])
                
                # Đóng database connection
                db.close()
                
            except Exception as e:
                pass  # Silent error handling
            
            # Sử dụng Event.wait() thay vì time.sleep()
            # Event.wait(timeout) sẽ:
            # - Trả về True ngay lập tức nếu event được set (stop() được gọi)
            # - Trả về False sau timeout giây nếu event chưa được set
            # Điều này cho phép thread thoát ngay lập tức khi stop() được gọi
            if self._running:
                self._stop_event.wait(timeout=self.check_interval)
        
    
    def stop(self):
        """
        Dừng luồng NGAY LẬP TỨC một cách an toàn.
        Sử dụng Event.set() để interrupt sleep ngay lập tức.
        """
        self._running = False
        self._stop_event.set()  # Interrupt sleep ngay lập tức!
        
        # Đợi tối đa 2 giây để thread kết thúc
        if not self.wait(2000):  # 2000ms = 2 giây
            self.terminate()
    
    def set_check_interval(self, seconds):
        """
        Thiết lập khoảng thời gian kiểm tra.
        
        Args:
            seconds (int): Số giây giữa các lần kiểm tra
        """
        self.check_interval = seconds

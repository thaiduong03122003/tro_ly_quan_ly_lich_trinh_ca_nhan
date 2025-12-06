import sys
import json
from datetime import datetime, timedelta

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QMessageBox,
    QSystemTrayIcon, QStyle, QListWidgetItem, QTableWidgetItem,
    QMenu, QFileDialog
)
from PySide6.QtCore import QDateTime, Qt
from PySide6.QtGui import QIcon, QClipboard, QAction

from ui_mainwindow import Ui_btn_send
from ui_event_form import Ui_Dialog
from database_manager import DatabaseManager
from nlp_pipeline import parse_user_input
from reminder_thread import ReminderThread
from chat_widget import ChatWidget

try:
    import winsound
    HAS_WINSOUND = True
except ImportError:
    HAS_WINSOUND = False


class EventDialog(QDialog):
    """Dialog for adding/editing events manually."""
    
    def __init__(self, parent=None, mode="add", event_data=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.mode = mode
        self.event_id = None
        
        if mode == "add":
            self.setWindowTitle("Thêm Sự Kiện Mới")
            self.ui.lb_title_event.setText("Thêm Sự Kiện")
        else:
            self.setWindowTitle("Sửa Sự Kiện")
            self.ui.lb_title_event.setText("Sửa Sự Kiện")
        
        if event_data:
            self.load_data_to_form(event_data)
    
    def load_data_to_form(self, data):
        """Load event data into form fields."""
        self.event_id = data.get('id')
        
        event_name = data.get('event_name') or data.get('event', '')
        self.ui.txt_event.setText(event_name)
        
        location = data.get('location', '')
        self.ui.txt_location.setText(location)
        
        reminder_minutes = data.get('reminder_minutes', 0) or 0
        self.ui.sb_reminder.setValue(reminder_minutes)
        
        start_time_str = data.get('start_time')
        if start_time_str:
            try:
                dt = datetime.fromisoformat(start_time_str)
                qdt = QDateTime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
                self.ui.dt_start.setDateTime(qdt)
            except Exception as e:
                print(f"Error converting time: {e}")
    
    def get_data(self):
        """Get form data as dictionary."""
        event_name = self.ui.txt_event.text().strip()
        location = self.ui.txt_location.text().strip()
        reminder_minutes = self.ui.sb_reminder.value()
        qdt = self.ui.dt_start.dateTime()
        start_time_str = qdt.toPython().isoformat()
        
        return {
            "event": event_name,
            "location": location,
            "start_time": start_time_str,
            "reminder_minutes": reminder_minutes
        }


class MainWindow(QMainWindow):
    """Main application window."""
    
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_btn_send()
        self.ui.setupUi(self)
        self.setWindowTitle("Trợ Lý Quản Lý Lịch Trình Cá Nhân")
        
        self.db = DatabaseManager()
        
        self.reminder_thread = ReminderThread()
        self.reminder_thread.start()
        
        self.setup_tray_icon()
        self.setup_connections()
        self.setup_table_columns()
        self.load_events_by_date()
        self.setup_chat_widget()
        self.load_chat_history()
    
    def setup_table_columns(self):
        """Setup table column widths."""
        # Events table - 5 columns
        self.ui.table_events.setColumnWidth(0, 40)   # ID
        self.ui.table_events.setColumnWidth(1, 200)  # Event name
        self.ui.table_events.setColumnWidth(2, 80)   # Time
        self.ui.table_events.setColumnWidth(3, 120)  # Location
        self.ui.table_events.setColumnWidth(4, 80)   # Reminder
        
        # Reminders table - 6 columns
        self.ui.table_reminders.setColumnWidth(0, 40)   # ID
        self.ui.table_reminders.setColumnWidth(1, 180)  # Event name
        self.ui.table_reminders.setColumnWidth(2, 100)  # Event time
        self.ui.table_reminders.setColumnWidth(3, 80)   # Reminder before
        self.ui.table_reminders.setColumnWidth(4, 100)  # Reminder time
        self.ui.table_reminders.setColumnWidth(5, 100)  # Status
    
    def setup_chat_widget(self):
        """Replace QListWidget with ChatWidget."""
        self.chat_widget = ChatWidget()
        layout = self.ui.verticalLayout_2
        layout.removeWidget(self.ui.list_chat)
        self.ui.list_chat.hide()
        self.ui.list_chat.deleteLater()
        layout.addWidget(self.chat_widget)
        self.chat_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.chat_widget.customContextMenuRequested.connect(self.show_chat_context_menu)
    
    def load_chat_history(self):
        """Load chat history from database."""
        try:
            messages = self.db.get_chat_history(limit=50)
            self.chat_widget.load_history(messages)
        except Exception as e:
            print(f"Error loading chat history: {e}")
    
    def show_chat_context_menu(self, position):
        """Show context menu for chat."""
        menu = QMenu(self)
        copy_all_action = menu.addAction("Copy tat ca hoi thoai")
        copy_all_action.triggered.connect(self.copy_all_chat)
        menu.addSeparator()
        clear_action = menu.addAction("Xoa tat ca hoi thoai")
        clear_action.triggered.connect(self.clear_all_chat)
        menu.exec(self.chat_widget.mapToGlobal(position))
    
    def copy_all_chat(self):
        """Copy all chat to clipboard."""
        count = self.chat_widget.copy_all_chat()
        if count > 0:
            QMessageBox.information(self, "Thanh cong", f"Da copy {count} tin nhan vao clipboard!")
    
    def clear_all_chat(self):
        """Clear all chat messages."""
        reply = QMessageBox.question(
            self, "Xac nhan",
            "Ban co chac muon xoa tat ca hoi thoai?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.chat_widget.clear_chat()
            self.db.clear_chat_history()
    
    def setup_tray_icon(self):
        """Setup system tray icon for notifications."""
        self.tray_icon = QSystemTrayIcon(self)
        icon = self.style().standardIcon(QStyle.SP_ComputerIcon)
        self.tray_icon.setIcon(icon)
        self.tray_icon.setToolTip("Quan Ly Lich Thong Minh")
        self.tray_icon.show()
    
    def setup_connections(self):
        """Connect all signals to slots."""
        # Chat
        self.ui.btn_send_2.clicked.connect(self.handle_chat)
        self.ui.txt_input.returnPressed.connect(self.handle_chat)
        
        # Calendar
        self.ui.calendar_widget.selectionChanged.connect(self.on_calendar_selection_changed)
        
        # CRUD
        self.ui.btn_add.clicked.connect(self.open_add_dialog)
        self.ui.btn_edit.clicked.connect(self.open_edit_dialog)
        self.ui.btn_delete.clicked.connect(self.delete_event)
        
        # Search and Filter
        self.ui.btn_search.clicked.connect(self.search_events)
        self.ui.txt_search.returnPressed.connect(self.search_events)
        self.ui.cmb_filter.currentIndexChanged.connect(self.on_filter_changed)
        
        # Export JSON
        self.ui.btn_export.clicked.connect(self.export_to_json)
        
        # Reminder history
        self.ui.btn_refresh_reminders.clicked.connect(self.load_reminder_history)
        self.ui.cmb_reminder_filter.currentIndexChanged.connect(self.load_reminder_history)
        
        # Reminder thread
        self.reminder_thread.reminder_signal.connect(self.show_reminder_notification)
        
        # Tab change
        self.ui.tabWidget.currentChanged.connect(self.on_tab_changed)
    
    def on_calendar_selection_changed(self):
        """Handle calendar date selection change."""
        # Reset filter to "Ngay" when calendar selection changes
        self.ui.cmb_filter.setCurrentIndex(0)
        self.load_events_by_date()
    
    def on_filter_changed(self, index):
        """Handle filter combobox change."""
        self.load_events_by_filter()
    
    def load_events_by_filter(self):
        """Load events based on current filter selection."""
        filter_type = self.ui.cmb_filter.currentText()
        selected_date = self.ui.calendar_widget.selectedDate().toPython()
        
        if filter_type == "Ngay":
            start_iso = datetime(selected_date.year, selected_date.month, selected_date.day, 0, 0, 0).isoformat()
            end_iso = datetime(selected_date.year, selected_date.month, selected_date.day, 23, 59, 59).isoformat()
        elif filter_type == "Tuan":
            # Get start of week (Monday)
            start_of_week = selected_date - timedelta(days=selected_date.weekday())
            end_of_week = start_of_week + timedelta(days=6)
            start_iso = datetime(start_of_week.year, start_of_week.month, start_of_week.day, 0, 0, 0).isoformat()
            end_iso = datetime(end_of_week.year, end_of_week.month, end_of_week.day, 23, 59, 59).isoformat()
        elif filter_type == "Thang":
            # Get start and end of month
            start_of_month = selected_date.replace(day=1)
            if selected_date.month == 12:
                end_of_month = selected_date.replace(year=selected_date.year + 1, month=1, day=1) - timedelta(days=1)
            else:
                end_of_month = selected_date.replace(month=selected_date.month + 1, day=1) - timedelta(days=1)
            start_iso = datetime(start_of_month.year, start_of_month.month, start_of_month.day, 0, 0, 0).isoformat()
            end_iso = datetime(end_of_month.year, end_of_month.month, end_of_month.day, 23, 59, 59).isoformat()
        else:  # Tat ca
            events = self.db.get_all_events()
            self.populate_events_table(events)
            return
        
        events = self.db.get_events_for_range(start_iso, end_iso)
        self.populate_events_table(events)
    
    def load_events_by_date(self):
        """Load events for selected date."""
        selected_date = self.ui.calendar_widget.selectedDate().toPython()
        start_iso = datetime(selected_date.year, selected_date.month, selected_date.day, 0, 0, 0).isoformat()
        end_iso = datetime(selected_date.year, selected_date.month, selected_date.day, 23, 59, 59).isoformat()
        
        events = self.db.get_events_for_range(start_iso, end_iso)
        self.populate_events_table(events)
    
    def populate_events_table(self, events):
        """Populate events table with data."""
        self.ui.table_events.setRowCount(0)
        
        for event in events:
            row = self.ui.table_events.rowCount()
            self.ui.table_events.insertRow(row)
            
            # Column 0: ID
            self.ui.table_events.setItem(row, 0, QTableWidgetItem(str(event['id'])))
            
            # Column 1: Event name
            self.ui.table_events.setItem(row, 1, QTableWidgetItem(event['event_name']))
            
            # Column 2: Time
            start_time = event.get('start_time', '')
            if start_time:
                try:
                    dt = datetime.fromisoformat(start_time)
                    time_str = dt.strftime("%d/%m %H:%M")
                except:
                    time_str = start_time
            else:
                time_str = ""
            self.ui.table_events.setItem(row, 2, QTableWidgetItem(time_str))
            
            # Column 3: Location
            self.ui.table_events.setItem(row, 3, QTableWidgetItem(event.get('location', '')))
            
            # Column 4: Reminder
            reminder = event.get('reminder_minutes', 0) or 0
            if reminder > 0:
                if reminder >= 60:
                    reminder_str = f"{reminder // 60}h"
                    if reminder % 60:
                        reminder_str += f"{reminder % 60}p"
                else:
                    reminder_str = f"{reminder}p"
            else:
                reminder_str = "-"
            self.ui.table_events.setItem(row, 4, QTableWidgetItem(reminder_str))
    
    def search_events(self):
        """Search events by name."""
        search_text = self.ui.txt_search.text().strip().lower()
        
        if not search_text:
            self.load_events_by_filter()
            return
        
        # Get all events and filter by name
        all_events = self.db.get_all_events()
        filtered_events = [e for e in all_events if search_text in e['event_name'].lower()]
        
        self.populate_events_table(filtered_events)
    
    def export_to_json(self):
        """Export events to JSON file."""
        # Get events based on current filter
        filter_type = self.ui.cmb_filter.currentText()
        
        if filter_type == "Tat ca":
            events = self.db.get_all_events()
        else:
            self.load_events_by_filter()
            # Get events from table
            events = []
            for row in range(self.ui.table_events.rowCount()):
                event_id = int(self.ui.table_events.item(row, 0).text())
                # Get full event data from database
                all_events = self.db.get_all_events()
                for e in all_events:
                    if e['id'] == event_id:
                        events.append(e)
                        break
        
        if not events:
            QMessageBox.warning(self, "Thong bao", "Khong co su kien nao de xuat!")
            return
        
        # Ask for save location
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Xuat JSON", "", "JSON Files (*.json)"
        )
        
        if not file_path:
            return
        
        if not file_path.endswith('.json'):
            file_path += '.json'
        
        try:
            # Prepare export data
            export_data = {
                "exported_at": datetime.now().isoformat(),
                "total_events": len(events),
                "events": events
            }
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, ensure_ascii=False, indent=2)
            
            QMessageBox.information(self, "Thanh cong", f"Da xuat {len(events)} su kien ra file:\n{file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Loi", f"Khong the xuat file:\n{str(e)}")
    
    def load_reminder_history(self):
        """Load reminder history based on filter."""
        filter_type = self.ui.cmb_reminder_filter.currentText()
        
        all_events = self.db.get_all_events()
        
        # Filter events that have reminders
        events_with_reminders = [e for e in all_events if e.get('reminder_minutes', 0) > 0]
        
        if filter_type == "Da thong bao":
            events_with_reminders = [e for e in events_with_reminders if e.get('is_notified', 0) == 1]
        elif filter_type == "Chua thong bao":
            events_with_reminders = [e for e in events_with_reminders if e.get('is_notified', 0) == 0]
        
        # Populate reminders table
        self.ui.table_reminders.setRowCount(0)
        
        for event in events_with_reminders:
            row = self.ui.table_reminders.rowCount()
            self.ui.table_reminders.insertRow(row)
            
            # Column 0: ID
            self.ui.table_reminders.setItem(row, 0, QTableWidgetItem(str(event['id'])))
            
            # Column 1: Event name
            self.ui.table_reminders.setItem(row, 1, QTableWidgetItem(event['event_name']))
            
            # Column 2: Event time
            start_time = event.get('start_time', '')
            if start_time:
                try:
                    dt = datetime.fromisoformat(start_time)
                    time_str = dt.strftime("%d/%m/%Y %H:%M")
                except:
                    time_str = start_time
            else:
                time_str = ""
            self.ui.table_reminders.setItem(row, 2, QTableWidgetItem(time_str))
            
            # Column 3: Reminder before
            reminder = event.get('reminder_minutes', 0)
            if reminder >= 60:
                reminder_str = f"{reminder // 60} gio"
            else:
                reminder_str = f"{reminder} phut"
            self.ui.table_reminders.setItem(row, 3, QTableWidgetItem(reminder_str))
            
            # Column 4: Reminder time
            reminder_time = event.get('reminder_time', '')
            if reminder_time:
                try:
                    dt = datetime.fromisoformat(reminder_time)
                    time_str = dt.strftime("%d/%m/%Y %H:%M")
                except:
                    time_str = reminder_time
            else:
                time_str = ""
            self.ui.table_reminders.setItem(row, 4, QTableWidgetItem(time_str))
            
            # Column 5: Status
            is_notified = event.get('is_notified', 0)
            status = "Da thong bao" if is_notified else "Chua thong bao"
            self.ui.table_reminders.setItem(row, 5, QTableWidgetItem(status))
    
    def handle_chat(self):
        """Handle NLP input from user."""
        raw_text = self.ui.txt_input.text().strip()
        
        if not raw_text:
            return
        
        self.chat_widget.add_user_message(raw_text)
        self.db.add_chat_message('user', raw_text)
        self.ui.txt_input.clear()
        
        try:
            result = parse_user_input(raw_text)
            
            if "error" in result:
                error_msg = result["error"]
                ai_response = f"Loi: {error_msg}"
                self.chat_widget.add_ai_message(ai_response)
                self.db.add_chat_message('ai', ai_response)
                return
            
            event_id = self.db.add_event(result)
            
            event_name = result.get("event", "Su kien")
            start_time = result.get("start_time", "")
            location = result.get("location", "")
            reminder = result.get("reminder_minutes", 0)
            
            success_msg = f"Đã tạo sự kiện: {event_name}"
            if start_time:
                try:
                    dt = datetime.fromisoformat(start_time)
                    time_formatted = dt.strftime("%d/%m/%Y %H:%M")
                    success_msg += f"\nThời gian: {time_formatted}"
                except:
                    success_msg += f"\nThời gian: {start_time}"
            if location:
                success_msg += f"\nĐịa điểm: {location}"
            if reminder:
                success_msg += f"\nNhắc trước: {reminder} phút"
            
            self.chat_widget.add_ai_message(success_msg)
            self.db.add_chat_message('ai', success_msg, event_id)
            self.load_events_by_date()
            
        except Exception as e:
            error_msg = f"Loi he thong: {str(e)}"
            self.chat_widget.add_ai_message(error_msg)
            self.db.add_chat_message('ai', error_msg)
    
    def open_add_dialog(self):
        """Open dialog to add new event."""
        dialog = EventDialog(self, mode="add")
        
        if dialog.exec() == QDialog.Accepted:
            data = dialog.get_data()
            
            if not data.get("event"):
                QMessageBox.warning(self, "Lỗi", "Vui lòng nhập tên sự kiện!")
                return
            
            # Kiểm tra thời gian quá khứ
            start_time_str = data.get("start_time")
            if start_time_str:
                try:
                    event_time = datetime.fromisoformat(start_time_str)
                    if event_time < datetime.now():
                        reply = QMessageBox.question(
                            self, "Cảnh báo",
                            "Thời gian sự kiện đã ở trong quá khứ!\n\nBạn có chắc muốn thêm sự kiện này?",
                            QMessageBox.Yes | QMessageBox.No,
                            QMessageBox.No
                        )
                        if reply == QMessageBox.No:
                            return
                except Exception as e:
                    print(f"Error parsing time: {e}")
            
            self.db.add_event(data)
            self.load_events_by_filter()
            QMessageBox.information(self, "Thành công", "Đã thêm sự kiện mới!")
    
    def open_edit_dialog(self):
        """Open dialog to edit selected event."""
        selected_row = self.ui.table_events.currentRow()
        
        if selected_row < 0:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn sự kiện cần sửa!")
            return
        
        event_id_item = self.ui.table_events.item(selected_row, 0)
        if not event_id_item:
            QMessageBox.warning(self, "Lỗi", "Không thể lấy ID sự kiện!")
            return
        
        event_id = int(event_id_item.text())
        
        # Get full event data from database
        all_events = self.db.get_all_events()
        event_data = None
        for e in all_events:
            if e['id'] == event_id:
                event_data = e
                break
        
        if not event_data:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy sự kiện!")
            return
        
        dialog = EventDialog(self, mode="edit", event_data=event_data)
        
        if dialog.exec() == QDialog.Accepted:
            updated_data = dialog.get_data()
            
            if not updated_data.get("event"):
                QMessageBox.warning(self, "Lỗi", "Vui lòng nhập tên sự kiện!")
                return
            
            # Kiểm tra thời gian quá khứ
            start_time_str = updated_data.get("start_time")
            if start_time_str:
                try:
                    event_time = datetime.fromisoformat(start_time_str)
                    if event_time < datetime.now():
                        reply = QMessageBox.question(
                            self, "Cảnh báo",
                            "Thời gian sự kiện đã ở trong quá khứ!\n\nBạn có chắc muốn cập nhật sự kiện này?",
                            QMessageBox.Yes | QMessageBox.No,
                            QMessageBox.No
                        )
                        if reply == QMessageBox.No:
                            return
                except Exception as e:
                    print(f"Error parsing time: {e}")
            
            update_dict = {
                "event_name": updated_data["event"],
                "location": updated_data["location"],
                "start_time": updated_data["start_time"],
                "reminder_minutes": updated_data["reminder_minutes"]
            }
            self.db.update_event(event_id, update_dict)
            self.load_events_by_filter()
            QMessageBox.information(self, "Thành công", "Đã cập nhật sự kiện!")
    
    def delete_event(self):
        """Delete selected event."""
        selected_row = self.ui.table_events.currentRow()
        
        if selected_row < 0:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn sự kiện cần xóa!")
            return
        
        event_id_item = self.ui.table_events.item(selected_row, 0)
        if not event_id_item:
            QMessageBox.warning(self, "Lỗi", "Không thể lấy ID sự kiện!")
            return
        
        event_id = int(event_id_item.text())
        event_name = self.ui.table_events.item(selected_row, 1).text() if self.ui.table_events.item(selected_row, 1) else "sự kiện"
        
        reply = QMessageBox.question(
            self, "Xác nhận xóa",
            f"Bạn có chắc muốn xóa sự kiện '{event_name}'?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self.db.delete_event(event_id)
            self.load_events_by_filter()
            QMessageBox.information(self, "Thành công", "Đã xóa sự kiện!")
    
    def show_reminder_notification(self, reminders):
        """Show reminder notification from ReminderThread."""
        for reminder in reminders:
            event_name = reminder.get('event_name', 'Sự kiện')
            start_time = reminder.get('start_time', '')
            location = reminder.get('location', '')
            
            message = f"Sắp đến giờ: {event_name}"
            if start_time:
                try:
                    dt = datetime.fromisoformat(start_time)
                    time_str = dt.strftime("%H:%M")
                    message += f" lúc {time_str}"
                except:
                    pass
            if location:
                message += f"\nĐịa điểm: {location}"
            
            self.tray_icon.showMessage(
                "Nhắc Nhở Sự Kiện",
                message,
                QSystemTrayIcon.Information,
                5000
            )
            
            try:
                if HAS_WINSOUND:
                    winsound.Beep(1000, 500)
            except Exception:
                pass
    
    def on_tab_changed(self, index):
        """Handle tab change."""
        if index == 1:  # Calendar tab
            self.load_events_by_filter()
        elif index == 2:  # Reminder history tab
            self.load_reminder_history()
    
    def closeEvent(self, event):
        """Handle application close."""
        if hasattr(self, 'reminder_thread') and self.reminder_thread.isRunning():
            self.reminder_thread.stop()
        
        if hasattr(self, 'db'):
            self.db.close()
        
        if hasattr(self, 'tray_icon'):
            self.tray_icon.hide()
        
        event.accept()


def main():
    """Main entry point."""
    app = QApplication(sys.argv)
    app.setApplicationName("Vietnamese Calendar Manager")
    app.setOrganizationName("AI Calendar")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

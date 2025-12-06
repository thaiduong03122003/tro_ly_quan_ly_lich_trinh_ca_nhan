import sqlite3
from datetime import datetime, timedelta
import json

class DatabaseManager:
    def __init__(self, db_name='events.db'):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        
        # Đảm bảo schema được tạo ngay khi khởi tạo
        self._create_schema()
    
    def _create_schema(self):
        """
        Tạo bảng events và chat_history với đầy đủ cột cần thiết.
        """
        # Bảng events
        create_events_sql = """
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_name TEXT NOT NULL,
            location TEXT,
            start_time TEXT NOT NULL,
            end_time TEXT,
            reminder_minutes INTEGER,
            reminder_time TEXT,
            is_notified INTEGER DEFAULT 0
        )
        """
        
        # Bảng chat_history để lưu lịch sử chat
        create_chat_sql = """
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            event_id INTEGER,
            FOREIGN KEY (event_id) REFERENCES events(id)
        )
        """
        
        self.cursor.execute(create_events_sql)
        self.cursor.execute(create_chat_sql)
        self.connection.commit()
    
    def _calculate_reminder_time(self, start_time_iso, reminder_minutes):
        if not reminder_minutes or reminder_minutes == 0:
            return None
            
        try:
            # Chuyển đổi ISO 8601 string thành datetime object
            start_time_dt = datetime.fromisoformat(start_time_iso)
            
            # Tính toán thời điểm nhắc nhở
            reminder_time_dt = start_time_dt - timedelta(minutes=reminder_minutes)
            
            # Chuyển về ISO 8601 string
            return reminder_time_dt.isoformat()
            
        except Exception as e:
            return None
    
    def add_event(self, event_data):
        # Tính toán reminder_time
        reminder_time = self._calculate_reminder_time(
            event_data.get('start_time'),
            event_data.get('reminder_minutes', 0)
        )
        
        insert_sql = """
        INSERT INTO events (
            event_name, location, start_time, end_time, 
            reminder_minutes, reminder_time, is_notified
        ) VALUES (?, ?, ?, ?, ?, ?, 0)
        """
        
        values = (
            event_data.get('event', ''),
            event_data.get('location', ''),
            event_data.get('start_time'),
            event_data.get('end_time'),
            event_data.get('reminder_minutes', 0),
            reminder_time
        )
        
        self.cursor.execute(insert_sql, values)
        self.connection.commit()
        
        event_id = self.cursor.lastrowid
        return event_id
    
    def get_events_for_range(self, start_date_iso, end_date_iso):
        select_sql = """
        SELECT id, event_name, location, start_time, end_time, 
               reminder_minutes, reminder_time, is_notified
        FROM events
        WHERE start_time BETWEEN ? AND ?
        ORDER BY start_time
        """
        
        self.cursor.execute(select_sql, (start_date_iso, end_date_iso))
        rows = self.cursor.fetchall()
        
        events = []
        for row in rows:
            event = {
                'id': row[0],
                'event_name': row[1],
                'location': row[2],
                'start_time': row[3],
                'end_time': row[4],
                'reminder_minutes': row[5],
                'reminder_time': row[6],
                'is_notified': row[7]
            }
            events.append(event)
        
        return events
    
    def get_reminders_due(self, current_time_iso):
        select_sql = """
        SELECT id, event_name, location, start_time, end_time,
               reminder_minutes, reminder_time, is_notified
        FROM events
        WHERE reminder_time IS NOT NULL
          AND reminder_time <= ?
          AND is_notified = 0
        ORDER BY reminder_time
        """
        
        self.cursor.execute(select_sql, (current_time_iso,))
        rows = self.cursor.fetchall()
        
        reminders = []
        for row in rows:
            reminder = {
                'id': row[0],
                'event_name': row[1],
                'location': row[2],
                'start_time': row[3],
                'end_time': row[4],
                'reminder_minutes': row[5],
                'reminder_time': row[6],
                'is_notified': row[7]
            }
            reminders.append(reminder)
        
        return reminders
    
    def mark_as_notified(self, event_id):
        update_sql = "UPDATE events SET is_notified = 1 WHERE id = ?"
        self.cursor.execute(update_sql, (event_id,))
        self.connection.commit()
    
    def update_event(self, event_id, new_data):
        # Kiểm tra xem có thay đổi thời gian hoặc reminder không
        time_changed = 'start_time' in new_data or 'reminder_minutes' in new_data
        
        # Xây dựng câu SQL update động
        update_fields = []
        values = []
        
        for key, value in new_data.items():
            if key in ['event_name', 'location', 'start_time', 'end_time', 'reminder_minutes']:
                update_fields.append(f"{key} = ?")
                values.append(value)
        
        if time_changed:
            # Nếu thời gian thay đổi, cần tính lại reminder_time và reset is_notified
            # Lấy dữ liệu hiện tại để tính toán
            select_sql = "SELECT start_time, reminder_minutes FROM events WHERE id = ?"
            self.cursor.execute(select_sql, (event_id,))
            current_data = self.cursor.fetchone()
            
            if current_data:
                # Sử dụng dữ liệu mới hoặc dữ liệu cũ
                start_time = new_data.get('start_time', current_data[0])
                reminder_minutes = new_data.get('reminder_minutes', current_data[1])
                
                new_reminder_time = self._calculate_reminder_time(start_time, reminder_minutes)
                
                update_fields.extend(["reminder_time = ?", "is_notified = ?"])
                values.extend([new_reminder_time, 0])
        
        if update_fields:
            update_sql = f"UPDATE events SET {', '.join(update_fields)} WHERE id = ?"
            values.append(event_id)
            
            self.cursor.execute(update_sql, values)
            self.connection.commit()
            
            pass
    
    def delete_event(self, event_id):
        delete_sql = "DELETE FROM events WHERE id = ?"
        self.cursor.execute(delete_sql, (event_id,))
        self.connection.commit()
    
    def get_all_events(self):
        select_sql = """
        SELECT id, event_name, location, start_time, end_time,
               reminder_minutes, reminder_time, is_notified
        FROM events
        ORDER BY start_time
        """
        
        self.cursor.execute(select_sql)
        rows = self.cursor.fetchall()
        
        events = []
        for row in rows:
            event = {
                'id': row[0],
                'event_name': row[1],
                'location': row[2],
                'start_time': row[3],
                'end_time': row[4],
                'reminder_minutes': row[5],
                'reminder_time': row[6],
                'is_notified': row[7]
            }
            events.append(event)
        
        return events
    
    # ==================== CHAT HISTORY METHODS ====================
    
    def add_chat_message(self, sender, message, event_id=None):
        timestamp = datetime.now().isoformat()
        
        insert_sql = """
        INSERT INTO chat_history (sender, message, timestamp, event_id)
        VALUES (?, ?, ?, ?)
        """
        
        self.cursor.execute(insert_sql, (sender, message, timestamp, event_id))
        self.connection.commit()
        
        return self.cursor.lastrowid
    
    def get_chat_history(self, limit=100):
        select_sql = """
        SELECT id, sender, message, timestamp, event_id
        FROM chat_history
        ORDER BY timestamp DESC
        LIMIT ?
        """
        
        self.cursor.execute(select_sql, (limit,))
        rows = self.cursor.fetchall()
        
        messages = []
        for row in reversed(rows):  # Đảo ngược để tin nhắn cũ nhất ở đầu
            messages.append({
                'id': row[0],
                'sender': row[1],
                'message': row[2],
                'timestamp': row[3],
                'event_id': row[4]
            })
        
        return messages
    
    def get_chat_messages_today(self):
        today = datetime.now().date().isoformat()
        
        select_sql = """
        SELECT id, sender, message, timestamp, event_id
        FROM chat_history
        WHERE date(timestamp) = date(?)
        ORDER BY timestamp ASC
        """
        
        self.cursor.execute(select_sql, (today,))
        rows = self.cursor.fetchall()
        
        messages = []
        for row in rows:
            messages.append({
                'id': row[0],
                'sender': row[1],
                'message': row[2],
                'timestamp': row[3],
                'event_id': row[4]
            })
        
        return messages
    
    def delete_chat_message(self, message_id):
        delete_sql = "DELETE FROM chat_history WHERE id = ?"
        self.cursor.execute(delete_sql, (message_id,))
        self.connection.commit()
    
    def clear_chat_history(self):
        """
        Xóa tất cả lịch sử chat.
        """
        delete_sql = "DELETE FROM chat_history"
        self.cursor.execute(delete_sql)
        self.connection.commit()
    
    def close(self):
        """
        Đóng kết nối cơ sở dữ liệu.
        """
        if self.connection:
            self.connection.close()
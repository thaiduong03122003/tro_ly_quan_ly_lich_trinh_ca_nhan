"""
Component 3: Rule-based Extraction for Vietnamese NER System
===========================================================

This component runs after Component 2 (Model-based NER) and performs:
1. Reminder extraction using Regex patterns
2. Event name extraction using Subtractive Method

Author: AI Assistant
Date: November 2024
"""

import re

def extract_event_and_reminder(raw_text, time_entities, loc_entities):
    """
    Trích xuất tên sự kiện và thông tin nhắc nhở từ văn bản.
    
    Args:
        raw_text (str): Câu gốc
        time_entities (list): Danh sách các thực thể TIME đã được model NER tìm thấy
        loc_entities (list): Danh sách các thực thể LOCATION đã được model NER tìm thấy
        
    Returns:
        dict: {
            "event_name": str,        # Tên sự kiện đã được dọn dẹp
            "reminder_minutes": int   # Số phút nhắc nhở, 0 nếu không tìm thấy
        }
    """
    
    # Bước 1: Trích xuất thông tin nhắc nhở bằng Regex
    reminder_minutes, reminder_phrase = extract_reminder(raw_text)
    
    # Bước 2: Trích xuất tên sự kiện bằng Subtractive Method
    event_name = extract_event_name(raw_text, time_entities, loc_entities, reminder_phrase)
    
    result = {
        "event_name": event_name,
        "reminder_minutes": reminder_minutes
    }
    
    return result

def extract_reminder(text):
    """
    Trích xuất thông tin nhắc nhở từ văn bản bằng Regex.
    
    Args:
        text (str): Văn bản cần phân tích
        
    Returns:
        tuple: (reminder_minutes, reminder_phrase)
    """
    
    # QUAN TRỌNG: Pattern phải capture số và đơn vị liền nhau trong named groups
    # để tránh nhầm lẫn với các số khác trong câu (như 22h50)
    reminder_patterns = [
        # ============ NO DIACRITICS ============
        # Pattern 1: Phút - "nhac truoc 5 phut", "bao truoc 30p"
        r'(nhac\s*nho|nhac|bao|remind)\s*(toi|tui)?\s*truoc\s*(?P<num1>\d{1,3})\s*(?P<unit1>phut|p(?!h)|minute|minutes)\b',
        
        # Pattern 2: Giờ/Tiếng - "nhac truoc 2 tieng", "bao truoc 1h"
        r'(nhac\s*nho|nhac|bao|remind)\s*(toi|tui)?\s*truoc\s*(?P<num2>\d{1,3})\s*(?P<unit2>tieng|gio|h(?!o)|hour|hours)\b',
        
        # Pattern 3: Giây - "nhac truoc 30 giay", "bao truoc 60s"
        r'(nhac\s*nho|nhac|bao|remind)\s*(toi|tui)?\s*truoc\s*(?P<num3>\d{1,4})\s*(?P<unit3>giay|s(?!a)|second|seconds)\b',
        
        # Pattern 4: Phút (no prefix) - "truoc 5 phut", "truoc 30p"
        r'truoc\s*(?P<num4>\d{1,3})\s*(?P<unit4>phut|p(?!h)|minute|minutes)\b',
        
        # Pattern 5: Giờ/Tiếng (no prefix) - "truoc 2 tieng", "truoc 1h"
        r'truoc\s*(?P<num5>\d{1,3})\s*(?P<unit5>tieng|gio|h(?!o)|hour|hours)\b',
        
        # Pattern 6: Giây (no prefix) - "truoc 30 giay", "truoc 60s"
        r'truoc\s*(?P<num6>\d{1,4})\s*(?P<unit6>giay|s(?!a)|second|seconds)\b',
        
        # ============ WITH DIACRITICS ============
        # Pattern 7: Phút - "nhắc trước 5 phút"
        r'(nhắc\s*nhở|nhắc|báo)\s*(tôi|tui)?\s*trước\s*(?P<num7>\d{1,3})\s*(?P<unit7>phút|p(?!h))\b',
        
        # Pattern 8: Giờ/Tiếng - "nhắc trước 2 tiếng"
        r'(nhắc\s*nhở|nhắc|báo)\s*(tôi|tui)?\s*trước\s*(?P<num8>\d{1,3})\s*(?P<unit8>tiếng|giờ|h(?!ô))\b',
        
        # Pattern 9: Giây - "nhắc trước 30 giây"
        r'(nhắc\s*nhở|nhắc|báo)\s*(tôi|tui)?\s*trước\s*(?P<num9>\d{1,4})\s*(?P<unit9>giây|s(?!á))\b',
        
        # Pattern 10: Phút (no prefix) - "trước 5 phút"
        r'trước\s*(?P<num10>\d{1,3})\s*(?P<unit10>phút|p(?!h))\b',
        
        # Pattern 11: Giờ/Tiếng (no prefix) - "trước 2 tiếng"
        r'trước\s*(?P<num11>\d{1,3})\s*(?P<unit11>tiếng|giờ|h(?!ô))\b',
        
        # Pattern 12: Giây (no prefix) - "trước 30 giây"
        r'trước\s*(?P<num12>\d{1,4})\s*(?P<unit12>giây|s(?!á))\b',
    ]
    
    for i, pattern in enumerate(reminder_patterns):
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            # Lấy toàn bộ chuỗi match
            reminder_phrase = match.group(0)
            
            # Lấy số và đơn vị từ named groups
            number = None
            unit = None
            
            # Tìm trong các named groups
            for j in range(1, 13):
                num_key = f'num{j}'
                unit_key = f'unit{j}'
                if num_key in match.groupdict() and match.group(num_key):
                    number = int(match.group(num_key))
                    unit = match.group(unit_key).lower() if match.group(unit_key) else 'phút'
                    break
            
            if number is None:
                continue
            
            # Convert to minutes
            if unit in ['tieng', 'tiếng', 'gio', 'giờ', 'h', 'hour', 'hours']:
                reminder_minutes = number * 60
            elif unit in ['giay', 'giây', 's', 'second', 'seconds']:
                # Convert seconds to minutes (minimum 1 minute)
                reminder_minutes = max(1, number // 60)
            else:  # phut, phút, p, minute, minutes
                reminder_minutes = number
                
            return reminder_minutes, reminder_phrase
    
    return 0, ""

def extract_event_name(raw_text, time_entities, loc_entities, reminder_phrase):
    event_name = raw_text
    
    # Xóa reminder phrase TRƯỚC để tránh bị gom vào location
    if reminder_phrase and reminder_phrase in event_name:
        event_name = event_name.replace(reminder_phrase, "")
    
    # Remove TIME entities
    for time_entity in time_entities:
        if time_entity in event_name:
            event_name = event_name.replace(time_entity, "")
    
    # Remove LOCATION entities - clean them first
    for loc_entity in loc_entities:
        # Clean location entity trước khi remove
        clean_loc = clean_location_entity(loc_entity, reminder_phrase)
        if clean_loc and clean_loc in event_name:
            event_name = event_name.replace(clean_loc, "")
    
    # Bước dọn dẹp: Loại bỏ stop words và ký tự thừa
    event_name = cleanup_event_name(event_name)
    
    return event_name

def clean_location_entity(loc_entity, reminder_phrase):
    if not loc_entity:
        return ""
    
    clean_loc = loc_entity
    
    # Loại bỏ reminder phrase nếu bị gom vào location
    if reminder_phrase and reminder_phrase in clean_loc:
        clean_loc = clean_loc.replace(reminder_phrase, "")
    
    # Loại bỏ các từ chỉ reminder bị gom sai
    reminder_words = [
        r',?\s*hãy\s*nhắc\s*trước.*$',
        r',?\s*nhắc\s*trước.*$',
        r',?\s*báo\s*trước.*$',
        r',?\s*nhắc\s*nhở.*$',
        r',?\s*remind.*$',
        r',?\s*hay\s*nhac\s*truoc.*$',
        r',?\s*nhac\s*truoc.*$',
        r',?\s*bao\s*truoc.*$',
    ]
    
    for pattern in reminder_words:
        clean_loc = re.sub(pattern, '', clean_loc, flags=re.IGNORECASE)
    
    return clean_loc.strip()

def cleanup_event_name(text):
    # Stop words - CHỈ xóa các từ không có nghĩa quan trọng
    STOP_WORDS = [
        # Giới từ chỉ vị trí/thời gian
        'tai', 'o', 'vao', 'luc', 'tu', 'den', 'ra', 'qua',
        'ben', 'canh', 'gan', 'xa', 'giua', 'ngoai', 'theo',
        # With diacritics
        'tại', 'ở', 'vào', 'lúc', 'từ', 'đến', 'gần', 'giữa', 'ngoài',
        # Từ chỉ yêu cầu/mệnh lệnh - CHỈ xóa từ đơn lẻ không quan trọng
        'hãy', 'hay', 'xin', 'làm', 'ơn', 'giúp', 'tôi', 'toi', 'mình', 'minh'
    ]
    
    # Loại bỏ dấu phẩy, dấu chấm và ký tự đặc biệt
    cleaned_text = re.sub(r'[,.\-!?;:()"\[\]{}]', ' ', text)
    
    # Tách thành từ và loại bỏ stop words
    words = cleaned_text.split()
    filtered_words = []
    
    for word in words:
        word = word.strip().lower()
        if word and word not in STOP_WORDS and len(word) > 1:
            filtered_words.append(word)
    
    # Ghép lại và dọn dẹp
    result = ' '.join(filtered_words).strip()
    
    # Capitalize chữ cái đầu
    if result:
        result = result[0].upper() + result[1:] if len(result) > 1 else result.upper()
    
    return result

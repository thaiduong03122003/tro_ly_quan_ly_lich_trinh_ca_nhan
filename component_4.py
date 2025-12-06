import re
from datetime import datetime, time, timedelta, date
from dateutil.relativedelta import relativedelta, MO, TU, WE, TH, FR, SA, SU

def resolve_time(time_entities, current_time=None):
    now = current_time if current_time else datetime.now()
    full_time_string = ' '.join(time_entities).lower().strip()
    
    # Khởi tạo
    resolved_date = now.date()
    resolved_time = None
    
    resolved_date = resolve_date(full_time_string, now)
    resolved_time = resolve_time_component(full_time_string, now)
    
    if resolved_time is None:
        resolved_time = time(9, 0)  # Default 9h
    
    # Kết hợp ngày và giờ
    start_time = datetime.combine(resolved_date, resolved_time)
    end_time = None  # Tạm thời để None
    
    return {
        "start_time": start_time,
        "end_time": end_time
    }

def resolve_date(time_string, now):
    resolved_date = now.date()
    
    # Thứ tự kiểm tra phải ưu tiên các từ khóa cụ thể hơn trước!
    # "mai" phải được check trước "nay" vì "sáng mai" có thể bị nhầm với "nay"
    
    # Kiểm tra "ngày mai" hoặc "mai" - ƯU TIÊN CAO NHẤT
    if 'ngày mai' in time_string or ' mai' in time_string or time_string.startswith('mai') or time_string.endswith('mai'):
        resolved_date = now.date() + timedelta(days=1)
    elif 'hôm qua' in time_string or ' qua' in time_string or time_string.startswith('qua') or time_string.endswith('qua'):
        resolved_date = now.date() - timedelta(days=1)
    elif 'hôm nay' in time_string or time_string.endswith('nay') or ' nay' in time_string:
        resolved_date = now.date()
    elif 'cuối tuần' in time_string:
        resolved_date = now.date() + relativedelta(weekday=SA(1))
    elif 'thứ' in time_string or 'chủ nhật' in time_string:
        resolved_date = resolve_weekday(time_string, now)
    else:
        resolved_date = now.date()
    
    return resolved_date

def resolve_weekday(time_string, now):
    """Resolve weekday from time string."""
    weekday_map = {
        'thứ hai': MO(1), 'thứ ba': TU(1), 'thứ tư': WE(1),
        'thứ năm': TH(1), 'thứ sáu': FR(1), 'thứ bảy': SA(1),
        'chủ nhật': SU(1),
    }
    
    for weekday_name, weekday_obj in weekday_map.items():
        if weekday_name in time_string:
            if 'tuần sau' in time_string:
                return now.date() + relativedelta(weekday=weekday_obj, weeks=1)
            else:
                return now.date() + relativedelta(weekday=weekday_obj)
    
    return now.date()

def resolve_time_component(time_string, now):
    """Resolve time component from time string."""
    resolved_time = None
    hour = None
    minute = 0
    
    # Bước 1: Tìm giờ cụ thể bằng regex - ƯU TIÊN CAO NHẤT
    
    # Pattern 1a: 14h30, 9h15, 22h50 (có chữ h + phút liền)
    time_pattern_1a = r'(\d{1,2})h(\d{1,2})'
    match1a = re.search(time_pattern_1a, time_string)
    
    # Pattern 1b: 10h, 23h (chỉ có giờ, không có phút liền sau)
    time_pattern_1b = r'(\d{1,2})h(?!\d)'
    match1b = re.search(time_pattern_1b, time_string)
    
    # Pattern 2: 14:30, 9:15 (có dấu :)
    time_pattern_2 = r'(\d{1,2}):(\d{1,2})'
    match2 = re.search(time_pattern_2, time_string)
    
    # Pattern 3: "X giờ Y phút" hoặc "X giờ Y" hoặc "X giờ" (tiếng Việt đầy đủ)
    time_pattern_3 = r'(\d{1,2})\s*giờ\s*(\d{1,2})?\s*(phút)?'
    match3 = re.search(time_pattern_3, time_string)
    
    # Pattern 4: Chỉ số giờ đơn lẻ (ví dụ: "lúc 10", "vào 9")
    time_pattern_4 = r'(?:lúc|vào)\s*(\d{1,2})(?!\d)'
    match4 = re.search(time_pattern_4, time_string)
    
    if match1a:
        hour = int(match1a.group(1))
        minute = int(match1a.group(2))
    elif match2:
        hour = int(match2.group(1))
        minute = int(match2.group(2))
    elif match3:
        hour = int(match3.group(1))
        minute = int(match3.group(2)) if match3.group(2) else 0
    elif match1b:
        hour = int(match1b.group(1))
        minute = 0
    elif match4:
        hour = int(match4.group(1))
        minute = 0
    
    # Handle AM/PM
    if hour is not None:
        if ('chiều' in time_string or 'tối' in time_string):
            if hour < 12 and hour != 0:
                hour += 12
        elif 'sáng' in time_string:
            if hour == 12:
                hour = 0
        
        if 0 <= hour <= 23 and 0 <= minute <= 59:
            return time(hour, minute)
    
    # Default times for time-of-day keywords
    if 'sáng sớm' in time_string:
        return time(6, 0)
    elif 'sáng' in time_string:
        return time(9, 0)
    elif 'đầu giờ trưa' in time_string:
        return time(11, 0)
    elif 'trưa' in time_string:
        return time(12, 0)
    elif 'chiều' in time_string:
        return time(15, 0)
    elif 'tối' in time_string:
        return time(20, 0)
    
    return None
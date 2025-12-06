import joblib
import sys
import os
import json
import re
from datetime import datetime

# Import functions from other components
from predict import predict_ner, format_prediction_output
from component_3 import extract_event_and_reminder
from component_4 import resolve_time

def get_resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        # Nếu đang chạy file .exe: Lấy thư mục chứa file .exe
        base_path = os.path.dirname(sys.executable)
    else:
        # Nếu đang chạy code python thường: Lấy thư mục hiện tại
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path, relative_path)

try:
    model_path = get_resource_path('ner_crf.model')
    crf_model = joblib.load(model_path)
    print(f"Đã load model từ: {model_path}")
except Exception as e:
    print(f"Lỗi load model: {e}")
    crf_model = None

def extract_time_fallback(text):
    text_lower = text.lower()
    time_parts = []
    
    # ==================== GIỜ CỤ THỂ ====================
    
    # Pattern 1a: "10h", "10h30", "22h50", "23h" (viết tắt với chữ h liền)
    hour_pattern_1 = r'\d{1,2}h\d{0,2}'
    hour_matches = re.findall(hour_pattern_1, text_lower)
    time_parts.extend(hour_matches)
    
    # Pattern 1b: "10 h", "10 h 30" (có khoảng trắng)
    hour_pattern_2 = r'\d{1,2}\s+h\s*\d{0,2}'
    hour_matches_2 = re.findall(hour_pattern_2, text_lower)
    # Chuẩn hóa về dạng không khoảng trắng
    for match in hour_matches_2:
        normalized = re.sub(r'\s+', '', match)  # Xóa tất cả khoảng trắng
        if normalized not in time_parts:
            time_parts.append(normalized)
    
    # Pattern 2: "10:30", "14:15", "23:00" (với dấu :)
    colon_pattern = r'\d{1,2}:\d{2}'
    colon_matches = re.findall(colon_pattern, text_lower)
    time_parts.extend(colon_matches)
    
    # Pattern 3: "10 giờ 35 phút", "10 giờ 35", "10 giờ" (tiếng Việt đầy đủ)
    viet_hour_pattern = r'\d{1,2}\s*giờ\s*(\d{1,2})?\s*(phút)?'
    for match in re.finditer(viet_hour_pattern, text_lower):
        time_parts.append(match.group(0).strip())
    
    # Pattern 4: "lúc 10", "vào 9", "lúc 23" (số đơn lẻ sau từ chỉ thời gian)
    luc_pattern = r'(?:lúc|vào)\s*(\d{1,2})(?!\d|h|:)'
    for match in re.finditer(luc_pattern, text_lower):
        hour_num = match.group(1)
        time_parts.append(f"{hour_num}h")  # Chuyển thành dạng Xh
    
    # ==================== BUỔI TRONG NGÀY ====================
    
    # Pattern 5: Buoi trong ngay (both with and without diacritics)
    time_of_day = [
        ('sáng sớm', 'sang som'), ('sáng', 'sang'), 
        ('trưa', 'trua'),
        ('xế chiều', 'xe chieu'), ('chiều', 'chieu'),
        ('tối muộn', 'toi muon'), ('tối', 'toi'),
        ('đêm khuya', 'dem khuya'), ('đêm', 'dem')
    ]
    for tod_diac, tod_no_diac in time_of_day:
        if tod_diac in text_lower or tod_no_diac in text_lower:
            time_parts.append(tod_diac)  # Always use diacritic version
            break
    
    # ==================== NGÀY ====================
    
    # Pattern 6: Ngày tương đối
    day_keywords = ['hôm nay', 'hôm qua', 'ngày mai', 'mai', 'ngày mốt', 'mốt', 'ngày kia', 'kia']
    for day in day_keywords:
        if day in text_lower:
            time_parts.append(day)
            break  # Chỉ lấy một ngày
    
    # Pattern 7: "nay" đơn lẻ (như "tối nay", "sáng nay") 
    # Chỉ thêm nếu chưa có ngày nào
    if 'nay' in text_lower and not any(d in time_parts for d in ['hôm nay', 'mai', 'mốt', 'kia', 'hôm qua']):
        time_parts.append('nay')
    
    # ==================== THU TRONG TUAN ====================
    
    # Pattern 8: Thu trong tuan (both with and without diacritics)
    weekday_patterns = [
        (r'thứ\s*(hai|ba|tư|năm|sáu|bảy)', 'diacritic'),
        (r'thu\s*(hai|ba|tu|nam|sau|bay)', 'no_diacritic'),
        (r'chủ\s*nhật', 'diacritic'),
        (r'chu\s*nhat', 'no_diacritic')
    ]
    for pattern, _ in weekday_patterns:
        for match in re.finditer(pattern, text_lower):
            time_parts.append(match.group(0))
    
    # Pattern 9: Tuan sau (both)
    if 'tuần sau' in text_lower or 'tuan sau' in text_lower:
        time_parts.append('tuần sau')
    
    # Pattern 10: Cuoi tuan (both)
    if 'cuối tuần' in text_lower or 'cuoi tuan' in text_lower:
        time_parts.append('cuối tuần')
    
    # ==================== NGÀY CỤ THỂ ====================
    
    # Pattern 11: "ngày 25", "ngày 25/12", "25/12", "25-12"
    date_pattern_1 = r'ngày\s*(\d{1,2})'
    for match in re.finditer(date_pattern_1, text_lower):
        time_parts.append(match.group(0))
    
    date_pattern_2 = r'\d{1,2}[/-]\d{1,2}'
    date_matches = re.findall(date_pattern_2, text_lower)
    time_parts.extend(date_matches)
    
    return time_parts

# Load model globally (once) to avoid reloading on each call
try:
    CRF_MODEL = joblib.load('ner_crf.model')
except FileNotFoundError:
    CRF_MODEL = None
except Exception as e:
    CRF_MODEL = None

def parse_user_input(raw_text):
    # Check model
    if CRF_MODEL is None:
        return {"error": "Model NER không khả dụng. Vui lòng kiểm tra lại hệ thống."}
    
    # Kiểm tra đầu vào cơ bản
    if not raw_text or not raw_text.strip():
        return {"error": "Vui lòng nhập nội dung cần xử lý."}
    
    try:
        # Use raw_text directly - patterns support both with/without diacritics
        normalized_text = raw_text.lower()
        
        # NER prediction
        prediction_result = predict_ner(raw_text, CRF_MODEL)
        
        # Trích xuất entities từ kết quả
        time_entities = []
        loc_entities = []
        
        for word, label in prediction_result:
            if label.startswith('B-TIME'):
                current_time_entity = [word]
            elif label.startswith('I-TIME') and 'current_time_entity' in locals():
                current_time_entity.append(word)
            elif 'current_time_entity' in locals():
                # Kết thúc time entity
                time_entities.append(' '.join(current_time_entity))
                del current_time_entity
                
            if label.startswith('B-LOC'):
                current_loc_entity = [word]
            elif label.startswith('I-LOC') and 'current_loc_entity' in locals():
                current_loc_entity.append(word)
            elif 'current_loc_entity' in locals():
                # Kết thúc location entity
                loc_entities.append(' '.join(current_loc_entity))
                del current_loc_entity
        
        # Xử lý entities cuối cùng
        if 'current_time_entity' in locals():
            time_entities.append(' '.join(current_time_entity))
        if 'current_loc_entity' in locals():
            loc_entities.append(' '.join(current_loc_entity))
            
        
        # FALLBACK: LUÔN LUÔN chạy fallback regex trên normalized_text để đảm bảo không bỏ sót giờ
        # Vì tokenizer có thể tách "23h17" thành "23" và "h17" riêng biệt
        # Sử dụng normalized_text để hỗ trợ tiếng Việt không dấu
        fallback_time_entities = extract_time_fallback(normalized_text)
        
        # Merge: Ưu tiên fallback nếu nó chứa giờ cụ thể (pattern XhY, X:Y)
        # vì fallback extract từ raw_text trực tiếp, không bị tách từ sai
        has_specific_time_in_fallback = any(
            re.search(r'\d{1,2}h\d{1,2}|\d{1,2}:\d{2}|\d{1,2}\s*giờ\s*\d{1,2}', t) 
            for t in fallback_time_entities
        )
        
        if has_specific_time_in_fallback:
            time_entities = fallback_time_entities
        elif not time_entities:
            time_entities = fallback_time_entities
        else:
            for fb_entity in fallback_time_entities:
                if not any(fb_entity.lower() in te.lower() or te.lower() in fb_entity.lower() 
                          for te in time_entities):
                    time_entities.append(fb_entity)
        
        # Extract event and reminder
        event_data = extract_event_and_reminder(normalized_text, time_entities, loc_entities)
        event_name = event_data.get("event_name", "").strip()
        reminder_minutes = event_data.get("reminder_minutes", 0)
        
        # Resolve time
        time_data = resolve_time(time_entities)
        start_time = time_data.get("start_time")
        end_time = time_data.get("end_time")
        
        # Validation
        if not event_name:
            return {"error": "Khong tim thay ten su kien."}
        
        if start_time is None:
            return {"error": "Khong the xac dinh thoi gian."}
        
        # FALLBACK: Extract location nếu NER bỏ sót
        if not loc_entities:
            loc_fallback_patterns = [
                r'(?:tại|tai|ở|o)\s+([^\d,]+?)(?:\s+(?:nhắc|nhac|báo|bao|vào|lúc|\d+h)|\s*$)',
                r'(?:phòng|phong|room)\s+\S+',
                r'(?:văn phòng|van phong|hội trường|hoi truong|showroom|quán|quan)\s*[^\d,]*',
            ]
            for pattern in loc_fallback_patterns:
                matches = re.findall(pattern, normalized_text, re.IGNORECASE)
                for m in matches:
                    if isinstance(m, str) and len(m.strip()) > 2:
                        loc_entities.append(m.strip())
        
        # Chuẩn hóa location - clean các entities bị gom sai
        clean_locations = []
        for loc in loc_entities:
            # Loại bỏ các phần reminder bị gom sai vào location
            clean_loc = loc
            reminder_patterns = [
                r',?\s*hãy\s*nhắc\s*trước.*$',
                r',?\s*nhắc\s*trước.*$',
                r',?\s*báo\s*trước.*$',
                r',?\s*nhắc\s*nhở.*$',
                r',?\s*remind.*$',
                r',?\s*hay\s*nhac\s*truoc.*$',
                r',?\s*nhac\s*truoc.*$',
                r',?\s*bao\s*truoc.*$',
            ]
            for pattern in reminder_patterns:
                clean_loc = re.sub(pattern, '', clean_loc, flags=re.IGNORECASE)
            clean_loc = clean_loc.strip()
            if clean_loc:
                clean_locations.append(clean_loc)
        
        location_str = ", ".join(clean_locations) if clean_locations else ""
        
        # Chuẩn hóa thời gian thành ISO 8601
        start_time_str = start_time.isoformat() if start_time else None
        end_time_str = end_time.isoformat() if end_time else None
        
        result = {
            "event": event_name,
            "start_time": start_time_str,
            "end_time": end_time_str,
            "location": location_str,
            "reminder_minutes": int(reminder_minutes)
        }
        
        # Print JSON output to console (safe for Windows)
        print("\n" + "=" * 50)
        print("NLP PARSING RESULT:")
        print("=" * 50)
        try:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        except UnicodeEncodeError:
            # Fallback to ASCII if encoding fails
            print(json.dumps(result, indent=2, ensure_ascii=True))
        print("=" * 50 + "\n")
        
        return result
        
    except Exception as e:
        return {"error": f"Loi xu ly: {str(e)}"}

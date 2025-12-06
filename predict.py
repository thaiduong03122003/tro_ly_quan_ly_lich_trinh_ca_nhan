import joblib
from underthesea import word_tokenize

# Import bo tu khoa tu feature engineering
from feature_engineering import TIME_KEYWORDS, LOC_KEYWORDS

def word_to_features_predict(sentence_tokens, index):
    """
    Trích xuất các đặc trưng (features) cho một từ tại vị trí index trong câu (cho dự đoán).
    
    Args:
        sentence_tokens (list): Câu chưa gán nhãn dạng ['từ1', 'từ2', ...]
        index (int): Vị trí của từ cần trích xuất đặc trưng
        
    Returns:
        dict: Dictionary chứa các đặc trưng của từ
    """
    # Lấy từ tại vị trí index
    word = sentence_tokens[index]
    
    # Khởi tạo dictionary đặc trưng
    features = {
        # Đặc trưng cơ bản
        'bias': 1.0,
        'word.lower': word.lower(),
        'word.istitle': word.istitle(),
        'word.isdigit': word.isdigit(),
        
        # Đặc trưng từ khóa
        'word.is_time_keyword': word.lower() in TIME_KEYWORDS,
        'word.is_loc_keyword': word.lower() in LOC_KEYWORDS,
        
        # Đặc trưng số học nâng cao (giải quyết vấn đề '10h' vs '101')
        'word.contains_digit': any(char.isdigit() for char in word),
        'word.starts_with_digit': word and word[0].isdigit(),
        'word.ends_with_digit': word and word[-1].isdigit(),
        'word.is_alphanumeric': word.isalnum(),
    }
    
    # Đặc trưng ngữ cảnh - Từ phía trước
    if index == 0:
        # Từ đầu câu
        features['BOS'] = True
    else:
        # Lấy từ trước đó
        prev_word = sentence_tokens[index - 1]
        features.update({
            'word.before.lower': prev_word.lower(),
            'word.before.istitle': prev_word.istitle(),
            'word.before.isdigit': prev_word.isdigit(),
            'word.before.is_time_keyword': prev_word.lower() in TIME_KEYWORDS,
            'word.before.is_loc_keyword': prev_word.lower() in LOC_KEYWORDS,
            'word.before.contains_digit': any(char.isdigit() for char in prev_word),
            'word.before.starts_with_digit': prev_word and prev_word[0].isdigit(),
        })
    
    # Đặc trưng ngữ cảnh - Từ phía sau
    if index == len(sentence_tokens) - 1:
        # Từ cuối câu
        features['EOS'] = True
    else:
        # Lấy từ sau đó
        next_word = sentence_tokens[index + 1]
        features.update({
            'word.after.lower': next_word.lower(),
            'word.after.istitle': next_word.istitle(),
            'word.after.isdigit': next_word.isdigit(),
            'word.after.is_time_keyword': next_word.lower() in TIME_KEYWORDS,
            'word.after.is_loc_keyword': next_word.lower() in LOC_KEYWORDS,
            'word.after.contains_digit': any(char.isdigit() for char in next_word),
            'word.after.starts_with_digit': next_word and next_word[0].isdigit(),
        })
    
    return features

def sentence_to_features_predict(sentence_tokens):
    """
    Chuyển đổi một câu chưa gán nhãn thành danh sách các đặc trưng.
    
    Args:
        sentence_tokens (list): Câu chưa gán nhãn dạng ['từ1', 'từ2', ...]
        
    Returns:
        list: Danh sách các dictionary đặc trưng cho từng từ trong câu
    """
    return [word_to_features_predict(sentence_tokens, i) 
            for i in range(len(sentence_tokens))]

def predict_ner(raw_text, crf_model):
    """NER prediction - returns list of (word, label) tuples."""
    # Tokenize
    tokens = word_tokenize(raw_text)
    
    # Extract features
    features = sentence_to_features_predict(tokens)
    
    # Predict
    try:
        labels = crf_model.predict_single(features)
    except AttributeError:
        labels = crf_model.predict([features])[0]
    
    return list(zip(tokens, labels))

def format_prediction_output(prediction):
    """
    Định dạng kết quả dự đoán để hiển thị đẹp mắt.
    
    Args:
        prediction (list): Danh sách các tuple (từ, nhãn)
        
    Returns:
        str: Chuỗi đã được định dạng
    """
    output_lines = []
    
    # Tách entities
    time_entities = []
    loc_entities = []
    
    current_entity = []
    current_type = None
    
    for word, label in prediction:
        if label.startswith('B-'):
            # Lưu entity trước đó (nếu có)
            if current_entity:
                if current_type == 'TIME':
                    time_entities.append(' '.join(current_entity))
                elif current_type == 'LOC':
                    loc_entities.append(' '.join(current_entity))
            
            # Bắt đầu entity mới
            current_entity = [word]
            current_type = label[2:]  # Lấy phần sau 'B-'
            
        elif label.startswith('I-') and current_entity:
            # Tiếp tục entity hiện tại
            current_entity.append(word)
            
        else:
            # Kết thúc entity hiện tại (nếu có)
            if current_entity:
                if current_type == 'TIME':
                    time_entities.append(' '.join(current_entity))
                elif current_type == 'LOC':
                    loc_entities.append(' '.join(current_entity))
                current_entity = []
                current_type = None
    
    # Xử lý entity cuối cùng
    if current_entity:
        if current_type == 'TIME':
            time_entities.append(' '.join(current_entity))
        elif current_type == 'LOC':
            loc_entities.append(' '.join(current_entity))
    
    # Định dạng output
    output_lines.append(f"   📝 Tokens và nhãn: {prediction}")
    output_lines.append(f"   ⏰ TIME entities: {time_entities if time_entities else 'Không tìm thấy'}")
    output_lines.append(f"   📍 LOCATION entities: {loc_entities if loc_entities else 'Không tìm thấy'}")
    
    return '\n'.join(output_lines)
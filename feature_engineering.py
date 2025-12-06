# Định nghĩa các bộ từ khóa (Keyword Sets)
TIME_KEYWORDS = {
    # Đơn vị thời gian cơ bản
    'giờ', 'gio', 'phút', 'phut', 'giây', 'giay', 'tiếng', 'tieng',
    
    # Các buổi trong ngày
    'sáng', 'sang', 'trưa', 'trua', 'chiều', 'chieu', 'tối', 'toi', 'đêm', 'dem', 'khuya',
    
    # Ngày và thời gian tương đối
    'mai', 'nay', 'hôm', 'hom', 'qua', 'kia', 'mốt', 'mot',
    
    # Thứ trong tuần
    'thứ', 'thu', 'chủ', 'chu', 'nhật', 'nhat', 
    't2', 't3', 't4', 't5', 't6', 't7', 'cn',
    
    # Tháng và năm
    'tuần', 'tuan', 'tháng', 'thang', 'năm', 'nam', 'quý', 'quy',
    
    # Từ chỉ thời gian khác
    'lúc', 'luc', 'khi', 'bây', 'bay', 'rồi', 'roi', 
    'trước', 'truoc', 'sau',
    'sớm', 'som', 'muộn', 'muon', 'đúng', 'dung', 'khoảng', 'khoang', 'vào', 'vao'
}

LOC_KEYWORDS = {
    # Giới từ chỉ địa điểm
    'tại', 'tai', 'ở', 'o', 'trong', 'ngoài', 'ngoai', 'trên', 'tren', 'dưới', 'duoi',
    
    # Loại địa điểm (Building type)
    'phòng', 'phong', 'tầng', 'tang', 'lầu', 'lau', 'toà', 'toa', 'nhà', 'nha', 'căn', 'can',
    
    # Đơn vị hành chính
    'quận', 'quan', 'huyện', 'huyen', 'thành', 'thanh', 'phố', 'pho', 
    'thị', 'thi', 'xã', 'xa', 'phường', 'phuong',
    
    # Đường xá
    'đường', 'duong', 'ngõ', 'ngo', 'hẻm', 'hem', 'số', 'so',
    
    # Địa điểm công cộng
    'công', 'cong', 'ty', 
    'trường', 'truong', 'bệnh', 'benh', 'viện', 'vien', 
    'chợ', 'cho', 'siêu', 'sieu', 
    'ngân', 'ngan', 'hàng', 'hang', 
    'văn', 'van', 'cửa', 'cua',
    'quán', 'quan', 'shop', 'tiệm', 'tiem',
    
    # Từ chỉ vị trí tương đối
    'gần', 'gan', 'xa', 'cạnh', 'canh', 'bên', 'ben', 'đối', 'doi', 'diện', 'dien', 'góc', 'goc'
}


def word_to_features(sentence_tokens_with_labels, index):
    # Lấy từ và nhãn tại vị trí index
    word, label = sentence_tokens_with_labels[index]
    
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
        prev_word, prev_label = sentence_tokens_with_labels[index - 1]
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
    if index == len(sentence_tokens_with_labels) - 1:
        # Từ cuối câu
        features['EOS'] = True
    else:
        # Lấy từ sau đó
        next_word, next_label = sentence_tokens_with_labels[index + 1]
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


def sentence_to_features(sentence_with_labels):
    """
    Chuyển đổi một câu đã gán nhãn thành danh sách các đặc trưng.
    
    Args:
        sentence_with_labels (list): Câu đã gán nhãn dạng [('từ', 'nhãn'), ...]
        
    Returns:
        list: Danh sách các dictionary đặc trưng cho từng từ trong câu
    """
    return [word_to_features(sentence_with_labels, i) 
            for i in range(len(sentence_with_labels))]


def sentence_to_labels(sentence_with_labels):
    """
    Trích xuất danh sách các nhãn từ một câu đã gán nhãn.
    
    Args:
        sentence_with_labels (list): Câu đã gán nhãn dạng [('từ', 'nhãn'), ...]
        
    Returns:
        list: Danh sách các nhãn tương ứng với từng từ
    """
    return [label for word, label in sentence_with_labels]


def sentences_to_features(sentences_with_labels):
    """
    Chuyển đổi nhiều câu đã gán nhãn thành danh sách các đặc trưng.
    
    Args:
        sentences_with_labels (list): Danh sách các câu đã gán nhãn
        
    Returns:
        list: Danh sách các feature sets cho từng câu
    """
    return [sentence_to_features(sentence) for sentence in sentences_with_labels]


def sentences_to_labels(sentences_with_labels):
    """
    Trích xuất danh sách các nhãn từ nhiều câu đã gán nhãn.
    
    Args:
        sentences_with_labels (list): Danh sách các câu đã gán nhãn
        
    Returns:
        list: Danh sách các label sets cho từng câu
    """
    return [sentence_to_labels(sentence) for sentence in sentences_with_labels]
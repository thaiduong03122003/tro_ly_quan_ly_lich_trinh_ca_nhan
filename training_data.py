"""
Training Data for Vietnamese Named Entity Recognition (NER)

Format: [('từ', 'nhãn'), ('từ', 'nhãn'), ...]
Labels: B-TIME, I-TIME, B-LOC, I-LOC, O
"""

TRAINING_DATA = [
    # Câu 1-20: Các cuộc họp và sự kiện
    [('Họp', 'O'), ('team', 'O'), ('10h', 'B-TIME'), ('sáng', 'I-TIME'), ('mai', 'I-TIME'), ('tại', 'O'), ('phòng', 'B-LOC'), ('101', 'I-LOC')],
    [('Meeting', 'O'), ('lúc', 'O'), ('2', 'B-TIME'), ('giờ', 'I-TIME'), ('chiều', 'I-TIME'), ('ở', 'O'), ('văn', 'B-LOC'), ('phòng', 'I-LOC'), ('A', 'I-LOC')],
    [('Presentation', 'O'), ('9h30', 'B-TIME'), ('sáng', 'I-TIME'), ('thứ', 'I-TIME'), ('hai', 'I-TIME'), ('tầng', 'B-LOC'), ('3', 'I-LOC')],
    [('Gặp', 'O'), ('khách', 'O'), ('hàng', 'O'), ('3h', 'B-TIME'), ('chiều', 'I-TIME'), ('tại', 'O'), ('công', 'B-LOC'), ('ty', 'I-LOC')],
    [('Training', 'O'), ('từ', 'O'), ('8h', 'B-TIME'), ('đến', 'O'), ('12h', 'B-TIME'), ('ở', 'O'), ('phòng', 'B-LOC'), ('hội', 'I-LOC'), ('thảo', 'I-LOC')],
    [('Seminar', 'O'), ('14h', 'B-TIME'), ('chiều', 'I-TIME'), ('nay', 'I-TIME'), ('tại', 'O'), ('trung', 'B-LOC'), ('tâm', 'I-LOC'), ('hội', 'I-LOC'), ('nghị', 'I-LOC')],
    [('Workshop', 'O'), ('9h', 'B-TIME'), ('sáng', 'I-TIME'), ('chủ', 'I-TIME'), ('nhật', 'I-TIME'), ('ở', 'O'), ('tầng', 'B-LOC'), ('5', 'I-LOC')],
    [('Họp', 'O'), ('ban', 'O'), ('giám', 'O'), ('đốc', 'O'), ('10h30', 'B-TIME'), ('sáng', 'I-TIME'), ('mai', 'I-TIME'), ('phòng', 'B-LOC'), ('VIP', 'I-LOC')],
    [('Thuyết', 'O'), ('trình', 'O'), ('lúc', 'O'), ('15h30', 'B-TIME'), ('tại', 'O'), ('hội', 'B-LOC'), ('trường', 'I-LOC'), ('lớn', 'I-LOC')],
    [('Conference', 'O'), ('8h30', 'B-TIME'), ('sáng', 'I-TIME'), ('thứ', 'I-TIME'), ('sáu', 'I-TIME'), ('ở', 'O'), ('khách', 'B-LOC'), ('sạn', 'I-LOC'), ('Sheraton', 'I-LOC')],
    [('Đào', 'O'), ('tạo', 'O'), ('từ', 'O'), ('9h', 'B-TIME'), ('đến', 'O'), ('17h', 'B-TIME'), ('tại', 'O'), ('trung', 'B-LOC'), ('tâm', 'I-LOC'), ('đào', 'I-LOC'), ('tạo', 'I-LOC')],
    [('Cuộc', 'O'), ('họp', 'O'), ('13h', 'B-TIME'), ('trưa', 'I-TIME'), ('nay', 'I-TIME'), ('phòng', 'B-LOC'), ('301', 'I-LOC'), ('toà', 'I-LOC'), ('B', 'I-LOC')],
    [('Gặp', 'O'), ('mặt', 'O'), ('6h', 'B-TIME'), ('tối', 'I-TIME'), ('mai', 'I-TIME'), ('tại', 'O'), ('nhà', 'B-LOC'), ('hàng', 'I-LOC'), ('Starbucks', 'I-LOC')],
    [('Họp', 'O'), ('online', 'O'), ('11h', 'B-TIME'), ('trưa', 'I-TIME'), ('thứ', 'I-TIME'), ('năm', 'I-TIME'), ('qua', 'O'), ('Zoom', 'O')],
    [('Interview', 'O'), ('ứng', 'O'), ('viên', 'O'), ('14h30', 'B-TIME'), ('chiều', 'I-TIME'), ('ở', 'O'), ('phòng', 'B-LOC'), ('HR', 'I-LOC')],
    [('Review', 'O'), ('dự', 'O'), ('án', 'O'), ('16h', 'B-TIME'), ('chiều', 'I-TIME'), ('tại', 'O'), ('phòng', 'B-LOC'), ('làm', 'I-LOC'), ('việc', 'I-LOC'), ('chung', 'I-LOC')],
    [('Brainstorm', 'O'), ('8h45', 'B-TIME'), ('sáng', 'I-TIME'), ('mai', 'I-TIME'), ('ở', 'O'), ('căn', 'B-LOC'), ('tin', 'I-LOC'), ('số', 'I-LOC'), ('7', 'I-LOC')],
    [('Demo', 'O'), ('sản', 'O'), ('phẩm', 'O'), ('10h15', 'B-TIME'), ('sáng', 'I-TIME'), ('tại', 'O'), ('showroom', 'B-LOC'), ('chính', 'I-LOC')],
    [('Kick-off', 'O'), ('dự', 'O'), ('án', 'O'), ('9h', 'B-TIME'), ('sáng', 'I-TIME'), ('thứ', 'I-TIME'), ('ba', 'I-TIME'), ('phòng', 'B-LOC'), ('meeting', 'I-LOC'), ('room', 'I-LOC'), ('1', 'I-LOC')],
    [('Stand-up', 'O'), ('meeting', 'O'), ('8h30', 'B-TIME'), ('sáng', 'I-TIME'), ('hàng', 'I-TIME'), ('ngày', 'I-TIME'), ('ở', 'O'), ('khu', 'B-LOC'), ('làm', 'I-LOC'), ('việc', 'I-LOC')],
    
    # Câu 21-40: Địa chỉ và vị trí
    [('Đi', 'O'), ('đến', 'O'), ('số', 'B-LOC'), ('123', 'I-LOC'), ('đường', 'I-LOC'), ('Nguyễn', 'I-LOC'), ('Huệ', 'I-LOC'), ('lúc', 'O'), ('15h', 'B-TIME')],
    [('Gặp', 'O'), ('nhau', 'O'), ('tại', 'O'), ('quận', 'B-LOC'), ('1', 'I-LOC'), ('TP', 'I-LOC'), ('HCM', 'I-LOC'), ('vào', 'O'), ('20h', 'B-TIME'), ('tối', 'I-TIME')],
    [('Địa', 'O'), ('chỉ', 'O'), ('văn', 'B-LOC'), ('phòng', 'I-LOC'), ('phường', 'I-LOC'), ('Bến', 'I-LOC'), ('Nghé', 'I-LOC'), ('quận', 'I-LOC'), ('1', 'I-LOC')],
    [('Tham', 'O'), ('quan', 'O'), ('bảo', 'B-LOC'), ('tàng', 'I-LOC'), ('lịch', 'I-LOC'), ('sử', 'I-LOC'), ('9h', 'B-TIME'), ('sáng', 'I-TIME')],
    [('Đến', 'O'), ('trường', 'B-LOC'), ('đại', 'I-LOC'), ('học', 'I-LOC'), ('Bách', 'I-LOC'), ('Khoa', 'I-LOC'), ('lúc', 'O'), ('7h30', 'B-TIME')],
    [('Mua', 'O'), ('sắm', 'O'), ('tại', 'O'), ('siêu', 'B-LOC'), ('thị', 'I-LOC'), ('BigC', 'I-LOC'), ('chiều', 'B-TIME'), ('mai', 'I-TIME')],
    [('Ăn', 'O'), ('tối', 'O'), ('ở', 'O'), ('nhà', 'B-LOC'), ('hàng', 'I-LOC'), ('Phở', 'I-LOC'), ('24', 'I-LOC'), ('18h30', 'B-TIME')],
    [('Làm', 'O'), ('việc', 'O'), ('tại', 'O'), ('tòa', 'B-LOC'), ('nhà', 'I-LOC'), ('Landmark', 'I-LOC'), ('từ', 'O'), ('8h', 'B-TIME')],
    [('Đi', 'O'), ('khám', 'O'), ('bệnh', 'O'), ('viện', 'B-LOC'), ('Chợ', 'I-LOC'), ('Rẫy', 'I-LOC'), ('sáng', 'B-TIME'), ('mai', 'I-TIME')],
    [('Học', 'O'), ('tại', 'O'), ('trung', 'B-LOC'), ('tâm', 'I-LOC'), ('ngoại', 'I-LOC'), ('ngữ', 'I-LOC'), ('19h', 'B-TIME'), ('tối', 'I-TIME')],
    [('Gửi', 'O'), ('xe', 'O'), ('ở', 'O'), ('bãi', 'B-LOC'), ('đỗ', 'I-LOC'), ('xe', 'I-LOC'), ('tầng', 'I-LOC'), ('hầm', 'I-LOC')],
    [('Tập', 'O'), ('gym', 'O'), ('tại', 'O'), ('trung', 'B-LOC'), ('tâm', 'I-LOC'), ('thể', 'I-LOC'), ('thao', 'I-LOC'), ('6h', 'B-TIME'), ('sáng', 'I-TIME')],
    [('Đi', 'O'), ('cà', 'O'), ('phê', 'O'), ('quán', 'B-LOC'), ('Highlands', 'I-LOC'), ('Coffee', 'I-LOC'), ('15h', 'B-TIME')],
    [('Mua', 'O'), ('vé', 'O'), ('tại', 'O'), ('rạp', 'B-LOC'), ('chiếu', 'I-LOC'), ('phim', 'I-LOC'), ('CGV', 'I-LOC'), ('19h30', 'B-TIME')],
    [('Đến', 'O'), ('sân', 'B-LOC'), ('bay', 'I-LOC'), ('Tân', 'I-LOC'), ('Sơn', 'I-LOC'), ('Nhất', 'I-LOC'), ('5h', 'B-TIME'), ('sáng', 'I-TIME')],
    [('Ở', 'O'), ('khách', 'B-LOC'), ('sạn', 'I-LOC'), ('Rex', 'I-LOC'), ('Hotel', 'I-LOC'), ('đến', 'O'), ('22h', 'B-TIME'), ('đêm', 'I-TIME')],
    [('Làm', 'O'), ('việc', 'O'), ('tại', 'O'), ('văn', 'B-LOC'), ('phòng', 'I-LOC'), ('chi', 'I-LOC'), ('nhánh', 'I-LOC'), ('Hà', 'I-LOC'), ('Nội', 'I-LOC')],
    [('Gặp', 'O'), ('tại', 'O'), ('ngân', 'B-LOC'), ('hàng', 'I-LOC'), ('Vietcombank', 'I-LOC'), ('9h', 'B-TIME'), ('sáng', 'I-TIME')],
    [('Đi', 'O'), ('học', 'O'), ('ở', 'O'), ('trung', 'B-LOC'), ('tâm', 'I-LOC'), ('tin', 'I-LOC'), ('học', 'I-LOC'), ('từ', 'O'), ('13h', 'B-TIME')],
    [('Tham', 'O'), ('gia', 'O'), ('sự', 'O'), ('kiện', 'O'), ('tại', 'O'), ('nhà', 'B-LOC'), ('văn', 'I-LOC'), ('hóa', 'I-LOC'), ('thanh', 'I-LOC'), ('niên', 'I-LOC')],
    
    # Câu 41-60: Lịch làm việc và thời gian biểu
    [('Ca', 'O'), ('làm', 'O'), ('việc', 'O'), ('từ', 'O'), ('7h', 'B-TIME'), ('đến', 'O'), ('15h', 'B-TIME'), ('hàng', 'I-TIME'), ('ngày', 'I-TIME')],
    [('Nghỉ', 'O'), ('trưa', 'O'), ('từ', 'O'), ('12h', 'B-TIME'), ('đến', 'O'), ('13h', 'B-TIME'), ('tại', 'O'), ('căn', 'B-LOC'), ('tin', 'I-LOC')],
    [('Làm', 'O'), ('thêm', 'O'), ('giờ', 'O'), ('đến', 'O'), ('21h', 'B-TIME'), ('tối', 'I-TIME'), ('ở', 'O'), ('văn', 'B-LOC'), ('phòng', 'I-LOC')],
    [('Shift', 'O'), ('đêm', 'O'), ('từ', 'O'), ('23h', 'B-TIME'), ('đến', 'O'), ('7h', 'B-TIME'), ('sáng', 'I-TIME'), ('mai', 'I-TIME')],
    [('Part-time', 'O'), ('17h', 'B-TIME'), ('đến', 'O'), ('20h', 'B-TIME'), ('tại', 'O'), ('cửa', 'B-LOC'), ('hàng', 'I-LOC'), ('thời', 'I-LOC'), ('trang', 'I-LOC')],
    [('Deadline', 'O'), ('dự', 'O'), ('án', 'O'), ('23h59', 'B-TIME'), ('ngày', 'I-TIME'), ('mai', 'I-TIME')],
    [('Check-in', 'O'), ('8h', 'B-TIME'), ('sáng', 'I-TIME'), ('check-out', 'O'), ('17h30', 'B-TIME'), ('chiều', 'I-TIME')],
    [('Làm', 'O'), ('việc', 'O'), ('remote', 'O'), ('từ', 'O'), ('9h', 'B-TIME'), ('tại', 'O'), ('nhà', 'B-LOC'), ('riêng', 'I-LOC')],
    [('Tăng', 'O'), ('ca', 'O'), ('cuối', 'O'), ('tuần', 'O'), ('8h', 'B-TIME'), ('sáng', 'I-TIME'), ('chủ', 'I-TIME'), ('nhật', 'I-TIME')],
    [('Break', 'O'), ('15', 'B-TIME'), ('phút', 'I-TIME'), ('lúc', 'O'), ('10h30', 'B-TIME'), ('và', 'O'), ('15h30', 'B-TIME')],
    [('Họp', 'O'), ('weekly', 'O'), ('mỗi', 'O'), ('thứ', 'B-TIME'), ('hai', 'I-TIME'), ('9h', 'I-TIME'), ('sáng', 'I-TIME')],
    [('Review', 'O'), ('monthly', 'O'), ('cuối', 'B-TIME'), ('tháng', 'I-TIME'), ('tại', 'O'), ('phòng', 'B-LOC'), ('giám', 'I-LOC'), ('đốc', 'I-LOC')],
    [('Training', 'O'), ('nhân', 'O'), ('viên', 'O'), ('mới', 'O'), ('từ', 'O'), ('8h30', 'B-TIME'), ('đến', 'O'), ('16h30', 'B-TIME')],
    [('Lunch', 'O'), ('meeting', 'O'), ('12h30', 'B-TIME'), ('trưa', 'I-TIME'), ('ở', 'O'), ('nhà', 'B-LOC'), ('hàng', 'I-LOC'), ('gần', 'I-LOC'), ('công', 'I-LOC'), ('ty', 'I-LOC')],
    [('Night', 'O'), ('shift', 'O'), ('22h', 'B-TIME'), ('đêm', 'I-TIME'), ('đến', 'O'), ('6h', 'B-TIME'), ('sáng', 'I-TIME')],
    [('Flextime', 'O'), ('từ', 'O'), ('7h', 'B-TIME'), ('đến', 'O'), ('10h', 'B-TIME'), ('sáng', 'I-TIME')],
    [('Nghỉ', 'O'), ('giữa', 'O'), ('giờ', 'O'), ('từ', 'O'), ('14h', 'B-TIME'), ('đến', 'O'), ('14h30', 'B-TIME')],
    [('Onboarding', 'O'), ('nhân', 'O'), ('viên', 'O'), ('9h', 'B-TIME'), ('sáng', 'I-TIME'), ('thứ', 'I-TIME'), ('hai', 'I-TIME'), ('tại', 'O'), ('phòng', 'B-LOC'), ('training', 'I-LOC')],
    [('Annual', 'O'), ('review', 'O'), ('15h', 'B-TIME'), ('chiều', 'I-TIME'), ('thứ', 'I-TIME'), ('sáu', 'I-TIME')],
    [('Team', 'O'), ('building', 'O'), ('cả', 'B-TIME'), ('ngày', 'I-TIME'), ('chủ', 'I-TIME'), ('nhật', 'I-TIME'), ('tại', 'O'), ('resort', 'B-LOC'), ('Vũng', 'I-LOC'), ('Tàu', 'I-LOC')],
    
    # Câu 61-80: Giao thông và di chuyển
    [('Đi', 'O'), ('xe', 'O'), ('bus', 'O'), ('lúc', 'O'), ('7h30', 'B-TIME'), ('từ', 'O'), ('bến', 'B-LOC'), ('xe', 'I-LOC'), ('Miền', 'I-LOC'), ('Đông', 'I-LOC')],
    [('Chuyến', 'O'), ('tàu', 'O'), ('6h45', 'B-TIME'), ('sáng', 'I-TIME'), ('từ', 'O'), ('ga', 'B-LOC'), ('Sài', 'I-LOC'), ('Gòn', 'I-LOC')],
    [('Bay', 'O'), ('10h30', 'B-TIME'), ('sáng', 'I-TIME'), ('từ', 'O'), ('sân', 'B-LOC'), ('bay', 'I-LOC'), ('Nội', 'I-LOC'), ('Bài', 'I-LOC')],
    [('Taxi', 'O'), ('đón', 'O'), ('7h15', 'B-TIME'), ('sáng', 'I-TIME'), ('tại', 'O'), ('nhà', 'B-LOC'), ('số', 'I-LOC'), ('45', 'I-LOC')],
    [('Xe', 'O'), ('khách', 'O'), ('về', 'O'), ('quê', 'O'), ('22h30', 'B-TIME'), ('đêm', 'I-TIME'), ('từ', 'O'), ('bến', 'B-LOC'), ('xe', 'I-LOC')],
    [('Đi', 'O'), ('metro', 'O'), ('8h', 'B-TIME'), ('sáng', 'I-TIME'), ('từ', 'O'), ('ga', 'B-LOC'), ('Bến', 'I-LOC'), ('Thành', 'I-LOC')],
    [('Grab', 'O'), ('car', 'O'), ('đến', 'O'), ('lúc', 'O'), ('19h45', 'B-TIME'), ('tại', 'O'), ('tòa', 'B-LOC'), ('nhà', 'I-LOC'), ('Diamond', 'I-LOC')],
    [('Chuyến', 'O'), ('bay', 'O'), ('delay', 'O'), ('đến', 'O'), ('14h20', 'B-TIME'), ('chiều', 'I-TIME')],
    [('Đi', 'O'), ('tàu', 'O'), ('điện', 'O'), ('7h30', 'B-TIME'), ('từ', 'O'), ('ga', 'B-LOC'), ('trung', 'I-LOC'), ('tâm', 'I-LOC')],
    [('Xe', 'O'), ('buýt', 'O'), ('số', 'O'), ('152', 'O'), ('6h30', 'B-TIME'), ('sáng', 'I-TIME'), ('từ', 'O'), ('trạm', 'B-LOC'), ('BX', 'I-LOC'), ('An', 'I-LOC'), ('Sương', 'I-LOC')],
    [('Ship', 'O'), ('hàng', 'O'), ('đến', 'O'), ('cảng', 'B-LOC'), ('Cát', 'I-LOC'), ('Lái', 'I-LOC'), ('lúc', 'O'), ('16h', 'B-TIME')],
    [('Đi', 'O'), ('xe', 'O'), ('ôm', 'O'), ('5h45', 'B-TIME'), ('sáng', 'I-TIME'), ('từ', 'O'), ('ngã', 'B-LOC'), ('tư', 'I-LOC'), ('Hàng', 'I-LOC'), ('Xanh', 'I-LOC')],
    [('Ferry', 'O'), ('sang', 'O'), ('đảo', 'B-LOC'), ('Phú', 'I-LOC'), ('Quốc', 'I-LOC'), ('9h30', 'B-TIME'), ('sáng', 'I-TIME')],
    [('Helicopter', 'O'), ('tour', 'O'), ('15h', 'B-TIME'), ('chiều', 'I-TIME'), ('từ', 'O'), ('sân', 'B-LOC'), ('bay', 'I-LOC')],
    [('Xe', 'O'), ('đạp', 'O'), ('thuê', 'O'), ('8h', 'B-TIME'), ('sáng', 'I-TIME'), ('tại', 'O'), ('công', 'B-LOC'), ('viên', 'I-LOC'), ('Tao', 'I-LOC'), ('Đàn', 'I-LOC')],
    [('Đi', 'O'), ('bộ', 'O'), ('từ', 'O'), ('nhà', 'B-LOC'), ('đến', 'O'), ('công', 'B-LOC'), ('ty', 'I-LOC'), ('30', 'B-TIME'), ('phút', 'I-TIME')],
    [('Xe', 'O'), ('container', 'O'), ('đến', 'O'), ('cảng', 'B-LOC'), ('Sài', 'I-LOC'), ('Gòn', 'I-LOC'), ('11h', 'B-TIME')],
    [('Thuê', 'O'), ('xe', 'O'), ('máy', 'O'), ('10h', 'B-TIME'), ('sáng', 'I-TIME'), ('tại', 'O'), ('cửa', 'B-LOC'), ('hàng', 'I-LOC'), ('thuê', 'I-LOC'), ('xe', 'I-LOC')],
    [('Đi', 'O'), ('thuyền', 'O'), ('du', 'O'), ('lịch', 'O'), ('16h30', 'B-TIME'), ('từ', 'O'), ('bến', 'B-LOC'), ('Nhà', 'I-LOC'), ('Rồng', 'I-LOC')],
    [('Transit', 'O'), ('tại', 'O'), ('sân', 'B-LOC'), ('bay', 'I-LOC'), ('Singapore', 'I-LOC'), ('3', 'B-TIME'), ('tiếng', 'I-TIME')],
    
    # Câu 81-100: Ăn uống và giải trí
    [('Ăn', 'O'), ('sáng', 'O'), ('7h', 'B-TIME'), ('sáng', 'I-TIME'), ('tại', 'O'), ('quán', 'B-LOC'), ('phở', 'I-LOC'), ('Hà', 'I-LOC'), ('Nội', 'I-LOC')],
    [('Lunch', 'O'), ('break', 'O'), ('12h30', 'B-TIME'), ('trưa', 'I-TIME'), ('ở', 'O'), ('food', 'B-LOC'), ('court', 'I-LOC'), ('tầng', 'I-LOC'), ('3', 'I-LOC')],
    [('Happy', 'O'), ('hour', 'O'), ('17h', 'B-TIME'), ('đến', 'O'), ('19h', 'B-TIME'), ('tại', 'O'), ('bar', 'B-LOC'), ('rooftop', 'I-LOC')],
    [('Dinner', 'O'), ('date', 'O'), ('19h30', 'B-TIME'), ('tối', 'I-TIME'), ('ở', 'O'), ('nhà', 'B-LOC'), ('hàng', 'I-LOC'), ('Pháp', 'I-LOC')],
    [('Buffet', 'O'), ('tối', 'O'), ('18h', 'B-TIME'), ('tại', 'O'), ('khách', 'B-LOC'), ('sạn', 'I-LOC'), ('5', 'I-LOC'), ('sao', 'I-LOC')],
    [('Uống', 'O'), ('cà', 'O'), ('phê', 'O'), ('sáng', 'O'), ('8h30', 'B-TIME'), ('quán', 'B-LOC'), ('The', 'I-LOC'), ('Coffee', 'I-LOC'), ('House', 'I-LOC')],
    [('BBQ', 'O'), ('party', 'O'), ('19h', 'B-TIME'), ('tối', 'I-TIME'), ('chủ', 'I-TIME'), ('nhật', 'I-TIME'), ('tại', 'O'), ('sân', 'B-LOC'), ('thượng', 'I-LOC')],
    [('Ăn', 'O'), ('khuya', 'O'), ('23h', 'B-TIME'), ('đêm', 'I-TIME'), ('ở', 'O'), ('khu', 'B-LOC'), ('phố', 'I-LOC'), ('đi', 'I-LOC'), ('bộ', 'I-LOC')],
    [('Brunch', 'O'), ('cuối', 'O'), ('tuần', 'O'), ('10h30', 'B-TIME'), ('sáng', 'I-TIME'), ('tại', 'O'), ('bistro', 'B-LOC'), ('Pháp', 'I-LOC')],
    [('All-you-can-eat', 'O'), ('từ', 'O'), ('18h', 'B-TIME'), ('đến', 'O'), ('22h', 'B-TIME'), ('tại', 'O'), ('nhà', 'B-LOC'), ('hàng', 'I-LOC'), ('Nhật', 'I-LOC')],
    [('Xem', 'O'), ('phim', 'O'), ('20h45', 'B-TIME'), ('tối', 'I-TIME'), ('rạp', 'B-LOC'), ('Galaxy', 'I-LOC'), ('Cinema', 'I-LOC')],
    [('Concert', 'O'), ('19h30', 'B-TIME'), ('tối', 'I-TIME'), ('tại', 'O'), ('nhà', 'B-LOC'), ('hát', 'I-LOC'), ('lớn', 'I-LOC')],
    [('Karaoke', 'O'), ('21h', 'B-TIME'), ('đến', 'O'), ('1h', 'B-TIME'), ('sáng', 'I-TIME'), ('ở', 'O'), ('Arirang', 'B-LOC')],
    [('Đi', 'O'), ('club', 'O'), ('22h30', 'B-TIME'), ('đêm', 'I-TIME'), ('tại', 'O'), ('quận', 'B-LOC'), ('1', 'I-LOC')],
    [('Spa', 'O'), ('massage', 'O'), ('14h', 'B-TIME'), ('chiều', 'I-TIME'), ('tại', 'O'), ('trung', 'B-LOC'), ('tâm', 'I-LOC'), ('thẩm', 'I-LOC'), ('mỹ', 'I-LOC')],
    [('Bowling', 'O'), ('18h30', 'B-TIME'), ('tối', 'I-TIME'), ('ở', 'O'), ('Diamond', 'B-LOC'), ('Bowling', 'I-LOC')],
    [('Pool', 'O'), ('party', 'O'), ('15h', 'B-TIME'), ('chiều', 'I-TIME'), ('chủ', 'I-TIME'), ('nhật', 'I-TIME'), ('tại', 'O'), ('resort', 'B-LOC')],
    [('Game', 'O'), ('center', 'O'), ('19h', 'B-TIME'), ('tối', 'I-TIME'), ('ở', 'O'), ('tầng', 'B-LOC'), ('6', 'I-LOC'), ('Vincom', 'I-LOC')],
    [('Đi', 'O'), ('chợ', 'O'), ('đêm', 'O'), ('21h', 'B-TIME'), ('tối', 'I-TIME'), ('tại', 'O'), ('chợ', 'B-LOC'), ('Bến', 'I-LOC'), ('Thành', 'I-LOC')],
    [('Live', 'O'), ('music', 'O'), ('20h', 'B-TIME'), ('tối', 'I-TIME'), ('tại', 'O'), ('acoustic', 'B-LOC'), ('bar', 'I-LOC')],
    
    # Câu 101-120: Học tập và đào tạo
    [('Lớp', 'O'), ('học', 'O'), ('tiếng', 'O'), ('Anh', 'O'), ('19h', 'B-TIME'), ('tối', 'I-TIME'), ('tại', 'O'), ('trung', 'B-LOC'), ('tâm', 'I-LOC'), ('ILA', 'I-LOC')],
    [('Khóa', 'O'), ('học', 'O'), ('lái', 'O'), ('xe', 'O'), ('8h', 'B-TIME'), ('sáng', 'I-TIME'), ('ở', 'O'), ('trung', 'B-LOC'), ('tâm', 'I-LOC'), ('đào', 'I-LOC'), ('tạo', 'I-LOC')],
    [('Seminar', 'O'), ('marketing', 'O'), ('14h', 'B-TIME'), ('chiều', 'I-TIME'), ('thứ', 'I-TIME'), ('bảy', 'I-TIME'), ('phòng', 'B-LOC'), ('hội', 'I-LOC'), ('nghị', 'I-LOC')],
    [('Workshop', 'O'), ('photography', 'O'), ('9h30', 'B-TIME'), ('sáng', 'I-TIME'), ('chủ', 'I-TIME'), ('nhật', 'I-TIME'), ('tại', 'O'), ('studio', 'B-LOC')],
    [('Lớp', 'O'), ('yoga', 'O'), ('6h30', 'B-TIME'), ('sáng', 'I-TIME'), ('ở', 'O'), ('công', 'B-LOC'), ('viên', 'I-LOC'), ('Lê', 'I-LOC'), ('Văn', 'I-LOC'), ('Tám', 'I-LOC')],
    [('Khóa', 'O'), ('học', 'O'), ('nấu', 'O'), ('ăn', 'O'), ('10h', 'B-TIME'), ('sáng', 'I-TIME'), ('thứ', 'I-TIME'), ('hai', 'I-TIME'), ('tại', 'O'), ('bếp', 'B-LOC'), ('training', 'I-LOC')],
    [('Class', 'O'), ('piano', 'O'), ('16h', 'B-TIME'), ('chiều', 'I-TIME'), ('ở', 'O'), ('trung', 'B-LOC'), ('tâm', 'I-LOC'), ('âm', 'I-LOC'), ('nhạc', 'I-LOC')],
    [('Thi', 'O'), ('TOEIC', 'O'), ('8h30', 'B-TIME'), ('sáng', 'I-TIME'), ('chủ', 'I-TIME'), ('nhật', 'I-TIME'), ('tại', 'O'), ('trường', 'B-LOC'), ('đại', 'I-LOC'), ('học', 'I-LOC')],
    [('Học', 'O'), ('lái', 'O'), ('xe', 'O'), ('máy', 'O'), ('15h', 'B-TIME'), ('chiều', 'I-TIME'), ('ở', 'O'), ('sân', 'B-LOC'), ('tập', 'I-LOC'), ('lái', 'I-LOC')],
    [('Khóa', 'O'), ('học', 'O'), ('Excel', 'O'), ('nâng', 'O'), ('cao', 'O'), ('13h30', 'B-TIME'), ('tại', 'O'), ('phòng', 'B-LOC'), ('máy', 'I-LOC'), ('tính', 'I-LOC')],
    [('Workshop', 'O'), ('design', 'O'), ('thinking', 'O'), ('9h', 'B-TIME'), ('sáng', 'I-TIME'), ('phòng', 'B-LOC'), ('innovation', 'I-LOC'), ('lab', 'I-LOC')],
    [('Lớp', 'O'), ('học', 'O'), ('múa', 'O'), ('20h', 'B-TIME'), ('tối', 'I-TIME'), ('tại', 'O'), ('trung', 'B-LOC'), ('tâm', 'I-LOC'), ('văn', 'I-LOC'), ('hóa', 'I-LOC')],
    [('Training', 'O'), ('sales', 'O'), ('skills', 'O'), ('8h30', 'B-TIME'), ('sáng', 'I-TIME'), ('phòng', 'B-LOC'), ('đào', 'I-LOC'), ('tạo', 'I-LOC'), ('A', 'I-LOC')],
    [('Khóa', 'O'), ('học', 'O'), ('digital', 'O'), ('marketing', 'O'), ('19h', 'B-TIME'), ('tối', 'I-TIME'), ('online', 'O')],
    [('Lớp', 'O'), ('học', 'O'), ('vẽ', 'O'), ('17h', 'B-TIME'), ('chiều', 'I-TIME'), ('ở', 'O'), ('xưởng', 'B-LOC'), ('mỹ', 'I-LOC'), ('thuật', 'I-LOC')],
    [('Seminar', 'O'), ('đầu', 'O'), ('tư', 'O'), ('14h30', 'B-TIME'), ('chiều', 'I-TIME'), ('tại', 'O'), ('trung', 'B-LOC'), ('tâm', 'I-LOC'), ('hội', 'I-LOC'), ('nghị', 'I-LOC')],
    [('Workshop', 'O'), ('team', 'O'), ('building', 'O'), ('cả', 'B-TIME'), ('ngày', 'I-TIME'), ('tại', 'O'), ('resort', 'B-LOC'), ('gần', 'I-LOC'), ('Hà', 'I-LOC'), ('Nội', 'I-LOC')],
    [('Thi', 'O'), ('bằng', 'O'), ('lái', 'O'), ('xe', 'O'), ('9h', 'B-TIME'), ('sáng', 'I-TIME'), ('tại', 'O'), ('sở', 'B-LOC'), ('GTVT', 'I-LOC')],
    [('Khóa', 'O'), ('học', 'O'), ('Python', 'O'), ('programming', 'O'), ('18h30', 'B-TIME'), ('tối', 'I-TIME'), ('online', 'O')],
    [('Lớp', 'O'), ('học', 'O'), ('cắt', 'O'), ('tóc', 'O'), ('10h', 'B-TIME'), ('sáng', 'I-TIME'), ('ở', 'O'), ('học', 'B-LOC'), ('viện', 'I-LOC'), ('tóc', 'I-LOC')],
    
    # Câu 121-140: Y tế và sức khỏe
    [('Khám', 'O'), ('bệnh', 'O'), ('8h30', 'B-TIME'), ('sáng', 'I-TIME'), ('tại', 'O'), ('bệnh', 'B-LOC'), ('viện', 'I-LOC'), ('Chợ', 'I-LOC'), ('Rẫy', 'I-LOC')],
    [('Khám', 'O'), ('răng', 'O'), ('14h', 'B-TIME'), ('chiều', 'I-TIME'), ('ở', 'O'), ('phòng', 'B-LOC'), ('khám', 'I-LOC'), ('nha', 'I-LOC'), ('khoa', 'I-LOC')],
    [('Chích', 'O'), ('ngừa', 'O'), ('9h', 'B-TIME'), ('sáng', 'I-TIME'), ('tại', 'O'), ('trung', 'B-LOC'), ('tâm', 'I-LOC'), ('y', 'I-LOC'), ('tế', 'I-LOC')],
    [('Siêu', 'O'), ('âm', 'O'), ('thai', 'O'), ('15h30', 'B-TIME'), ('chiều', 'I-TIME'), ('phòng', 'B-LOC'), ('khám', 'I-LOC'), ('phụ', 'I-LOC'), ('khoa', 'I-LOC')],
    [('Xét', 'O'), ('nghiệm', 'O'), ('máu', 'O'), ('7h', 'B-TIME'), ('sáng', 'I-TIME'), ('ở', 'O'), ('phòng', 'B-LOC'), ('lab', 'I-LOC')],
    [('Tập', 'O'), ('vật', 'O'), ('lý', 'O'), ('trị', 'O'), ('liệu', 'O'), ('16h', 'B-TIME'), ('chiều', 'I-TIME'), ('tại', 'O'), ('trung', 'B-LOC'), ('tâm', 'I-LOC'), ('phục', 'I-LOC'), ('hồi', 'I-LOC')],
    [('Khám', 'O'), ('mắt', 'O'), ('10h30', 'B-TIME'), ('sáng', 'I-TIME'), ('ở', 'O'), ('bệnh', 'B-LOC'), ('viện', 'I-LOC'), ('mắt', 'I-LOC')],
    [('Đo', 'O'), ('huyết', 'O'), ('áp', 'O'), ('8h', 'B-TIME'), ('sáng', 'I-TIME'), ('tại', 'O'), ('trạm', 'B-LOC'), ('y', 'I-LOC'), ('tế', 'I-LOC')],
    [('Khám', 'O'), ('tim', 'O'), ('mạch', 'O'), ('13h30', 'B-TIME'), ('chiều', 'I-TIME'), ('ở', 'O'), ('viện', 'B-LOC'), ('tim', 'I-LOC')],
    [('Chụp', 'O'), ('X-quang', 'O'), ('11h', 'B-TIME'), ('trưa', 'I-TIME'), ('phòng', 'B-LOC'), ('chẩn', 'I-LOC'), ('đoán', 'I-LOC'), ('hình', 'I-LOC'), ('ảnh', 'I-LOC')],
    [('Khám', 'O'), ('da', 'O'), ('liễu', 'O'), ('14h30', 'B-TIME'), ('chiều', 'I-TIME'), ('tại', 'O'), ('phòng', 'B-LOC'), ('khám', 'I-LOC'), ('da', 'I-LOC')],
    [('Tập', 'O'), ('thể', 'O'), ('dục', 'O'), ('phục', 'O'), ('hồi', 'O'), ('17h', 'B-TIME'), ('chiều', 'I-TIME'), ('ở', 'O'), ('trung', 'B-LOC'), ('tâm', 'I-LOC'), ('y', 'I-LOC'), ('tế', 'I-LOC')],
    [('Khám', 'O'), ('tổng', 'O'), ('quát', 'O'), ('7h30', 'B-TIME'), ('sáng', 'I-TIME'), ('bệnh', 'B-LOC'), ('viện', 'I-LOC'), ('quận', 'I-LOC'), ('1', 'I-LOC')],
    [('Chữa', 'O'), ('răng', 'O'), ('19h', 'B-TIME'), ('tối', 'I-TIME'), ('ở', 'O'), ('phòng', 'B-LOC'), ('nha', 'I-LOC'), ('khoa', 'I-LOC'), ('tư', 'I-LOC')],
    [('Massage', 'O'), ('trị', 'O'), ('liệu', 'O'), ('20h', 'B-TIME'), ('tối', 'I-TIME'), ('tại', 'O'), ('spa', 'B-LOC'), ('y', 'I-LOC'), ('học', 'I-LOC')],
    [('Khám', 'O'), ('tai', 'O'), ('mũi', 'O'), ('họng', 'O'), ('9h30', 'B-TIME'), ('sáng', 'I-TIME'), ('ở', 'O'), ('phòng', 'B-LOC'), ('TMH', 'I-LOC')],
    [('Tiêm', 'O'), ('vaccine', 'O'), ('COVID', 'O'), ('15h', 'B-TIME'), ('chiều', 'I-TIME'), ('tại', 'O'), ('trung', 'B-LOC'), ('tâm', 'I-LOC'), ('y', 'I-LOC'), ('tế', 'I-LOC')],
    [('Khám', 'O'), ('thần', 'O'), ('kinh', 'O'), ('10h', 'B-TIME'), ('sáng', 'I-TIME'), ('phòng', 'B-LOC'), ('khám', 'I-LOC'), ('thần', 'I-LOC'), ('kinh', 'I-LOC')],
    [('Chụp', 'O'), ('MRI', 'O'), ('16h30', 'B-TIME'), ('chiều', 'I-TIME'), ('tại', 'O'), ('trung', 'B-LOC'), ('tâm', 'I-LOC'), ('chẩn', 'I-LOC'), ('đoán', 'I-LOC')],
    [('Khám', 'O'), ('sản', 'O'), ('phụ', 'O'), ('khoa', 'O'), ('8h45', 'B-TIME'), ('sáng', 'I-TIME'), ('ở', 'O'), ('bệnh', 'B-LOC'), ('viện', 'I-LOC'), ('phụ', 'I-LOC'), ('sản', 'I-LOC')],
    
    # Câu 141-150: Mua sắm và dịch vụ
    [('Mua', 'O'), ('sắm', 'O'), ('10h', 'B-TIME'), ('sáng', 'I-TIME'), ('chủ', 'I-TIME'), ('nhật', 'I-TIME'), ('ở', 'O'), ('trung', 'B-LOC'), ('tâm', 'I-LOC'), ('Vincom', 'I-LOC')],
    [('Đi', 'O'), ('siêu', 'O'), ('thị', 'O'), ('19h', 'B-TIME'), ('tối', 'I-TIME'), ('tại', 'O'), ('BigC', 'B-LOC'), ('Thăng', 'I-LOC'), ('Long', 'I-LOC')],
    [('Cắt', 'O'), ('tóc', 'O'), ('14h30', 'B-TIME'), ('chiều', 'I-TIME'), ('ở', 'O'), ('salon', 'B-LOC'), ('tóc', 'I-LOC'), ('cao', 'I-LOC'), ('cấp', 'I-LOC')],
    [('Sửa', 'O'), ('xe', 'O'), ('máy', 'O'), ('8h', 'B-TIME'), ('sáng', 'I-TIME'), ('tại', 'O'), ('garage', 'B-LOC'), ('Honda', 'I-LOC')],
    [('Giặt', 'O'), ('khô', 'O'), ('17h', 'B-TIME'), ('chiều', 'I-TIME'), ('ở', 'O'), ('tiệm', 'B-LOC'), ('giặt', 'I-LOC'), ('là', 'I-LOC')],
    [('Làm', 'O'), ('nail', 'O'), ('15h30', 'B-TIME'), ('chiều', 'I-TIME'), ('tại', 'O'), ('tiệm', 'B-LOC'), ('nail', 'I-LOC'), ('Hàn', 'I-LOC'), ('Quốc', 'I-LOC')],
    [('Mua', 'O'), ('điện', 'O'), ('thoại', 'O'), ('11h', 'B-TIME'), ('trưa', 'I-TIME'), ('ở', 'O'), ('cửa', 'B-LOC'), ('hàng', 'I-LOC'), ('FPT', 'I-LOC')],
    [('Sửa', 'O'), ('laptop', 'O'), ('13h30', 'B-TIME'), ('chiều', 'I-TIME'), ('tại', 'O'), ('trung', 'B-LOC'), ('tâm', 'I-LOC'), ('bảo', 'I-LOC'), ('hành', 'I-LOC')],
    [('Đổi', 'O'), ('tiền', 'O'), ('9h15', 'B-TIME'), ('sáng', 'I-TIME'), ('ở', 'O'), ('ngân', 'B-LOC'), ('hàng', 'I-LOC'), ('Vietcombank', 'I-LOC')],
    [('Mua', 'O'), ('sách', 'O'), ('16h', 'B-TIME'), ('chiều', 'I-TIME'), ('tại', 'O'), ('hiệu', 'B-LOC'), ('sách', 'I-LOC'), ('Fahasa', 'I-LOC')],
    
    # Câu 151-200: Các trường hợp khó và biên để giải quyết lỗi phân loại
    
    # Nhóm 1: Tránh lỗi "tham lam" - Phân biệt giữa từ thường và địa điểm
    [('Hẹn', 'O'), ('cafe', 'O'), ('với', 'O'), ('An', 'O'), ('ở', 'O'), ('Starbucks', 'B-LOC'), ('Quận', 'I-LOC'), ('1', 'I-LOC')],
    [('Gặp', 'O'), ('mặt', 'O'), ('với', 'O'), ('Nam', 'O'), ('tại', 'O'), ('BigC', 'B-LOC'), ('Thăng', 'I-LOC'), ('Long', 'I-LOC')],
    [('Đi', 'O'), ('ăn', 'O'), ('với', 'O'), ('bạn', 'O'), ('ở', 'O'), ('nhà', 'B-LOC'), ('hàng', 'I-LOC'), ('Phở', 'I-LOC'), ('24', 'I-LOC')],
    [('Chơi', 'O'), ('game', 'O'), ('với', 'O'), ('anh', 'O'), ('tại', 'O'), ('cyber', 'B-LOC'), ('game', 'I-LOC')],
    [('Học', 'O'), ('bài', 'O'), ('với', 'O'), ('em', 'O'), ('ở', 'O'), ('thư', 'B-LOC'), ('viện', 'I-LOC')],
    
    # Nhóm 2: Phân biệt thứ trong tuần (TIME) vs địa danh có "thứ"
    [('Nộp', 'O'), ('báo', 'O'), ('cáo', 'O'), ('vào', 'O'), ('thứ', 'B-TIME'), ('Hai', 'I-TIME')],
    [('Deadline', 'O'), ('dự', 'O'), ('án', 'O'), ('vào', 'O'), ('thứ', 'B-TIME'), ('Sáu', 'I-TIME')],
    [('Họp', 'O'), ('team', 'O'), ('vào', 'O'), ('thứ', 'B-TIME'), ('Tư', 'I-TIME')],
    [('Nộp', 'O'), ('hồ', 'O'), ('sơ', 'O'), ('vào', 'O'), ('thứ', 'B-TIME'), ('Năm', 'I-TIME')],
    [('Presentation', 'O'), ('vào', 'O'), ('thứ', 'B-TIME'), ('Ba', 'I-TIME'), ('tuần', 'I-TIME'), ('sau', 'I-TIME')],
    
    # Nhóm 3: Các từ có thể gây nhầm lẫn - chỉ là từ thường
    [('Nộp', 'O'), ('deadline', 'O'), ('dự', 'O'), ('án', 'O'), ('sớm', 'O')],
    [('Hoàn', 'O'), ('thành', 'O'), ('báo', 'O'), ('cáo', 'O'), ('tốt', 'O')],
    [('Viết', 'O'), ('proposal', 'O'), ('mới', 'O'), ('cho', 'O'), ('dự', 'O'), ('án', 'O')],
    [('Review', 'O'), ('code', 'O'), ('của', 'O'), ('team', 'O'), ('developer', 'O')],
    [('Fix', 'O'), ('bug', 'O'), ('trong', 'O'), ('hệ', 'O'), ('thống', 'O')],
    
    # Nhóm 4: Câu phức tạp có cả TIME và LOC rõ ràng
    [('Họp', 'O'), ('với', 'O'), ('khách', 'O'), ('hàng', 'O'), ('10h', 'B-TIME'), ('sáng', 'I-TIME'), ('mai', 'I-TIME'), ('tại', 'O'), ('tòa', 'B-LOC'), ('nhà', 'I-LOC'), ('Bitexco', 'I-LOC')],
    [('Đào', 'O'), ('tạo', 'O'), ('nhân', 'O'), ('viên', 'O'), ('từ', 'O'), ('9h', 'B-TIME'), ('đến', 'O'), ('17h', 'B-TIME'), ('tại', 'O'), ('phòng', 'B-LOC'), ('hội', 'I-LOC'), ('thảo', 'I-LOC'), ('tầng', 'I-LOC'), ('5', 'I-LOC')],
    [('Giao', 'O'), ('hàng', 'O'), ('cho', 'O'), ('khách', 'O'), ('trước', 'O'), ('15h', 'B-TIME'), ('chiều', 'I-TIME'), ('tại', 'O'), ('văn', 'B-LOC'), ('phòng', 'I-LOC'), ('chi', 'I-LOC'), ('nhánh', 'I-LOC')],
    [('Kiểm', 'O'), ('tra', 'O'), ('tiến', 'O'), ('độ', 'O'), ('lúc', 'O'), ('14h30', 'B-TIME'), ('ở', 'O'), ('phòng', 'B-LOC'), ('làm', 'I-LOC'), ('việc', 'I-LOC')],
    [('Thuyết', 'O'), ('trình', 'O'), ('sản', 'O'), ('phẩm', 'O'), ('8h45', 'B-TIME'), ('sáng', 'I-TIME'), ('tại', 'O'), ('showroom', 'B-LOC'), ('chính', 'I-LOC')],
    
    # Nhóm 5: Các câu có từ đệm không phải địa điểm
    [('Cùng', 'O'), ('đi', 'O'), ('ăn', 'O'), ('trưa', 'O'), ('12h30', 'B-TIME')],
    [('Cùng', 'O'), ('họp', 'O'), ('bàn', 'O'), ('về', 'O'), ('dự', 'O'), ('án', 'O')],
    [('Cùng', 'O'), ('thảo', 'O'), ('luận', 'O'), ('vấn', 'O'), ('đề', 'O'), ('quan', 'O'), ('trọng', 'O')],
    [('Cùng', 'O'), ('xem', 'O'), ('xét', 'O'), ('báo', 'O'), ('cáo', 'O'), ('tài', 'O'), ('chính', 'O')],
    [('Cùng', 'O'), ('phát', 'O'), ('triển', 'O'), ('ý', 'O'), ('tưởng', 'O'), ('mới', 'O')],
    
    # Nhóm 6: Địa danh thật vs từ thường có chung âm
    [('Đến', 'O'), ('Hà', 'B-LOC'), ('Nội', 'I-LOC'), ('công', 'O'), ('tác', 'O')],
    [('Bay', 'O'), ('từ', 'O'), ('Sài', 'B-LOC'), ('Gòn', 'I-LOC'), ('ra', 'O'), ('Huế', 'B-LOC')],
    [('Nghỉ', 'O'), ('mát', 'O'), ('ở', 'O'), ('Đà', 'B-LOC'), ('Lạt', 'I-LOC'), ('3', 'B-TIME'), ('ngày', 'I-TIME')],
    [('Du', 'O'), ('lịch', 'O'), ('Phú', 'B-LOC'), ('Quốc', 'I-LOC'), ('cuối', 'B-TIME'), ('tuần', 'I-TIME')],
    [('Về', 'O'), ('quê', 'O'), ('Long', 'B-LOC'), ('An', 'I-LOC'), ('thăm', 'O'), ('gia', 'O'), ('đình', 'O')],
    
    # Nhóm 7: Thời gian phức tạp
    [('Làm', 'O'), ('việc', 'O'), ('từ', 'O'), ('8h30', 'B-TIME'), ('sáng', 'I-TIME'), ('đến', 'O'), ('17h30', 'B-TIME'), ('chiều', 'I-TIME')],
    [('Nghỉ', 'O'), ('từ', 'O'), ('12h', 'B-TIME'), ('trưa', 'I-TIME'), ('đến', 'O'), ('13h15', 'B-TIME')],
    [('Tăng', 'O'), ('ca', 'O'), ('từ', 'O'), ('18h', 'B-TIME'), ('đến', 'O'), ('22h', 'B-TIME'), ('tối', 'I-TIME')],
    [('Học', 'O'), ('thêm', 'O'), ('từ', 'O'), ('19h30', 'B-TIME'), ('đến', 'O'), ('21h30', 'B-TIME')],
    [('Họp', 'O'), ('khẩn', 'O'), ('từ', 'O'), ('20h', 'B-TIME'), ('đến', 'O'), ('22h30', 'B-TIME'), ('đêm', 'I-TIME')],
    
    # Nhóm 8: Tránh nhầm lẫn từ có chữ số
    [('Mua', 'O'), ('iPhone', 'O'), ('15', 'O'), ('Pro', 'O'), ('Max', 'O')],
    [('Cài', 'O'), ('Windows', 'O'), ('11', 'O'), ('cho', 'O'), ('laptop', 'O')],
    [('Xem', 'O'), ('phim', 'O'), ('Fast', 'O'), ('&', 'O'), ('Furious', 'O'), ('9', 'O')],
    [('Đọc', 'O'), ('sách', 'O'), ('Harry', 'O'), ('Potter', 'O'), ('7', 'O')],
    [('Chơi', 'O'), ('FIFA', 'O'), ('23', 'O'), ('với', 'O'), ('bạn', 'O')],
    
    # Nhóm 9: Địa điểm có số vs thời gian có số
    [('Ở', 'O'), ('tầng', 'B-LOC'), ('5', 'I-LOC'), ('toà', 'I-LOC'), ('nhà', 'I-LOC')],
    [('Tại', 'O'), ('phòng', 'B-LOC'), ('301', 'I-LOC'), ('tòa', 'I-LOC'), ('B', 'I-LOC')],
    [('Đến', 'O'), ('số', 'B-LOC'), ('25', 'I-LOC'), ('đường', 'I-LOC'), ('Lý', 'I-LOC'), ('Tự', 'I-LOC'), ('Trọng', 'I-LOC')],
    [('Gặp', 'O'), ('tại', 'O'), ('lô', 'B-LOC'), ('B1', 'I-LOC'), ('chung', 'I-LOC'), ('cư', 'I-LOC')],
    [('Họp', 'O'), ('ở', 'O'), ('phòng', 'B-LOC'), ('A203', 'I-LOC')],
    
    # So sánh với thời gian:
    [('Họp', 'O'), ('lúc', 'O'), ('5h30', 'B-TIME'), ('chiều', 'I-TIME')],
    [('Đến', 'O'), ('trước', 'O'), ('10h15', 'B-TIME'), ('sáng', 'I-TIME')],
    [('Bắt', 'O'), ('đầu', 'O'), ('từ', 'O'), ('8h45', 'B-TIME')],
    [('Kết', 'O'), ('thúc', 'O'), ('lúc', 'O'), ('17h30', 'B-TIME')],
    [('Nghỉ', 'O'), ('lúc', 'O'), ('12h', 'B-TIME'), ('trưa', 'I-TIME')],
    
    # Nhóm 10: Câu dài và phức tạp
    [('Tham', 'O'), ('gia', 'O'), ('hội', 'O'), ('thảo', 'O'), ('về', 'O'), ('AI', 'O'), ('từ', 'O'), ('9h', 'B-TIME'), ('đến', 'O'), ('17h', 'B-TIME'), ('ngày', 'I-TIME'), ('mai', 'I-TIME'), ('tại', 'O'), ('trung', 'B-LOC'), ('tâm', 'I-LOC'), ('hội', 'I-LOC'), ('nghị', 'I-LOC'), ('quốc', 'I-LOC'), ('gia', 'I-LOC')],
    [('Thực', 'O'), ('hiện', 'O'), ('dự', 'O'), ('án', 'O'), ('nghiên', 'O'), ('cứu', 'O'), ('từ', 'O'), ('tháng', 'B-TIME'), ('1', 'I-TIME'), ('đến', 'O'), ('tháng', 'B-TIME'), ('6', 'I-TIME'), ('tại', 'O'), ('phòng', 'B-LOC'), ('thí', 'I-LOC'), ('nghiệm', 'I-LOC'), ('trường', 'I-LOC'), ('đại', 'I-LOC'), ('học', 'I-LOC')],
    [('Tổ', 'O'), ('chức', 'O'), ('sự', 'O'), ('kiện', 'O'), ('ra', 'O'), ('mắt', 'O'), ('sản', 'O'), ('phẩm', 'O'), ('20h', 'B-TIME'), ('tối', 'I-TIME'), ('thứ', 'I-TIME'), ('Bảy', 'I-TIME'), ('tại', 'O'), ('khách', 'B-LOC'), ('sạn', 'I-LOC'), ('5', 'I-LOC'), ('sao', 'I-LOC'), ('trung', 'I-LOC'), ('tâm', 'I-LOC'), ('thành', 'I-LOC'), ('phố', 'I-LOC')],
    
    # Nhóm 11: Các trường hợp đặc biệt khác
    [('Làm', 'O'), ('remote', 'O'), ('từ', 'O'), ('nhà', 'B-LOC'), ('riêng', 'I-LOC')],
    [('Work', 'O'), ('from', 'O'), ('home', 'O'), ('cả', 'B-TIME'), ('tuần', 'I-TIME')],
    [('Online', 'O'), ('meeting', 'O'), ('15h', 'B-TIME'), ('chiều', 'I-TIME')],
    [('Video', 'O'), ('call', 'O'), ('với', 'O'), ('team', 'O'), ('9h', 'B-TIME'), ('sáng', 'I-TIME')],
    [('Zoom', 'O'), ('meeting', 'O'), ('lúc', 'O'), ('14h', 'B-TIME')],
    
    # Nhóm 12: Thêm nhiều mẫu khó khác
    [('Đặt', 'O'), ('lịch', 'O'), ('hẹn', 'O'), ('với', 'O'), ('bác', 'O'), ('sĩ', 'O'), ('9h', 'B-TIME'), ('sáng', 'I-TIME'), ('thứ', 'I-TIME'), ('Hai', 'I-TIME')],
    [('Book', 'O'), ('vé', 'O'), ('máy', 'O'), ('bay', 'O'), ('chuyến', 'O'), ('6h30', 'B-TIME'), ('sáng', 'I-TIME')],
    [('Reserve', 'O'), ('bàn', 'O'), ('nhà', 'O'), ('hàng', 'O'), ('cho', 'O'), ('19h30', 'B-TIME'), ('tối', 'I-TIME')],
    [('Đăng', 'O'), ('ký', 'O'), ('khóa', 'O'), ('học', 'O'), ('bắt', 'O'), ('đầu', 'O'), ('tuần', 'B-TIME'), ('sau', 'I-TIME')],
    [('Gia', 'O'), ('hạn', 'O'), ('deadline', 'O'), ('đến', 'O'), ('cuối', 'B-TIME'), ('tháng', 'I-TIME')]
]

# Thống kê dữ liệu
def get_data_statistics():
    """
    Hàm tính toán thống kê về dữ liệu huấn luyện
    """
    total_sentences = len(TRAINING_DATA)
    total_tokens = sum(len(sentence) for sentence in TRAINING_DATA)
    
    # Đếm số lượng entity
    time_entities = 0
    loc_entities = 0
    o_labels = 0
    
    for sentence in TRAINING_DATA:
        for word, label in sentence:
            if label.startswith('B-TIME') or label.startswith('I-TIME'):
                time_entities += 1
            elif label.startswith('B-LOC') or label.startswith('I-LOC'):
                loc_entities += 1
            else:
                o_labels += 1
    
    return {
        'total_sentences': total_sentences,
        'total_tokens': total_tokens,
        'time_entities': time_entities,
        'location_entities': loc_entities,
        'o_labels': o_labels
    }

if __name__ == "__main__":
    stats = get_data_statistics()
    print("=== THỐNG KÊ DỮ LIỆU HUẤN LUYỆN ===")
    print(f"Tổng số câu: {stats['total_sentences']}")
    print(f"Tổng số từ: {stats['total_tokens']}")
    print(f"Số TIME entities: {stats['time_entities']}")
    print(f"Số LOCATION entities: {stats['location_entities']}")
    print(f"Số nhãn O: {stats['o_labels']}")
    print(f"Tỷ lệ TIME: {stats['time_entities']/stats['total_tokens']:.2%}")
    print(f"Tỷ lệ LOC: {stats['location_entities']/stats['total_tokens']:.2%}")

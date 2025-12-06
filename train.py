print("Đang import các thư viện...")
import sklearn_crfsuite
import joblib
from sklearn_crfsuite import metrics

# Import dữ liệu và module feature engineering
print("Đang import dữ liệu và module feature engineering...")
from training_data import TRAINING_DATA, get_data_statistics
from feature_engineering import sentences_to_features, sentences_to_labels

def train_crf_model():
    """
    Hàm chính thực hiện quá trình huấn luyện mô hình CRF NER
    """
    print("\n=== BẮT ĐẦU QUÁ TRÌNH HUẤN LUYỆN MÔ HÌNH NER ===")
    
    # 1. Hiển thị thống kê dữ liệu
    print("\n1. Thông tin dữ liệu huấn luyện:")
    stats = get_data_statistics()
    print(f"   - Tổng số câu: {stats['total_sentences']}")
    print(f"   - Tổng số từ: {stats['total_tokens']}")
    print(f"   - Số TIME entities: {stats['time_entities']}")
    print(f"   - Số LOCATION entities: {stats['location_entities']}")
    print(f"   - Số nhãn O: {stats['o_labels']}")
    print(f"   - Tỷ lệ TIME: {stats['time_entities']/stats['total_tokens']:.2%}")
    print(f"   - Tỷ lệ LOC: {stats['location_entities']/stats['total_tokens']:.2%}")
    
    # 2. Chuẩn bị dữ liệu
    print("\n2. Đang chuẩn bị dữ liệu...")
    print("   - Đang trích xuất features từ dữ liệu huấn luyện...")
    X_train = sentences_to_features(TRAINING_DATA)
    print("   - Đang trích xuất labels từ dữ liệu huấn luyện...")
    y_train = sentences_to_labels(TRAINING_DATA)
    
    print(f"   ✓ Đã chuẩn bị xong dữ liệu:")
    print(f"     • X_train: {len(X_train)} câu")
    print(f"     • y_train: {len(y_train)} câu")
    print(f"     • Tổng số features cho câu đầu tiên: {len(X_train[0][0]) if X_train and X_train[0] else 0}")
    
    # 3. Khởi tạo Model
    print("\n3. Đang khởi tạo mô hình CRF...")
    crf = sklearn_crfsuite.CRF(
        algorithm='lbfgs',      # Thuật toán tối ưu hóa L-BFGS
        c1=0.1,                 # L1 regularization coefficient
        c2=0.1,                 # L2 regularization coefficient  
        max_iterations=100,     # Số iteration tối đa
        all_possible_transitions=True  # Cho phép tất cả các transition có thể
    )
    print("   ✓ Đã khởi tạo mô hình CRF với các tham số tối ưu:")
    print("     • Algorithm: L-BFGS")
    print("     • L1 regularization (c1): 0.1")
    print("     • L2 regularization (c2): 0.1")
    print("     • Max iterations: 100")
    print("     • All possible transitions: True")
    
    # 4. Huấn luyện Model
    print("\n4. Bắt đầu huấn luyện model...")
    print("   (Quá trình này có thể mất vài phút tùy thuộc vào kích thước dữ liệu)")
    
    try:
        crf.fit(X_train, y_train)
        print("   ✓ Huấn luyện thành công!")
        
        # Hiển thị thông tin về quá trình huấn luyện
        try:
            # Một số version của sklearn-crfsuite có thuộc tính n_iter_
            if hasattr(crf, 'n_iter_'):
                print(f"   • Số iteration đã thực hiện: {crf.n_iter_}")
                print(f"   • Thuật toán hội tụ: {'Có' if crf.n_iter_ < 100 else 'Không (đạt max iterations)'}")
            else:
                print("   • Model đã được huấn luyện với các tham số tối ưu")
        except:
            print("   • Model đã được huấn luyện thành công")
        
    except Exception as e:
        print(f"   ❌ Lỗi trong quá trình huấn luyện: {str(e)}")
        return None
    
    # 5. Lưu Model
    model_filename = 'ner_crf.model'
    print(f"\n5. Đang lưu model vào file '{model_filename}'...")
    
    try:
        joblib.dump(crf, model_filename)
        print(f"   ✓ Đã lưu model thành công vào file '{model_filename}'")
        
    except Exception as e:
        print(f"   ❌ Lỗi khi lưu model: {str(e)}")
        return None
    
    print("\n=== HOÀN THÀNH QUÁ TRÌNH HUẤN LUYỆN ===")
    print("✅ Model đã sẵn sàng để sử dụng cho việc dự đoán NER!")
    
    return crf

def evaluate_on_training_data(crf):
    """
    Đánh giá model trên dữ liệu huấn luyện để kiểm tra tính đúng đắn
    """
    print("\n=== ĐÁNH GIÁ MODEL TRÊN DỮ LIỆU HUẤN LUYỆN ===")
    
    # Chuẩn bị dữ liệu
    X_train = sentences_to_features(TRAINING_DATA)
    y_train = sentences_to_labels(TRAINING_DATA)
    
    # Dự đoán
    print("Đang thực hiện dự đoán trên dữ liệu huấn luyện...")
    y_pred = crf.predict(X_train)
    
    # Tính toán metrics
    print("Đang tính toán các chỉ số đánh giá...")
    
    # Classification report
    labels = ['B-TIME', 'I-TIME', 'B-LOC', 'I-LOC']
    print("\nBáo cáo phân loại:")
    print(metrics.flat_classification_report(y_train, y_pred, labels=labels))
    
    # F1 score
    f1_score = metrics.flat_f1_score(y_train, y_pred, labels=labels, average='weighted')
    print(f"F1 Score (weighted): {f1_score:.4f}")
    
    return y_pred

def demonstrate_prediction(crf):
    """
    Demo dự đoán trên một vài câu mẫu
    """
    print("\n=== DEMO DỰ ĐOÁN TRÊN CÂU MẪU ===")
    
    # Lấy 3 câu đầu tiên từ training data để demo
    demo_sentences = TRAINING_DATA[:3]
    
    for i, sentence in enumerate(demo_sentences, 1):
        print(f"\nCâu {i}: {[word for word, _ in sentence]}")
        print(f"Nhãn thực tế: {[label for _, label in sentence]}")
        
        # Chuẩn bị features cho câu này
        sentence_features = sentences_to_features([sentence])
        
        # Dự đoán
        prediction = crf.predict(sentence_features)[0]
        print(f"Nhãn dự đoán: {prediction}")
        
        # So sánh
        actual = [label for _, label in sentence]
        correct = sum(1 for a, p in zip(actual, prediction) if a == p)
        accuracy = correct / len(actual) * 100
        print(f"Độ chính xác: {accuracy:.1f}% ({correct}/{len(actual)})")

def main():
    """
    Hàm main thực hiện toàn bộ pipeline huấn luyện
    """
    print("🚀 KHỞI ĐỘNG CHƯƠNG TRÌNH HUẤN LUYỆN MÔ HÌNH NER TIẾNG VIỆT")
    print("=" * 60)
    
    # Huấn luyện model
    crf = train_crf_model()
    
    if crf is not None:
        # Đánh giá model
        evaluate_on_training_data(crf)
        
        # Demo dự đoán
        demonstrate_prediction(crf)
        
        print("\n" + "=" * 60)
        print("🎉 CHƯƠNG TRÌNH HOÀN THÀNH THÀNH CÔNG!")
        print("📁 File model đã được lưu: 'ner_crf.model'")
        print("📘 Bạn có thể sử dụng model này để dự đoán NER cho văn bản mới.")
    else:
        print("\n" + "=" * 60)
        print("❌ CHƯƠNG TRÌNH KẾT THÚC VỚI LỖI!")
        print("Vui lòng kiểm tra lại thông báo lỗi ở trên.")

if __name__ == "__main__":
    main()

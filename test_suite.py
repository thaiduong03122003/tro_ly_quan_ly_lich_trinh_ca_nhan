import sys
import json
from nlp_pipeline import parse_user_input

# ============================================================================
# TEST CASES - Sắp xếp từ DỄ đến KHÓ
# ============================================================================

TEST_CASES = [
    # ==================== LEVEL 1: CƠ BẢN (1-10) ====================
    {
        "id": 1,
        "level": "Easy",
        "input": "Hop 10h",
        "expected_event": "Hop",
        "expected_has_time": True,
        "desc": "Cau don gian nhat"
    },
    {
        "id": 2,
        "level": "Easy",
        "input": "Meeting 14h30",
        "expected_event": "Meeting",
        "expected_has_time": True,
        "desc": "Tieng Anh don gian"
    },
    {
        "id": 3,
        "level": "Easy",
        "input": "Hop team 9h sang",
        "expected_event": "Hop team",
        "expected_has_time": True,
        "desc": "Co buoi trong ngay"
    },
    {
        "id": 4,
        "level": "Easy",
        "input": "Hop 10h tai phong 101",
        "expected_event": "Hop",
        "expected_has_time": True,
        "expected_location": "phong 101",
        "desc": "Co dia diem"
    },
    {
        "id": 5,
        "level": "Easy",
        "input": "An trua 12h",
        "expected_event": "An trua",
        "expected_has_time": True,
        "desc": "Sinh hoat ca nhan"
    },
    {
        "id": 6,
        "level": "Easy",
        "input": "Họp lúc 8 giờ sáng",
        "expected_event": "Họp",
        "expected_has_time": True,
        "desc": "Co dau tieng Viet"
    },
    {
        "id": 7,
        "level": "Easy",
        "input": "Gặp khách 15h chiều",
        "expected_event": "Gặp khách",
        "expected_has_time": True,
        "desc": "Co dau + buoi"
    },
    {
        "id": 8,
        "level": "Easy",
        "input": "Deadline 17h",
        "expected_event": "Deadline",
        "expected_has_time": True,
        "desc": "Tu tieng Anh"
    },
    {
        "id": 9,
        "level": "Easy",
        "input": "Hop 10h nhac truoc 5 phut",
        "expected_event": "Hop",
        "expected_has_time": True,
        "expected_reminder": 5,
        "desc": "Nhac nho co ban"
    },
    {
        "id": 10,
        "level": "Easy",
        "input": "Meeting 14h nhắc trước 10 phút",
        "expected_event": "Meeting",
        "expected_has_time": True,
        "expected_reminder": 10,
        "desc": "Nhac nho co dau"
    },
    
    # ==================== LEVEL 2: TRUNG BÌNH (11-20) ====================
    {
        "id": 11,
        "level": "Medium",
        "input": "Hop team 10h sang mai tai van phong",
        "expected_event": "Hop team",
        "expected_has_time": True,
        "expected_location": "van phong",
        "desc": "Ngay mai + dia diem"
    },
    {
        "id": 12,
        "level": "Medium",
        "input": "Call voi doi tac 16h30 chieu nay",
        "expected_event": "Call voi doi tac",
        "expected_has_time": True,
        "desc": "Hom nay + su kien dai"
    },
    {
        "id": 13,
        "level": "Medium",
        "input": "Phong van ung vien 9h sang thu Hai",
        "expected_event": "Phong van ung vien",
        "expected_has_time": True,
        "desc": "Thu trong tuan"
    },
    {
        "id": 14,
        "level": "Medium",
        "input": "Hop 10h tai phong 101 nhac truoc 15 phut",
        "expected_event": "Hop",
        "expected_has_time": True,
        "expected_location": "phong 101",
        "expected_reminder": 15,
        "desc": "Dia diem + nhac nho"
    },
    {
        "id": 15,
        "level": "Medium",
        "input": "Họp team lúc 10h sáng mai tại phòng họp A",
        "expected_event": "Họp team",
        "expected_has_time": True,
        "expected_location": "phòng họp A",
        "desc": "Day du thong tin co dau"
    },
    {
        "id": 16,
        "level": "Medium",
        "input": "Meeting 14h nhac truoc 1 tieng",
        "expected_event": "Meeting",
        "expected_has_time": True,
        "expected_reminder": 60,
        "desc": "Nhac theo gio"
    },
    {
        "id": 17,
        "level": "Medium",
        "input": "Hop 10h bao truoc 2h",
        "expected_event": "Hop",
        "expected_has_time": True,
        "expected_reminder": 120,
        "desc": "Nhac 2 gio"
    },
    {
        "id": 18,
        "level": "Medium",
        "input": "Gap khach hang tai quan ca phe 15h",
        "expected_event": "Gap khach hang",
        "expected_has_time": True,
        "expected_location": "quan ca phe",
        "desc": "Dia diem dai"
    },
    {
        "id": 19,
        "level": "Medium",
        "input": "Lich hop 10h ngay 25/12",
        "expected_event": "Lich hop",
        "expected_has_time": True,
        "desc": "Ngay cu the"
    },
    {
        "id": 20,
        "level": "Medium",
        "input": "Trinh bay du an 14h30 tai hoi truong",
        "expected_event": "Trinh bay du an",
        "expected_has_time": True,
        "expected_location": "hoi truong",
        "desc": "Su kien cong viec"
    },
    
    # ==================== LEVEL 3: KHÓ (21-30) ====================
    {
        "id": 21,
        "level": "Hard",
        "input": "Toi co cuoc hop luc 1 gio 30 phut tai van phong hay nhac truoc 15 phut",
        "expected_event": "cuoc hop",
        "expected_has_time": True,
        "expected_location": "van phong",
        "expected_reminder": 15,
        "desc": "Cau dai + nhieu thanh phan"
    },
    {
        "id": 22,
        "level": "Hard",
        "input": "Hẹn gặp đối tác quan trọng lúc 10h sáng thứ Ba tuần sau tại văn phòng chi nhánh",
        "expected_event": "Hẹn gặp đối tác quan trọng",
        "expected_has_time": True,
        "expected_location": "văn phòng chi nhánh",
        "desc": "Tuan sau + dia diem dai"
    },
    {
        "id": 23,
        "level": "Hard",
        "input": "Nhac toi hop khẩn cấp 23h17 toi nay tai phong giam doc nhac truoc 30p",
        "expected_event": "hop khẩn cấp",
        "expected_has_time": True,
        "expected_reminder": 30,
        "desc": "Gio khuya + hon hop"
    },
    {
        "id": 24,
        "level": "Hard",
        "input": "Bay di cong tac Ha Noi 6h sang thu Nam bao truoc 2 tieng",
        "expected_event": "Bay di cong tac Ha Noi",
        "expected_has_time": True,
        "expected_reminder": 120,
        "desc": "Su kien di chuyen"
    },
    {
        "id": 25,
        "level": "Hard",
        "input": "Review code voi team backend 16h30 chieu mai o phong dev nhac truoc 20 phut",
        "expected_event": "Review code voi team backend",
        "expected_has_time": True,
        "expected_location": "phong dev",
        "expected_reminder": 20,
        "desc": "Su kien ky thuat"
    },
    {
        "id": 26,
        "level": "Hard",
        "input": "Họp toàn công ty cuối tuần lúc 9h sáng tại hội trường lớn nhắc trước 1 giờ",
        "expected_event": "Họp toàn công ty cuối tuần",
        "expected_has_time": True,
        "expected_location": "hội trường lớn",
        "expected_reminder": 60,
        "desc": "Cuoi tuan + nhac theo gio"
    },
    {
        "id": 27,
        "level": "Hard",
        "input": "Demo san pham moi cho khach hang VIP 14h ngay 20 tai showroom bao truoc 3h",
        "expected_event": "Demo san pham moi cho khach hang VIP",
        "expected_has_time": True,
        "expected_location": "showroom",
        "expected_reminder": 180,
        "desc": "Ngay cu the + nhac 3 gio"
    },
    {
        "id": 28,
        "level": "Hard",
        "input": "Hoc tieng Anh online 20h toi thu Bay nhac truoc 60 giay",
        "expected_event": "Hoc tieng Anh online",
        "expected_has_time": True,
        "expected_reminder": 1,
        "desc": "Nhac theo giay"
    },
    {
        "id": 29,
        "level": "Hard",
        "input": "Toi muon dat lich gap bac si luc 2 gio 45 phut chieu ngay mai tai benh vien trung uong hay nhac truoc 45 phut",
        "expected_event": "dat lich gap bac si",
        "expected_has_time": True,
        "expected_location": "benh vien trung uong",
        "expected_reminder": 45,
        "desc": "Cau hoi thoai tu nhien"
    },
    {
        "id": 30,
        "level": "Hard",
        "input": "Webinar ve AI trong y te 19h30 toi thu Sau tuan sau o online bao truoc 15 minutes",
        "expected_event": "Webinar ve AI trong y te",
        "expected_has_time": True,
        "expected_reminder": 15,
        "desc": "Su kien online + tieng Anh"
    }
]

def run_tests():
    """Run all test cases and show results."""
    print("=" * 70)
    print("VIETNAMESE NER TEST SUITE - 30 TEST CASES")
    print("=" * 70)
    
    passed = 0
    failed = 0
    results = []
    
    for test in TEST_CASES:
        test_id = test["id"]
        level = test["level"]
        input_text = test["input"]
        desc = test["desc"]
        
        print(f"\n[Test {test_id:02d}] [{level}] {desc}")
        print(f"Input: \"{input_text}\"")
        
        try:
            result = parse_user_input(input_text)
            
            # Check for errors
            if "error" in result:
                print(f"ERROR: {result['error']}")
                failed += 1
                results.append({"id": test_id, "status": "FAILED", "reason": result['error']})
                continue
            
            # Validate results
            is_pass = True
            issues = []
            
            # Check event name
            event = result.get("event", "")
            expected_event = test.get("expected_event", "")
            if expected_event and expected_event.lower() not in event.lower():
                issues.append(f"Event mismatch: got '{event}', expected contains '{expected_event}'")
                is_pass = False
            
            # Check time
            has_time = result.get("start_time") is not None
            if test.get("expected_has_time") and not has_time:
                issues.append("Missing start_time")
                is_pass = False
            
            # Check location
            location = result.get("location", "")
            expected_loc = test.get("expected_location", "")
            if expected_loc and expected_loc.lower() not in location.lower():
                issues.append(f"Location mismatch: got '{location}', expected contains '{expected_loc}'")
                is_pass = False
            
            # Check reminder
            reminder = result.get("reminder_minutes", 0)
            expected_reminder = test.get("expected_reminder")
            if expected_reminder is not None:
                # Allow 10% tolerance for conversions
                if abs(reminder - expected_reminder) > max(1, expected_reminder * 0.1):
                    issues.append(f"Reminder mismatch: got {reminder}, expected {expected_reminder}")
                    is_pass = False
            
            # Print result
            if is_pass:
                print(f"PASSED - Event: '{event}' | Time: {result.get('start_time', 'N/A')[:16] if result.get('start_time') else 'N/A'} | Loc: '{location}' | Remind: {reminder}m")
                passed += 1
                results.append({"id": test_id, "status": "PASSED"})
            else:
                print(f"FAILED - {'; '.join(issues)}")
                print(f"  Got: Event='{event}' | Time={result.get('start_time')} | Loc='{location}' | Remind={reminder}m")
                failed += 1
                results.append({"id": test_id, "status": "FAILED", "reason": "; ".join(issues)})
                
        except Exception as e:
            print(f"EXCEPTION: {str(e)}")
            failed += 1
            results.append({"id": test_id, "status": "FAILED", "reason": str(e)})
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    total = len(TEST_CASES)
    accuracy = (passed / total) * 100 if total > 0 else 0
    
    print(f"Total Tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Accuracy: {accuracy:.1f}%")
    
    if accuracy >= 80:
        print("\n>>> STATUS: PASS (>= 80%)")
    else:
        print("\n>>> STATUS: FAIL (< 80%)")
    
    # Show failed tests
    if failed > 0:
        print("\n--- Failed Tests ---")
        for r in results:
            if r["status"] == "FAILED":
                print(f"  Test {r['id']}: {r.get('reason', 'Unknown')}")
    
    print("=" * 70)
    return accuracy >= 80

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)

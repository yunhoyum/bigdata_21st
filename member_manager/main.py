import member_manager

while True:
    print("="*33)
    print("   다음 메뉴 중 하나를 선택하세요.")
    print("="*33)
    print("1. 회원 추가")
    print("2. 회원 목록 보기")
    print("3. 회원 정보 수정하기")
    print("4. 회원 삭제")
    print("5. 종료")

    menu = input()
    if menu == "1":
        print("등록할 회원의 정보를 입력하세요.")
        while True:
            print("이름:", end=" ")
            name = input()
            if member_manager.validate_name(name):
                break
            print("잘못된 입력입니다.")
        while True:
            print("전화번호(ex: 01012345678):", end=" ")
            phone = input()
            if member_manager.validate_phone(phone):
                break
            print("잘못된 입력입니다.")

        print("주소:", end=" ")
        address = input()

        while True:
            print("구분(ex. 가족, 친구, 기타):", end=" ")
            type = input()
            if member_manager.validate_type(type):
                break
            print("잘못된 입력입니다.")

        members = {
            "name" : name,
            "phone" : phone,
            "address" : address,
            "type" : type
        }
        member_manager.add_member(members)
    elif menu == "2":
        member_manager.list_members()
    elif menu == "3":
        member_manager.update_member()
    elif menu == "4":
        member_manager.delete_member()
    elif menu == "5":
        print("프로그램이 종료됩니다.")
        break
    else :
        print("잘못된 입력입니다.")
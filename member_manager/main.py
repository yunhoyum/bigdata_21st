import member_manager as mm

while True:
    mm.print_menu()

    menu = input()
    if menu == "1":
        print("등록할 회원의 정보를 입력하세요.")
        while True:
            print("이름:", end=" ")
            name = input()
            if mm.validate_name(name):
                break
            print("잘못된 입력입니다.")
        while True:
            print("전화번호(ex: 01012345678):", end=" ")
            phone = input()
            if mm.validate_phone(phone):
                break
            print("잘못된 입력입니다.")

        print("주소:", end=" ")
        address = input()

        while True:
            print("구분(ex. 가족, 친구, 기타):", end=" ")
            type = input()
            if mm.validate_type(type):
                break
            print("잘못된 입력입니다.")

        members = {
            "name" : name,
            "phone" : phone,
            "address" : address,
            "type" : type
        }
        mm.add_member(members)
    elif menu == "2":
        mm.list_members()
    elif menu == "3":
        mm.update_member()
    elif menu == "4":
        mm.delete_member()
    elif menu == "5":
        print("프로그램이 종료됩니다.")
        break
    else :
        print("잘못된 입력입니다.")
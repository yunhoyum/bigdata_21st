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
        member_manager.add_member()
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
import re, pickle

###################### 함수 ##########################

def load_data():
    with open("members.dat", "rb") as f:
        return pickle.load(f)
    

def print_menu():
    print("="*33)
    print("   다음 메뉴 중 하나를 선택하세요.")
    print("="*33)
    print("1. 회원 추가")
    print("2. 회원 목록 보기")
    print("3. 회원 정보 수정하기")
    print("4. 회원 삭제")
    print("5. 종료")

def add_member(members: dict):
    # with open("members.dat", "ab") as f:
    #     pickle.dump(members, f)
    member_datas.append(members)

def list_members():
    print(member_datas)
    return None

def find_by_name():
    return None

def update_member():
    return None

def delete_member():
    return None

def save_member():
    return None

def validate_name(name: str) -> bool:
    return 1 <= len(name) <= 5

def validate_phone(phone: str) -> bool:
    pat_str = r"[010]\d{8}"
    pat = re.compile(pat_str)
    return pat.match(phone)

def validate_type(type: str) -> bool:
    return type in ("가족", "친구", "기타")

###################### main ##########################

member_datas = []
while True:
    try:
        member_datas.append(load_data())
    except FileNotFoundError as e:
        print("파일이 존재하지 않습니다.")
    try: 
        if load_data() == []:        # 생성 안 하고 하는 방법 찾아보기
            raise Exception("데이터가 없습니다.")
    except pickle.UnpicklingError as e:
        print(e)

    print_menu()

    menu = input()
    if menu == "1":
        print("등록할 회원의 정보를 입력하세요.")
        while True:
            print("이름:", end=" ")
            name = input()
            if validate_name(name):
                break
            print("잘못된 입력입니다.")
        while True:
            print("전화번호(ex: 01012345678):", end=" ")
            phone = input()
            if validate_phone(phone):
                break
            print("잘못된 입력입니다.")

        print("주소:", end=" ")
        address = input()

        while True:
            print("구분(ex. 가족, 친구, 기타):", end=" ")
            type = input()
            if validate_type(type):
                break
            print("잘못된 입력입니다.")

        members = {
            "name" : name,
            "phone" : phone,
            "address" : address,
            "type" : type
        }
        add_member(members)
    elif menu == "2":
        list_members()
    elif menu == "3":
        update_member()
    elif menu == "4":
        delete_member()
    elif menu == "5":
        print("프로그램이 종료됩니다.")
        break
    else :
        try:
            raise Exception("잘못된 입력입니다.")
        except Exception as e:
            print(e)




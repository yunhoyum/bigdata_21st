import re, pickle

###################### 함수 ##########################


def load_data(path):
    try:
        with open(path+"/members.dat", "rb") as f:
            member_datas = pickle.load(f)
    except FileNotFoundError as e:
        print("파일이 존재하지 않습니다.")
        return []
    return member_datas
    
def save_data(path, members):
    with open(path+"/members.dat", "wb") as f:
        return pickle.dump(members, f)

def print_menu():
    print("="*33)
    print("   다음 메뉴 중 하나를 선택하세요.")
    print("="*33)
    print("1. 회원 추가")
    print("2. 회원 목록 보기")
    print("3. 회원 정보 수정하기")
    print("4. 회원 삭제")
    print("5. 종료")

def validate_name(name: str) -> bool:
    return 1 <= len(name) <= 5

def validate_phone(phone: str) -> bool:
    pat_str = r"[010]\d{8}"
    pat = re.compile(pat_str)
    return pat.match(phone)

def validate_type(t: str) -> bool:
    return t in ("가족", "친구", "기타")

def add_member(members: list):
    print("등록할 회원의 정보를 입력하세요.")
    while True:
        print("이름:", end=" ")
        name = input()
        if validate_name(name):
            break
        print("이름은 5자 이내로 입력하세요.")
    while True:
        print("전화번호(ex: 01012345678):", end=" ")
        phone = input()
        if validate_phone(phone):
            break
        print("전화번호 형식이 올바르지 않습니다.(예: 01012345678)")

    print("주소:", end=" ")
    address = input()

    while True:
        print("구분(ex. 가족, 친구, 기타):", end=" ")
        type = input()
        if validate_type(type):
            break
        print("구분은 가족/친구/기타 중 하나여야 합니다.")

    member_data = {
        "name" : name,
        "phone" : phone,
        "address" : address,
        "type" : type
    }
    members.append(member_data)

def list_members(members):
    if members == [] :
        print("총 0명의 회원이 저장되어 있습니다.")
        return None
    print(f"총 {len(members)}명의 회원이 저장되어 있습니다.")
    
    for member in members:
        print(f"회원정보 : 이름 = {member['name']}, 전화번호 : {member['phone']}, 주소 : {member['address']}, 종류 : {member['type']}")

def find_by_name(members, name):
    found_names = []
    for member in members:
        if member["name"] == name :
            found_names.append(member)
    return found_names

def update_member(members):
    print("수정할 회원의 이름을 입력하세요.")
    print("이름 :", end=" ")
    name = input()
    found_names = find_by_name(members, name)
    if found_names == []:
        try :
            raise Exception("해당하는 회원 정보가 없습니다.")
        except Exception as e:
            print(e)
            return None
    if len(found_names) > 1:
        selected_index = duplicated_name(found_names, "수정")
        if selected_index == -1:
            return None
    else:
        selected_index = 0

    members.pop(selected_index)

    print("수정할 정보를 입력하세요.")
    add_member(members)
    print("수정이 완료되었습니다.")

def delete_member(members):
    print("삭제할 회원의 이름을 입력하세요.")
    print("이름 :", end=" ")
    name = input()
    found_names = find_by_name(members, name)
    
    if found_names == []:
        try :
            raise Exception("해당하는 회원 정보가 없습니다.")
        except Exception as e:
            print(e)
            return None
    if len(found_names) > 1:
        selected_index = duplicated_name(found_names, "삭제")
        if selected_index == -1:
            return None
    else:
        selected_index = 0

    members.pop(selected_index)
    print("삭제가 완료되었습니다.")

def duplicated_name(found_names, crud="선택"):
    while True:
        print(f"총 {len(found_names)}개의 목록이 검색되었습니다.")
        print(f"아래의 목록 중 {crud}할 회원의 번호를 입력하세요.")
        for index, found_name in enumerate(found_names, start=1):
            print(f"{index}. 이름 = {found_name['name']}, 전화번호 : {found_name['phone']}, 주소 : {found_name['address']}, 구분 : {found_name['type']}")
        pick_number = input()
        if int(pick_number) > len(found_names) or int(pick_number) < 1:
            try:
                raise Exception("잘못된 번호입니다. 다시 입력하세요.")
            except Exception as e:
                print(e)
                continue
        break
    return int(pick_number)-1

###################### main ##########################
def main():
    try:
        members = load_data(".")
        while True:
            print_menu()

            
            try:
                menu = int(input())
            except ValueError as e:
                print("정수 1~5 사이의 값을 입력해 주세요.")
                continue

            if menu == 1:     # 함수 안에서 만들기
                add_member(members)
            elif menu == 2:
                members
                list_members(members)
            elif menu == 3:
                update_member(members)
            elif menu == 4:
                delete_member(members)
            elif menu == 5:
                print("프로그램이 종료됩니다.")
                save_data(".", members)
                break
            else :
                try:
                    raise Exception("1~5 숫자를 입력해 주세요.")
                except Exception as e:
                    print(e)
    except Exception as e:
        print(e)
    finally:
        save_data(".", members)

main()
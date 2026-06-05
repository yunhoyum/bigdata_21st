import re, pickle

def load_data():
    return None

def print_menu():
    return None

def add_member(members: dict) -> None:
    with open("members.dat", "ab") as f:
        data = members
        pickle.dump(data, f)

def list_members():
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
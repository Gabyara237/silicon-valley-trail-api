import re

def is_valid(choice: int, start: int, end: int) -> bool:
    return start <= choice <= end


def is_email_valid(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

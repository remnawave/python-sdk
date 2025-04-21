import random
import string
from datetime import datetime, timedelta
from typing import Tuple


def generate_random_string(length: int = 8, chars: str = string.ascii_letters) -> str:
    return "".join(random.choices(chars, k=length))


def generate_password(length: int) -> str:
    return generate_random_string(
        length=length, chars=string.ascii_letters + string.digits
    )


def generate_email(length: int, chars: str = string.ascii_letters) -> str:
    return generate_random_string(length=length, chars=chars) + "@mail.com"


def generate_isoformat_range() -> Tuple[str, str]:
    start = (datetime.now() - timedelta(days=7)).isoformat(timespec="seconds")
    end = datetime.now().isoformat(timespec="seconds")
    return start, end

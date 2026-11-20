import random
import string


def generate_email():
    name = "irina"
    surname = "khlamova"
    cohort = "56"
    random_numbers = random.randint(100, 999)
    email = f"{name}{surname}{cohort}{random_numbers}@yandex.ru"
    return email


def generate_password(length=6):
    characters = string.ascii_letters + string.digits
    password = "".join(random.choices(characters, k=length))
    return password

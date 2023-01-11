import random
import string


def generator_code_verification() -> str:
    """Функция для генерации кода верификации состоящего из цифр и ascii символов"""
    letters = string.digits + string.ascii_lowercase + string.ascii_uppercase
    ver_cod = ""
    for _ in range(10):
        ver_cod += letters[random.randrange(0, len(letters))]

    return ver_cod

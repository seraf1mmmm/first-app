import re
names_list = {
    "Ivan": 50,
    "Alex": 33,
    "Stepan": 18
}

class UserValidationError(Exception):
    pass

class InvalidNameError(UserValidationError):
    def __init__(self, message = "Ім'я користувача не знайдено"):
        super().__init__(message)


name = input("Wha is your name? ")


def validation_name(name):
    if not name.strip():
        raise InvalidNameError
    return name


try:
    name = validation_name(name)
    if name in names_list:
        print(f"{name} - {names_list[name]}")

    else:
        raise InvalidNameError
except UserValidationError as e:
    print(f"Validation Error: {e}")
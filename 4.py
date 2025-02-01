import re


class UserValidationError(Exception):
    """базовий клас для винятків валідації користувача."""
    pass

class InvalidNameError(UserValidationError):
    def __init__(self, messege = "Ім'я не може бути порожнім."):
        super().__init__(messege)


class InvalidAgeError(UserValidationError):
    def __init__(self, message = "Вік має бути цілисним і не менше 18 років."):
        super().__init__(message)


class InvalidEmailError(UserValidationError):
    def __init__(self, message = "Невірний формат електронної пошти."):
        super().__init__(message)


class User:
    def __init__(self, name, age, email):
        self.name = self.validate_name(name)
        self.age = self.validate_age(age)
        self.email = self.validate_email(email)

        @staticmethod
        def validate_name(name):
            if not name.strip():
                raise InvalidNameError()
            return name


        @staticmethod
        def validete_age(age):
            if not isinstance(age, int) or age < 18:
                raise InvalidNameError
            return age

        @staticmethod
        def validate_email(email):
            pattern = r'^[\w\.\-]+@[\w\.\-]+\.\w+$'
            if not re.match(pattern, email):
                raise InvalidEmailError
            return email

try:
    user = User("", 17, "invalid-email")
except UserValidationError as e:
    print(f"Помилка віліції: {e}")

try:
    user = User("Іван", 20, "ivan@example.com")
    print(f"Успішно створено користувача: {user.name}, {user.age}, {user.email}")
except UserValidationError as e:
    print(f"Valiation Error: "{e})
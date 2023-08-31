import string


class UsernameExists(Exception):
    def __init__(self, username):
        self._username = username


class UsernameContainsIllegalCharacter(UsernameExists):
    def __init__(self, username,  wrong_char):
        self._username = username
        self._wrong_char = wrong_char

    def __str__(self):
        return f"The username contains an illegal character \"{self._wrong_char}\" at index {self._username.index(self._wrong_char)}"


class UsernameTooShort(UsernameExists):
    def __str__(self):
        return f"Username \"{self._username}\" too short"


class UsernameTooLong(UsernameExists):
    def __str__(self):
        return f"Username \"{self._username}\" too long"


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character "


class PasswordMissingCharacterUpper(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Upper Case)"


class PasswordMissingCharacterLower(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Lower Case)"


class PasswordMissingDigits(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Digits)"


class PasswordMissingSpecialChars(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Special Chars)"


class PasswordTooShort(Exception):
    def __str__(self):
        return "The password is too short"


class PasswordTooLong(Exception):
    def __str__(self):
        return "The password is too long"


speical_char = """!"#$%&'()*+,-./:;<=>?@[\]^`{|}~"""


def check_input(username, password):

    if len(username) < 3:
        raise UsernameTooShort(username)

    if len(username) > 16:
        raise UsernameTooLong(username)

    illigal_char = "".join([i for i in username if i in speical_char])
    if illigal_char:
        raise UsernameContainsIllegalCharacter(username, illigal_char)

    if len(password) < 8:
        raise PasswordTooShort()

    if len(password) > 40:
        raise PasswordTooLong()

    if not any(ch.isupper() for ch in password):
        raise PasswordMissingCharacterUpper()

    if not any(ch.islower() for ch in password):
        raise PasswordMissingCharacterLower()

    if not any(ch.isdigit() for ch in password):
        raise PasswordMissingDigits()

    if not any(ch in string.punctuation for ch in password):
        raise PasswordMissingSpecialChars()

    else:
        print("OK")


def main():
    while True:
        try:
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            check_input(username, password)
            break
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()

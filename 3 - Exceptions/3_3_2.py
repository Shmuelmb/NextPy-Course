
class UnderAge(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return f"Your age is {self._arg}, In {18 - self._arg} years you will be able to enter the party "


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
    except UnderAge as e:
        print(e)
    else:
        print("You should send an invite to " + name)


send_invitation("John", 18)

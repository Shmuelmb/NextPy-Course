class Animal():
    """

    This is Animal class with name and hunger attributes
    methods: get_name, is_hungry, feed, talk
    get_name(): return name
    is_hungry(): return True if hungry and False otherwise
    feed(): increase hunger
    talk(): print message

    zoo_name: name of the zoo
    """

    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0, ):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    def is_hungry(self):
        if self._hunger > 0:
            return True
        else:
            return False

    def feed(self):
        self._hunger -= 1

    def talk(self, message):
        self._message = message
        print(self._message)


class Dog(Animal):
    def talk(self):
        super().talk("Woof!")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    def talk(self):
        super().talk("mewo")

    def chase_laser(self):
        print("Meeewo")


class Skunk(Animal):

    def __init__(self, name, hunger=0, stink_count=6):
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        super().talk("tsssss")

    def stink(self):
        print("SDear lord!")


class Unicorn(Animal):
    def talk(self):
        super().talk("Good day, darling")

    def sing(self):
        print("I’m not your toy...")


class Dragon(Animal):
    def __init__(self, name, hunger=0, color="Green"):
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        super().talk("Raaaawr")

    def breath_fire(self):
        print("@#%#@")


def main():
    Brownie = Dog('Brownie', 10)
    Zelda = Cat('Zelda', 3)
    Stinky = Skunk('Stinky', 0)
    Keith = Unicorn('Keith', 7)
    Lizzy = Dragon('Lizzy', 1450)

    # New animals
    Doggo = Dog("Doggo", 80)
    Kitty = Cat("Kitty", 80)
    Stinky_Jr = Skunk("Stinky Jr.", 80)
    Clair = Unicorn("Clair", 80)
    McFly = Dragon("McFly", 80)

    zoo_lst = [Brownie, Zelda, Stinky, Keith, Lizzy]
    new_animals = [Doggo, Kitty, Stinky_Jr, Clair, McFly]

    for new_animal in new_animals:
        zoo_lst.append(new_animal)

    for animal in zoo_lst:
        if animal.is_hungry():
            print(type(animal).__name__, animal.get_name())
            while animal.is_hungry():
                animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    print(Animal.zoo_name)


if __name__ == "__main__":
    main()

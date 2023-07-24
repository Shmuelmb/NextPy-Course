class Octopus:
    count_animals = 0

    def __init__(self, name='Octavio'):
        self._life = 1
        self._name = name
        Octopus.count_animals += 1

    def birthday(self):
        self._life += 1

    def set_name(self, name):
        self._name = name

    def get_name(self):
        print(self._name)


octavio = Octopus()
octavio.birthday()
octavio.get_name()

shmulik = Octopus("shmulik")
shmulik.get_name()
shmulik.set_name("shmulik kipod")
shmulik.get_name()
print(Octopus.count_animals)

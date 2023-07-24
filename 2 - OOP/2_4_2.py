class BigThing:
    def __init__(self, input):
        self._input = input

    def size(self):
        if isinstance(self._input, int):
            return self._input
        else:
            return len(self._input)


class BigCat(BigThing):
    def __init__(self, input, weight):
        super().__init__(input)
        self._weight = weight

    def size(self):
        if self._weight >= 15 and self._weight < 20:
            return "Fat"
        elif self._weight >= 20:
            return "Very Fat"
        else:
            return "OK"


def main():

    my_thing = BigThing("balloon")
    print(my_thing.size())
    cutie = BigCat("mitzy", 20)
    print(cutie.size())


if __name__ == "__main__":
    main()

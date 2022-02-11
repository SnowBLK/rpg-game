import random


class Orc:
    def __init__(self):
        self.__degat = random.randint(3, 5)
        self.__loot = random.choice([1, 2])

    @property
    def degat(self):
        """The degat property."""
        return self.__degat

    @degat.setter
    def degat(self, value):
        self.__degat = value

    @property
    def loot(self):
        """The loot property."""
        return self.__loot

    @loot.setter
    def loot(self, value):
        self.__loot = value


if __name__ == "__main__":
    o = Orc()
    l = Orc()

    print("O :")
    print(o.degat)  # 3 or 4 or 5
    print(o.loot)  # 1 or 2

    print("L :")
    print(l.degat)  # 3 or 4 or 5
    print(l.loot)  # 1 or 2

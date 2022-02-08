import random


class Warrior:
    def __init__(self):
        self.__degat = random.randint(3, 5)
        self.__chance = 5
        self.__fuite = 3
        self.__prix = 10
        self.__unit_type = "warrior"

    @property
    def degat(self):
        """The degat property."""
        return self.__degat

    @degat.setter
    def degat(self, value):
        self.__degat = value

    @property
    def chance(self):
        """The chance property."""
        return self.__chance

    @chance.setter
    def chance(self, value):
        self.__chance = value

    @property
    def fuite(self):
        """The fuite property."""
        return self.__fuite

    @fuite.setter
    def fuite(self, value):
        self.__fuite = value

    @property
    def prix(self):
        """The prix property."""
        return self.__prix

    @prix.setter
    def prix(self, value):
        self.__prix = value

    @property
    def unit_type(self):
        """The unit_type property."""
        return self.__unit_type

    @unit_type.setter
    def unit_type(self, value):
        self.__unit_type = value


if __name__ == "__main__":
    print(Warrior.degat)

import random

class Zombie:

        def __init__(self):
                self.__degat=random.randint(1,2)
                self.__loot=random.choice([0.5,1])

        # getter method
        def getdegat(self):
                return self.__degat
        def getloot(self):
                return self.__loot

        # setter method
        def setdegat(self, x):
                self.__degat = x
        def setloot(self, x):
                self.__loot = x


if __name__ == '__main__':
        Z = Zombie()
        Z.setdegat(1)
        print(Z.getdegat())
        print(Z.getloot())


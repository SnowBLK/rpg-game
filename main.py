import random


class Wizard:

        def __init__(self):
                self.__degat=random.randint(2,4)
                self.__chance=20
                self.__fuite=10
                self.__prix=15
                self.__unit_type="wizard"

        def getdegat(self):
                return self.__degat
        def getchance(self):
                return self.__chance
        def getfuite(self):
                return self.__fuite
        def getprix(self):
                return self.__prix
        def getunit(self):
                return self.__unit_type
        def setdegat(self, x):
                self.__degat = x
        def setchance(self, x):
                self.__chance = x
        def setfuite(self, x):
                self.__fuite = x
        def setprix(self, x):
                self.__prix = x

if __name__ == '__main__':
        W = Wizard()
        print(W.getchance())
        print(W.getdegat())
        print(W.getprix())
        print(W.getfuite())
        print(W.getfuite())


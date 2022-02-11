from typing import Collection
from Orc import Orc
from Warrior import Warrior

from TeamIterator import TeamIterator


class Team:

    # instance attributes
    def __init__(self, members: Collection):
        self._members = members

    def __iter__(self):
        return TeamIterator(self._members)

    def __len__(self):
        return len(self._members)

    def __getitem__(self, index):
        return self._members[index]

    def __iter__(self):
        return TeamIterator(self._members)


if __name__ == "__main__":
    t = Team([Orc(), Warrior(), Orc()])

    # il print tout les degat de mon team
    for unit in t:
        print(unit.degat)

    # il fait appel a la methode magique __getitem__
    print(t[1])  # <Warrior.Warrior object at 0x000001896F103F70>

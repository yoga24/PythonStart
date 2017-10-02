import random


class Warrior:
    def __init__(self, name='Player_0', health=50, attack=1, block=0):
        self.__name = name
        self.__health = health
        self.__attack = attack
        self.__block = block

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def name(self):
        return self.__name

    def attack(self, enemy):
        attack_points = random.randint(0, enemy.health)
        print('{} attacks {} and deals {} damage'.format(self.name, enemy.name, attack_points))

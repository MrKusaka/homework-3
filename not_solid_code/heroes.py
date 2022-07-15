from abc import ABC, abstractmethod

from antagonistfinder import AntagonistFinder
import attack_types


class SuperHero(attack_types.FireGunMixin):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    def attack(self):
        self.fire_a_gun()


class Ultimate(ABC):

    @abstractmethod
    def ultimate(self):
        pass


class Superman(SuperHero, attack_types.KickMixin, attack_types.LaserMixin, Ultimate):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def attack(self):
        return self.kick()

    def ultimate(self):
        self.incinerate_with_lasers()


class ChakNorris(SuperHero, attack_types.KickMixin, attack_types.BumpMixin):

    def __init__(self):
        super(ChakNorris, self).__init__('Chak Norris', False)

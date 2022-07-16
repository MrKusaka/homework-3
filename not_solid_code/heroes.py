from abc import ABC, abstractmethod

from antagonistfinder import AntagonistFinder
import attack_types


class SuperHero(ABC):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    @abstractmethod
    def find(self, place):
        pass

    @abstractmethod
    def attack(self):
        pass


class Superman(SuperHero, attack_types.KickMixin, attack_types.LaserMixin, attack_types.Ultimate):

    def __init__(self):
        super().__init__('Clark Kent', True)

    def find(self, place):
        self.finder.get_antagonist(place)

    def attack(self):
        return self.kick()

    def ultimate(self):
        self.incinerate_with_lasers()


class ChuckNorris(SuperHero, attack_types.KickMixin, attack_types.FireGunMixin, attack_types.BumpMixin):

    def __init__(self):
        super().__init__('Chuck Norris', False)

    def find(self, place):
        self.finder.get_antagonist(place)

    def attack(self):
        return self.fire_a_gun()

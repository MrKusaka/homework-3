from abc import ABC, abstractmethod


class FireGunMixin:

    @staticmethod
    def fire_a_gun():
        print('PIU PIU')


class LaserMixin:

    @staticmethod
    def incinerate_with_lasers():
        print('Wzzzuuuup!')


class BumpMixin:

    @staticmethod
    def roundhouse_kick():
        print('Bump')


class KickMixin:

    @staticmethod
    def kick():
        print('Kick')


class Ultimate(ABC):

    @abstractmethod
    def ultimate(self):
        pass
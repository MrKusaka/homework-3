from abc import ABC, abstractmethod


class Place(ABC):

    @abstractmethod
    def get_antagonist(self):
        pass


class Kostroma(Place):
    name = 'Kostroma'

    @staticmethod
    def get_orcs():
        print('Orcs hid in the forest')

    def get_antagonist(self):
        self.get_orcs()


class Tokyo(Place):
    name = 'Tokyo'

    @staticmethod
    def get_godzilla():
        print('Godzilla stands near a skyscraper')

    def get_antagonist(self):
        self.get_godzilla()


class Mars(Place):
    coordinates = [66.66, 60.60, 69.69]

    @staticmethod
    def get_marsiane():
        print('Mars starts attack on Earth')

    def get_antagonist(self):
        self.get_marsiane()

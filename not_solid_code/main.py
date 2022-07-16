from typing import Union
from heroes import ChuckNorris, Superman, SuperHero
from places import Kostroma, Tokyo, Mars
from media import MassMedia


def save_the_place(hero: SuperHero, place: Union[Kostroma, Tokyo, Mars]):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        getattr(hero, 'ultimate')()
    MassMedia().create_news(hero.name, place, 'TV')


if __name__ == '__main__':
    save_the_place(Superman(), Mars())
    print('-' * 20)
    save_the_place(ChuckNorris(), Tokyo())

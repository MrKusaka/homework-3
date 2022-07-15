class MassMedia:

    @staticmethod
    def create_news(super_hero_name, place, media):
        print(f'{media} informs {super_hero_name} saved the '
              f'{place.name if hasattr(place, "name") else f"Planet {tuple(place.coordinates)}"}!')

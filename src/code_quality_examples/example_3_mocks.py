import random
from typing import Optional


class WithoutSideEffects:
    """Showcases a class definition without side effects on init.

    number_of_the_day has a default value of 4.
    The contents of contents_of_file only changes when the using code explicitely calls read_the_file
    """

    ingredients: Optional[list[str]]
    number_of_the_day: int
    menu: Optional[list[str]]

    def __init__(self):
        self.ingredients = None
        self.number_of_the_day = 4
        self.menu = None

    def assign_random_number(self):
        self.number_of_the_day = WithoutSideEffects.still_a_side_effect()

    def assign_menu(self, path: str):
        with open(path) as open_file:
            self.ingredients = open_file.readlines()

        self.menu = WithoutSideEffects.create_menu_of_the_week(self.ingredients, self.number_of_the_day)

    @staticmethod
    def still_a_side_effect() -> int:
        return random.randint(1, 7)

    @staticmethod
    def create_menu_of_the_week(ingredients: list[str], number_of_the_day: int) -> list[str]:
        menu = []
        for line in ingredients:
            if 'broccoli' in line:
                menu.append('Spaghetti with broccoli sauce')
            elif 'goat' in line:
                menu.append('Kebab')
            elif 'cat' in line:
                menu.append(f'Mystery meat surprise {number_of_the_day}')
            elif 'Tomatoes' in line:
                menu.append('Lasagna')
            else:
                raise RuntimeError('Unknown ingredient in ingredients file')

        return menu



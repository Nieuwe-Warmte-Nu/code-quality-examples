"""A class which has isolated side effects, is documented and has type hints"""
import random
from typing import Optional


class WithoutSideEffects:
    """Showcases a class definition without side effects on init.

    The class can generate a menu for a given day of the week based on an ingredients list. `number_of_the_day` has a
    default value of 4. The contents of `ingredients` only changes when the using code explicitely calls `assign_menu`.

    :param ingredients: The current list of ingredients
    :param number_of_the_day: Day of the week for which a menu is generated
    :param menu: The generated menu
    """

    ingredients: Optional[list[str]]
    number_of_the_day: int
    menu: Optional[list[str]]

    def __init__(self):
        self.ingredients = None
        self.number_of_the_day = 4
        self.menu = None

    def assign_random_number(self) -> None:
        """Assign a randomnly selected number between 1 and 7 as the number of the day."""
        self.number_of_the_day = WithoutSideEffects.still_a_side_effect()

    def assign_menu(self, path: str) -> None:
        """Assign a menu for the day of the week based on the ingredients list.

        Expect that `number_of_the_day` is set to the correct day.

        :param path: Path to the ingredients list file
        """
        with open(path, encoding='ascii') as open_file:
            self.ingredients = open_file.readlines()

        self.menu = WithoutSideEffects.create_menu_of_the_week(self.ingredients, self.number_of_the_day)

    @staticmethod
    def still_a_side_effect() -> int:
        """Randomly selects a number between 1 and 7

        :return: Number between 1 and 7
        """
        return random.randint(1, 7)

    @staticmethod
    def create_menu_of_the_week(ingredients: list[str], number_of_the_day: int) -> list[str]:
        """Creates the menu based on the ingredients list

        :param ingredients: List of ingredients that will go into the menu
        :param number_of_the_day: For which day the menu is generated
        :return: A list of dishes which make up the menu
        """
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

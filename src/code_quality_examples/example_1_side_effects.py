import random
from typing import Optional
from unittest import TestCase


class WithSideEffects:
    ingredients: list[str]
    number_of_the_day: int
    menu: list[str]

    def __init__(self, use_random_value: bool) -> None:
        with open('side_effect_file.txt') as open_file:
            self.ingredients = open_file.readlines()

        if use_random_value:
            self.number_of_the_day = self.still_a_side_effect()
        else:
            self.number_of_the_day = 4

        self.menu = []
        for line in self.ingredients:
            if 'broccoli' in line:
                self.menu.append('Spaghetti with broccoli sauce')
            elif 'goat' in line:
                self.menu.append('Kebab')
            elif 'cat' in line:
                self.menu.append('Mystery meat surprise')
            elif 'Tomatoes' in line:
                self.menu.append('Lasagna')
            else:
                raise RuntimeError('Unknown ingredient in ingredients file')

    @staticmethod
    def still_a_side_effect() -> int:
        return random.randint(1, 7)


class TestWithSideEffects(TestCase):
    def test__init__happy_path(self):
        # Arrange
        use_random_value = True

        # Act
        with_side_effects = WithSideEffects(use_random_value)

        # Assert
        # TODO ISSUE: We have a random value, how can we test this?
        # TODO ISSUE: We have some random file in here, how can we test the contents of the menu neatly?
        # TODO ISSUE: So much is happening in this function....


#  ------------------------------------------
# Without side effects

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

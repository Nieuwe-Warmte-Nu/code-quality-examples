from unittest import TestCase
from unittest.mock import patch

from code_quality_examples.example_1_side_effects import WithoutSideEffects


class TestWithoutSideEffects(TestCase):
    def test__init__happy_path(self):
        # Arrange / Act
        without_side_effects = WithoutSideEffects()

        # Assert
        # SO much easier to test now...
        expected_number_of_the_day = 4
        self.assertIsNone(without_side_effects.ingredients)
        self.assertIsNone(without_side_effects.menu)
        self.assertEqual(without_side_effects.number_of_the_day, expected_number_of_the_day)

    def test__assign_random_number__happy_path(self):
        # Arrange
        # Random number if still in here... but it is isolated so we can keep the 'test magic' to a minimum!
        without_side_effects = WithoutSideEffects()

        with patch('random.randint') as mock_randint:
            mock_randint.return_value = 3

            # Act
            # Notice how we moved the indent to fall within the 'with'!
            without_side_effects.assign_random_number()

        # Assert
        expected_number_of_the_day = 3
        self.assertEqual(without_side_effects.number_of_the_day, expected_number_of_the_day)

    def test__create_menu_of_the_week__happy_path(self):
        # This logic is completely isolated and can be tested perfectly now
        # Arrange
        ingredients = ['broccoli', 'goat']
        number_of_the_day = 3

        # Act
        menu = WithoutSideEffects.create_menu_of_the_week(ingredients, number_of_the_day)

        # Assert
        expected_menu = ['Spaghetti with broccoli sauce', 'Kebab']
        self.assertEqual(menu, expected_menu)

    def test__create_menu_of_the_week__unknown_ingredient(self):
        # This logic is completely isolated and can be tested perfectly now
        # Arrange
        ingredients = ['Spinach']
        number_of_the_day = 3

        # Act / Assert
        with self.assertRaises(RuntimeError):
            WithoutSideEffects.create_menu_of_the_week(ingredients, number_of_the_day)

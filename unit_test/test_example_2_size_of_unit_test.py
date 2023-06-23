import os
from unittest import TestCase
from unittest.mock import patch

from code_quality_examples.example_2_size_of_unit_test import WithoutSideEffects


class TestWithoutSideEffects(TestCase):
    def test__module__happy_path(self):
        # This test case looks small, but is a bit intricate don't you agree? Unit is too big...
        # If something breaks, it can be anywhere within this module..

        # Arrange
        ingredients = 'broccoli\ngoat\n'
        with open('super_secret_temp_test_file.txt', 'w+') as open_file:
            open_file.write(ingredients)

        without_side_effects = WithoutSideEffects()
        with patch('random.randint') as mock_randint:
            mock_randint.return_value = 3

            # Act
            without_side_effects.assign_random_number()
            without_side_effects.assign_menu('super_secret_temp_test_file.txt')

        # Assert
        #   Clean first
        os.remove('super_secret_temp_test_file.txt')
        expected_menu = ['Spaghetti with broccoli sauce', 'Kebab']
        self.assertEqual(without_side_effects.menu, expected_menu)

    def test__still_a_side_effect__happy_path(self):
        # This test case looks like it is testing something significant, but it is testing a single line of code
        # from the stdlib. Unit is too small, we should be testing more with this function.
        # Arrange
        with patch('random.randint') as mock_randint:
            mock_randint.return_value = 3

            # Act
            random_number = WithoutSideEffects.still_a_side_effect()

        # Assert
        self.assertEqual(random_number, 3)

    # TODO Go back to 1_side_effects to discuss why the unit tests are of significant size!
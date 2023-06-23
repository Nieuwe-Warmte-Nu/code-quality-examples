import random
from unittest import TestCase
from unittest.mock import Mock, patch

from code_quality_examples.example_3_mocks import WithoutSideEffects


class TestWithoutSideEffects(TestCase):
    def test__assign_random_number__happy_path(self):
        # Arrange
        # Random number if still in here... but it is isolated so we can keep the 'test magic' to a minimum!
        random.randint = Mock()
        random.randint.return_value = 3

        without_side_effects = WithoutSideEffects()

        # Act
        without_side_effects.assign_random_number()

        # Assert
        expected_number_of_the_day = 3
        self.assertEqual(without_side_effects.number_of_the_day, expected_number_of_the_day)

    def test__assign_random_number__happy_path_without_mock(self):
        # Arrange
        without_side_effects = WithoutSideEffects()

        # Act
        without_side_effects.assign_random_number()

        # TODO Secret trick to check if something is a mock
        #  print(random.randint)

        # Assert
        self.assertTrue(0 < without_side_effects.number_of_the_day < 8)
        # TODO This keeps breaking.. why is it always 3 here?
        #  Answer: We haven't cleaned up our mock properly from the previous function!!
        # self.assertNotEqual(without_side_effects.number_of_the_day, 3)

    # def test__assign_random_number__happy_path_proper(self):
    #     # Arrange
    #     # Random number if still in here... but it is isolated so we can keep the 'test magic' to a minimum!
    #     without_side_effects = WithoutSideEffects()
    #
    #     with patch('random.randint') as mock_randint:
    #         mock_randint.return_value = 3
    #
    #         # Act
    #         # Notice how we moved the indent to fall within the 'with'!
    #         without_side_effects.assign_random_number()
    #
    #     # Assert
    #     expected_number_of_the_day = 3
    #     self.assertEqual(without_side_effects.number_of_the_day, expected_number_of_the_day)

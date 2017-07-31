"""Tests for question 1 - rearranging cars."""

from itertools import permutations
from random import randint
import unittest
import logging

from rearranging_cars import rearrange_cars

_NUMBER_OF_GENERATED_TESTS = 100
_NUMBER_OF_CARS_TO_PERMUTE = 10


def _apply_moves(initial_car_park, moves):
    """
    The method applies a sequence of moves to the given cars' layout on the parking and returns the resulting layout.

        Args:
            initial_car_park:   an array of integers, indicates the initial locations (layout) of cars on the parking
            moves:              an array of Move objects, indicates how the cars are supposed to be moved.

        Returns:
            a list of integers, indicates the resulting cars' layout after the sequence of moves is applied.
    """
    for move in moves:
        # Swap 'start' and 'end' of the move to perform the move
        initial_car_park[move.get_origin()], initial_car_park[move.get_destination()] =\
            initial_car_park[move.get_destination()], initial_car_park[move.get_origin()]
    return initial_car_park


def _test_result(initial_car_park, final_car_park):
    """
    The method verifies the correctness of the move sequence to rearrange cars and checks the number of moves.

        Args:
            initial_car_park:    a list of integers, indicates the initial locations (layout) of cars on the parking
            final_car_park:      a list of integers, indicates the desired locations (layout) of cars on the parking

        Returns:
            a boolean,  indicates whether the generated rearrangement is valid (leads to desired cars' positions)
            an integer, the number of moves performed
    """
    # Copy the initial car park to not change it in place. Helps in testing.
    current_car_park = list(initial_car_park)
    move_sequence = rearrange_cars(current_car_park, final_car_park)
    positions_after_rearranging = _apply_moves(initial_car_park, move_sequence)
    if final_car_park == positions_after_rearranging:
        return True, len(move_sequence)
    else:
        return False, len(move_sequence)


class RearrangingCarsTest(unittest.TestCase):
    logging.basicConfig(level=logging.INFO)

    def testInvalidInput(self):
        """Tests the error is raised when the parking size (lists lengths) don't match."""
        initial_car_park = [1, 2, 0, 3]
        final_car_park = [1, 2, 0, 3, 4]
        with self.assertRaises(ValueError):
            rearrange_cars(initial_car_park, final_car_park)

        logger = logging.getLogger(__name__)
        logger.info(
            'Test with ValueError expected: start positions = %s, end positions = %s, input length\' don\'t match',
            initial_car_park, final_car_park)

    def testNoMoveCases(self):
        """Tests examples where no moves are expected."""
        initial_car_park = [1, 2, 0, 3]
        final_car_park = [1, 2, 0, 3]
        verify_result, number_of_moves = _test_result(initial_car_park, final_car_park)
        self.assertTrue(verify_result and number_of_moves == 0)

        logger = logging.getLogger(__name__)
        logger.info(
            'Test with no moves expected: start positions = %s, end positions = %s, number of moves performed = %s',
            initial_car_park, final_car_park, number_of_moves)

        initial_car_park = []
        final_car_park = []
        verify_result, number_of_moves = _test_result(initial_car_park, final_car_park)
        self.assertTrue(verify_result and number_of_moves == 0)

        logger = logging.getLogger(__name__)
        logger.info(
            'Test with no moves expected: start positions = %s, end positions = %s, number of moves performed = %s',
            initial_car_park, final_car_park, number_of_moves)

    def testGivenCases(self):
        """Tests the given example cases."""
        initial_car_park = [1, 2, 0, 3]
        final_car_park = [3, 1, 2, 0]
        verify_result, number_of_moves = _test_result(initial_car_park, final_car_park)
        self.assertTrue(verify_result)

        logger = logging.getLogger(__name__)
        logger.info('Testing given example: start positions = %s, end positions = %s, number of moves performed = %s',
                    initial_car_park, final_car_park, number_of_moves)

    def testNumberOfMovesPerformed(self):
        """Generate all possible permutations of 10 cars' layouts on the parking and randomly choose 100 pairs
           from the pairs of of those permutations. Use the pairs of permutations as paris of start and end
           positions of cars.

           The purpose of the given test is to check the number of moves the algorithm uses to get to desired parking
           layout. The number of moves is presented in the logging message."""
        # Generate all permutations of 10 cars on the parking.
        permutations_of_cars = list(permutations(range(_NUMBER_OF_CARS_TO_PERMUTE)))
        number_of_permutations = len(permutations_of_cars)

        moves_sum = 0

        for i in range(_NUMBER_OF_GENERATED_TESTS):
            # Randomly choose a pair of those permutations.
            initial_car_park = list(permutations_of_cars[randint(0, number_of_permutations - 1)])
            final_car_park = list(permutations_of_cars[randint(0, number_of_permutations - 1)])

            logger = logging.getLogger(__name__)
            logger.info('Generating test: start positions = %s, end positions = %s',
                        initial_car_park, final_car_park)

            verify_result, number_of_moves = _test_result(initial_car_park, final_car_park)
            self.assertTrue(verify_result)
            self.assertTrue(verify_result)

            logger.info('Test passed, number of moves performed = %s', number_of_moves)
            moves_sum += number_of_moves

        mean_number_of_moves = float(moves_sum) / _NUMBER_OF_GENERATED_TESTS
        logger.info('The mean number of moves in %s generated tests with %s cars in the parking lot is: %s',
                    _NUMBER_OF_GENERATED_TESTS, _NUMBER_OF_CARS_TO_PERMUTE, mean_number_of_moves)


if __name__ == '__main__':
    unittest.main()

import unittest
import main
import sys
import io
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

class TestMarsRoverFunctions(TestCase):
    # Format input tests
    def test_format_input(self):
        self.assertEqual(main.format_input("(3, 4, N) FLFFR"), ((3,4), "N", "FLFFR"))
    
    # Update orientation tests
    def test_update_orientation_success_case(self):
        self.assertEqual(main.update_orientation('L', 'N'), 'W')
        self.assertEqual(main.update_orientation('R', 'N'),'E')
        self.assertEqual(main.update_orientation('R', 'W'),'N')
        self.assertEqual(main.update_orientation('L', 'W'),'S')

    def test_update_orientation_no_change_case(self):
        self.assertEqual(main.update_orientation('F', 'N'),'N')

    # check positions tests
    def test_check_position_success_case(self):
        self.assertTrue(main.check_position([5, 5], (2,3)))
    
    def test_check_position_below_zero(self):
        self.assertFalse(main.check_position([5, 5], (-1,3))) 
        self.assertFalse(main.check_position([59, 57], (3,-1)))

    def test_check_position_above_max(self):
        self.assertFalse(main.check_position([5, 5], (1,6)))
        self.assertFalse(main.check_position([6, 60],(6,61)))
    
    def test_check_position_edge_cases(self):
        self.assertTrue(main.check_position([5, 5],(0,3)))
        self.assertTrue(main.check_position([5, 7],(3,0)))
        grid = [6, 3]
        self.assertTrue(main.check_position(grid, (3,grid[1])))
        grid = [20, 4]
        self.assertTrue(main.check_position(grid, (5,grid[1])))

    # Move rover tests
    def test_move_rover_success_case(self):
        self.assertEqual(main.move_rover([5,5], 'F', 'N', (3,3)), ((3,4), True))
    
    def test_move_rover_lost_rover_case(self):
        grid = [5,15]
        self.assertEqual(main.move_rover(grid, 'F', 'E', (grid[0], 3)), ((grid[0], 3), False))
        grid = [7,2]
        self.assertEqual(main.move_rover(grid, 'F', 'N', (3,grid[1])), ((3,grid[1]), False))
        grid = [4,9]
        self.assertEqual(main.move_rover(grid, 'F', 'W', (0,3)), ((0,3), False))
        grid = [20,9]
        self.assertEqual(main.move_rover(grid, 'F', 'S', (3,0)), ((3,0), False))

    # compute positions tests
    def test_compute_positions_success_case(self):
        with patch('sys.stdout', new = StringIO()) as fake_out:
            main.compute_positions('(2, 3, N) FLRRFFRL', [5, 5])
            self.assertEqual(fake_out.getvalue().strip(), '(4, 4, E)')
    
    def test_compute_positions_lost_rover_case(self):
        with patch('sys.stdout', new = StringIO()) as fake_out:
            main.compute_positions('(2, 3, N) FLRRFFFFRL', [5, 5])
            self.assertEqual(fake_out.getvalue().strip(), '(5, 4, E) LOST')
    
    # run premade tests
    def test_run_premade(self):
        expected = '(2, 3, W)\n(1, 0, S) LOST'
        with patch('sys.stdout', new = StringIO()) as fake_out:
            main.run_premade('test.txt')
            self.assertEqual(fake_out.getvalue().strip(), expected)
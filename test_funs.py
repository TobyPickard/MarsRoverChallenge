import unittest
import main

class TestMarsRoverFunctions(unittest.TestCase):
    def test_format_input(self):
        input = "(3, 4, N) FLFFR"
        pos, ori, instructions = main.format_input(input)
        assert pos == (3,4)
        assert ori == "N"
        assert instructions == "FLFFR"
    
    def test_update_orientation_success(self):
        new_orientation = main.update_orientation('L', 'N')
        assert new_orientation == 'W'
        new_orientation = main.update_orientation('R', 'N')
        assert new_orientation == 'E'
        new_orientation = main.update_orientation('R', 'W')
        assert new_orientation == 'N'
        new_orientation = main.update_orientation('L', 'W')
        assert new_orientation == 'S'
    
    def test_update_orientation_no_change(self):
        new_orientation = main.update_orientation('F', 'N')
        assert new_orientation == 'N'

    def test_move_rover_success_case(self):
        grid = [5,5]
        instruction = 'F'
        orientation = 'N'
        initial_position = (3,3)
        new_pos, success = main.move_rover(grid, instruction, orientation, initial_position)
        assert success is True
        assert new_pos == (4,3)
    
    def test_move_rover_lost_rover_case(self):
        grid = [5,15]
        pos, success = main.move_rover(grid, 'F', 'N', (grid[0],3))
        assert success is False
        assert pos == (grid[0],3)

        grid = [7,2]
        pos, success = main.move_rover(grid, 'F', 'E', (3,grid[1]))
        assert success is False
        assert pos == (3,grid[1])

        grid = [4,9]
        pos, success = main.move_rover(grid, 'F', 'S', (0,3))
        assert success is False
        assert pos == (0,3)

        grid = [20,9]
        pos, success = main.move_rover(grid, 'F', 'W', (3,0))
        assert success is False
        assert pos == (3,0)

    def test_check_position_success_case(self):
        grid = [5, 5]
        position = (2,3)
        assert main.check_position(grid, position) is True
    
    def test_check_position_below_zero(self):
        grid = [5, 5]
        position = (-1,3)
        assert main.check_position(grid, position) is False
        grid = [59, 57]
        position = (3,-1)
        assert main.check_position(grid, position) is False

    def test_check_position_above_max(self):
        grid = [5, 5]
        position = (1,6)
        assert main.check_position(grid, position) is False
        grid = [6, 60]
        position = (6,61)
        assert main.check_position(grid, position) is False
    
    def test_check_position_edge_cases(self):
        grid = [5, 5]
        position = (0,3)
        assert main.check_position(grid, position) is True
        grid = [5, 7]
        position = (3,0)
        assert main.check_position(grid, position) is True 
        grid = [6, 3]
        position = (3,grid[1])
        assert main.check_position(grid, position) is True
        grid = [20, 4]
        position = (5,grid[1])
        assert main.check_position(grid, position) is True
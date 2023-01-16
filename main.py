def format_input(input: str):
    instructions = input.replace('(', '').replace(')', '').replace(',', '').split(' ')
    return (int(instructions[0]), int(instructions[1])), \
        instructions[2], instructions[3]

#==============================================================================

def update_orientation(instruction: str, initial_orientation: str):
    possible_orientations = ['N', 'E', 'S', 'W']
    orientation_index = possible_orientations.index(initial_orientation)
    if instruction == 'L':
        orientation_index = (len(possible_orientations) - 1 if orientation_index <= 0 
                                else orientation_index - 1)
        return possible_orientations[orientation_index]
    if instruction == 'R':
        orientation_index = (0 if orientation_index >= len(possible_orientations) - 1 
                                else orientation_index + 1)
        return possible_orientations[orientation_index]
    return initial_orientation

#==============================================================================

def move_rover(grid: list, instruction: str, orientation: str, initial_position: tuple):
    row, col = initial_position
    if instruction == 'F':
        match orientation:
            case 'N':
                col += 1
            case 'S':
                col -= 1
            case 'W':
                row -= 1
            case 'E':
                row += 1
    if check_position(grid, (row,col)) is True:
        return (row,col), True
    return initial_position, False

#==============================================================================

def check_position(grid: list, position: tuple):
    return (True if position[0] in range(0,grid[0]+1) and 
            position[1] in range(0,grid[1]+1) else False)

#==============================================================================

def compute_positions(data: list, grid: list):
    for i in data:
        position, orientation, instructions = format_input(i)
        for step in instructions: 
            orientation = update_orientation(step, orientation)                                                            
            position, success = move_rover(grid, step, orientation, position)
            if success is False:
                break
        print(f'({position[0]}, {position[1]}, {orientation}) LOST' 
                if success is False 
                else f'({position[0]}, {position[1]}, {orientation})')

#==============================================================================

def run_premade(file_path = 'robotInstructions.txt'):
    with open(file_path, 'r') as file:
        robots = file.read().split('\n')
    grid = robots[0]
    robots.remove(grid)
    grid = grid.split(' ')
    grid = list(map(int, grid))

    compute_positions(robots, grid)

#==============================================================================

def loop_inputs(prompt):
    while True: 
        user = input(prompt)
        check = input(f'{user}. Is this correct? (y/n)')
        match check:
            case 'y':
                return user
            case 'n':
                continue 
            case _: 
                print('Invalid input')

#==============================================================================

def run_user_inputs():
    robots = []
    grid = loop_inputs('Grid dimensions: ')
    grid = grid.split(' ')
    grid = list(map(int, grid))
    while True:
        instructions = loop_inputs('Robot instructions: ')
        robots.append(instructions)
        if input('Add another robot? (y/n)') == 'n':
            break
    
    compute_positions(robots, grid)

#==============================================================================

def main():
    while True:
        choice = input('''
            would you like to:
            (1) Run script using premade set of values i.e. instructions.txt
            (2) run with new user input values
            (q) Quit
            ''')
        match choice:
            case '1':
                run_premade()
            case '2': 
                run_user_inputs()
            case'q':
                return
            case _:
                print('Invalid input')

if __name__ == "__main__": 
    main()
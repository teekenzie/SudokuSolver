import Solver, Puzzle
import Puzzle_examples #For Testing purpose 

def help_guide():
    """
    (row, col, val) --> Sets the grid at (row, col) to val
    Solve --> Solves the puzzle
    Display Puzzle --> Display the puzzle
    """
    print ('(row, col, val) --> Sets the grid at (row, col) to val')
    print ('Solve --> Solves the puzzle')
    print ('Display Puzzle --> Display the puzzle')

def set_answer(puzzle, inpt):
    inpt = [int(x) for x in inpt if x.isdigit()]
    puzzle.set_loc_answer(inpt[0], inpt[1], inpt[2])


puzzle = Puzzle.Puzzle()
solver = Solver.Solver()
commands_dict ={
    'h': 'help_guide()', 
    '(': 'set_answer(puzzle, inpt)',
    's': 'print(solver.solve_puzzle(puzzle))',
    'd': 'puzzle.show_puzzle()'
}
print ("Sodoku Solver")
print ("Enter 'Help' for help")
while True:
    inpt = input('Enter Command: ').strip().lower()
    command = inpt[0]
    if command in commands_dict:
        eval(commands_dict[command])
    else:
        print("Command not available")

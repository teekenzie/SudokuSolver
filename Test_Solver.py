from Test_Template import *
import Puzzle, Solver, Puzzle_examples
from SolvingMethods import *

"""
Test functionality of Solver
"""

puzzle_dict = {
    1: Puzzle_examples._puzzle1(),
    2: Puzzle_examples._puzzle2(),
    3: Puzzle_examples._puzzle3(),
    4: Puzzle_examples._puzzle4(),
    5: Puzzle_examples._puzzle5(),
    6: Puzzle_examples._puzzle6(),
    7: Puzzle_examples._puzzle7(),
    8: Puzzle_examples._puzzle8(), 
    9: Puzzle_examples._puzzle9()
}
def test_solver(puzzle_num ):
    solver = Solver.Solver()
    puzzle_test = puzzle_dict[puzzle_num]
    print('Puzzle {}'.format(puzzle_num))
    puzzle_test.show_puzzle()
    print ('\n')
    print (solver.solve_puzzle(puzzle_test))
    puzzle_test.show_puzzle()
    print('\n')
    return puzzle_test

def test_all():
    test_solver(1)
    test_solver(2)
    test_solver(3)
    test_solver(4)
    test_solver(5)
    test_solver(6)
    test_solver(7)
    test_solver(8)
    test_solver(9)
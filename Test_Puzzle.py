import Grid, Puzzle, SolvingMethods
from Test_Template import *
"""
Test the functionality of the puzzle and grid implementation
"""
def test_all():
    funcs = [ 
        test_gridLoc,
        test_Notegrid,
        test_Answergrid,
        test_puzzle,
        test_puzzleSetGrid]
    test_funcs(funcs)

@test_decorator
def test_gridLoc():
    show_test("Grid(0,0)", Grid.Grid(0,0), 
        "Grid at (0, 0), square: 0; Note: [1, 2, 3, 4, 5, 6, 7, 8, 9]")
    show_test("Grid(2,0)", Grid.Grid(2,0), 
        "Grid at (2, 0), square: 0; Note: [1, 2, 3, 4, 5, 6, 7, 8, 9]")
    show_test("Grid(8,8)", Grid.Grid(8,8), 
        "Grid at (8, 8), square: 8; Note: [1, 2, 3, 4, 5, 6, 7, 8, 9]")
    show_test("Grid(4,4)", Grid.Grid(4,4), 
        "Grid at (4, 4), square: 4; Note: [1, 2, 3, 4, 5, 6, 7, 8, 9]")
    show_test("Grid(6,5)", Grid.Grid(6,5), 
        "Grid at (6, 5), square: 7; Note: [1, 2, 3, 4, 5, 6, 7, 8, 9]")

@test_decorator
def test_Notegrid():
    noteGrid = Grid.Grid(0,0)
    show_run_func("noteGrid = Grid.Grid(0,0)")
    show_test("noteGrid.get_note()", noteGrid.get_note(), 
       "[1, 2, 3, 4, 5, 6, 7, 8, 9]" )
    noteGrid.remove_note_val(4)
    show_run_func("noteGrid.remove_note_val(4)")
    show_test("noteGrid.get_note()",noteGrid.get_note(), 
       "[1, 2, 3, 5, 6, 7, 8, 9]" )
    show_test("noteGrid.get_answer()", noteGrid.get_answer(), "0")
    show_test("str(noteGrid)", noteGrid, 
        "Grid at (0, 0), square: 0; Note: [1, 2, 3, 5, 6, 7, 8, 9]")

@test_decorator
def test_Answergrid():
    answerGrid = Grid.Grid(7,4)
    show_run_func("answerGrid = Grid.Grid(7,4)")
    answerGrid.set_answer(6)
    show_run_func("answerGrid.set_answer(6)")
    show_test("answerGrid.get_answer()", answerGrid.get_answer(), "6")
    show_test("answerGrid.get_note()", answerGrid.get_note(), "[]")
    show_test("str(answerGrid)", answerGrid,
        'Grid at (7, 4), square: 7; Value: 6' )

@test_decorator
def test_puzzle():
    puz = Puzzle.Puzzle()
    puz.show_puzzle()
    puz.set_loc_answer(0,0, 1)
    print ("Ran set_loc_answer(0,0,1) Set grid at 0,0  to 1")
    print ("")
    puz.show_puzzle()
    show_test("get_grid(0,0).get_answer()", puz.get_grid(0,0).get_answer(), "1")

@test_decorator
def test_puzzleSetGrid():
    puz = Puzzle.Puzzle()
    puz.show_puzzle()
    print ('')
    tempGrid = puz.get_grid(0,8)
    temp_loc = 0
    temp_val = 1
    for ind in range (0,9):
        puz.set_loc_answer(temp_loc+ind, temp_loc+ind, temp_val + ind)
    puz.set_grid_answer(tempGrid,3)
    puz.show_puzzle()
    print("expects the values of the diagonal lines to be values 1 - 9, value at top right corner to be 3")
    show_test("get_grid(2,1).get_note()", puz.get_grid(2,1).get_note(), "[4, 5, 6, 7, 8, 9]" )

import Puzzle

"""
Example puzzles for testing
"""

def _puzzle_xwing_row(): #used to test solving method x_wing_row
    puzzle = Puzzle.Puzzle()
    puzzle.set_loc_answer(0,0,1)
    puzzle.set_loc_answer(0,6,5)
    puzzle.set_loc_answer(0,7,6)
    puzzle.set_loc_answer(0,8,9)

    puzzle.set_loc_answer(1,0,4)
    puzzle.set_loc_answer(1,1,9)
    puzzle.set_loc_answer(1,2,2)
    puzzle.set_loc_answer(1,4,5)
    puzzle.set_loc_answer(1,5,6)
    puzzle.set_loc_answer(1,6,1)
    puzzle.set_loc_answer(1,8,8)

    puzzle.set_loc_answer(2,1,5)
    puzzle.set_loc_answer(2,2,6)
    puzzle.set_loc_answer(2,3,1)
    puzzle.set_loc_answer(2,5,9)
    puzzle.set_loc_answer(2,6,2)
    puzzle.set_loc_answer(2,7,4)

    puzzle.set_loc_answer(3,2,9)
    puzzle.set_loc_answer(3,3,6)
    puzzle.set_loc_answer(3,4,4)
    puzzle.set_loc_answer(3,6,8)
    puzzle.set_loc_answer(3,8,1)

    puzzle.set_loc_answer(4,1,6)
    puzzle.set_loc_answer(4,2,4)
    puzzle.set_loc_answer(4,4,1)
    
    puzzle.set_loc_answer(5,0,2)
    puzzle.set_loc_answer(5,1,1)
    puzzle.set_loc_answer(5,2,8)
    puzzle.set_loc_answer(5,4,3)
    puzzle.set_loc_answer(5,5,5)
    puzzle.set_loc_answer(5,6,6)
    puzzle.set_loc_answer(5,8,4)

    puzzle.set_loc_answer(6,1,4)
    puzzle.set_loc_answer(6,3,5)
    puzzle.set_loc_answer(6,7,1)
    puzzle.set_loc_answer(6,8,6)

    puzzle.set_loc_answer(7,0,9)
    puzzle.set_loc_answer(7,2,5)
    puzzle.set_loc_answer(7,4,6)
    puzzle.set_loc_answer(7,5,1)
    puzzle.set_loc_answer(7,6,4)
    puzzle.set_loc_answer(7,8,2)
    
    puzzle.set_loc_answer(8,0,6)
    puzzle.set_loc_answer(8,1,2)
    puzzle.set_loc_answer(8,2,1)
    puzzle.set_loc_answer(8,8,5)
    return puzzle

def _puzzle_xwing_col():
    puzzle= Puzzle.Puzzle()
    puzzle.set_loc_answer(0,7,9)
    puzzle.set_loc_answer(0,8,4)
    
    puzzle.set_loc_answer(1,0,7)
    puzzle.set_loc_answer(1,1,6)
    puzzle.set_loc_answer(1,3,9)
    puzzle.set_loc_answer(1,4,1)
    puzzle.set_loc_answer(1,7,5)

    puzzle.set_loc_answer(2,1,9)
    puzzle.set_loc_answer(2,5,2)
    puzzle.set_loc_answer(2,7,8)
    puzzle.set_loc_answer(2,8,1)

    puzzle.set_loc_answer(3,1,7)
    puzzle.set_loc_answer(3,4,5)
    puzzle.set_loc_answer(3,7,1)
    
    puzzle.set_loc_answer(4,3,7)
    puzzle.set_loc_answer(4,5,9)
    
    puzzle.set_loc_answer(5,1,8)
    puzzle.set_loc_answer(5,4,3)
    puzzle.set_loc_answer(5,5,1)
    puzzle.set_loc_answer(5,7,6)
    puzzle.set_loc_answer(5,8,7)

    puzzle.set_loc_answer(6,0,2)
    puzzle.set_loc_answer(6,1,4)
    puzzle.set_loc_answer(6,3,1)
    puzzle.set_loc_answer(6,7,7)
    
    puzzle.set_loc_answer(7,1,1)
    puzzle.set_loc_answer(7,4,9)
    puzzle.set_loc_answer(7,7,4)
    puzzle.set_loc_answer(7,8,5)

    puzzle.set_loc_answer(8,0,9)
    puzzle.set_loc_answer(8,6,1)

    return puzzle 
     

def _puzzle1(): #easy puzzle
    puzzle = Puzzle.Puzzle()
    puzzle.set_loc_answer(0,1,4)
    puzzle.set_loc_answer(0,2,7)
    puzzle.set_loc_answer(0,4,1)
    puzzle.set_loc_answer(0,7,3)

    puzzle.set_loc_answer(1,0,9)
    puzzle.set_loc_answer(1, 3, 3)
    puzzle.set_loc_answer(1,5,6)
    puzzle.set_loc_answer(1,7,7)

    puzzle.set_loc_answer(2,0,5)
    puzzle.set_loc_answer(2,2,6)
    puzzle.set_loc_answer(2,3,8)
    puzzle.set_loc_answer(2,4,4)
    puzzle.set_loc_answer(2,5,7)
    puzzle.set_loc_answer(2,6,2)

    puzzle.set_loc_answer(3,1,7)
    puzzle.set_loc_answer(3,2,2)
    puzzle.set_loc_answer(3,6,1)
    puzzle.set_loc_answer(3,7,5)
    puzzle.set_loc_answer(3,8,3)

    puzzle.set_loc_answer(4,0,1)
    puzzle.set_loc_answer(4,2,5)
    puzzle.set_loc_answer(4,5,4)
    puzzle.set_loc_answer(4,7,9)
    puzzle.set_loc_answer(4,8,2)

    puzzle.set_loc_answer(5,1,6)
    puzzle.set_loc_answer(5,2,9)
    puzzle.set_loc_answer(5,4,2)
    puzzle.set_loc_answer(5,6,7)
    
    puzzle.set_loc_answer(6,2,4)
    puzzle.set_loc_answer(6,3,9)
    puzzle.set_loc_answer(6,5,2)
    puzzle.set_loc_answer(6,6,3)

    puzzle.set_loc_answer(7,0,2)
    puzzle.set_loc_answer(7,1,9)
    puzzle.set_loc_answer(7,3,5)
    puzzle.set_loc_answer(7,4,7)
    
    puzzle.set_loc_answer(8,3,4)
    puzzle.set_loc_answer(8,4,8)
    puzzle.set_loc_answer(8,8,7)
    return puzzle

def _puzzle2(): # IMPOSSIBLE TO SOLVE PUZZLE
    puzzle = Puzzle.Puzzle()
    puzzle.set_loc_answer(0,0,1)
    puzzle.set_loc_answer(0,1,2)
    puzzle.set_loc_answer(0,2,3)
    
    puzzle.set_loc_answer(0,3,4)
    puzzle.set_loc_answer(0,4,5)
    puzzle.set_loc_answer(0,5,6)

    puzzle.set_loc_answer(0,6,7)
    puzzle.set_loc_answer(0,7,8)
    puzzle.set_loc_answer(0,8,9)

    puzzle.set_loc_answer(1,0,1)
    return puzzle

def _puzzle3(): #already solved puzzle
    puzzle = Puzzle.Puzzle()
    puzzle.set_loc_answer(0,0,8)
    puzzle.set_loc_answer(0,1,4)
    puzzle.set_loc_answer(0,2,7)
    puzzle.set_loc_answer(0,3,2)
    puzzle.set_loc_answer(0,4,1)
    puzzle.set_loc_answer(0,5,9)
    puzzle.set_loc_answer(0,6,5)
    puzzle.set_loc_answer(0,7,3)
    puzzle.set_loc_answer(0,8,6)

    puzzle.set_loc_answer(1,0,9)
    puzzle.set_loc_answer(1,1,2)
    puzzle.set_loc_answer(1,2,1)
    puzzle.set_loc_answer(1, 3, 3)
    puzzle.set_loc_answer(1,4,5)
    puzzle.set_loc_answer(1,5,6)
    puzzle.set_loc_answer(1,6,8)
    puzzle.set_loc_answer(1,7,7)
    puzzle.set_loc_answer(1,8,4)

    puzzle.set_loc_answer(2,0,5)
    puzzle.set_loc_answer(2,1,3)
    puzzle.set_loc_answer(2,2,6)
    puzzle.set_loc_answer(2,3,8)
    puzzle.set_loc_answer(2,4,4)
    puzzle.set_loc_answer(2,5,7)
    puzzle.set_loc_answer(2,6,2)
    puzzle.set_loc_answer(2,7,1)
    puzzle.set_loc_answer(2,8,9)

    puzzle.set_loc_answer(3,0,4)
    puzzle.set_loc_answer(3,1,7)
    puzzle.set_loc_answer(3,2,2)
    puzzle.set_loc_answer(3,3,6)
    puzzle.set_loc_answer(3,4,9)
    puzzle.set_loc_answer(3,5,8)
    puzzle.set_loc_answer(3,6,1)
    puzzle.set_loc_answer(3,7,5)
    puzzle.set_loc_answer(3,8,3)

    puzzle.set_loc_answer(4,0,1)
    puzzle.set_loc_answer(4,1,8)
    puzzle.set_loc_answer(4,2,5)
    puzzle.set_loc_answer(4,3,7)
    puzzle.set_loc_answer(4,4,3)
    puzzle.set_loc_answer(4,5,4)
    puzzle.set_loc_answer(4,6,6)
    puzzle.set_loc_answer(4,7,9)
    puzzle.set_loc_answer(4,8,2)

    puzzle.set_loc_answer(5,0,3)
    puzzle.set_loc_answer(5,1,6)
    puzzle.set_loc_answer(5,2,9)
    puzzle.set_loc_answer(5,3,1)
    puzzle.set_loc_answer(5,4,2)
    puzzle.set_loc_answer(5,5,5)
    puzzle.set_loc_answer(5,6,7)
    puzzle.set_loc_answer(5,7,4)
    puzzle.set_loc_answer(5,8,8)

    puzzle.set_loc_answer(6,0,7)
    puzzle.set_loc_answer(6,1,1)
    puzzle.set_loc_answer(6,2,4)
    puzzle.set_loc_answer(6,3,9)
    puzzle.set_loc_answer(6,4,6)
    puzzle.set_loc_answer(6,5,2)
    puzzle.set_loc_answer(6,6,3)
    puzzle.set_loc_answer(6,7,8)
    puzzle.set_loc_answer(6,8,5)

    puzzle.set_loc_answer(7,0,2)
    puzzle.set_loc_answer(7,1,9)
    puzzle.set_loc_answer(7,2,8)
    puzzle.set_loc_answer(7,3,5)
    puzzle.set_loc_answer(7,4,7)
    puzzle.set_loc_answer(7,5,3)
    puzzle.set_loc_answer(7,6,4)
    puzzle.set_loc_answer(7,7,6)
    puzzle.set_loc_answer(7,8,1)
    
    puzzle.set_loc_answer(8,0,6)
    puzzle.set_loc_answer(8,1,5)
    puzzle.set_loc_answer(8,2,3)
    puzzle.set_loc_answer(8,3,4)
    puzzle.set_loc_answer(8,4,8)
    puzzle.set_loc_answer(8,5,1)
    puzzle.set_loc_answer(8,6,9)
    puzzle.set_loc_answer(8,7,2)
    puzzle.set_loc_answer(8,8,7)
    return puzzle

def _puzzle4(): #hard puzzle
    puzzle = Puzzle.Puzzle()
    
    puzzle.set_loc_answer(0,4, 6)
    puzzle.set_loc_answer(0,7,1)
    puzzle.set_loc_answer(0,8,9)

    puzzle.set_loc_answer(1,1,1)
    puzzle.set_loc_answer(1,6,7)
    puzzle.set_loc_answer(1,7,8)
    puzzle.set_loc_answer(1,8,6)

    puzzle.set_loc_answer(2,0,6)
    puzzle.set_loc_answer(2,2,3)
    puzzle.set_loc_answer(2,3,1)
    puzzle.set_loc_answer(2,4,9)

    puzzle.set_loc_answer(3,0,7)
    puzzle.set_loc_answer(3,1,6)
    puzzle.set_loc_answer(3,5,9)
    
    puzzle.set_loc_answer(4,3,7)
    puzzle.set_loc_answer(4,7,6)

    puzzle.set_loc_answer(5,4,8)
    puzzle.set_loc_answer(5,6,9)
    puzzle.set_loc_answer(5,7,7)
    puzzle.set_loc_answer(5,8,4)

    puzzle.set_loc_answer(6,0,8)
    puzzle.set_loc_answer(6,2,1)
    puzzle.set_loc_answer(6,3,9)
    puzzle.set_loc_answer(6,4,2)
    puzzle.set_loc_answer(6,6,5)

    puzzle.set_loc_answer(7,1,5)
    puzzle.set_loc_answer(7,4,7)
    puzzle.set_loc_answer(7,5,3)

    puzzle.set_loc_answer(8,1,4)
    puzzle.set_loc_answer(8,5,1)

    return puzzle

def _puzzle5(): #expert puzzle
    puzzle = Puzzle.Puzzle()

    puzzle.set_loc_answer(0,0,3)
    puzzle.set_loc_answer(0,1,7)
    puzzle.set_loc_answer(0,2,9)

    puzzle.set_loc_answer(1,0,8)
    puzzle.set_loc_answer(1,3,4)
    puzzle.set_loc_answer(1,4,2)

    puzzle.set_loc_answer(2,0,2)
    puzzle.set_loc_answer(2,4,1)

    puzzle.set_loc_answer(3,1,5)
    puzzle.set_loc_answer(3,7,2)

    puzzle.set_loc_answer(4,2,7)
    puzzle.set_loc_answer(4,8,8)

    puzzle.set_loc_answer(5,4,6)
    puzzle.set_loc_answer(5,5,5)
    puzzle.set_loc_answer(5,8,4)

    puzzle.set_loc_answer(6,3,9)

    puzzle.set_loc_answer(7,1,8)
    puzzle.set_loc_answer(7,3,3)
    puzzle.set_loc_answer(7,6,7)

    puzzle.set_loc_answer(8,5,2)
    puzzle.set_loc_answer(8,6,3)
    puzzle.set_loc_answer(8,7,9)

    return puzzle

def _puzzle6(): # expert puzzle
    puzzle = Puzzle.Puzzle()

    puzzle.set_loc_answer(0,0,8)
    puzzle.set_loc_answer(0,1,4)
    puzzle.set_loc_answer(0,4,2)
    puzzle.set_loc_answer(0,5,7)
    puzzle.set_loc_answer(0,7,3)
    puzzle.set_loc_answer(0,8,1)

    puzzle.set_loc_answer(1,3,8)

    puzzle.set_loc_answer(2,0,1)
    puzzle.set_loc_answer(2,1,3)
    puzzle.set_loc_answer(2,5,4)

    puzzle.set_loc_answer(3,0,3)
    puzzle.set_loc_answer(3,1,2)
    puzzle.set_loc_answer(3,4,7)
    puzzle.set_loc_answer(3,6,4)
    
    puzzle.set_loc_answer(4,1,5)
    puzzle.set_loc_answer(4,7,1)
    puzzle.set_loc_answer(4,8,8)

    puzzle.set_loc_answer(5,7,5)

    puzzle.set_loc_answer(6,0,6)
    puzzle.set_loc_answer(6,3,9)
    puzzle.set_loc_answer(6,4,8)

    puzzle.set_loc_answer(7,8,5)
    
    puzzle.set_loc_answer(8,0,7)
    puzzle.set_loc_answer(8,7,6)
    return puzzle 

def _puzzle7():
    puzzle = Puzzle.Puzzle()

    puzzle.set_loc_answer(0,1,5)

    puzzle.set_loc_answer(1,0,4)
    puzzle.set_loc_answer(1,1,6)
    puzzle.set_loc_answer(1,2,9)
    puzzle.set_loc_answer(1,8,5)

    puzzle.set_loc_answer(2,5,9)
    puzzle.set_loc_answer(2,6,3)

    puzzle.set_loc_answer(3,3,5)
    puzzle.set_loc_answer(3,5,7)
    puzzle.set_loc_answer(3,6,2)

    puzzle.set_loc_answer(4,0,1)
    puzzle.set_loc_answer(4,4,3)

    puzzle.set_loc_answer(5,7,1)

    puzzle.set_loc_answer(6,0,6)
    puzzle.set_loc_answer(6,8,7)

    puzzle.set_loc_answer(7,0,7)
    puzzle.set_loc_answer(7,2,4)
    puzzle.set_loc_answer(7,3,2)
    puzzle.set_loc_answer(7,6,1)

    puzzle.set_loc_answer(8,0,8)
    puzzle.set_loc_answer(8,3,6)
    puzzle.set_loc_answer(8,7,4)
    puzzle.set_loc_answer(8,8,2)

    return puzzle

def _puzzle8():
    puzzle = Puzzle.Puzzle()
    puzzle.set_loc_answer(0,6,1)
    puzzle.set_loc_answer(1,0,2)
    puzzle.set_loc_answer(1,3,7)
    puzzle.set_loc_answer(1,7,9)

    puzzle.set_loc_answer(2,2,3)
    puzzle.set_loc_answer(2,3,1)
    puzzle.set_loc_answer(2,7,8)
    puzzle.set_loc_answer(2,8,4)

    puzzle.set_loc_answer(3,1,6)
    puzzle.set_loc_answer(3,5,8)
    
    puzzle.set_loc_answer(4,0,1)
    puzzle.set_loc_answer(4,1,8)
    puzzle.set_loc_answer(4,4,2)
    puzzle.set_loc_answer(4,6,7)
    puzzle.set_loc_answer(4,7,6)

    puzzle.set_loc_answer(5,2,4)

    puzzle.set_loc_answer(6,1,3)
    puzzle.set_loc_answer(6,5,4)

    puzzle.set_loc_answer(7,0,6)
    puzzle.set_loc_answer(7,3,2)
    puzzle.set_loc_answer(7,6,8)

    puzzle.set_loc_answer(8,5,3)
    puzzle.set_loc_answer(8,6,5)
    puzzle.set_loc_answer(8,8,9)
    return puzzle

def _puzzle9(): # Impossible puzzle
    puzzle = Puzzle.Puzzle()
    puzzle.set_loc_answer(0,0,1)
    return puzzle
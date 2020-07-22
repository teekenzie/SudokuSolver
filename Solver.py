import SolvingMethods, copy
times_run = 0
"""
Check the grids by applying the solving methods on the rows, then the grids, then the squares
"""
class Solver:
    def solve_puzzle(self, puzzle):
        """
        Takes in an unsolved puzzle
        The method that would run other methods to solve the puzzle
        Should be run from the interface
        """
        if puzzle.is_puzzle_complete() == True:
            return 'Puzzle already solved'
        self._evaluate(puzzle, 'rows', [SolvingMethods.validate] )
        self._evaluate(puzzle, 'cols', [SolvingMethods.validate] )
        self._evaluate(puzzle, 'squares', [SolvingMethods.validate] )
        if puzzle.is_valid == False:
            return  "This puzzle is unsolvable"
        while puzzle.is_puzzle_complete() == False:
            puzzle.is_change_made = False
            funcs = [
                SolvingMethods.lonely,
                SolvingMethods.lonestar, 
                SolvingMethods.double,
                SolvingMethods.triple, 
                SolvingMethods.quad
            ]
    
            self._evaluate(puzzle,'rows', funcs + [SolvingMethods.x_wing_row])
            self._evaluate(puzzle,'cols', funcs + [SolvingMethods.x_wing_col])
            self._evaluate(puzzle,'squares', funcs + [SolvingMethods.candidate_line])
            if puzzle.is_change_made == False:
                global times_run
                if times_run > 25: #prevent it from guessing too many 
                    #if guessing more than 25, chances are that the puzzle is unsolvable
                    return "This puzzle is unsolvable"
                if puzzle.is_still_valid() == True:
                    times_run +=1
                    return self._rand_puzz(puzzle)
                else:
                    return "This puzzle is unsolvable"
        print (times_run)
        return 'Puzzle Solved'

    def _evaluate(self, puzzle, grids_name, funcs):
        """
        Execute all the func in funcs on the appropriate grids. 
        Grids_name could be rows, cols or squares
        """
        puzzle.reset_belong()
        name_dict = {'rows': puzzle.get_row_grids, 'cols':puzzle.get_col_grids, 'squares': puzzle.get_square_grids}
        for ind in range(9):
            lst_of_grids = name_dict[grids_name](ind)
            for func in funcs:
                func(lst_of_grids, puzzle)
    
    def _rand_puzz(self, puzzle):
        """
        Use when stuck at a dead end 
        Finds a grid with a two value note and then sets the grid answer to the values
        Works like a tree 
        if the first value of the note doesn't work out, then use the second value 
        if stuck at a dead end after trying the value, will try implementing this method again
        """
        def set_first_couple(puzzle, ind):
            for col in range(9):
                for row in range(9):
                    grid = puzzle.get_grid(row, col)
                    note = grid.get_note()
                    if len(note) == 2:
                        puzzle.set_grid_answer(grid, note[ind])
                        return
        
        new_puzzle0 = copy.deepcopy(puzzle)
        new_puzzle1 = copy.deepcopy(puzzle)
        set_first_couple(new_puzzle0, 0)
        set_first_couple(new_puzzle1,1)
        message0 = self.solve_puzzle(new_puzzle0)
        if message0 == 'Puzzle Solved':
            puzzle.replace(new_puzzle0)
            return message0
        else:
            message1 = self.solve_puzzle(new_puzzle1)
            if message1 == 'Puzzle Solved':
                puzzle.replace(new_puzzle1)
                return message1
            return message1
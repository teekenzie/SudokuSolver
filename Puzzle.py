import Grid
class Puzzle:
    
    """
    Represents the sudoku puzzle and is made of grids 
    Top right corner has the location (0,0) and square 0
    Top left corner has the locatoin (0,8) and square 2
    Bottom right corner has the location (8,0) and square 6
    Bottom left corner has the location (8,8) and square 8
    """
    def __init__(self):
        # puzzle in form of list of list 
        self._puzzle = self._gen_puzzle()
        # grid_filled in form of int
        self._grid_filled = 0
        self._gen_relatives() #generates the rows, columns, and squares of the puzzle
        self.is_change_made = False #Use in solver to determine if any changes has been made to the grid
        self.is_valid = True 
        self.times_run = 0

    def get_grid(self, row, col):
        """
        Returns the grid given the location
        """
        return self._puzzle[row][col]

    def get_row_grids(self, ind):
        """
        Returns the corresponding row of the ind 
        """
        return self.rows[ind]
    def get_col_grids(self, ind):
        """
        Returns the corresponding column of the ind 
        """
        return self.cols[ind]
    def get_square_grids(self, ind):
        """
        Returns the corresponding square of the ind 
        """
        return self.squares[ind]

    def _gen_relatives(self):
        """
        Creates and assign the rows, columns, and sqaures
        Private Method, should not be used outside
        """
        self.rows = self._puzzle
        tempSquares = [[] for _ in range(0,9)]
        tempCols = [[] for _ in range(0,9)]
        for rows in self._puzzle:
            for grid in rows:
                tempSquares[grid.get_square()].append(grid)
                tempCols[grid.get_location()[1]].append(grid)
        self.squares = tempSquares
        self.cols = tempCols

    def _gen_puzzle(self):
        """
        Creates the puzzle by placing corresponding grids to the corresponding locations in the puzzle
        Private Method, should not be used outside

        """
        result = [[] for _ in range(0,9)]
        for row in range(0,9):
            for col in range(0,9):
                result[row].append(Grid.Grid(row, col))
        return result
    
    def show_puzzle(self):
        """
        Display the Puzzle
        """
        print(" x  | 0 1 2  | 3 4 5  | 6 7 8")
        print ("********************************")
        for row in range(len(self._puzzle)):
            result = " " + str(row) + "  { "  
            if row ==3 or row ==6:
                print ("--------------------------------")
            for col in range(len(self._puzzle)):
                if col == 3 or col ==6:
                    result += " | "
                result += repr(self.get_grid(row, col)) + " "
            print (result)
    
    def set_loc_answer(self, row, col, val):
        """
        Set the answer of the grid with the given location to the given val
        Remove val from the note of row, col, square corresponding to the grid
        """
        if self.is_puzzle_complete() == True:
            return 
        self._puzzle[row][col].set_answer(val)
        self._grid_filled += 1
        grid_square = self._puzzle[row][col].get_square()
        for ind in range(0,9):
            self.rows[row][ind].remove_note_val(val)
            self.cols[col][ind].remove_note_val(val)
            self.squares[grid_square][ind].remove_note_val(val)
    
    def set_grid_answer(self, grid, val):
        """
        Sets the given grid to the given val
        Uses the set_loc_answer method
        """
        grid_loc = grid.get_location()
        self.set_loc_answer(grid_loc[0], grid_loc[1], val)

    def is_puzzle_complete(self):
        """
        Returns True if the puzzle is complete, else False
        """
        if self._grid_filled >= 81:
            return True
        return False
    
    def made_change(self):
        """
        Tells the puzzle that changes to the puzzle have been made
        """
        self.is_change_made = True

    def reset_belong(self):
        """
        Reset every grids belong to False 
        """
        for rows in self._puzzle:
            for grid in rows:
                grid.belong = False

    def replace(self, puzz):
        """
        Replace the whole puzzle with a new puzzle
        Use on when guessing starts
        """
        for row_ind in range(9):
            for col_ind in range(9):
                self._puzzle[row_ind][col_ind]= puzz.get_grid(row_ind, col_ind)

    def is_still_valid(self):
        """
        Checks if the puzzle is still valid
        Checks if any grid has empty note and no answer
        """
        for row_ind in range(9):
            for col_ind in range(9):
                grid = self._puzzle[row_ind][col_ind]
                if len(grid.get_note()) == 0 and grid.get_answer() ==0:
                    return False 
        return True 
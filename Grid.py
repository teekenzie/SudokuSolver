import Puzzle
class Grid:
    """
    Represent every grid of the sudoku puzzle. 
    The location is represnted with a tuple (row, column) and square property. 
    All grids in the same square will have the same square number
    Each grid has its corresponding notes
    Answer is represented by 0 if it doens't have an ansewr yet
    """

    def __init__(self, row, column):
        # location in form of tuples, square in form of int
        self._location, self._square = self._gen_location(row, column)
        # note in form of list
        self._note = [x for x in range (1,10)]
        # answer in form of int
        self._answer = 0
        # is the grid belongs to double, triple, quad or none
        self.belong = False
    
    def get_note (self):
        """ Returns the note values of the grid in form of list"""
        return self._note
    def remove_note_val(self, val):
        """ 
        Removes the given val from the note of the grid
        If there is only one val in the grid, then the answer is the val
        """
        assert val > 0 and val <10, "Value is not in range"
        if val in self._note:
            self._note.remove(val)

    def get_answer(self):
        """ Returns the answer of the grid"""
        return self._answer
    def set_answer(self, answer): 
        """ 
        Sets the answer of the grid to the answer given, removes all values in notes
        """
        self._answer = answer
        self._note = []

    def get_location(self):
        """Returns the location of the grid in tuples"""
        return self._location

    def get_square(self):
        """Returns the square that the grid is in"""
        return self._square

    def _gen_location(self, row, column): #privateMethod
        """ 
        Generate the location and square that the grid is in given the row and the column
        Private method and should not be used outside
        """
        if row <= 2 and column <=2:
            return (row, column), 0
        elif row <= 2 and column <= 5:
            return (row, column), 1
        elif row <= 2 and column <= 8:
            return (row, column),2

        elif row <= 5 and column <=2:
            return (row, column), 3
        elif row <= 5 and column <= 5:
            return (row, column), 4
        elif row <= 5 and column <= 8:
            return (row, column), 5

        elif row <= 8 and column <= 2:
            return (row, column), 6
        elif row <= 8 and column <= 5:
            return (row, column), 7
        elif row <= 8 and column <= 8:
            return (row, column), 8
        else:
            raise ValueError("Row or Column given is out of range")

    def __str__(self):
        result = "Grid at {}, square: {}; ".format(self.get_location(), self.get_square())
        if self.get_answer() == 0:
            result += "Note: {}".format(self.get_note())
        else:
            result += "Value: {}".format(self.get_answer())
        return result
    def __repr__(self):
        return "{}".format(self.get_answer())

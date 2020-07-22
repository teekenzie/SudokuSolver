from SolvingMethods import * 
import Grid, Puzzle, Puzzle_examples
from Test_Template import *

"""
Test the functionalities of the solving methods implemented
"""
def helper_lst(fn, fnName):
    def temp_func(lst, lstname, lstresult):
        show_run_func(lst)
        fn(lst)
        output = "{}({})".format(fnName, lstname)
        show_test(output, lst, lstresult)
    return temp_func

def helper_grid(fn, fnName):
    def make_grid_lst(lst):
        puzzle = Puzzle.Puzzle()
        grid_lst= [puzzle.get_grid(0,x) for x in range(len(lst))]
        for ind in range(len(grid_lst)):
            grid = grid_lst[ind]
            grid._note = lst[ind] 
            """
            if lst[ind] == [5,6] or lst[ind] == [5,6,7]: # for test_quad
                grid.belong = True
            """
        return grid_lst, puzzle
    def temp_func(lst, lstname, lstresult):
        show_run_func(lst)
        grids, puzzle = make_grid_lst(lst)
        fn(grids, puzzle)
        lstran = []
        for grid in grids:
            lstran.append(grid.get_note())
        output = "{}({})".format(fnName, lstname)
        show_test(output, lstran, lstresult)
    return temp_func

def test_all():
    funcs = [
        test_lonely,
        test_lonestar, 
        test_double,
        test_remove_grid_vals,
        test_triple,
        test_quad
        ]
    test_funcs(funcs)

@test_decorator
def test_lonely():
    puzz = Puzzle.Puzzle()
    grid1= puzz.get_grid(0,0)
    grid2 = puzz.get_grid(0, 6)
    grid1._note = [1]
    grid2._note = [9]
    lonely(puzz.get_row_grids(grid1), puzz)
    show_run_func("lonely(puzz.get_row_grids(grid1), puzz)")
    show_test("get_grid(0,0)",str(puzz.get_grid(0,0)), 
        'Grid at (0, 0), square: 0; Value: 1')
    show_test("get_grid(0,6)",str(puzz.get_grid(0,6)), 
        'Grid at (0, 6), square: 2; Value: 9')
    show_test('get_grid(0,3).get_note()', puzz.get_grid(0,3).get_note(), 
        [x for x in range(2,9)]) #check column 
    show_test('get_grid(6,0).get_note()', puzz.get_grid(6,0).get_note(), 
        [x for x in range(2,10)]) #check row
    show_test('get_grid(2,2).get_note()', puzz.get_grid(2,2).get_note(), 
        [x for x in range(2,10)]) #check square  
    
@test_decorator
def test_lonestar(form="grid"):
    lst1 = [[1,2,3] for _ in range(0,8)] +[[1,2,3,4]] # basic check 
    lst1result = [[1,2,3] for _ in range(0,8)] +[[]]
    lst2 = [[num for num in range(1,10) if num != 3] for _ in range(0,8)] + [[3]] # lonestar in the end
    lst2result = [[num for num in range(1,10) if num != 3] for _ in range(0,8)] + [[]]
    lst3 = [[num for num in range(1,10) if num != 6] for _ in range(0,5)] + [[6]] + [[num for num in range(1,10) if num != 6] for _ in range(5,8)]
        # lonestar in the middle
    lst3result = [[num for num in range(1,10) if num != 6] for _ in range(0,5)] + [[]] + [[num for num in range(1,10) if num != 6] for _ in range(5,8)]
    lst4 = [[2,8], [1,3,7], [2,9], [1,4], [3,5,6], [1,6], [1,3], [1,8], [4,7]] # two lonestars, 5 & 9
    lst4result = [[2,8], [1,3,7], [], [1,4], [], [1,6], [1,3], [1,8], [4,7]] 
    def test_lonestar_lst():
        helper = helper_lst(lonestar_lst, 'lonestar_lst')
        helper(lst1, 'lst1', lst1result)
        helper(lst2, 'lst2', lst2result)
        helper(lst3, 'lst3', lst3result)
        helper(lst4, 'lst4', lst4result)
    def test_lonestar():
        helper = helper_grid(lonestar, 'lonestar')
        helper(lst1, 'lst1', lst1result)
        helper(lst2, 'lst2', lst2result)
        helper(lst3, 'lst3', lst3result)
        helper(lst4, 'lst4' , lst4result)
        puzzle = Puzzle.Puzzle()
        grid_lst= [puzzle.get_grid(0,x) for x in range(len(lst4))]
        for ind in range(len(grid_lst)):
            grid = grid_lst[ind]
            grid._note = lst4[ind]
        lonestar(grid_lst, puzzle)
        show_test("get_grid(0,2)",str(puzzle.get_grid(0,2)), 
            'Grid at (0, 2), square: 0; Value: 9')
        show_test("get_grid(0,4)",str(puzzle.get_grid(0,4)), 
            'Grid at (0, 4), square: 1; Value: 5')
        show_test('get_grid(4,2).get_note()', puzzle.get_grid(4,2).get_note(), 
            [x for x in range(1,9)]) #check column note is missing 9
        show_test('get_grid(1,1).get_note()', puzzle.get_grid(1,1).get_note(), 
            [x for x in range(1,9)]) #check row note is mssing 9
    if form =='lst':
        test_lonestar_lst()
    else:
        test_lonestar()

@test_decorator
def test_double(form="grid"):
    lst1 =[[1,5,8], [2,8], [2,8], [2,4,7], [1,3,8]] #the double pair is next to each other
    lst1result = [[1,5], [2,8], [2,8], [4,7], [1,3]]
    lst2 =[[2,8], [1,5,8], [2,7,4], [2,8], [1,3,8]] #the double pair is seperated from each other
    lst2result =  [[2,8], [1,5], [7,4], [2,8], [1,3]]
    lst3 = [ [1,4,6], [4,6] ,[2,9] ,[1,2,3,4,5,6,7,8], [3,8,9], [4,6] ,[1,2,5,7,8] ,[2,9], [2,3,5,7,8,9] ] 
        #Two double pair among the notes
    lst3result = [ [1], [4,6] ,[2,9] ,[1,3,5,7,8], [3,8], [4,6] ,[1,5,7,8] ,[2,9], [3,5,7,8] ]
    lst4 = [[1,2,6], [],[3,6,7], [],[],[],[1,2],[], [1,2]] #includes empty list, represent the grid is already filled
    lst4result= [[6], [],[3,6,7], [],[],[],[1,2],[], [1,2]] 
    lst5 = [[x for x in range(1,10)] for _ in range(0,9)] #all list are fully filled, no double pair
    lst5result = [[x for x in range(1,10)] for _ in range(0,9)]
    lst6 = [[1,2],[3,4],[5,6],[1,2],[3,4],[5,6]] #only double pairs
    lst6result = [[1,2],[3,4],[5,6],[1,2],[3,4],[5,6]]
    lst7 =[[6, 8], [3, 9], [3, 9], [], [], [], [1, 6, 8], [1, 6], []]
    lst7result = [[6, 8], [3, 9], [3, 9], [], [], [], [1, 6, 8], [1, 6], []]
    def test_double_lst():
        helper = helper_lst(double_lst, 'double_lst')
        helper(lst1, 'lst1', lst1result)
        helper(lst2, 'lst2', lst2result)
        helper(lst3, 'lst3', lst3result)
        helper(lst4, 'lst4', lst4result)
        helper(lst5, 'lst5', lst5result)
        helper(lst6, 'lst6', lst6result)
        helper(lst7, 'lst7', lst7result)
    def test_double():
        helper = helper_grid(double, 'double')
        helper(lst1, 'lst1', lst1result)
        helper(lst2, 'lst2', lst2result)
        helper(lst3, 'lst3', lst3result)
        helper(lst4, 'lst4', lst4result)
        helper(lst5, 'lst5', lst5result)
        helper(lst6, 'lst6', lst6result)
    if form == "lst":
        test_double_lst()
    else:
        test_double()

@test_decorator
def test_remove_grid_vals():
    grid1 = Grid.Grid(0,0)
    grid2 = Grid.Grid(2,3)
    grid3 = Grid.Grid(6,1)
    lst1 = [grid1, grid2, grid3]
    show_run_func("lst1 = [grid1, grid2, grid3]")
    keep1 = [grid2]
    show_run_func("keep1 = [grid2]")
    remove_grid_vals(lst1, keep1, [1,2,3,4,5,6,7], Puzzle.Puzzle())
    show_test("remove_grid_vals(lst1, keep1, [1,2,3,4,5,6,7])", [grid.get_note() for grid in lst1],
        [[8,9],[1,2,3,4,5,6,7,8,9],[8,9] ])

@test_decorator
def test_triple(form = 'grid'):
    lst1 =[[3,8,9], [3,9], [3,8,9], [1,3,8,9]] # basic test
    lst1result = [[3,8,9], [3,9], [3,8,9], [1]]
    lst2 = [[2,6], [2,5], [5,6],[1,2,5,6]] # triple is hidden
    lst2result = [[2,6], [2,5], [5,6],[1]]
    lst3 = [[2,6], [7,8], [7,8], [2,5], [5,6],[1,2,5,6]] # triple is hidden with double in between 
    lst3result = [[2,6], [7,8], [7,8], [2,5], [5,6],[1]]
    lst4 = [[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9]]# all triples
    lst4result = [[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9]]
    lst5 = [[1,2],[4,5], [1,3], [4,6], [2,3],[7,8], [8,9],[7,9]] # all triples are hidden
    lst5result = [[1,2],[4,5], [1,3], [4,6], [2,3],[7,8], [8,9],[7,9]]
    lst6 = [[1,2,3],[1,2,3,7],[4,5,6],[4,5,6,8],[1,2,3],[4,5,6],[1,2,3], [2,4,6,9], [4,5,6]] # check if values are remove when two triples
    lst6result = [[1,2,3],[7], [4,5,6],[8],[1,2,3],[4,5,6],[1,2,3], [9], [4,5,6]]
    lst7 = [[1,2],[1,5,7], [4,5], [1,3],[5,6], [2,6,8], [4,6], [2,3],[1,3, 9]]
    lst7result = [[1,2],[7], [4,5], [1,3],[5,6], [8], [4,6], [2,3],[9]] #check if values are remove with two hidden triples
    lst8 = [[1,2,3], [], [2,3],[1,3],[], [1,2,3,4,5,6]] #triples with empty list in between 
    lst8result = [[1,2,3], [], [2,3],[1,3],[], [4,5,6]]
    lst9 = [[5,6,9], [2,6,7,9],[2,5,6,7,8],[], [2,3,7], [2,3,7], [2,3,7], [1,3,8,9], [1,2,3,8,9]]
    lst9result = [[5,6,9], [6,9],[5,6,8],[], [2,3,7], [2,3,7], [2,3,7], [1,8,9], [1,8,9]]
    lst10 = [[5, 7, 8, 9], [], [1, 7], [], [], [5, 9], [7, 8], [2, 7], [1, 2, 7]]
    lst10result= [[5, 8, 9], [], [1, 7], [], [], [5, 9], [8], [2, 7], [1, 2, 7]]
    def test_triple_lst():
        helper = helper_lst(triple_lst, 'triple_lst')
        helper(lst1, 'lst1', lst1result)
        helper(lst2, 'lst2', lst2result)
        helper(lst3, 'lst3', lst3result)
        helper(lst4, 'lst4', lst4result)
        helper(lst5, 'lst5', lst5result)
        helper(lst6, 'lst6', lst6result)
        helper(lst7, 'lst7', lst7result)
        helper(lst8, 'lst8', lst8result)
        helper(lst9, 'lst9', lst9result)
    def test_triple():
        helper = helper_grid(triple, 'triple')
        helper(lst1, 'lst1', lst1result)
        helper(lst2, 'lst2', lst2result)
        helper(lst3, 'lst3', lst3result)
        helper(lst4, 'lst4', lst4result)
        helper(lst5, 'lst5', lst5result)
        helper(lst6, 'lst6', lst6result)
        helper(lst7, 'lst7', lst7result)
        helper(lst8, 'lst8', lst8result)
        helper(lst9, 'lst9', lst9result)
        #helper(lst10, 'lst10', lst10result)
    if form == "lst":
        test_triple_lst()
    else:
        test_triple()

@test_decorator
def test_quad(form = 'grid'):
    lst1 = [[1,2,3,4] for _ in range(4)] + [[1,2,3,4,5]] #basic check
    lst1result = [[1,2,3,4] for _ in range(4)] + [[5]]
    lst2 = [[1,2], [1,3], [1,4], [2,4], [1,2,3,4,5]] #quad is hidden
    lst2result = [[1,2], [1,3], [1,4], [2,4], [5]] 
    lst3 = [[1,2,3,4] for _ in range(4)] + [[x for x in range(1,10)]]+[[5,6,7,8]  for _ in range(4)] # double quad
    lst3result =  [[1,2,3,4] for _ in range(4)] + [[9]]+[[5,6,7,8]  for _ in range(4)]
    lst4 = [[1,2], [1,3], [1,4], [2,4]] + [[x for x in range(1,10)]] + [[5,6],[5,7],[5,9],[6,9]] #double hidden quad
    lst4result = [[1,2], [1,3], [1,4], [2,4]] + [[8]] + [[5,6],[5,7],[5,9],[6,9]]
    lst5 = [[1,2,3], [1,3,4],[1,2], [1,4] ,[1,2,3,4,5],[]] #quad with some list of threes and empty list
    lst5result = [[1,2,3], [1,3,4],[1,2] ,[1,4]] +[[5] ,[]]
    lst6 = [[5,6], [5,6], [1,2], [1,3], [1,4], [2,4], [1,2,3,4,5,6,7,8,9]] #quad with doubles
    lst6result = [[5,6], [5,6], [1,2], [1,3], [1,4], [2,4], [5,6,7,8,9]] 
    lst7 = [[5,6], [5,6,7], [5,6,7], [1,2], [1,3], [1,4], [2,4], [1,2,3,4,5,6,7,8,9]] # quad with triples
    lst7result =[[5,6], [5,6,7], [5,6,7], [1,2], [1,3], [1,4], [2,4], [5,6,7,8,9]]
    def test_quad_lst():
        helper = helper_lst(quad_lst, 'quad_lst')
        helper(lst1, 'lst1', lst1result)
        helper(lst2, 'lst2', lst2result)
        helper(lst3, 'lst3', lst3result)
        helper(lst4, 'lst4', lst4result)
        helper(lst5, 'lst5', lst5result)
        """
        # not tested because the 'belong' feature cannot apply here
        # could mock that feature by changing the first of the lst to negative 
        helper(lst6, 'lst6', lst6result)
        helper(lst7, 'lst7', lst7result)
        """
    def test_quad():
        helper = helper_grid(quad, 'quad')
        
        helper(lst1, 'lst1', lst1result)
        helper(lst2, 'lst2', lst2result)
        helper(lst3, 'lst3', lst3result)
        helper(lst4, 'lst4', lst4result)
        helper(lst5, 'lst5', lst5result)
        """
        helper(lst6, 'lst6', lst6result)
        helper(lst7, 'lst7', lst7result)
        """
    if form == 'lst':
        test_quad_lst()
    else:
        test_quad()

@test_decorator
def test_xwing_row():
    puzzle = Puzzle_examples._puzzle_xwing_row()
    for ind in range(9):
        x_wing_row(puzzle.get_row_grids(ind), puzzle)
        puzzle.show_puzzle()

@test_decorator
def test_xwing_col():
    puzzle = Puzzle_examples._puzzle_xwing_col()
    for ind in range(9):
        x_wing_col(puzzle.get_col_grids(ind), puzzle)
        puzzle.show_puzzle()

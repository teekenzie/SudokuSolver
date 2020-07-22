
def validate(lst_of_grids, puzzle):
    """
    Checks that there are no same numbers in the column, row, and square 
    """
    nums = []
    for grid in lst_of_grids:
        answer = grid.get_answer()
        if answer != 0 and answer not in nums:
            nums.append(answer)
        elif answer in nums:
            puzzle.is_valid = False
            return 

def lonely(lst_of_grids, puzzle):
    """
    Checks which grid only has note with length of one
    Sets the answer of the grid to the note if note is length of one
    """
    for grid in lst_of_grids:
        note = grid.get_note()
        if len(note) == 1:
            puzzle.set_grid_answer(grid, note[0])
            puzzle.made_change()
    # COMPLETED 

def lonestar(lst_of_grids, puzzle):
    """
    Checks which number appears in the notes of the grids only once
    Sets the answer of the grid to that value
    """
    count_dict = {x:[] for x in range(1,10)}
    for grid in lst_of_grids:
        note = grid.get_note()
        for val in note:
            count_dict[val].append(grid)
    for val in count_dict:
        if len(count_dict[val]) == 1:
            puzzle.set_grid_answer(count_dict[val][0], val)
            puzzle.made_change()
    # COMPLETED

def double(lst_of_grids, puzzle, avoid = []):
    """
    Check which grids only has two value in the note
    If found two grids with the same two values
        Remove the two values from the notes of all corresponding grids
    """
    pair = None
    second_pair = False
    grid1, grid2 = None, None
    for grid in lst_of_grids:
        note = grid.get_note()
        if note in avoid or grid.belong == True:
            pass
        elif len(note)==2 and pair != None and note != pair:
            double(lst_of_grids, puzzle, avoid + [pair])
        elif len(note) ==2 and note == pair:
            second_pair = True
            grid2 = grid
        elif len(note) ==2:
            pair, grid1 = note, grid
    if second_pair == True:
        grid1.belong = True 
        grid2.belong = True
        remove_grid_vals(lst_of_grids, [grid1,grid2], pair, puzzle)
    # COMPLETED

def triple(lst_of_grids, puzzle, avoid =[]):
    """
    Check if any triples exist within the lst_of_grids
    Remove the notes of the appropriate grids
    """
    target = []
    second_triple, third_triple = False, False
    grid1, grid2, grid3 = None, None, None 
    for grid in lst_of_grids:
        note = grid.get_note()
        if len(note) <=1 or grid.belong == True :
            pass
        elif len(note) <=3 and is_val_in_lst(note, avoid):
            pass 
        elif len(note) <=3 and second_triple and is_all_in_lst(note, target):
            grid3 = grid 
            third_triple = True 
        elif len(note) <=3 and len(target)!=0:
            temp_target = list(target)
            temp_target.extend(note)
            temp_target = set(temp_target)
            if len(temp_target) > 3:
                triple(lst_of_grids, puzzle,  avoid + list(target))
            elif len(temp_target) ==3:
                target = temp_target
                grid2 = grid 
                second_triple = True
        elif len(note) <=3:
            target.extend(note)
            grid1 = grid  
    if third_triple == True:
        grid1.belong = True 
        grid2.belong = True
        grid3.belong = True 
        remove_grid_vals(lst_of_grids, [grid1,grid2, grid3], target, puzzle)
    # COMPLETED

def quad(lst_of_grids, puzzle, avoid = []):
    """
    Checks if any quads exist within the lst_of_grids
    Remove the notes of the appropriate grids
    """
    target = []
    second_quad, third_quad, fourth_quad = [False for _ in range(3)] #indicate whether the quads are found
    grid1, grid2, grid3, grid4 = [None for _ in range(4)]
    for grid in lst_of_grids:
        note = grid.get_note()
        if len(note )==0 or grid.belong == True:
            pass
        elif len(note) <=4 and is_val_in_lst(note, avoid)==True:
            pass
        elif len(note) <= 4 and third_quad == True and is_all_in_lst(note, target):
            # at this point, target should already have len 4
            grid4 = grid
            fourth_quad = True  
        elif len(note) <= 4 and second_quad == True:
            temp_target = list(target)
            temp_target.extend(note)
            temp_target = set(temp_target) #remove any duplicates 
            if len(temp_target) >4:
                quad(lst_of_grids, puzzle, avoid + list(target))
            elif len(temp_target) ==4:
                target = temp_target
                grid3= grid
                third_quad = True
        elif len(note) <=4 and len(target) != 0:
            # if the target len end up being greater than 4, call recursively 
            temp_target = list(target)
            temp_target.extend(note)
            temp_target = set(temp_target) #remove any duplicates 
            if len(temp_target) >4:
                quad(lst_of_grids,puzzle, avoid + list(target))
            elif len(temp_target) <=4:
                target = temp_target
                grid2 = grid 
                second_quad = True 
        elif len(note) <=4:
            target.extend(note)
            grid1= grid
    if fourth_quad == True:
        remove_grid_vals(lst_of_grids, [grid1, grid2, grid3,grid4], target, puzzle)

def candidate_line(lst_of_grids, puzzle):
    """
    Gets a list of grids in a square
    If a value only appears in a row or column, can remove that value from the whole corresponding row or column 
    """
    def _get_direction(val, lst_of_grids, length):
        """
        Return the direction the grids line up in, whether it is row or column
        Return None if it doesnt line up in row or column 
        """
        grid0_location = lst_of_grids[0].get_location()
        row = 1
        col = 1
        for ind in range(1, len(lst_of_grids)):
            grid = lst_of_grids[ind]
            if grid.get_location()[0] == grid0_location[0]:
                row+= 1
            elif grid.get_location()[1] == grid0_location[1]:
                col+= 1
            else:
                return None 
        if row == length:
            return 'row'
        elif col == length:
            return 'col'  
    vals_dict = {x:[] for x in range(1,10)}
    for grid in lst_of_grids:
        note = grid.get_note()
        for val in note:
            vals_dict[val].append(grid)
    for val in vals_dict:
        if len(vals_dict[val]) in range(2,4):
            direction = _get_direction(val, vals_dict[val], len(vals_dict[val]))
            if direction == 'row':
                grid_row = vals_dict[val][0].get_location()[0]
                remove_grid_vals(puzzle.get_row_grids(grid_row), vals_dict[val], [val], puzzle)
            elif direction == 'col':
                grid_col = vals_dict[val][0].get_location()[1]
                remove_grid_vals(puzzle.get_col_grids(grid_col), vals_dict[val], [val], puzzle)
    # COMPLETED 

def _count_val(lst_of_grids,val):
    """
    returns the number of times the value appears in the note of the list of grids
    """
    count = 0
    for grid in lst_of_grids:
        note= grid.get_note()
        if val in note:
            count += 1
    return count

def _helper(grids, val, puzzle, direction_study):
    """
    Helper function for x_wing functions
    """
    loc_ind = {'row':1, 'col':0} # the key is the direction study
    get_opposite = {'row': puzzle.get_col_grids, 'col': puzzle.get_row_grids}
    get_same = {'row': puzzle.get_row_grids, 'col': puzzle.get_col_grids}
    grid1_loc = grids[0].get_location()[loc_ind[direction_study]]
    grid2_loc = grids[1].get_location()[loc_ind[direction_study]]
    grids1 = get_opposite[direction_study](grid1_loc) # the grids of the other direction of grid1
    grids2 = get_opposite[direction_study](grid2_loc)
    for ind in range(9):
        if grids1[ind] != grids[0] and val in grids1[ind].get_note() and val in grids2[ind].get_note():
            second_row = get_same[direction_study](ind)
            count = _count_val(second_row, val)
            if count == 2:
                remove_grid_vals(grids1,[grids[0],grids1[ind]], [val],puzzle ) # keeps is the grids at the row study and other row
                remove_grid_vals(grids2,[grids[1],grids2[ind]] ,[val],puzzle )

def _val_twice_grids(lst_of_grids):
    """
    Takes a list of grids and find the values that appears only twice in notes of the list of grids
    Returns a dict with the val as the key and the grids as the value
    """
    vals_dict = {x:[] for x in range(1,10)} 
    result = {}
    for grid in lst_of_grids:
        note = grid.get_note()
        for val in note:
            vals_dict[val].append(grid)
    for val in vals_dict:
        grids = vals_dict[val] # represents the grids that have that value
        if len(grids) == 2:
            result[val] = grids
    return result
              
def x_wing_row(lst_of_grids, puzzle):
    """
    Looks for x-wing row by row with row as the direction of study 
    """
    val_twice_dict = _val_twice_grids(lst_of_grids)
    for val in val_twice_dict:
        _helper(val_twice_dict[val], val, puzzle, 'row')
    # COMPLETED 

def x_wing_col(lst_of_grids, puzzle):
    """
    Looks for x-wing col by col with col as the direction of study 
    """
    val_twice_dict=  _val_twice_grids(lst_of_grids)
    for val in val_twice_dict:
        _helper(val_twice_dict[val], val, puzzle, 'col')
# COMPLETED
    
def remove_grid_vals(lst_of_grids, keeps, vals_remove, puzzle):
    """
    For every grid in lst_of_grids
    Every value in vals_remove will be remove from the grid
    unless the grid is part of keeps
    """
    for grid in lst_of_grids:
        if grid not in keeps:
            for val in vals_remove:
                if val in grid.get_note():
                    grid.remove_note_val(val)
                    puzzle.made_change()
    # COMPLETED

def lonestar_lst(lst_of_lst):
    count_dict = {x:[] for x in range(1,10)}
    for ind in range(len(lst_of_lst)):
        note = lst_of_lst[ind]
        for val in note:
            count_dict[val].append(ind)
    for val in count_dict:
        if len(count_dict[val]) == 1:
            lst_of_lst[count_dict[val][0]] = [] # set answer to that value
    # COMPLETED

def double_lst (lst, avoid=[]):
    """
    Rough draft of the double function, takes a list of list
    Removes the two values if found the corresponding pair 
    """
    pair = None
    second_pair = False
    lst1, lst2 = None, None
    for ind in range(len(lst)):
        note = lst[ind]
        if note in avoid:
            pass
        #elif second_pair == True:
            #break
        elif len(note) ==2 and note == pair:
            second_pair = True
            lst2 = ind
        elif len(note)==2 and pair != None and note != pair:
            double_lst(lst, avoid + [pair])
        elif len(note) ==2:
            pair, lst1 = note, ind
    if second_pair == True:
        remove_lst_vals(lst, [lst1,lst2], pair)
    # INCOMPLETE

def triple_lst(lst_of_lst, avoid = []):
    """
    Rough draft of the triple function, takes a list of list
    """
    target = []
    second_triple = False #indicate whether the second triple is found
    third_triple = False
    lst1, lst2, lst3 = None, None, None
    for ind in range(len(lst_of_lst)):
        note = lst_of_lst[ind] 
        if len(note) <=3 and is_val_in_lst(note, avoid)==True:
            pass
        elif len(note) <= 3 and second_triple == True and is_all_in_lst(note, target):
            # at this point, target should already have len 3
            lst3 = ind
            third_triple = True  
        elif len(note) <=3 and len(target) != 0:
            # if the target len end up being greater than 3, call recursively 
            temp_target = list(target)
            temp_target.extend(note)
            temp_target = set(temp_target) #remove any duplicates 
            if len(temp_target) >3:
                triple_lst(lst_of_lst, avoid + list(target))
            elif len(temp_target) ==3:
                target = temp_target
                lst2 = ind 
                second_triple = True 
        elif len(note) <=3:
            target.extend(note)
            lst1= ind
    if third_triple == True:
        remove_lst_vals(lst_of_lst, [lst1, lst2, lst3], target)
    # COMPLETED 

def quad_lst(lst_of_lst, avoid = []):
    """
    Rough draft of the triple function, takes a list of list
    """
    target = []
    second_quad, third_quad, fourth_quad = [False for _ in range(3)] #indicate whether the quads are found
    lst1, lst2, lst3,lst4 = [None for _ in range(4)]
    for ind in range(len(lst_of_lst)):
        note = lst_of_lst[ind] 
        if len(note )==0 or note[0] <0: #change to check wheter the grid belong = True
            pass
        elif len(note) <=4 and is_val_in_lst(note, avoid)==True:
            pass
        elif len(note) <= 4 and third_quad == True and is_all_in_lst(note, target):
            # at this point, target should already have len 3
            lst4 = ind
            fourth_quad = True  
        elif len(note) <= 4 and second_quad == True:
            temp_target = list(target)
            temp_target.extend(note)
            temp_target = set(temp_target) #remove any duplicates 
            if len(temp_target) >4:
                quad_lst(lst_of_lst, avoid + list(target))
            elif len(temp_target) ==4:
                target = temp_target
                lst3= ind
                third_quad = True
        elif len(note) <=4 and len(target) != 0:
            # if the target len end up being greater than 4, call recursively 
            temp_target = list(target)
            temp_target.extend(note)
            temp_target = set(temp_target) #remove any duplicates 
            if len(temp_target) >4:
                quad_lst(lst_of_lst, avoid + list(target))
            elif len(temp_target) <=4:
                target = temp_target
                lst2 = ind 
                second_quad = True 
        elif len(note) <=4:
            target.extend(note)
            lst1= ind
    if fourth_quad == True:
        remove_lst_vals(lst_of_lst, [lst1, lst2, lst3,lst4], target)
    # COMPLETED 

def remove_lst_vals(lst_of_lst, keeps, vals_remove):
    for lst_ind in range(len(lst_of_lst)):
        if lst_ind not in keeps:
            for val in vals_remove:
                if val in lst_of_lst[lst_ind]:
                    lst_of_lst[lst_ind].remove(val)
    # COMPLETED

def is_val_in_lst(lst1,lst2):
    """
    Takes two list
    Return True if any val of lst1 is in lst2 
    else False
    """
    if len(lst2)==0:
        return False
    for val in lst1:
        if val in lst2:
            return True
    return False

def is_all_in_lst(lst1, lst2):
    """
    Takes two list
    Return True if all vals of lst1 is in lst2
    else False 
    """
    for val in lst1:
        if val not in lst2:
            return False
    return  True
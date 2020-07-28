from tkinter import *
from tkinter import messagebox
import Solver, Puzzle, Puzzle_examples

root = Tk()
solver = Solver.Solver()
puzzle = Puzzle.Puzzle()
root.title('Sudoku Solver')

# title label
extraLabel1 = Label(root, text = " ").grid(row =1, column = 0, padx = 20)
extraLabel2 = Label(root, text = " ").grid(row =1, column = 4, padx = 20)
extraLabel2 = Label(root,text = " ").grid(row =5, column = 0, pady = 50)
titleLabel = Label(root, text='SUDOKU SOLVER', font= ('Helvetica 20 bold'),padx = 50,pady=20)
titleLabel.grid(row = 0, column =1, columnspan = 3)

# Make the frames
framelst = []
for row_ind in range(1,4):
    for col_ind in range(1,4):
        tempframe = Frame(root, width = 50 ,highlightthickness =5, highlightbackground = 'black' )
        tempframe.grid(row = row_ind, column = col_ind)
        framelst.append(tempframe)

# returns which frame the entry should be put in 
def which_frame(row, col):
    if row <= 2 and col <=2:
        return 0
    elif row <= 2 and col <= 5:
        return 1
    elif row <= 2 and col <= 8:
        return 2

    elif row <= 5 and col <=2:
        return 3
    elif row <= 5 and col <= 5:
        return  4
    elif row <= 5 and col <= 8:
        return  5

    elif row <= 8 and col <= 2:
        return  6
    elif row <= 8 and col <= 5:
        return  7
    elif row <= 8 and col <= 8:
        return 8 

# Make the entries and send it to the appropritate frames
entries = []
for row_ind in range(0,9):
    row_entries = []
    for col_ind in range(0,9):
        frame = framelst[which_frame(row_ind, col_ind)]
        tempEntry = Entry(frame ,width = 3, font = ('Helvetica', 30), justify = CENTER )
        tempEntry.insert(0,0)
        tempEntry.grid(row=row_ind%3, column = col_ind%3)
        row_entries.append(tempEntry)
    entries.append(row_entries)

# update the entry so it shows the proper values
def update_vals():
    for row_ind in range(len(entries)):
        for col_ind in range(len(entries[row_ind])):
            entry = entries[row_ind][col_ind]
            entry.delete(0, END)
            val = puzzle.get_grid(row_ind, col_ind).get_answer()
            entry.insert(0, val)

# takes action based on the message given by solver solve method
def action(txt):
    # if unable to complete, set puzzle to a new empty puzzle
    if txt == 'Puzzle Solved':
        update_vals()
    elif txt == "This puzzle is unsolvable":
        messagebox.showinfo(message = txt)
        global puzzle
        puzzle = Puzzle.Puzzle()
    elif txt == 'Puzzle already solved':
        messagebox.showinfo(message=txt)
        update_vals()

# run when the buttton solve is being clicked
def click_solve():
    """
    Checks if the puzzle is complete, return a message and do nothing if it is 
    else, get every values of the entry and input it into the puzzle 
    if value is anything else not from 1 to 9, value will be ignored
    if value is 0, won't be inputted into puzzle
    """
    if puzzle.is_puzzle_complete() == True:
        action('Puzzle already solved')
        return # show a message box with the puzzle complete, chagne every value of the grid to correct value
    for row_ind in range(len(entries)):
        for col_ind in range(len(entries[row_ind])):
            entry = entries[row_ind][col_ind]
            val = entry.get()
            if val.isdigit():
                val = int(val)
                if val in range (1,10):
                    puzzle.set_loc_answer(row_ind, col_ind, val)
    message = solver.solve_puzzle(puzzle)
    action(message)
    

# Make the solve Button
solveButton = Button(root, text = 'SOLVE', borderwidth = 3,bg = 'green', fg ='white', font =('Helvetica 30 bold'), command = click_solve)
solveButton.grid(row = 5, column = 1, columnspan =3)

root.geometry("+{}+{}".format(250, 0))
root.resizable(False, False)
root.mainloop()

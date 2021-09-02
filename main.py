import pygame
import tkinter as tk
import matplotlib as mpl

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
puzzle = grid

def square(row, col):
    if row < 3:
        if col < 3:
            square = [grid[i][0:3] for i in range(0, 3)]
        elif col < 6:
            square = [grid[i][3:6] for i in range(0, 3)]
        else:
            square = [grid[i][6:9] for i in range(0, 3)]
    elif row < 6:
        if col < 3:
            square = [grid[i][0:3] for i in range(3, 6)]
        elif col < 6:
            square = [grid[i][3:6] for i in range(3, 6)]
        else:
            square = [grid[i][6:9] for i in range(3, 6)]
    else:
        if col < 3:
            square = [grid[i][0:3] for i in range(6, 9)]
        elif col < 6:
            square = [grid[i][3:6] for i in range(6, 9)]
        else:
            square = [grid[i][6:9] for i in range(6, 9)]
    return square


def backtrack(i):
        if i < 81:
            row = i//9
            col = i%9
            if puzzle[row][col] == 0:
                #try for values 1-9
                for x in range(1, 10):
                    #check for x in row
                    if not (x in grid(row)):
                        #check for x in column
                        if not (x in (grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col], grid[6][col], grid[7][col], grid[8][col])):
                            #check if x is in square
                            if not (x in square(row, col)):
                                grid[row][col] = x
                                backtrack(i+1)
                #if no number solves the cell then retry old answers
                ix = i
                while(True):
                    ix - 1
                    rowx = ix // 9
                    colx = ix % 9
                    if puzzle[rowx][colx] == 0:
                        backtrack(ix)
                        break
            else:
                backtrack(i+1)
        else:
            return

def solve():
    puzzle = grid


backtrack(0)
print(grid)

window = tk.Tk()
window.grid()
window.mainloop()
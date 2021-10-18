import pygame
import tkinter as tk
import matplotlib as mpl
import time

# grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

grid = []
grid.append([3, 0, 6, 5, 0, 8, 4, 0, 0])
grid.append([5, 2, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 8, 7, 0, 0, 0, 0, 3, 1])
grid.append([0, 0, 3, 0, 1, 0, 0, 8, 0])
grid.append([9, 0, 0, 8, 6, 3, 0, 0, 5])
grid.append([0, 5, 0, 0, 9, 0, 6, 0, 0])
grid.append([1, 3, 0, 0, 0, 0, 2, 5, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 7, 4])
grid.append([0, 0, 5, 2, 0, 6, 3, 0, 0])

# grid = []
# grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
# grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
# grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
# grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
# grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
# grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
# grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
# grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
# grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])



cell = 0

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


def backtrack(cell):
    if cell <= 81:
        row = cell // 9
        col = (cell % 9)
        if grid[row][col] == 0:
            for x in range(1, 10):
                # check for x in row
                if x not in grid[row]:
                    # check for x in column
                    if x not in ((
                            grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col],
                            grid[6][col],
                            grid[7][col], grid[8][col])):
                        # check if x is in square
                        if x not in square(row, col):
                            grid[row][col] = x
                            print(grid)
                            backtrack(cell + 1)
            else:
                grid[row][col] = 0
                return
        else:
            backtrack(cell + 1)
            return
    else:
        return

# def backtrack(cell):
#     if cell <= 81:
#         row = cell // 9
#         col = (cell % 9)-1
#         if grid[row][col] == 0:
#             # try for values 1-9
#             for x in range(1, 10):
#                 # check for x in row
#                 if x not in grid[row]:
#                     # check for x in column
#                     if x not in ((
#                             grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col],
#                             grid[6][col],
#                             grid[7][col], grid[8][col])):
#                         # check if x is in square
#                         if x not in square(row, col):
#                             puzzle[row][col] = x
#                             print(puzzle)
#                             backtrack(cell+1)
#             else:
#                 return
#         else:
#             backtrack(cell + 1)
#             return
#     else:
#         print(puzzle)
#         return


def solve():
    puzzle = grid


start_time = time.time()
backtrack(cell)
print(time.time() - start_time)
print(grid)

window = tk.Tk()
window.grid()
window.mainloop()

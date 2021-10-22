import copy


class SudokuSolver:
    # creates sudoku grid to solve
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
    # blank grid for new puzzle creation
    puz_grid = []
    puz_grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    puz_grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    puz_grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    puz_grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    puz_grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    puz_grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    puz_grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    puz_grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    puz_grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

    def square(self, row, col, _grid):
        if row < 3:
            if col < 3:
                _square = [_grid[i][0:3] for i in range(0, 3)]
            elif col < 6:
                _square = [_grid[i][3:6] for i in range(0, 3)]
            else:
                _square = [_grid[i][6:9] for i in range(0, 3)]
        elif row < 6:
            if col < 3:
                _square = [_grid[i][0:3] for i in range(3, 6)]
            elif col < 6:
                _square = [_grid[i][3:6] for i in range(3, 6)]
            else:
                _square = [_grid[i][6:9] for i in range(3, 6)]
        else:
            if col < 3:
                _square = [_grid[i][0:3] for i in range(6, 9)]
            elif col < 6:
                _square = [_grid[i][3:6] for i in range(6, 9)]
            else:
                _square = [_grid[i][6:9] for i in range(6, 9)]
        _ = []
        for x in _square:
            for z in x:
                _.append(z)

        _.sort()
        return _

    def backtrack(self, cell, _grid):
        if cell <= 80:
            row = cell // 9
            col = cell % 9
            if _grid[row][col] == 0:
                # check all possible values for cell
                for x in range(1, 10):
                    # check for x in row
                    if x not in _grid[row]:
                        # check for x in column
                        if x not in ((
                                _grid[0][col], _grid[1][col], _grid[2][col], _grid[3][col], _grid[4][col], _grid[5][col],
                                _grid[6][col],
                                _grid[7][col], _grid[8][col])):
                            # check if x is in square
                            if x not in self.square(row, col, _grid):
                                _grid[row][col] = x
                                # final crawler instance returns True
                                if row == 8 & col == 8:
                                    return _grid
                                # print(grid)
                                # disables crawlers once one finds a solution, creates next crawler
                                if self.backtrack(cell + 1, _grid):
                                    return _grid
                else:
                    # removes guesses once the cell can't be solved
                    _grid[row][col] = 0
                    return
            else:
                # disables crawlers once one finds a solution, creates next crawler
                if self.backtrack(cell + 1, _grid):
                    return _grid
                return
        else:
            return _grid

    def solve(self, grid):
        return copy.deepcopy(self.backtrack(0, grid))

    def get_puzzle(self):
        grid = copy.deepcopy(self.grid)
        return grid

    def set_puzzle(self, new_grid):
        self.grid = new_grid

    def get_column(self, col, _grid):
        _ = []
        for x in range(9):
            _.append(_grid[x][col])
        print(_)
        return sorted(_)

    def reset_puzzle(self):
        self.puz_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# start_time = time.time()
# backtrack(cell)
# print(time.time() - start_time)
# print(grid)

# # creates grid of tkinter labels
# def __pgrid_build(self, win):
#     col_array = []
#     for x in range(0, 9):
#         col = x
#         row_array = []
#         col_array.append(row_array)
#         win.grid_columnconfigure(x, weight=1, uniform="fred")
#         for x in range(0, 9):
#             _ = tk.Button(win).grid(column=col, row=x + 1, sticky="NESW")
#
#             row_array.append(_)
#     return col_array

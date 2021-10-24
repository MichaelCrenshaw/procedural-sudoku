import math
import copy
import tkinter as tk
from tkinter import Frame
from Solver import SudokuSolver

SIDE = 50
MARGIN = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9


class Board(Frame):
    victory = False
    row = 0
    col = 0
    button = None

    def __init__(self, parent, solver, window):
        self.parent = parent
        self.solver = solver
        self.window = window
        Frame.__init__(self)

        self.label = tk.Label(self)

        self.board_grid = solver.get_puzzle()
        self.start_grid = solver.get_puzzle()
        self.__build_GUI(window)

    def __build_GUI(self, window):
        window.title("Board")
        self.pack(fill="both", expand=1)
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT)
        self.canvas.pack(side="top")

        self.__build_grid()
        self.__build_puzzle()

        self.canvas.bind("<Button-1>", self.__on_cell_clicked)
        self.canvas.bind("<Key>", self.__on_key_pressed)
        self.button = tk.Button(self, text="Solve", command=lambda: self.__solve())
        self.button.pack(side="bottom")

    def __build_grid(self):
        for _ in range(10):
            if _ % 3 != 0:
                color = "grey"
            else:
                color = "black"

            x0 = MARGIN + _ * SIDE
            y0 = MARGIN
            x1 = MARGIN + _ * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = MARGIN
            y0 = MARGIN + _ * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + _ * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

    def __build_puzzle(self):
        self.canvas.delete("numbers")
        puzzle = self.board_grid
        for i in range(9):
            for j in range(9):
                answer = puzzle[i][j]
                if answer != 0:
                    x = MARGIN + j * SIDE + SIDE / 2
                    y = MARGIN + i * SIDE + SIDE / 2
                    if self.solver.get_puzzle()[i][j] != 0:
                        self.board_grid[i][j] = self.solver.get_puzzle()[i][j]
                        self.canvas.create_text(x, y, text=self.solver.get_puzzle()[i][j], tags="numbers", fill="black", font=("Helvetica",
                                                                                                       "24",
                                                                                                       "bold"))
                    else:
                        self.canvas.create_text(x, y, text=answer, tags="numbers", fill="#424242", font=("Helvetica",
                                                                                                         "22"))
        self.__check_solve()
        # # for later implementation which highlights conflicting answered cells
        # self.__check_cell(j, i)

    def __on_cell_clicked(self, event):
        x, y = event.x, event.y
        if self.victory:
            return
        elif MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN:
            self.canvas.focus_set()

            row = math.floor((y - MARGIN) / SIDE)
            col = math.floor((x - MARGIN) / SIDE)

            # get row and column of clicked cell
            if row == self.row and col == self.col:
                self.row = -1
                self.col = -1
            else:
                self.row = row
                self.col = col

        self.__select_cell()

    def __select_cell(self):
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            x0 = MARGIN + self.col * SIDE + 1
            y0 = MARGIN + self.row * SIDE + 1
            x1 = MARGIN + (self.col + 1) * SIDE - 1
            y1 = MARGIN + (self.row + 1) * SIDE - 1
            self.canvas.create_rectangle(x0, y0, x1, y1, outline="grey", tags="cursor", width=3)

    def __on_key_pressed(self, event):
        if self.victory:
            return
        elif self.row >= 0 and self.col >= 0 and event.char in "1234567890":
            self.board_grid[self.row][self.col] = int(event.char)
            self.col, self.row = -1, -1
            self.__build_puzzle()
            self.__select_cell()
            if self.__check_solve():
                self.__draw_victory()

    def __check_solve(self):
        points = 0
        for _ in range(81):
            grid = copy.deepcopy(self.board_grid)
            row = _ // 9
            col = _ % 9
            __logic = list(range(1, 10))
            if self.solver.square(row, col, grid) == __logic:
                if sorted(grid[row]) == __logic:
                    if self.solver.get_column(col, grid) == __logic:
                        points += 1

        if points == 81:
            print("you win")
            self.victory = True
            self.__draw_victory()

    def __draw_victory(self):
        self.label.destroy()
        self.label = tk.Label(self, text="You Win!", font=("Ariel", "20"))
        self.label.pack(side="bottom")
        self.button.configure(text="New Puzzle", command=lambda: self.__create_puzzle())

    # solve puzzle using solver backtracking
    def __solve(self):
        self.board_grid = []
        self.board_grid = self.solver.solve(self.start_grid)
        self.__build_puzzle()

    # create new puzzle for user to solve
    def __create_puzzle(self):
        self.label.configure(text="Please wait up to ten seconds for your puzzle...")
        self.update()
        self.solver.make_puzzle()
        self.board_grid = self.solver.get_puzzle()
        self.start_grid = self.solver.get_puzzle()

        self.__build_grid()
        self.__build_puzzle()

        self.button.configure(text="Solve", command=lambda: self.__solve())
        self.label.destroy()
        self.victory = False


def main():
    solver = SudokuSolver()
    win = tk.Tk()
    Board(tk.Frame, solver, win)
    win.mainloop()


main()

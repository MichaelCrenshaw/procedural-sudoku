import tkinter as tk
from tkinter import Frame
from Solver import SudokuSolver

SIDE = 50
MARGIN = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9


class Board(Frame):

    def __init__(self, parent, solver, window):
        self.parent = parent
        self.solver = solver
        self.window = window
        Frame.__init__(self)

        self._build_GUI(window)

    def _build_GUI(self, window):
        window.title("Board")
        self.pack(fill="both", expand=1)
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT)
        self.canvas.pack(side="top")

        self._build_grid()
        self._build_puzzle()

        # self.canvas.bind("<Button-1>", self._cell_clicked)
        # self.canvas.bind("<Key>", self._key_pressed)

    def _build_grid(self):
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

    def _build_puzzle(self):
        puzzle = self.solver.get_puzzle()
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                answer = puzzle[i][j]
                if answer != 0:
                    x = MARGIN + j * SIDE + SIDE / 2
                    y = MARGIN + i * SIDE + SIDE / 2
                    self.canvas.create_text(x, y, text=answer, tags="numbers", fill="black", font=("Helvetica", "25*"))

    # updates a cell in the visual grid
    def updatecell(self, row, col, x):
        self.pgrid[row][col] = x

    # creates grid of tkinter labels
    def pgrid_build(self, win):
        col_array = []
        for x in range(0, 9):
            col = x
            row_array = []
            col_array.append(row_array)
            win.grid_columnconfigure(x, weight=1, uniform="fred")
            for x in range(0, 9):
                _ = tk.Button(win).grid(column=col, row=x + 1, sticky="NESW")

                row_array.append(_)
        return col_array


def main():
    solver = SudokuSolver()
    win = tk.Tk()
    Board(tk.Frame, solver, win)
    win.mainloop()


main()

import tkinter as tk
import random

SIZE = 4

class Game2048:
    def __init__(self, root):
        self.root = root
        self.root.title("2048")
        self.grid = [[0]*SIZE for _ in range(SIZE)]

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.cells = []
        for i in range(SIZE):
            row = []
            for j in range(SIZE):
                label = tk.Label(self.frame, text="", width=5, height=2,
                                 font=("Arial", 24), borderwidth=2, relief="solid")
                label.grid(row=i, column=j)
                row.append(label)
            self.cells.append(row)
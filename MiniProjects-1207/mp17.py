# 37. Sudoku Solver and Player
# •	9x9 board with entry fields
# •	Input custom puzzle or load from file
# •	Solve using backtracking algorithm
# •	Timer for solving mode
# •	Hint option

import tkinter as tk
from tkinter import filedialog, messagebox
import time
import threading
import random

class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧩 Sudoku Solver and Player")
        self.board = [[tk.StringVar() for _ in range(9)] for _ in range(9)]
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.timer_label = tk.Label(root, text="Timer: 0s", font=("Arial", 12))
        self.timer_label.grid(row=10, column=0, columnspan=9, pady=10)
        self.timer_running = False
        self.start_time = 0
        self.original_puzzle = [[0]*9 for _ in range(9)]

        self.build_gui()

    def build_gui(self):
        for i in range(9):
            for j in range(9):
                e = tk.Entry(self.root, textvariable=self.board[i][j], width=3, font=("Arial", 18), justify="center")
                e.grid(row=i, column=j, padx=1, pady=1)
                self.entries[i][j] = e
                # Highlight 3x3 blocks
                if (i // 3 + j // 3) % 2 == 0:
                    e.configure(bg="#f0f0ff")

        btn_frame = tk.Frame(self.root)
        btn_frame.grid(row=11, column=0, columnspan=9, pady=10)

        tk.Button(btn_frame, text="Load", command=self.load_puzzle).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Solve", command=self.solve_puzzle).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Hint", command=self.show_hint).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Reset", command=self.reset_board).grid(row=0, column=3, padx=5)

    def load_puzzle(self):
        file_path = filedialog.askopenfilename(title="Select Puzzle File", filetypes=[("Text Files", "*.txt")])
        if not file_path:
            return

        with open(file_path, "r") as f:
            lines = f.readlines()
            for i in range(9):
                line = lines[i].strip()
                for j in range(9):
                    val = line[j]
                    if val != '0':
                        self.board[i][j].set(val)
                        self.entries[i][j].config(state="disabled")
                        self.original_puzzle[i][j] = int(val)
                    else:
                        self.board[i][j].set("")
                        self.entries[i][j].config(state="normal")
                        self.original_puzzle[i][j] = 0

        self.start_timer()

    def start_timer(self):
        self.timer_running = True
        self.start_time = time.time()

        def update_timer():
            while self.timer_running:
                elapsed = int(time.time() - self.start_time)
                self.timer_label.config(text=f"Timer: {elapsed}s")
                time.sleep(1)

        threading.Thread(target=update_timer, daemon=True).start()

    def stop_timer(self):
        self.timer_running = False

    def get_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.board[i][j].get()
                row.append(int(val) if val.isdigit() else 0)
            board.append(row)
        return board

    def set_board(self, board):
        for i in range(9):
            for j in range(9):
                self.board[i][j].set(str(board[i][j]) if board[i][j] != 0 else "")

    def is_valid(self, board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if self.is_valid(board, i, j, num):
                            board[i][j] = num
                            if self.solve(board):
                                return True
                            board[i][j] = 0
                    return False
        return True

    def solve_puzzle(self):
        board = self.get_board()
        if self.solve(board):
            self.set_board(board)
            self.stop_timer()
            messagebox.showinfo("Solved", "Puzzle solved successfully!")
        else:
            messagebox.showerror("Error", "No solution found.")

    def reset_board(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j].set("")
                self.entries[i][j].config(state="normal")
                self.original_puzzle[i][j] = 0
        self.stop_timer()
        self.timer_label.config(text="Timer: 0s")

    def show_hint(self):
        board = self.get_board()
        solved_board = [row[:] for row in board]
        if not self.solve(solved_board):
            messagebox.showerror("Error", "Cannot provide hint (no solution).")
            return

        empty_cells = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
        if not empty_cells:
            messagebox.showinfo("Hint", "No empty cells for hint.")
            return

        i, j = random.choice(empty_cells)
        self.board[i][j].set(str(solved_board[i][j]))

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()

# 38. Minesweeper Game with Timer and Leaderboard
# •	Create grid with random mines
# •	Reveal/flag tiles with mouse
# •	Game over and win detection
# •	Timer + high score table
# •	Save leaderboard in SQLite

import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import time
import sqlite3
import os

DB_NAME = "minesweeper_leaderboard.db"

# --- Setup Leaderboard DB ---
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS leaderboard (
            name TEXT,
            time INTEGER,
            grid_size TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_score(name, elapsed, grid_size):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO leaderboard VALUES (?, ?, ?)", (name, elapsed, grid_size))
    conn.commit()
    conn.close()

def get_top_scores(grid_size):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT name, time FROM leaderboard WHERE grid_size=? ORDER BY time ASC LIMIT 5", (grid_size,))
    scores = cur.fetchall()
    conn.close()
    return scores

# --- Minesweeper Logic ---
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.adjacent_mines = 0

class MinesweeperGame:
    def __init__(self, root, rows=9, cols=9, mines=10):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.total_mines = mines
        self.grid_size = f"{rows}x{cols}"
        self.board = []
        self.buttons = {}
        self.first_click = True
        self.flags_left = mines
        self.timer_id = None
        self.start_time = None

        self.status_label = tk.Label(root, text="Flags left: 0 | Time: 0s", font=("Arial", 12))
        self.status_label.pack()

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.restart_btn = tk.Button(root, text="Restart", command=self.restart_game)
        self.restart_btn.pack(pady=5)

        self.build_grid()
        self.update_timer()

    def restart_game(self):
        self.frame.destroy()
        self.status_label.config(text="Flags left: 0 | Time: 0s")
        self.first_click = True
        self.flags_left = self.total_mines
        self.board = []
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.build_grid()

    def build_grid(self):
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                cell = Cell(r, c)
                row.append(cell)

                btn = tk.Button(self.frame, width=3, height=1,
                                command=lambda row=r, col=c: self.reveal_cell(row, col))
                btn.bind("<Button-3>", lambda e, row=r, col=c: self.toggle_flag(row, col))
                btn.grid(row=r, column=c)
                self.buttons[(r, c)] = btn
            self.board.append(row)

    def place_mines(self, safe_r, safe_c):
        available = [(r, c) for r in range(self.rows) for c in range(self.cols)
                     if not (r == safe_r and c == safe_c)]
        mines = random.sample(available, self.total_mines)
        for r, c in mines:
            self.board[r][c].is_mine = True

        for r in range(self.rows):
            for c in range(self.cols):
                self.board[r][c].adjacent_mines = self.count_adjacent_mines(r, c)

    def count_adjacent_mines(self, r, c):
        count = 0
        for i in range(max(0, r-1), min(self.rows, r+2)):
            for j in range(max(0, c-1), min(self.cols, c+2)):
                if self.board[i][j].is_mine:
                    count += 1
        return count

    def reveal_cell(self, r, c):
        if self.first_click:
            self.place_mines(r, c)
            self.start_time = time.time()
            self.first_click = False

        cell = self.board[r][c]
        btn = self.buttons[(r, c)]

        if cell.is_flagged or cell.is_revealed:
            return

        cell.is_revealed = True
        btn.config(relief=tk.SUNKEN, state=tk.DISABLED)

        if cell.is_mine:
            btn.config(text="💣", bg="red")
            self.game_over(False)
            return

        if cell.adjacent_mines > 0:
            btn.config(text=str(cell.adjacent_mines))
        else:
            btn.config(text="")
            for i in range(max(0, r-1), min(self.rows, r+2)):
                for j in range(max(0, c-1), min(self.cols, c+2)):
                    if not self.board[i][j].is_revealed:
                        self.reveal_cell(i, j)

        if self.check_win():
            self.game_over(True)

    def toggle_flag(self, r, c):
        cell = self.board[r][c]
        btn = self.buttons[(r, c)]

        if cell.is_revealed:
            return

        if cell.is_flagged:
            cell.is_flagged = False
            btn.config(text="")
            self.flags_left += 1
        else:
            if self.flags_left == 0:
                return
            cell.is_flagged = True
            btn.config(text="🚩")
            self.flags_left -= 1

        self.update_status()

    def check_win(self):
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.board[r][c]
                if not cell.is_mine and not cell.is_revealed:
                    return False
        return True

    def game_over(self, won):
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.board[r][c]
                btn = self.buttons[(r, c)]
                if cell.is_mine and not cell.is_flagged:
                    btn.config(text="💣", bg="gray")
                btn.config(state=tk.DISABLED)

        elapsed = int(time.time() - self.start_time) if self.start_time else 0
        if won:
            name = simpledialog.askstring("You Won!", "Enter your name for leaderboard:")
            if name:
                save_score(name, elapsed, self.grid_size)
            messagebox.showinfo("Victory 🎉", f"You cleared the field in {elapsed} seconds!")
        else:
            messagebox.showerror("Game Over", "Oops! You clicked a mine.")

        self.show_leaderboard()

    def update_status(self):
        elapsed = int(time.time() - self.start_time) if self.start_time else 0
        self.status_label.config(text=f"Flags left: {self.flags_left} | Time: {elapsed}s")

    def update_timer(self):
        self.update_status()
        self.root.after(1000, self.update_timer)

    def show_leaderboard(self):
        scores = get_top_scores(self.grid_size)
        if scores:
            text = "\n".join([f"{i+1}. {n} - {t}s" for i, (n, t) in enumerate(scores)])
            messagebox.showinfo("🏆 Leaderboard", text)
        else:
            messagebox.showinfo("Leaderboard", "No scores yet.")

# --- Main ---
if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    root.title("🧨 Minesweeper")
    game = MinesweeperGame(root, rows=9, cols=9, mines=10)  # Customize difficulty here
    root.mainloop()

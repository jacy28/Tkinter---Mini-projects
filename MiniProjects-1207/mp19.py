# 39. Memory Card Matching Game
# •	Grid of cards (hidden face)
# •	Match pairs by flipping
# •	Time/tries tracking
# •	Theme customization (images or text)
# •	Optional: difficulty levels

import tkinter as tk
from tkinter import messagebox
import random
import time

# Difficulty settings
DIFFICULTIES = {
    "Easy": (2, 2),     # 2x2 = 4 cards
    "Medium": (4, 4),   # 4x4 = 16 cards
    "Hard": (6, 6)      # 6x6 = 36 cards
}

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Memory Matching Game")
        self.theme = "text"  # or 'image' for extension
        self.first_card = None
        self.lock = False
        self.tries = 0
        self.matches = 0
        self.start_time = None

        # Menu for difficulty
        self.difficulty_var = tk.StringVar(value="Medium")
        tk.Label(root, text="Select Difficulty:").pack()
        tk.OptionMenu(root, self.difficulty_var, *DIFFICULTIES.keys()).pack()

        tk.Button(root, text="Start Game", command=self.start_game).pack(pady=10)
        self.info_label = tk.Label(root, text="Tries: 0 | Time: 0s", font=("Arial", 12))
        self.info_label.pack()

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.root.after(1000, self.update_timer)

    def start_game(self):
        self.clear_grid()
        self.tries = 0
        self.matches = 0
        self.first_card = None
        self.lock = False
        self.start_time = time.time()

        rows, cols = DIFFICULTIES[self.difficulty_var.get()]
        total_cards = rows * cols
        if total_cards % 2 != 0:
            messagebox.showerror("Error", "Grid must have even number of cards!")
            return

        symbols = list("🍎🍌🍒🍇🍉🍑🥝🍍🌽🥕🍓🥥🥑🍋🍊🍈🍅🥬")
        needed_pairs = total_cards // 2
        chosen = random.sample(symbols, needed_pairs)
        cards = chosen * 2
        random.shuffle(cards)

        self.buttons = []
        self.card_values = cards
        index = 0
        for r in range(rows):
            row = []
            for c in range(cols):
                btn = tk.Button(self.frame, text="❓", width=6, height=3,
                                command=lambda idx=index: self.reveal_card(idx))
                btn.grid(row=r, column=c, padx=5, pady=5)
                row.append(btn)
                index += 1
            self.buttons.extend(row)

    def clear_grid(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def reveal_card(self, idx):
        if self.lock or self.buttons[idx]["state"] == "disabled":
            return

        self.buttons[idx]["text"] = self.card_values[idx]
        self.buttons[idx]["state"] = "disabled"

        if not self.first_card:
            self.first_card = idx
        else:
            self.lock = True
            self.root.after(800, self.check_match, self.first_card, idx)
            self.first_card = None
            self.tries += 1
            self.update_stats()

    def check_match(self, first, second):
        if self.card_values[first] == self.card_values[second]:
            self.buttons[first].config(bg="lightgreen")
            self.buttons[second].config(bg="lightgreen")
            self.matches += 1
        else:
            self.buttons[first]["text"] = "❓"
            self.buttons[second]["text"] = "❓"
            self.buttons[first]["state"] = "normal"
            self.buttons[second]["state"] = "normal"
        self.lock = False

        if self.matches == len(self.card_values) // 2:
            elapsed = int(time.time() - self.start_time)
            messagebox.showinfo("🎉 Game Over", f"Completed in {self.tries} tries and {elapsed} seconds!")

    def update_stats(self):
        elapsed = int(time.time() - self.start_time) if self.start_time else 0
        self.info_label.config(text=f"Tries: {self.tries} | Time: {elapsed}s")

    def update_timer(self):
        self.update_stats()
        self.root.after(1000, self.update_timer)

# Run game
if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryGame(root)
    root.mainloop()

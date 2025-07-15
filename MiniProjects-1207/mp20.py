# 40. Typing Speed Test with Real-time Results
# •	Load random text passages
# •	Measure typing speed and accuracy
# •	Real-time WPM counter
# •	Result summary and leaderboard
# •	Store past attempts in SQLite

import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
import random
import time
import sqlite3

# Sample text passages
passages = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing tests help improve your speed and accuracy.",
    "Python is a powerful and versatile programming language.",
    "Practice daily to become a faster and more accurate typist.",
    "Keyboard shortcuts can significantly improve productivity."
]

# SQLite Setup
conn = sqlite3.connect("typing_leaderboard.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS leaderboard (
    name TEXT,
    wpm REAL,
    accuracy REAL,
    timestamp TEXT
)''')
conn.commit()

# ------------------- GUI -------------------

class TypingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("⌨️ Typing Speed Test")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.start_time = None
        self.word_count = 0
        self.current_text = ""

        self.setup_widgets()

    def setup_widgets(self):
        # Heading
        tk.Label(self.root, text="Typing Speed Test", font=("Arial", 20, "bold")).pack(pady=10)

        # Random Text
        self.text_display = tk.Label(self.root, text="", font=("Arial", 14), wraplength=650, justify="left", fg="blue")
        self.text_display.pack(pady=10)

        # Input box
        self.input_box = tk.Text(self.root, height=5, width=80, font=("Arial", 12))
        self.input_box.pack(pady=10)
        self.input_box.bind("<KeyRelease>", self.update_metrics)

        # Timer + Stats
        self.stats_label = tk.Label(self.root, text="WPM: 0   Accuracy: 0%", font=("Arial", 12))
        self.stats_label.pack(pady=5)

        # Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Start Test", command=self.start_test).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Submit", command=self.submit_test).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Leaderboard", command=self.show_leaderboard).grid(row=0, column=2, padx=10)

    def start_test(self):
        self.input_box.delete("1.0", tk.END)
        self.current_text = random.choice(passages)
        self.text_display.config(text=self.current_text)
        self.start_time = time.time()
        self.word_count = len(self.current_text.split())
        self.stats_label.config(text="WPM: 0   Accuracy: 0%")

    def update_metrics(self, event=None):
        if not self.start_time:
            return

        elapsed = max(time.time() - self.start_time, 1)
        typed = self.input_box.get("1.0", tk.END).strip()
        words_typed = len(typed.split())

        wpm = (words_typed / elapsed) * 60

        correct_chars = sum(1 for i, c in enumerate(typed) if i < len(self.current_text) and c == self.current_text[i])
        accuracy = (correct_chars / len(self.current_text)) * 100 if self.current_text else 0

        self.stats_label.config(text=f"WPM: {int(wpm)}   Accuracy: {int(accuracy)}%")

    def submit_test(self):
        if not self.start_time:
            messagebox.showwarning("Warning", "Start the test first!")
            return

        elapsed = max(time.time() - self.start_time, 1)
        typed = self.input_box.get("1.0", tk.END).strip()
        words_typed = len(typed.split())
        wpm = (words_typed / elapsed) * 60
        correct_chars = sum(1 for i, c in enumerate(typed) if i < len(self.current_text) and c == self.current_text[i])
        accuracy = (correct_chars / len(self.current_text)) * 100 if self.current_text else 0

        name = simpledialog.askstring("Name", "Enter your name for the leaderboard:")
        if name:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            c.execute("INSERT INTO leaderboard (name, wpm, accuracy, timestamp) VALUES (?, ?, ?, ?)",
                      (name, round(wpm, 2), round(accuracy, 2), timestamp))
            conn.commit()
            messagebox.showinfo("Result", f"WPM: {int(wpm)}\nAccuracy: {int(accuracy)}%")
        else:
            messagebox.showinfo("Cancelled", "Result not saved")

        self.start_time = None

    def show_leaderboard(self):
        top = tk.Toplevel(self.root)
        top.title("🏆 Leaderboard")
        top.geometry("500x300")

        tree = ttk.Treeview(top, columns=("Name", "WPM", "Accuracy", "Time"), show="headings")
        tree.heading("Name", text="Name")
        tree.heading("WPM", text="WPM")
        tree.heading("Accuracy", text="Accuracy")
        tree.heading("Time", text="Timestamp")
        tree.pack(fill=tk.BOTH, expand=True)

        c.execute("SELECT name, wpm, accuracy, timestamp FROM leaderboard ORDER BY wpm DESC LIMIT 10")
        rows = c.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingApp(root)
    root.mainloop()
    conn.close()

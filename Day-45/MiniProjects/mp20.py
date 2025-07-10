# 🔰 20. File Preview and Word Counter
# Goal: Open file and count number of words.
# Requirements:
# •	Use askopenfilename() to select file.
# •	Load file in Text widget.
# •	Show word/line/char count in Labels.

import tkinter as tk
from tkinter import filedialog

def open_file():
    path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if path:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        text.delete("1.0", tk.END)
        text.insert(tk.END, content)
        update_counts(content)

def update_counts(content):
    words = len(content.split())
    lines = content.count("\n") + 1 if content else 0
    chars = len(content)
    word_label.config(text=f"Words: {words}")
    line_label.config(text=f"Lines: {lines}")
    char_label.config(text=f"Characters: {chars}")

root = tk.Tk()
root.title("File Preview and Word Counter")
root.geometry("600x500")

tk.Button(root, text="Open File", command=open_file).pack(pady=10)

text = tk.Text(root, wrap="word")
text.pack(expand=True, fill="both", padx=10, pady=5)

word_label = tk.Label(root, text="Words: 0")
line_label = tk.Label(root, text="Lines: 0")
char_label = tk.Label(root, text="Characters: 0")

word_label.pack()
line_label.pack()
char_label.pack()

root.mainloop()


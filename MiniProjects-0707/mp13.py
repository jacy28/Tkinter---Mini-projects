# ✅ 13. Text Editor with Formatting
# Scenario: Basic notepad-style editor.
# Features:
# •	Text widget with buttons for Save, Clear.
# •	Insert sample content using .insert().
# •	Show char/word count in Label.
# •	Window resizing disabled.

import tkinter as tk
from tkinter import filedialog

def update_count(event=None):
    text = editor.get("1.0", tk.END)
    words = len(text.split())
    chars = len(text) - 1
    count_label.config(text=f"Words: {words}  Characters: {chars}")

def save_text():
    file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file:
        content = editor.get("1.0", tk.END)
        file.write(content)
        file.close()

def clear_text():
    editor.delete("1.0", tk.END)
    update_count()

def insert_sample():
    sample = "This is a sample text.\nYou can edit or replace it."
    editor.insert("1.0", sample)
    update_count()

root = tk.Tk()
root.title("Text Editor")
root.geometry("500x400")
root.resizable(False, False)

editor = tk.Text(root, wrap="word", width=60, height=15)
editor.pack(padx=10, pady=10)
editor.bind("<KeyRelease>", update_count)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Insert Sample", command=insert_sample).pack(side="left", padx=5)
tk.Button(btn_frame, text="Save", command=save_text).pack(side="left", padx=5)
tk.Button(btn_frame, text="Clear", command=clear_text).pack(side="left", padx=5)

count_label = tk.Label(root, text="Words: 0  Characters: 0")
count_label.pack(pady=5)

root.mainloop()

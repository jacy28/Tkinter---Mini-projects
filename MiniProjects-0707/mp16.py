# ✅ 16. Live Character Counter
# Scenario: Typing area with live word and character counter.
# Features:
# •	Text widget for input.
# •	Label shows count (updated via <Key> binding).
# •	Clear and Reset buttons.
# •	Organized using place() for custom layout.

import tkinter as tk

def update_count(event=None):
    text = input_text.get("1.0", tk.END).strip()
    char_count = len(text)
    word_count = len(text.split())
    count_label.config(text=f"Characters: {char_count} | Words: {word_count}")

def clear_text():
    input_text.delete("1.0", tk.END)
    update_count()

def reset_text():
    input_text.delete("1.0", tk.END)
    input_text.insert("1.0", "Type here...")
    update_count()

root = tk.Tk()
root.title("Live Character Counter")
root.geometry("400x300")

input_text = tk.Text(root, wrap="word", width=40, height=10)
input_text.place(x=20, y=20)
input_text.bind("<Key>", update_count)

count_label = tk.Label(root, text="Characters: 0 | Words: 0")
count_label.place(x=20, y=220)

clear_btn = tk.Button(root, text="Clear", command=clear_text)
clear_btn.place(x=250, y=250)

reset_btn = tk.Button(root, text="Reset", command=reset_text)
reset_btn.place(x=310, y=250)

reset_text()
root.mainloop()

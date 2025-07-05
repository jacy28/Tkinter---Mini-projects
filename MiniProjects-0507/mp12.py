# 🟢 12. Live Typing Tracker
# Goal: Show real-time character count while typing.
# Requirements:
# •	Use Text widget for input.
# •	Use .bind("<Key>") to update Label with char count.
# •	Clear button deletes all.
# •	Layout using place() for flexibility.

import tkinter as tk

root = tk.Tk()
root.title("Live Typing Tracker")
root.geometry("400x300")

text_widget = tk.Text(root, width=40, height=10)
text_widget.place(x=20, y=20)

char_count_var = tk.StringVar(value="Characters: 0")
char_label = tk.Label(root, textvariable=char_count_var)
char_label.place(x=20, y=220)

def update_count(event=None):
    content = text_widget.get("1.0", tk.END)
    char_count_var.set(f"Characters: {len(content) - 1}")  # exclude final newline

def clear_text():
    text_widget.delete("1.0", tk.END)
    char_count_var.set("Characters: 0")

clear_btn = tk.Button(root, text="Clear", command=clear_text)
clear_btn.place(x=300, y=215)

text_widget.bind("<Key>", update_count)

root.mainloop()

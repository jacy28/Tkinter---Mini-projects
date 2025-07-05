# 🟢 3. Simple Notepad
# Goal: Multi-line text editor.
# Requirements:
# •	Use Text widget for input.
# •	Buttons: Save (to file), Clear, Show word count.
# •	Use .insert(), .get(), .delete() on Text.
# •	Add keyboard shortcut using .bind() for save (e.g., Ctrl+S).
# •	Use Frame to group text and controls.

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Simple Notepad")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

text = tk.Text(frame, wrap='word', width=60, height=20)
text.pack()

controls = tk.Frame(root)
controls.pack(pady=5)

def save_file(event=None):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get("1.0", tk.END))

def clear_text():
    text.delete("1.0", tk.END)

def show_word_count():
    words = text.get("1.0", tk.END).split()
    word_count_var.set(f"Word Count: {len(words)}")

save_button = tk.Button(controls, text="Save", command=save_file)
save_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(controls, text="Clear", command=clear_text)
clear_button.pack(side=tk.LEFT, padx=5)

word_count_button = tk.Button(controls, text="Word Count", command=show_word_count)
word_count_button.pack(side=tk.LEFT, padx=5)

word_count_var = tk.StringVar()
word_count_label = tk.Label(root, textvariable=word_count_var)
word_count_label.pack()

root.bind("<Control-s>", save_file)

root.mainloop()

# 16. Live Typing Tracker
# Objective: Track and display text typed in real time.
# Features:
# •	Text widget to enter multi-line text.
# •	Show word & character count live in a Label.
# •	Reset button clears the field.
# •	Use .bind("<Key>") for live update.

import tkinter as tk

def update_count(event=None):
    content = text_widget.get("1.0", tk.END).strip()
    words = content.split()
    word_count = len(words)
    char_count = len(content)
    count_label.config(text=f"Words: {word_count} | Characters: {char_count}")

def reset_text():
    text_widget.delete("1.0", tk.END)
    update_count()

root = tk.Tk()
root.title("Live Typing Tracker")
root.geometry("500x400")

text_widget = tk.Text(root, wrap="word", font=("Arial", 12))
text_widget.pack(expand=True, fill="both", padx=10, pady=10)
text_widget.bind("<Key>", update_count)

count_label = tk.Label(root, text="Words: 0 | Characters: 0", anchor="w")
count_label.pack(fill="x", padx=10)

reset_button = tk.Button(root, text="Reset", command=reset_text)
reset_button.pack(pady=10)

root.mainloop()

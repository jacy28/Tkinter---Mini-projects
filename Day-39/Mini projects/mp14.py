# 14.	Word Counter
# 	Multi-line Text widget for typing/pasting text, Button to count words, and Label to show the word count.

import tkinter as tk
from tkinter import messagebox

def count_words():
    text = text_box.get("1.0", tk.END).strip()
    word_list = text.split()
    word_count = len(word_list)
    result_label.config(text=f"Word Count: {word_count}")

# Create main window
root = tk.Tk()
root.title("Word Counter")
root.geometry("400x300")

# Label
tk.Label(root, text="Enter your text below:").pack(pady=5)

# Multi-line Text widget
text_box = tk.Text(root, height=10, width=40)
text_box.pack(pady=5)

# Count Button
count_button = tk.Button(root, text="Count Words", command=count_words)
count_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Word Count: 0")
result_label.pack(pady=5)

root.mainloop()

# 🟢 14. Text Formatter
# Goal: Modify text with formatting options.
# Requirements:
# •	Text widget for input.
# •	Use Combobox to select font size.
# •	Use Button to apply formatting (bold, italic).
# •	Display formatted output in another Text box.
# •	Use .insert(), .get() methods.

import tkinter as tk
from tkinter import ttk, font

def apply_format(style):
    content = input_text.get("1.0", tk.END).strip()
    size = int(size_box.get())
    output_text.delete("1.0", tk.END)
    if style == "bold":
        f = font.Font(weight="bold", size=size)
    elif style == "italic":
        f = font.Font(slant="italic", size=size)
    else:
        f = font.Font(size=size)
    output_text.tag_config("custom", font=f)
    output_text.insert("1.0", content, "custom")

root = tk.Tk()
root.title("Text Formatter")
root.geometry("600x500")

frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

input_label = tk.Label(frame, text="Input Text:")
input_label.grid(row=0, column=0, sticky="w")
input_text = tk.Text(frame, width=60, height=6)
input_text.grid(row=1, column=0, columnspan=3, pady=5)

size_label = tk.Label(frame, text="Font Size:")
size_label.grid(row=2, column=0, sticky="w")
size_box = ttk.Combobox(frame, values=[10, 12, 14, 16, 18, 20, 24, 28], width=5, state="readonly")
size_box.set(12)
size_box.grid(row=2, column=1, sticky="w")

bold_btn = tk.Button(frame, text="Bold", command=lambda: apply_format("bold"))
bold_btn.grid(row=3, column=0, pady=10)

italic_btn = tk.Button(frame, text="Italic", command=lambda: apply_format("italic"))
italic_btn.grid(row=3, column=1, pady=10)

output_label = tk.Label(frame, text="Formatted Output:")
output_label.grid(row=4, column=0, sticky="w")
output_text = tk.Text(frame, width=60, height=6)
output_text.grid(row=5, column=0, columnspan=3, pady=5)

root.mainloop()

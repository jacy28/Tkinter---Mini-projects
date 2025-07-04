# 4. Notepad App (Mini Text Editor)
# Objective: Allow user to type, edit, and clear multi-line text.
# Features:
# •	Use Text widget for editing area.
# •	Button to Save (prints to console), Clear, and Load preset content.
# •	Insert/Delete/Get methods on Text.
# •	Display word count in a Label.

import tkinter as tk

def save_text():
    content = text_area.get("1.0", tk.END).strip()
    print("Saved Content:\n", content)

def clear_text():
    text_area.delete("1.0", tk.END)
    update_word_count()

def load_text():
    preset = "This is a sample notepad. You can edit this text freely."
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, preset)
    update_word_count()

def update_word_count(event=None):
    content = text_area.get("1.0", tk.END).strip()
    words = content.split()
    word_count_label.config(text=f"Word Count: {len(words)}")

root = tk.Tk()
root.title("Notepad App")
root.geometry("500x400")

text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(padx=10, pady=(10, 0))
text_area.bind("<KeyRelease>", update_word_count)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

save_btn=tk.Button(button_frame, text="Save", command=save_text)
save_btn.pack(side="left", padx=10)
clear_btn=tk.Button(button_frame, text="Clear", command=clear_text)
clear_btn.pack(side="left", padx=10)
load_btn=tk.Button(button_frame, text="Load", command=load_text)
load_btn.pack(side="left", padx=10)

word_count_label = tk.Label(root, text="Word Count: 0", anchor="w")
word_count_label.pack(fill="x", padx=10, pady=(0, 10))

root.mainloop()


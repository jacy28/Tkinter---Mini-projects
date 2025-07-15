# 📝 2. Simple Notepad
# Goal: Build a basic notepad where users can write, save, clear, and load notes.
# Requirements:
# •	Use Text widget for input.
# •	Buttons: Save, Load, Clear.
# •	Save/load data to a .txt file.
# •	Use pack() layout.
# •	Allow resizing using geometry().

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("📝 Simple Notepad")
root.geometry("600x400")  # Allow resizing
root.resizable(True, True)

FILENAME = "note.txt"

# --- Functions ---
def save_note():
    content = text_area.get("1.0", tk.END).strip()
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            file.write(content)
        messagebox.showinfo("Success", "Note saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save note:\n{e}")

def load_note():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            content = file.read()
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, content)
    except FileNotFoundError:
        messagebox.showwarning("Not Found", "No saved note found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load note:\n{e}")

def clear_note():
    text_area.delete("1.0", tk.END)

# --- Widgets ---
text_area = tk.Text(root, font=("Arial", 12), wrap=tk.WORD)
text_area.pack(expand=True, fill="both", padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

save_btn = tk.Button(button_frame, text="Save", command=save_note, width=10)
save_btn.pack(side="left", padx=5)

load_btn = tk.Button(button_frame, text="Load", command=load_note, width=10)
load_btn.pack(side="left", padx=5)

clear_btn = tk.Button(button_frame, text="Clear", command=clear_note, width=10)
clear_btn.pack(side="left", padx=5)

root.mainloop()

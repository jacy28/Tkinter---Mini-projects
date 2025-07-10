import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os
import sqlite3
import time

filename = None
img_tk = None

# 49.	Automatically load the most recently used file (store filename in SQLite).
conn = sqlite3.connect("recent.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS recent_file (id INTEGER PRIMARY KEY, filepath TEXT)")
conn.commit()

# --- GUI Setup ---
root = tk.Tk()
root.title("Notepad App")
text = tk.Text(root, wrap="word", width=80, height=25)
text.pack(expand=1, fill="both")
canvas = tk.Canvas(root, height=200)
canvas.pack()

# 36.	Create a button that opens a file using filedialog.askopenfilename() and displays file path.
# 37.	Use a file filter to allow only .txt files to be selected.
# 38.	Add a Text widget and load selected .txt file content into it.
def open_file():
    global filename
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not file_path:
            raise FileNotFoundError("No file selected.")
        with open(file_path, "r") as f:
            text.delete(1.0, tk.END)
            text.insert(tk.END, f.read())
        filename = file_path
        save_recent_file(filename)

        size = os.path.getsize(file_path)
        modified = time.ctime(os.path.getmtime(file_path))
        messagebox.showinfo("File Info", f"File: {file_path}\nSize: {size} bytes\nModified: {modified}")
    except FileNotFoundError:
        messagebox.showwarning("Warning", "File not found or cancelled.")

# 39.	Implement a Save button that saves content of the Text widget to a file.
# 40.	Add file type filters to the Save dialog (e.g., .txt, .csv, .json).
def save_file():
    global filename
    if not filename:
        return save_as_file()
# 45.	Implement Save button with confirmation using messagebox (askyesno()).
    if messagebox.askyesno("Confirm Save", f"Do you want to overwrite '{filename}'?"):
        with open(filename, "w") as f:
            f.write(text.get(1.0, tk.END))
        messagebox.showinfo("Saved", f"File saved: {filename}")

# 43.	Automatically suggest a default file name in the Save dialog.
def save_as_file():
    global filename
    default_name = "untitled.txt"
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=default_name, filetypes=[("Text files", "*.txt"), ("CSV files", "*.csv"), ("JSON files", "*.json")])
    if file_path:
        with open(file_path, "w") as f:
            f.write(text.get(1.0, tk.END))
        filename = file_path
        save_recent_file(filename)
        messagebox.showinfo("Saved", f"File saved as: {file_path}")

# 46.	Add “New” button to clear the Text widget and reset current filename.
def new_file():
    global filename
    text.delete(1.0, tk.END)
    filename = None

# 41.	Add an “Open Image” button and display the selected image using PIL and Canvas.
def open_image():
    global img_tk
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if not file_path:
            raise FileNotFoundError()
        img = Image.open(file_path)
        img.thumbnail((400, 200))
        img_tk = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor="nw", image=img_tk)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "Image not selected.")

# 42.	Let the user choose a directory using filedialog.askdirectory() and display it.
def choose_directory():
    dir_path = filedialog.askdirectory()
    if dir_path:
        messagebox.showinfo("Selected Directory", f"Directory: {dir_path}")

# 49.	Automatically load the most recently used file (store filename in SQLite).
def load_recent_file():
    global filename
    c.execute("SELECT filepath FROM recent_file ORDER BY id DESC LIMIT 1")
    result = c.fetchone()
    if result and os.path.exists(result[0]):
        filename = result[0]
        with open(filename, "r") as f:
            text.delete(1.0, tk.END)
            text.insert(tk.END, f.read())

def save_recent_file(path):
    c.execute("DELETE FROM recent_file")
    c.execute("INSERT INTO recent_file(filepath) VALUES (?)", (path,))
    conn.commit()

# 50.	Allow users to import a .txt file and auto-fill a registration form with its content.
def import_to_form():
    top = tk.Toplevel(root)
    top.title("Registration Form")
    labels = ["Name", "Email", "Phone"]
    entries = []

    for i, label in enumerate(labels):
        tk.Label(top, text=label).grid(row=i, column=0)
        entry = tk.Entry(top, width=40)
        entry.grid(row=i, column=1)
        entries.append(entry)

    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r") as f:
                lines = f.readlines()
                for i in range(min(3, len(lines))):
                    entries[i].insert(0, lines[i].strip())
        except Exception as e:
            messagebox.showerror("Error", f"Failed to import: {e}")

# --- Buttons ---
ttk.Button(root, text="Open File", command=open_file).pack(side="left")
ttk.Button(root, text="Open Image", command=open_image).pack(side="left")
ttk.Button(root, text="Save", command=save_file).pack(side="left")
ttk.Button(root, text="Save As", command=save_as_file).pack(side="left")
ttk.Button(root, text="New", command=new_file).pack(side="left")
ttk.Button(root, text="Choose Directory", command=choose_directory).pack(side="left")
ttk.Button(root, text="Import to Form", command=import_to_form).pack(side="left")

# 49.	Automatically load the most recently used file (store filename in SQLite).
load_recent_file()

root.mainloop()

conn.close()

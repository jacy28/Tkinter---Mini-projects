# 🔷 18. Photo Gallery Viewer
# Widgets Used: Listbox, Scrollbar, Canvas, Combobox
# Requirements:
# •	Listbox with image file names.
# •	Scrollbar for list.
# •	Select image → display on Canvas.
# •	Combobox for filter by image type (JPG, PNG).
# •	Buttons to delete or rename image entries.

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
import os

# --- Settings ---
IMAGE_FOLDER = "images"  # Make sure this folder exists and has images

# --- Main Window ---
root = tk.Tk()
root.title("🔷 Photo Gallery Viewer")
root.geometry("800x500")

# --- Functions ---
image_list = []
current_image = None

def load_images(extension_filter="All"):
    listbox.delete(0, tk.END)
    image_list.clear()

    for filename in os.listdir(IMAGE_FOLDER):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            if extension_filter == "All" or filename.lower().endswith(extension_filter.lower()):
                listbox.insert(tk.END, filename)
                image_list.append(filename)

def show_image(event):
    global current_image
    selected = listbox.curselection()
    if selected:
        filename = listbox.get(selected[0])
        path = os.path.join(IMAGE_FOLDER, filename)
        try:
            img = Image.open(path)
            img.thumbnail((400, 400))
            current_image = ImageTk.PhotoImage(img)
            canvas.delete("all")
            canvas.create_image(200, 200, image=current_image)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to open image:\n{e}")

def filter_images(event=None):
    ext = filter_combo.get()
    load_images(ext if ext != "All" else "All")

def delete_image():
    selected = listbox.curselection()
    if selected:
        filename = listbox.get(selected[0])
        confirm = messagebox.askyesno("Delete", f"Delete '{filename}'?")
        if confirm:
            try:
                os.remove(os.path.join(IMAGE_FOLDER, filename))
                load_images(filter_combo.get())
                canvas.delete("all")
            except Exception as e:
                messagebox.showerror("Error", f"Could not delete:\n{e}")

def rename_image():
    selected = listbox.curselection()
    if selected:
        old_name = listbox.get(selected[0])
        new_name = simpledialog.askstring("Rename", "Enter new name (with extension):")
        if new_name:
            old_path = os.path.join(IMAGE_FOLDER, old_name)
            new_path = os.path.join(IMAGE_FOLDER, new_name)
            try:
                os.rename(old_path, new_path)
                load_images(filter_combo.get())
            except Exception as e:
                messagebox.showerror("Error", f"Could not rename:\n{e}")

# --- Widgets Layout ---
# Left panel: listbox with scrollbar
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

tk.Label(left_frame, text="Images").pack()

scrollbar = tk.Scrollbar(left_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(left_frame, yscrollcommand=scrollbar.set, width=30)
listbox.pack()
scrollbar.config(command=listbox.yview)

listbox.bind("<<ListboxSelect>>", show_image)

# Canvas
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(side=tk.LEFT, padx=10, pady=10)

# Right panel
right_frame = tk.Frame(root)
right_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

tk.Label(right_frame, text="Filter by Type:").pack()
filter_combo = ttk.Combobox(right_frame, values=["All", ".jpg", ".png"], state="readonly")
filter_combo.set("All")
filter_combo.pack(pady=5)
filter_combo.bind("<<ComboboxSelected>>", filter_images)

tk.Button(right_frame, text="🗑 Delete", width=15, command=delete_image).pack(pady=5)
tk.Button(right_frame, text="✏️ Rename", width=15, command=rename_image).pack(pady=5)

# --- Start ---
load_images()

root.mainloop()

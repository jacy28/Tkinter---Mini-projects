# 🔰 4. Image Organizer App (FileDialog + Directory)
# Goal: Organize and view image files in a folder.
# Requirements:
# •	Select directory via askdirectory().
# •	Display list of image files (.jpg, .png).
# •	Open selected image in canvas.
# •	Show image dimensions.

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

def select_directory():
    folder = filedialog.askdirectory()
    if folder:
        listbox.delete(0, tk.END)
        root.folder = folder
        for file in os.listdir(folder):
            if file.lower().endswith(('.jpg', '.png')):
                listbox.insert(tk.END, file)

def show_image(event):
    if not listbox.curselection():
        return
    filename = listbox.get(listbox.curselection()[0])
    path = os.path.join(root.folder, filename)
    img = Image.open(path)
    root.current_img = ImageTk.PhotoImage(img.resize((300, 300)))
    canvas.delete("all")
    canvas.create_image(150, 150, image=root.current_img)
    dimensions_label.config(text=f"{img.width} x {img.height}")

root = tk.Tk()
root.title("Image Organizer")
root.geometry("500x500")
root.folder = ""
root.current_img = None

tk.Button(root, text="Select Folder", command=select_directory).pack(pady=10)

listbox = tk.Listbox(root)
listbox.pack(fill="x", padx=10)
listbox.bind("<<ListboxSelect>>", show_image)

canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack(pady=10)

dimensions_label = tk.Label(root, text="")
dimensions_label.pack()

root.mainloop()

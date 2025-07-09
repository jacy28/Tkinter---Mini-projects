# ✅ 7. Image Viewer UI
# Objective: Display and manage local images.
# Requirements:
# •	Use Frame for toolbar and canvas/image area.
# •	Toolbar buttons: Open Image, Zoom In, Zoom Out.
# •	Add Menu: File > Open, Exit.
# •	Show errors in messagebox if the image path is invalid.

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image Viewer")
root.geometry("800x600")

img = None
img_display = None
zoom_factor = 1.0

def open_image():
    global img, img_display, zoom_factor
    path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp *.gif")])
    if not path:
        return
    try:
        img = Image.open(path)
        zoom_factor = 1.0
        display_image()
    except Exception as e:
        messagebox.showerror("Error", f"Unable to open image.\n{e}")

def display_image():
    global img, img_display
    if img:
        resized = img.resize((int(img.width * zoom_factor), int(img.height * zoom_factor)))
        img_display = ImageTk.PhotoImage(resized)
        canvas.delete("all")
        canvas.create_image(10, 10, anchor="nw", image=img_display)
        canvas.config(scrollregion=canvas.bbox("all"))

def zoom_in():
    global zoom_factor
    if img:
        zoom_factor *= 1.2
        display_image()

def zoom_out():
    global zoom_factor
    if img:
        zoom_factor /= 1.2
        display_image()

# Menu
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=open_image)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

# Toolbar
toolbar = tk.Frame(root)
toolbar.pack(side="top", fill="x")
tk.Button(toolbar, text="Open Image", command=open_image).pack(side="left", padx=5)
tk.Button(toolbar, text="Zoom In", command=zoom_in).pack(side="left", padx=5)
tk.Button(toolbar, text="Zoom Out", command=zoom_out).pack(side="left", padx=5)

# Canvas with Scrollbars
canvas_frame = tk.Frame(root)
canvas_frame.pack(fill="both", expand=True)

x_scroll = tk.Scrollbar(canvas_frame, orient="horizontal")
x_scroll.pack(side="bottom", fill="x")
y_scroll = tk.Scrollbar(canvas_frame, orient="vertical")
y_scroll.pack(side="right", fill="y")

canvas = tk.Canvas(canvas_frame, bg="gray", xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)
canvas.pack(side="left", fill="both", expand=True)

x_scroll.config(command=canvas.xview)
y_scroll.config(command=canvas.yview)

root.mainloop()

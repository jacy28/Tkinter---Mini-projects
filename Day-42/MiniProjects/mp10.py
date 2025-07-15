# 🔷 10. Font Preview Tool
# Widgets Used: Combobox, Spinbox, Canvas
# Requirements:
# •	Combobox to choose font family.
# •	Spinbox for font size.
# •	Draw preview text on Canvas.
# •	Change font live when options change.
# •	Option to save the preview image as PNG.

import tkinter as tk
from tkinter import ttk, font, filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk

root = tk.Tk()
root.title("🔷 Font Preview Tool")
root.geometry("600x450")

# === Canvas for Preview === #
canvas = tk.Canvas(root, width=500, height=200, bg="white")
canvas.pack(pady=20)

# Default values
preview_text = "The quick brown fox"
font_size = tk.IntVar(value=24)
font_family = tk.StringVar()

# === Font Controls === #
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

# Font family selector
tk.Label(control_frame, text="Font:").grid(row=0, column=0, padx=5)
font_families = list(font.families())
font_combo = ttk.Combobox(control_frame, values=font_families, textvariable=font_family, state="readonly", width=25)
font_combo.set("Arial")
font_combo.grid(row=0, column=1, padx=5)

# Font size selector
tk.Label(control_frame, text="Size:").grid(row=0, column=2, padx=5)
size_spin = tk.Spinbox(control_frame, from_=8, to=72, textvariable=font_size, width=5)
size_spin.grid(row=0, column=3, padx=5)

# === Draw Function === #
def draw_preview():
    canvas.delete("all")
    current_font = (font_family.get(), font_size.get())
    canvas.create_text(250, 100, text=preview_text, font=current_font, fill="black")

# === Save Function === #
def save_as_png():
    # Create an image using Pillow
    img = Image.new("RGB", (500, 200), "white")
    draw = ImageDraw.Draw(img)
    
    try:
        pil_font = ImageFont.truetype(font_family.get(), font_size.get())
    except:
        pil_font = ImageFont.load_default()

    draw.text((20, 80), preview_text, font=pil_font, fill="black")
    
    filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if filepath:
        img.save(filepath)

# === Event Bindings === #
font_combo.bind("<<ComboboxSelected>>", lambda e: draw_preview())
size_spin.bind("<KeyRelease>", lambda e: draw_preview())
size_spin.bind("<ButtonRelease-1>", lambda e: draw_preview())

# === Save Button === #
tk.Button(root, text="💾 Save as PNG", command=save_as_png).pack(pady=10)

# Initial draw
draw_preview()

root.mainloop()

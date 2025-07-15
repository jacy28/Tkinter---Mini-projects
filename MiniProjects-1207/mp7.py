# 27. Pixel Art Editor with Export to Image
# •	Canvas with grid (e.g., 32x32)
# •	Click to fill pixels with chosen color
# •	Export as PNG
# •	Color palette + eraser
# •	Save/load project from .json

import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from PIL import Image
import json
import os

class PixelArtEditor:
    def __init__(self, root, grid_size=32, pixel_size=20):
        self.root = root
        self.root.title("Pixel Art Editor")

        self.grid_size = grid_size
        self.pixel_size = pixel_size
        self.current_color = "#000000"
        self.default_color = "#ffffff"

        self.pixels = [[self.default_color for _ in range(grid_size)] for _ in range(grid_size)]
        self.rect_ids = [[None for _ in range(grid_size)] for _ in range(grid_size)]

        self.create_ui()

    def create_ui(self):
        # Controls
        ctrl = tk.Frame(self.root)
        ctrl.pack(pady=5)

        tk.Button(ctrl, text="Pick Color", command=self.pick_color).pack(side='left', padx=3)
        tk.Button(ctrl, text="Eraser", command=self.use_eraser).pack(side='left', padx=3)
        tk.Button(ctrl, text="Export PNG", command=self.export_png).pack(side='left', padx=3)
        tk.Button(ctrl, text="Save JSON", command=self.save_json).pack(side='left', padx=3)
        tk.Button(ctrl, text="Load JSON", command=self.load_json).pack(side='left', padx=3)

        # Canvas
        self.canvas = tk.Canvas(self.root, width=self.grid_size * self.pixel_size,
                                height=self.grid_size * self.pixel_size, bg="white")
        self.canvas.pack()

        self.draw_grid()
        self.canvas.bind("<Button-1>", self.fill_pixel)

    def draw_grid(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                x1 = col * self.pixel_size
                y1 = row * self.pixel_size
                x2 = x1 + self.pixel_size
                y2 = y1 + self.pixel_size
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.default_color, outline="gray")
                self.rect_ids[row][col] = rect

    def pick_color(self):
        color = colorchooser.askcolor(title="Choose Color")[1]
        if color:
            self.current_color = color

    def use_eraser(self):
        self.current_color = self.default_color

    def fill_pixel(self, event):
        col = event.x // self.pixel_size
        row = event.y // self.pixel_size
        if 0 <= row < self.grid_size and 0 <= col < self.grid_size:
            self.pixels[row][col] = self.current_color
            rect = self.rect_ids[row][col]
            self.canvas.itemconfig(rect, fill=self.current_color)

    def export_png(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if not file_path:
            return

        img = Image.new("RGB", (self.grid_size, self.grid_size), self.default_color)
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                color = self.pixels[row][col]
                img.putpixel((col, row), Image.new("RGB", (1, 1), color).getpixel((0, 0)))

        # Scale up
        img = img.resize((self.grid_size * self.pixel_size, self.grid_size * self.pixel_size), Image.NEAREST)
        img.save(file_path)

    def save_json(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json")
        if not file_path:
            return
        try:
            with open(file_path, 'w') as f:
                json.dump(self.pixels, f)
            messagebox.showinfo("Saved", "Project saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def load_json(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if not file_path or not os.path.exists(file_path):
            return
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            if len(data) != self.grid_size or len(data[0]) != self.grid_size:
                messagebox.showerror("Error", "Invalid grid size.")
                return
            self.pixels = data
            for row in range(self.grid_size):
                for col in range(self.grid_size):
                    rect = self.rect_ids[row][col]
                    self.canvas.itemconfig(rect, fill=self.pixels[row][col])
            messagebox.showinfo("Loaded", "Project loaded successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = PixelArtEditor(root)
    root.mainloop()

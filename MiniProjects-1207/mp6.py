# 26. Drawing App with Shape Tools and Color Picker
# •	Canvas with drawing options: line, rectangle, oval
# •	Color and width pickers
# •	Save drawing as PNG
# •	Undo/redo feature
# •	Keyboard shortcuts for tools

import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import ImageGrab

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App")

        self.tool = "line"
        self.color = "black"
        self.width = 2
        self.start_x = None
        self.start_y = None
        self.current_item = None
        self.history = []
        self.redo_stack = []

        self.create_widgets()

    def create_widgets(self):
        toolbar = tk.Frame(self.root)
        toolbar.pack(fill='x')

        tk.Button(toolbar, text="Line (L)", command=lambda: self.set_tool("line")).pack(side='left')
        tk.Button(toolbar, text="Rectangle (R)", command=lambda: self.set_tool("rectangle")).pack(side='left')
        tk.Button(toolbar, text="Oval (O)", command=lambda: self.set_tool("oval")).pack(side='left')
        tk.Button(toolbar, text="Color", command=self.choose_color).pack(side='left')
        tk.Button(toolbar, text="Undo (Z)", command=self.undo).pack(side='left')
        tk.Button(toolbar, text="Redo (Y)", command=self.redo).pack(side='left')
        tk.Button(toolbar, text="Save (S)", command=self.save).pack(side='left')

        self.width_slider = tk.Scale(toolbar, from_=1, to=10, orient='horizontal', label='Width')
        self.width_slider.set(self.width)
        self.width_slider.pack(side='left')

        self.canvas = tk.Canvas(self.root, bg='white', width=800, height=500)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.finish_draw)

        # Shortcuts
        self.root.bind("<l>", lambda e: self.set_tool("line"))
        self.root.bind("<r>", lambda e: self.set_tool("rectangle"))
        self.root.bind("<o>", lambda e: self.set_tool("oval"))
        self.root.bind("<z>", lambda e: self.undo())
        self.root.bind("<y>", lambda e: self.redo())
        self.root.bind("<s>", lambda e: self.save())

    def set_tool(self, tool):
        self.tool = tool

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color

    def start_draw(self, event):
        self.start_x, self.start_y = event.x, event.y
        self.width = self.width_slider.get()

    def draw(self, event):
        if self.current_item:
            self.canvas.delete(self.current_item)

        args = (self.start_x, self.start_y, event.x, event.y)
        options = {'fill': self.color, 'width': self.width} if self.tool == 'line' else {'outline': self.color, 'width': self.width}

        if self.tool == "line":
            self.current_item = self.canvas.create_line(*args, **options)
        elif self.tool == "rectangle":
            self.current_item = self.canvas.create_rectangle(*args, **options)
        elif self.tool == "oval":
            self.current_item = self.canvas.create_oval(*args, **options)

    def finish_draw(self, event):
        if self.current_item:
            self.history.append(self.current_item)
            self.current_item = None
            self.redo_stack.clear()

    def undo(self):
        if self.history:
            item = self.history.pop()
            self.canvas.itemconfig(item, state='hidden')
            self.redo_stack.append(item)

    def redo(self):
        if self.redo_stack:
            item = self.redo_stack.pop()
            self.canvas.itemconfig(item, state='normal')
            self.history.append(item)

    def save(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            x = self.root.winfo_rootx() + self.canvas.winfo_x()
            y = self.root.winfo_rooty() + self.canvas.winfo_y()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()
            ImageGrab.grab(bbox=(x, y, x1, y1)).save(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()

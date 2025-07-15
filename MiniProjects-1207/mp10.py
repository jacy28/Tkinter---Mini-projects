# 30. Mind Map Creator with Drag-and-Drop
# •	Canvas-based node editor
# •	Add text nodes, connect with lines
# •	Drag nodes, update links
# •	Save/load as .json
# •	Export mind map as PNG

import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox
import json
from PIL import ImageGrab

class MindMapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mind Map Creator")

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(fill="both", expand=True)

        self.nodes = []  # List of nodes (dict with id, x, y, text)
        self.connections = []  # List of (from_id, to_id)
        self.drag_data = {"item": None, "x": 0, "y": 0}

        # Menu
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Add Node", command=self.add_node)
        filemenu.add_command(label="Connect Nodes", command=self.connect_nodes)
        filemenu.add_separator()
        filemenu.add_command(label="Save Project", command=self.save_json)
        filemenu.add_command(label="Load Project", command=self.load_json)
        filemenu.add_command(label="Export as PNG", command=self.export_png)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        root.config(menu=menubar)

        # Bindings
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<B1-Motion>", self.on_canvas_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_canvas_release)

    def add_node(self):
        text = simpledialog.askstring("Node Text", "Enter node text:")
        if text:
            x, y = 100, 100
            node_id = self.canvas.create_oval(x, y, x+100, y+50, fill="lightblue")
            text_id = self.canvas.create_text(x+50, y+25, text=text)
            self.nodes.append({"id": node_id, "label": text_id, "x": x, "y": y, "text": text})

    def connect_nodes(self):
        if len(self.nodes) < 2:
            messagebox.showerror("Error", "Need at least 2 nodes to connect.")
            return

        ids = [str(i+1) + ": " + node["text"] for i, node in enumerate(self.nodes)]
        msg = "\n".join(ids)
        i1 = simpledialog.askinteger("From Node", f"Select FROM node:\n{msg}") or 0
        i2 = simpledialog.askinteger("To Node", f"Select TO node:\n{msg}") or 0
        if 0 < i1 <= len(self.nodes) and 0 < i2 <= len(self.nodes):
            n1 = self.nodes[i1-1]
            n2 = self.nodes[i2-1]
            x1 = n1["x"] + 50
            y1 = n1["y"] + 25
            x2 = n2["x"] + 50
            y2 = n2["y"] + 25
            line = self.canvas.create_line(x1, y1, x2, y2, arrow="last")
            self.connections.append((n1["id"], n2["id"], line))

    def on_canvas_click(self, event):
        found = self.canvas.find_closest(event.x, event.y)
        if not found:
            return

        item = found[0]
        for node in self.nodes:
            if item == node["id"] or item == node["label"]:
                self.drag_data["item"] = node
                self.drag_data["x"] = event.x
                self.drag_data["y"] = event.y
                return

    def on_canvas_drag(self, event):
        node = self.drag_data["item"]
        if node:
            dx = event.x - self.drag_data["x"]
            dy = event.y - self.drag_data["y"]
            self.canvas.move(node["id"], dx, dy)
            self.canvas.move(node["label"], dx, dy)
            node["x"] += dx
            node["y"] += dy
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y
            self.redraw_connections()

    def on_canvas_release(self, event):
        self.drag_data["item"] = None

    def redraw_connections(self):
        for from_id, to_id, line in self.connections:
            n1 = next((n for n in self.nodes if n["id"] == from_id), None)
            n2 = next((n for n in self.nodes if n["id"] == to_id), None)
            if n1 and n2:
                x1 = n1["x"] + 50
                y1 = n1["y"] + 25
                x2 = n2["x"] + 50
                y2 = n2["y"] + 25
                self.canvas.coords(line, x1, y1, x2, y2)

    def save_json(self):
        file = filedialog.asksaveasfilename(defaultextension=".json")
        if file:
            data = {
                "nodes": [{"x": n["x"], "y": n["y"], "text": n["text"]} for n in self.nodes],
                "connections": [(self.get_node_index(fid), self.get_node_index(tid)) for fid, tid, _ in self.connections]
            }
            with open(file, "w") as f:
                json.dump(data, f)

    def load_json(self):
        file = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if file:
            with open(file, "r") as f:
                data = json.load(f)
            self.canvas.delete("all")
            self.nodes.clear()
            self.connections.clear()
            for node in data["nodes"]:
                x, y, text = node["x"], node["y"], node["text"]
                node_id = self.canvas.create_oval(x, y, x+100, y+50, fill="lightblue")
                text_id = self.canvas.create_text(x+50, y+25, text=text)
                self.nodes.append({"id": node_id, "label": text_id, "x": x, "y": y, "text": text})
            for i1, i2 in data["connections"]:
                if i1 < len(self.nodes) and i2 < len(self.nodes):
                    n1 = self.nodes[i1]
                    n2 = self.nodes[i2]
                    x1 = n1["x"] + 50
                    y1 = n1["y"] + 25
                    x2 = n2["x"] + 50
                    y2 = n2["y"] + 25
                    line = self.canvas.create_line(x1, y1, x2, y2, arrow="last")
                    self.connections.append((n1["id"], n2["id"], line))

    def get_node_index(self, canvas_id):
        for i, node in enumerate(self.nodes):
            if node["id"] == canvas_id:
                return i
        return -1

    def export_png(self):
        file = filedialog.asksaveasfilename(defaultextension=".png")
        if file:
            x = self.root.winfo_rootx() + self.canvas.winfo_x()
            y = self.root.winfo_rooty() + self.canvas.winfo_y()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(file)

if __name__ == "__main__":
    root = tk.Tk()
    app = MindMapApp(root)
    root.mainloop()


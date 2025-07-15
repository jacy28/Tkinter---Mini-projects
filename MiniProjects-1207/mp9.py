# 29. Storyboard Editor with Scene Management
# •	Add scenes with title, text, image
# •	Reorder scenes with drag-and-drop
# •	Save project to .json
# •	Export storyboard to printable PDF
# •	Search/filter scenes

import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter import ttk
from PIL import Image, ImageTk
import json
from fpdf import FPDF
import os

class StoryboardEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Storyboard Editor")
        self.scenes = []

        self.build_ui()

    def build_ui(self):
        top_frame = tk.Frame(self.root)
        top_frame.pack(fill="x")

        tk.Button(top_frame, text="Add Scene", command=self.add_scene).pack(side="left")
        tk.Button(top_frame, text="Remove Selected", command=self.remove_selected).pack(side="left")
        tk.Button(top_frame, text="Move Up", command=lambda: self.move_scene(-1)).pack(side="left")
        tk.Button(top_frame, text="Move Down", command=lambda: self.move_scene(1)).pack(side="left")
        tk.Button(top_frame, text="Save JSON", command=self.save_json).pack(side="left")
        tk.Button(top_frame, text="Load JSON", command=self.load_json).pack(side="left")
        tk.Button(top_frame, text="Export PDF", command=self.export_pdf).pack(side="left")

        self.search_var = tk.StringVar()
        tk.Entry(top_frame, textvariable=self.search_var).pack(side="right")
        tk.Button(top_frame, text="Search", command=self.search_scenes).pack(side="right")

        self.tree = ttk.Treeview(self.root, columns=("Title", "Text"), show='headings')
        self.tree.heading("Title", text="Title")
        self.tree.heading("Text", text="Description")
        self.tree.pack(fill="both", expand=True)

    def add_scene(self):
        title = simpledialog.askstring("Title", "Enter scene title:")
        if not title:
            return
        text = simpledialog.askstring("Description", "Enter scene description:")
        if text is None:
            return

        image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if not image_path:
            return

        scene = {
            "title": title,
            "text": text,
            "image": image_path
        }
        self.scenes.append(scene)
        self.refresh_tree()

    def refresh_tree(self, filtered=None):
        self.tree.delete(*self.tree.get_children())
        data = filtered if filtered is not None else self.scenes
        for scene in data:
            self.tree.insert("", "end", values=(scene["title"], scene["text"][:40] + "..."))

    def remove_selected(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            del self.scenes[index]
            self.refresh_tree()

    def move_scene(self, direction):
        selected = self.tree.selection()
        if not selected:
            return
        index = self.tree.index(selected[0])
        new_index = index + direction
        if 0 <= new_index < len(self.scenes):
            self.scenes[index], self.scenes[new_index] = self.scenes[new_index], self.scenes[index]
            self.refresh_tree()
            self.tree.selection_set(self.tree.get_children()[new_index])

    def save_json(self):
        path = filedialog.asksaveasfilename(defaultextension=".json")
        if path:
            with open(path, "w") as f:
                json.dump(self.scenes, f)
            messagebox.showinfo("Saved", "Storyboard saved successfully.")

    def load_json(self):
        path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if path:
            with open(path, "r") as f:
                self.scenes = json.load(f)
            self.refresh_tree()

    def export_pdf(self):
        if not self.scenes:
            messagebox.showwarning("Empty", "No scenes to export.")
            return

        pdf = FPDF()
        for scene in self.scenes:
            pdf.add_page()
            pdf.set_font("Arial", "B", 16)
            pdf.multi_cell(0, 10, f"Title: {scene['title']}")
            pdf.set_font("Arial", "", 12)
            pdf.multi_cell(0, 10, f"Description: {scene['text']}")
            try:
                img_path = scene['image']
                if os.path.exists(img_path):
                    pdf.image(img_path, w=100)
            except:
                continue

        save_path = filedialog.asksaveasfilename(defaultextension=".pdf")
        if save_path:
            pdf.output(save_path)
            messagebox.showinfo("Exported", f"PDF saved to {save_path}")

    def search_scenes(self):
        keyword = self.search_var.get().lower()
        filtered = [s for s in self.scenes if keyword in s["title"].lower() or keyword in s["text"].lower()]
        self.refresh_tree(filtered=filtered)

if __name__ == "__main__":
    root = tk.Tk()
    app = StoryboardEditor(root)
    root.mainloop()

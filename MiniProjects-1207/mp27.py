# 47. Recipe Book Manager with Search and Categories
# •	Add/edit recipes with ingredients and steps
# •	Organize by cuisine/type
# •	Search/filter by keyword
# •	Import/export .json
# •	Image attachment support

import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter import ttk
from PIL import Image, ImageTk
import json
import os

recipes = []

def add_recipe():
    name = name_var.get()
    cuisine = cuisine_var.get()
    ingredients = ingredients_text.get("1.0", tk.END).strip()
    steps = steps_text.get("1.0", tk.END).strip()
    image_path = image_var.get()

    if not name or not ingredients or not steps:
        messagebox.showerror("Error", "Please fill in all required fields.")
        return

    recipes.append({
        "name": name,
        "cuisine": cuisine,
        "ingredients": ingredients,
        "steps": steps,
        "image": image_path
    })
    update_list()
    clear_fields()

def clear_fields():
    name_var.set("")
    cuisine_var.set("")
    ingredients_text.delete("1.0", tk.END)
    steps_text.delete("1.0", tk.END)
    image_var.set("")
    image_label.config(image='')

def update_list(filtered=None):
    recipe_list.delete(0, tk.END)
    display = filtered if filtered else recipes
    for r in display:
        recipe_list.insert(tk.END, r["name"])

def search_recipes():
    keyword = search_var.get().lower()
    filtered = [r for r in recipes if keyword in r["name"].lower() or keyword in r["ingredients"].lower()]
    update_list(filtered)

def on_select(event):
    if not recipe_list.curselection():
        return
    index = recipe_list.curselection()[0]
    selected = recipes[index]
    name_var.set(selected["name"])
    cuisine_var.set(selected["cuisine"])
    ingredients_text.delete("1.0", tk.END)
    ingredients_text.insert(tk.END, selected["ingredients"])
    steps_text.delete("1.0", tk.END)
    steps_text.insert(tk.END, selected["steps"])
    image_var.set(selected.get("image", ""))
    show_image()

def save_recipes():
    path = filedialog.asksaveasfilename(defaultextension=".json")
    if path:
        with open(path, "w") as f:
            json.dump(recipes, f)
        messagebox.showinfo("Saved", "Recipes saved successfully.")

def load_recipes():
    global recipes
    path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if path:
        with open(path, "r") as f:
            recipes = json.load(f)
        update_list()
        messagebox.showinfo("Loaded", "Recipes loaded successfully.")

def attach_image():
    path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    if path:
        image_var.set(path)
        show_image()

def show_image():
    path = image_var.get()
    if os.path.exists(path):
        img = Image.open(path)
        img.thumbnail((150, 150))
        tk_img = ImageTk.PhotoImage(img)
        image_label.config(image=tk_img)
        image_label.image = tk_img  # Keep a reference

# ---------- GUI SETUP ---------- #
root = tk.Tk()
root.title("Recipe Book Manager")
root.geometry("1000x600")

name_var = tk.StringVar()
cuisine_var = tk.StringVar()
image_var = tk.StringVar()
search_var = tk.StringVar()

# --- Left Form --- #
form = tk.Frame(root)
form.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)

tk.Label(form, text="Recipe Name:").pack(anchor='w')
tk.Entry(form, textvariable=name_var, width=40).pack()

tk.Label(form, text="Cuisine/Type:").pack(anchor='w')
tk.Entry(form, textvariable=cuisine_var, width=40).pack()

tk.Label(form, text="Ingredients:").pack(anchor='w')
ingredients_text = tk.Text(form, width=40, height=5)
ingredients_text.pack()

tk.Label(form, text="Steps:").pack(anchor='w')
steps_text = tk.Text(form, width=40, height=5)
steps_text.pack()

tk.Button(form, text="Attach Image", command=attach_image).pack(pady=5)
tk.Label(form, textvariable=image_var, wraplength=300).pack()

tk.Button(form, text="Add Recipe", command=add_recipe).pack(pady=5)
tk.Button(form, text="Save to JSON", command=save_recipes).pack()
tk.Button(form, text="Load from JSON", command=load_recipes).pack()

# --- Right Display --- #
right = tk.Frame(root)
right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

tk.Label(right, text="Search:").pack(anchor='w')
tk.Entry(right, textvariable=search_var).pack(anchor='w')
tk.Button(right, text="Search", command=search_recipes).pack(anchor='w')

recipe_list = tk.Listbox(right, width=40, height=25)
recipe_list.pack(pady=5)
recipe_list.bind("<<ListboxSelect>>", on_select)

image_label = tk.Label(right)
image_label.pack()

update_list()

root.mainloop()

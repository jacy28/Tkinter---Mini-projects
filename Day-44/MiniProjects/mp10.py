# ✅ 10. Listbox Navigator with Keyboard
# Objective: Navigate a Listbox using arrow keys.
# Features:
# •	Listbox with several items.
# •	Bind <Up> and <Down> to change selection.
# •	Show selected item in a Label when Enter is pressed.

import tkinter as tk

def on_key(event):
    cur = listbox.curselection()
    if not cur:
        index = 0
    else:
        index = cur[0]

    if event.keysym == "Down":
        if index < listbox.size() - 1:
            listbox.selection_clear(0, tk.END)
            listbox.selection_set(index + 1)
            listbox.activate(index + 1)

    elif event.keysym == "Up":
        if index > 0:
            listbox.selection_clear(0, tk.END)
            listbox.selection_set(index - 1)
            listbox.activate(index - 1)

    elif event.keysym == "Return":
        selected = listbox.get(index)
        selected_label.config(text=f"Selected: {selected}")

root = tk.Tk()
root.geometry("300x250")

listbox = tk.Listbox(root, height=10)
items = ["Python", "Java", "C++", "JavaScript", "Ruby", "Go", "Swift"]
for item in items:
    listbox.insert(tk.END, item)
listbox.pack(pady=10)

selected_label = tk.Label(root, text="Selected: ")
selected_label.pack()

root.bind("<Up>", on_key)
root.bind("<Down>", on_key)
root.bind("<Return>", on_key)

root.mainloop()

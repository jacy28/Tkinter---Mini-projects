# # 21.	Create a Listbox and insert five static items.
# import tkinter as tk
# root = tk.Tk()
# root.geometry("400x300")
# root.title("Listbox with Static Items")
# # Create a Listbox
# listbox = tk.Listbox(root, height=5)
# listbox.pack(padx=10, pady=10)
# # Insert five static items
# items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
# for item in items:
#     listbox.insert(tk.END, item)
# root.mainloop()


# # 22.	Select and print the selected item using a button.
# import tkinter as tk
# def print_selected():
#     selected = listbox.curselection()
#     if selected:
#         item = listbox.get(selected[0])
#         print(f"Selected item: {item}")
#     else:
#         print("No item selected")
# root = tk.Tk()
# root.title("Listbox Selection")
# root.geometry("400x300")
# # Create Listbox
# listbox = tk.Listbox(root, height=5)
# listbox.pack(padx=10, pady=10)
# # Insert items
# items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
# for item in items:
#     listbox.insert(tk.END, item)
# # Create Button
# btn = tk.Button(root, text="Print Selected", command=print_selected)
# btn.pack(pady=5)
# root.mainloop()


# # 23.	Allow multiple selections and print all selected items.
# import tkinter as tk

# def print_selected():
#     selected_indices = listbox.curselection()
#     if selected_indices:
#         selected_items = [listbox.get(i) for i in selected_indices]
#         print("Selected items:", ", ".join(selected_items))
#     else:
#         print("No items selected")

# root = tk.Tk()
# root.title("Multiple Selection Listbox")

# # Create Listbox with multiple selection enabled
# listbox = tk.Listbox(root, height=5, selectmode='multiple')
# listbox.pack(padx=10, pady=10)

# # Insert items
# items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
# for item in items:
#     listbox.insert(tk.END, item)

# # Button to print selected items
# btn = tk.Button(root, text="Print Selected", command=print_selected)
# btn.pack(pady=5)

# root.mainloop()


# # 24.	Clear all items from the Listbox using a button.
# import tkinter as tk
# def clear_listbox():
#     listbox.delete(0, tk.END)
# root = tk.Tk()
# root.title("Clear Listbox")
# # Create Listbox
# listbox = tk.Listbox(root, height=5)
# listbox.pack(padx=10, pady=10)
# # Insert some items
# items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
# for item in items:
#     listbox.insert(tk.END, item)
# # Button to clear all items
# btn_clear = tk.Button(root, text="Clear Listbox", command=clear_listbox)
# btn_clear.pack(pady=5)
# root.mainloop()

# # 25.	Add a new item dynamically using an Entry and Button.
# import tkinter as tk
# def add_item():
#     new_item = entry.get().strip()
#     if new_item:
#         listbox.insert(tk.END, new_item)
#         entry.delete(0, tk.END)
# root = tk.Tk()
# root.title("Add Item to Listbox")
# # Listbox
# listbox = tk.Listbox(root, height=6)
# listbox.pack(padx=10, pady=5)
# # Entry for new item
# entry = tk.Entry(root)
# entry.pack(padx=10, pady=5)
# # Button to add item
# btn_add = tk.Button(root, text="Add Item", command=add_item)
# btn_add.pack(pady=5)
# # Optional: Pre-fill list with items
# initial_items = ["Apple", "Banana", "Cherry"]
# for item in initial_items:
#     listbox.insert(tk.END, item)
# root.mainloop()

# # 26.	Create a Listbox with 20+ items and add a vertical scrollbar.
# import tkinter as tk
# root = tk.Tk()
# root.title("Listbox with Scrollbar")
# # Frame to hold Listbox and Scrollbar side by side
# frame = tk.Frame(root)
# frame.pack(padx=10, pady=10)
# # Create Scrollbar
# scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
# # Create Listbox and link it to Scrollbar
# listbox = tk.Listbox(frame, height=10, yscrollcommand=scrollbar.set)
# scrollbar.config(command=listbox.yview)
# # Pack Listbox and Scrollbar
# listbox.pack(side=tk.LEFT, fill=tk.BOTH)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# # Insert 20+ items
# for i in range(1, 31):
#     listbox.insert(tk.END, f"Item {i}")
# root.mainloop()

# # 27.	Create a horizontal scrollbar for long text items.
# import tkinter as tk
# root = tk.Tk()
# root.title("Listbox with Horizontal Scrollbar")
# # Frame to hold Listbox and both scrollbars
# frame = tk.Frame(root)
# frame.pack(padx=10, pady=10)
# # Vertical Scrollbar
# v_scroll = tk.Scrollbar(frame, orient=tk.VERTICAL)
# # Horizontal Scrollbar
# h_scroll = tk.Scrollbar(root, orient=tk.HORIZONTAL)
# # Create Listbox with scroll commands
# listbox = tk.Listbox(frame, width=40, height=8, xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)
# # Configure scrollbars
# v_scroll.config(command=listbox.yview)
# h_scroll.config(command=listbox.xview)
# # Pack Listbox and Scrollbars
# listbox.pack(side=tk.LEFT, fill=tk.BOTH)
# v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
# h_scroll.pack(fill=tk.X)
# # Insert long text items
# long_items = [
#     "This is a very long item that might not fit in the Listbox window.",
#     "Another extremely lengthy line of text for testing scrolling functionality.",
#     "Short",
#     "Medium length item",
#     "One more super long text entry to scroll horizontally across the Listbox.",
# ]
# for item in long_items:
#     listbox.insert(tk.END, item)
# root.mainloop()


# # 28.	Synchronize scrollbar with Listbox using yscrollcommand.
# import tkinter as tk

# root = tk.Tk()
# root.title("Synchronized Scrollbar and Listbox")

# # Frame to hold the Listbox and Scrollbar
# frame = tk.Frame(root)
# frame.pack(padx=10, pady=10)

# # Create the Scrollbar
# scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)

# # Create the Listbox and link to scrollbar
# listbox = tk.Listbox(frame, height=10, yscrollcommand=scrollbar.set)
# scrollbar.config(command=listbox.yview)

# # Pack the widgets
# listbox.pack(side=tk.LEFT, fill=tk.BOTH)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# # Insert items to fill list
# for i in range(1, 51):
#     listbox.insert(tk.END, f"Item {i}")

# root.mainloop()

# # 29.	Scroll programmatically to a specific item (e.g., Item 10).
# import tkinter as tk

# def scroll_to_item_10():
#     listbox.see(9)  # Index 9 = Item 10 (0-based indexing)

# root = tk.Tk()
# root.title("Scroll to Item")

# # Frame for Listbox and scrollbar
# frame = tk.Frame(root)
# frame.pack(padx=10, pady=10)

# # Scrollbar
# scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)

# # Listbox
# listbox = tk.Listbox(frame, height=10, yscrollcommand=scrollbar.set)
# scrollbar.config(command=listbox.yview)

# # Pack Listbox and Scrollbar
# listbox.pack(side=tk.LEFT, fill=tk.BOTH)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# # Insert 50 items
# for i in range(1, 51):
#     listbox.insert(tk.END, f"Item {i}")

# # Button to scroll to Item 10
# btn = tk.Button(root, text="Go to Item 10", command=scroll_to_item_10)
# btn.pack(pady=5)

# root.mainloop()

# # 30.	Display the current scroll position using listbox.yview().
# import tkinter as tk

# def show_scroll_position():
#     position = listbox.yview()
#     label.config(text=f"Scroll position: {position[0]:.2f} - {position[1]:.2f}")

# root = tk.Tk()
# root.title("Listbox Scroll Position")

# # Frame for Listbox and Scrollbar
# frame = tk.Frame(root)
# frame.pack(padx=10, pady=10)

# # Scrollbar
# scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)

# # Listbox
# listbox = tk.Listbox(frame, height=10, yscrollcommand=scrollbar.set)
# scrollbar.config(command=listbox.yview)

# # Pack Listbox and Scrollbar
# listbox.pack(side=tk.LEFT, fill=tk.BOTH)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# # Add many items
# for i in range(1, 101):
#     listbox.insert(tk.END, f"Item {i}")

# # Button to show scroll position
# btn = tk.Button(root, text="Show Scroll Position", command=show_scroll_position)
# btn.pack(pady=5)

# # Label to display position
# label = tk.Label(root, text="Scroll position: ")
# label.pack()

# root.mainloop()


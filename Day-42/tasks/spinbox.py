# # 41.	Create a Spinbox from 0 to 100.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("400x300")
# tk.Label(root, text="Select a number (0–100):").pack(pady=10)
# spin=tk.Spinbox(root, from_=0, to=100)
# spin.pack()
# root.mainloop()

# # 42.	Create a Spinbox that steps by 5 (e.g., 0, 5, 10...).
# import tkinter as tk
# root = tk.Tk()
# root.geometry("400x300")
# root.title("Spinbox Step by 5")
# # Label
# tk.Label(root, text="Select a number (0–100, step 5):").pack(pady=10)
# # Spinbox with increment of 5
# spin = tk.Spinbox(root, from_=0, to=100, increment=5)
# spin.pack(pady=5)
# root.mainloop()

# # 43.	Get the value from Spinbox using a Button.
# import tkinter as tk
# def show_value():
#     value = spin.get()
#     print("Selected value:", value)
#     label.config(text=f"Selected: {value}")
# root = tk.Tk()
# root.geometry("400x300")
# root.title("Get Spinbox Value")
# # Spinbox
# spin = tk.Spinbox(root, from_=0, to=100, increment=5)
# spin.pack(pady=10)
# # Button to fetch value
# btn = tk.Button(root, text="Get Value", command=show_value)
# btn.pack(pady=5)
# # Label to display value
# label = tk.Label(root, text="Selected: ")
# label.pack(pady=5)
# root.mainloop()

# # 44.	Display Spinbox value dynamically as user changes it.
# import tkinter as tk
# def on_spin_change(*args):
#     current_value = spin_var.get()
#     label.config(text=f"Selected: {current_value}")
# root = tk.Tk()
# root.geometry("400x300")
# root.title("Dynamic Spinbox Display")
# # StringVar to track Spinbox value
# spin_var = tk.StringVar()
# # Spinbox linked to variable
# spin = tk.Spinbox(root, from_=0, to=100, increment=5, textvariable=spin_var)
# spin.pack(pady=10)
# # Label to show value
# label = tk.Label(root, text="Selected: ")
# label.pack(pady=5)
# # Trace value changes
# spin_var.trace_add("write", on_spin_change)
# root.mainloop()

# # 45.	Disable the Spinbox conditionally using a checkbox.
# import tkinter as tk
# def toggle_spinbox():
#     if check_var.get() == 1:
#         spin.config(state='disabled')
#     else:
#         spin.config(state='normal')
# root = tk.Tk()
# root.geometry("400x300")
# root.title("Disable Spinbox with Checkbox")
# # Spinbox
# spin = tk.Spinbox(root, from_=0, to=100, increment=5)
# spin.pack(pady=10)
# # Checkbox variable
# check_var = tk.IntVar()
# # Checkbox to toggle Spinbox
# checkbox = tk.Checkbutton(root, text="Disable Spinbox", variable=check_var, command=toggle_spinbox)
# checkbox.pack(pady=5)
# root.mainloop()

# # 46.	Limit Spinbox to time format (1–12) and AM/PM using two widgets.
# import tkinter as tk
# def show_time():
#     hour = hour_spin.get()
#     period = ampm_spin.get()
#     label.config(text=f"Selected Time: {hour} {period}")
# root = tk.Tk()
# root.geometry("400x300")
# root.title("Time Selector")
# # Hour Spinbox (1 to 12)
# tk.Label(root, text="Hour (1–12):").pack()
# hour_spin = tk.Spinbox(root, from_=1, to=12, width=5)
# hour_spin.pack(pady=5)
# # AM/PM Spinbox 
# tk.Label(root, text="AM / PM:").pack()
# ampm_spin = tk.Spinbox(root, values=("AM", "PM"), width=5, state="readonly")
# ampm_spin.pack(pady=5)
# # Button to display selected time
# tk.Button(root, text="Show Time", command=show_time).pack(pady=10)
# # Label to display result
# label = tk.Label(root, text="Selected Time: ")
# label.pack()
# root.mainloop()

# # 47.	Create a numeric input Spinbox for selecting Quantity (1–10).
# import tkinter as tk
# root = tk.Tk()
# root.geometry("300x200")
# root.title("Quantity Selector")
# # Label
# tk.Label(root, text="Select Quantity (1–10):").pack(pady=10)
# # Spinbox for quantity
# quantity_spin = tk.Spinbox(root, from_=1, to=10, width=5)
# quantity_spin.pack(pady=5)
# root.mainloop()

# # 48.	Use Spinbox to control canvas size dynamically.
# import tkinter as tk
# def update_canvas(*args):
#     w = int(width_var.get())
#     h = int(height_var.get())
#     canvas.config(width=w, height=h)
#     label.config(text=f"Canvas Size: {w} x {h}")
# root = tk.Tk()
# root.geometry("500x400")
# root.title("Dynamic Canvas Size Control")
# # Variables for Spinboxes
# width_var = tk.StringVar(value="200")
# height_var = tk.StringVar(value="150")
# # Spinbox for width
# tk.Label(root, text="Width:").pack()
# width_spin = tk.Spinbox(root, from_=50, to=500, increment=10, textvariable=width_var)
# width_spin.pack()
# # Spinbox for height
# tk.Label(root, text="Height:").pack()
# height_spin = tk.Spinbox(root, from_=50, to=400, increment=10, textvariable=height_var)
# height_spin.pack()
# # Canvas
# canvas = tk.Canvas(root, width=200, height=150, bg="lightblue")
# canvas.pack(pady=10)
# # Label to display current size
# label = tk.Label(root, text="Canvas Size: 200 x 150")
# label.pack()
# # Trace changes to update canvas
# width_var.trace_add("write", update_canvas)
# height_var.trace_add("write", update_canvas)
# root.mainloop()

# # 49.	Use Spinbox to control animation speed of canvas object.
# import tkinter as tk
# def move_circle():
#     global dx, delay
#     canvas.move(circle, dx, 0)
#     canvas.after(delay, move_circle)
# def update_speed(*args):
#     global delay
#     try:
#         delay = int(speed_var.get())
#     except ValueError:
#         delay = 100  # fallback if input is invalid
# root = tk.Tk()
# root.geometry("500x300")
# root.title("Control Animation Speed with Spinbox")
# # Canvas and shape
# canvas = tk.Canvas(root, width=400, height=200, bg="white")
# canvas.pack(pady=10)
# circle = canvas.create_oval(10, 80, 40, 110, fill="blue")
# # Animation variables
# dx = 5  # pixels per step
# delay = 100  # milliseconds
# speed_var = tk.StringVar(value=str(delay))
# # Spinbox to control speed
# tk.Label(root, text="Animation Delay (ms):").pack()
# speed_spin = tk.Spinbox(root, from_=10, to=1000, increment=10, textvariable=speed_var)
# speed_spin.pack()
# # Trace spinbox changes
# speed_var.trace_add("write", update_speed)
# # Start animation
# move_circle()
# root.mainloop()

# 50.	Combine Combobox + Spinbox to select “Item” and “Quantity”
import tkinter as tk
from tkinter import ttk
def show_selection():
    item = item_combo.get()
    qty = qty_spin.get()
    label.config(text=f"Selected: {qty} x {item}")
root = tk.Tk()
root.geometry("400x250")
root.title("Item and Quantity Selector")
# Combobox for item selection
tk.Label(root, text="Select Item:").pack(pady=5)
item_combo = ttk.Combobox(root, values=["Apple", "Banana", "Cherry"], state="readonly")
item_combo.current(0)
item_combo.pack(pady=5)
# Spinbox for quantity
tk.Label(root, text="Select Quantity:").pack(pady=5)
qty_spin = tk.Spinbox(root, from_=1, to=10, width=5)
qty_spin.pack(pady=5)
# Button to confirm selection
tk.Button(root, text="Confirm", command=show_selection).pack(pady=10)
# Label to display selection
label = tk.Label(root, text="Selected: ")
label.pack(pady=5)
root.mainloop()

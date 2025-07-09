# ✅ 19. Responsive Layout Demo
# Objective: Demonstrate use of pack(), grid(), place().
# Requirements:
# •	Section 1: pack() layout of 3 buttons.
# •	Section 2: grid() layout of form fields.
# •	Section 3: place() layout with absolute positioning.
# •	Use separate Frames to show all 3 layouts side by side.

import tkinter as tk

root = tk.Tk()
root.title("Responsive Layout Demo")
root.geometry("900x300")

# Section 1: pack() layout
pack_frame = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10, bg="#f0f0f0")
pack_frame.pack(side="left", fill="both", expand=True)
tk.Label(pack_frame, text="Pack Layout", font=("Arial", 12, "bold")).pack(pady=5)
tk.Button(pack_frame, text="Button A").pack(pady=5)
tk.Button(pack_frame, text="Button B").pack(pady=5)
tk.Button(pack_frame, text="Button C").pack(pady=5)

# Section 2: grid() layout
grid_frame = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10, bg="#e0f7fa")
grid_frame.pack(side="left", fill="both", expand=True)
tk.Label(grid_frame, text="Grid Layout", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=5)
tk.Label(grid_frame, text="Name:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
tk.Entry(grid_frame).grid(row=1, column=1, padx=5, pady=5)
tk.Label(grid_frame, text="Email:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
tk.Entry(grid_frame).grid(row=2, column=1, padx=5, pady=5)

# Section 3: place() layout
place_frame = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10, bg="#ffe0b2", width=300, height=250)
place_frame.pack(side="left", fill="both", expand=True)
place_frame.pack_propagate(False)
tk.Label(place_frame, text="Place Layout", font=("Arial", 12, "bold")).place(x=90, y=10)
tk.Button(place_frame, text="Top Left").place(x=10, y=50)
tk.Button(place_frame, text="Center").place(x=100, y=100)
tk.Button(place_frame, text="Bottom Right").place(x=180, y=180)

root.mainloop()

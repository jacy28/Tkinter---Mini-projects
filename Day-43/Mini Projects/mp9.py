# ✅ 9. Admin Dashboard Layout
# Objective: Create an admin panel UI layout.
# Requirements:
# •	Left Frame: navigation menu.
# •	Right Frame: content display.
# •	Menu bar: Manage > Users, Roles, Reports.
# •	Toolbar: Quick actions (Add, Edit, Delete).
# •	Open a Toplevel() window to add new user.

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Admin Dashboard")
root.geometry("800x500")

def open_add_user_window():
    win = tk.Toplevel(root)
    win.title("Add New User")
    win.geometry("300x200")

    tk.Label(win, text="Username").grid(row=0, column=0, padx=10, pady=10)
    tk.Entry(win).grid(row=0, column=1)

    tk.Label(win, text="Role").grid(row=1, column=0, padx=10, pady=10)
    tk.Entry(win).grid(row=1, column=1)

    tk.Button(win, text="Submit", command=lambda: messagebox.showinfo("Info", "User Added")).grid(row=2, columnspan=2, pady=10)

# Menu bar
menubar = tk.Menu(root)
manage_menu = tk.Menu(menubar, tearoff=0)
manage_menu.add_command(label="Users")
manage_menu.add_command(label="Roles")
manage_menu.add_command(label="Reports")
menubar.add_cascade(label="Manage", menu=manage_menu)
root.config(menu=menubar)

# Toolbar
toolbar = tk.Frame(root, bg="#ddd")
toolbar.pack(side="top", fill="x")

tk.Button(toolbar, text="Add", command=open_add_user_window).pack(side="left", padx=5, pady=5)
tk.Button(toolbar, text="Edit").pack(side="left", padx=5, pady=5)
tk.Button(toolbar, text="Delete").pack(side="left", padx=5, pady=5)

# Main layout: navigation + content
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Left frame - navigation
nav_frame = tk.Frame(main_frame, width=200, bg="#f0f0f0")
nav_frame.pack(side="left", fill="y")

tk.Label(nav_frame, text="Navigation", bg="#f0f0f0", font=('Arial', 12, 'bold')).pack(pady=10)
tk.Button(nav_frame, text="Dashboard", width=20).pack(pady=5)
tk.Button(nav_frame, text="Users", width=20).pack(pady=5)
tk.Button(nav_frame, text="Reports", width=20).pack(pady=5)

# Right frame - content area
content_frame = tk.Frame(main_frame, bg="white")
content_frame.pack(side="right", fill="both", expand=True)

tk.Label(content_frame, text="Welcome to Admin Panel", font=("Arial", 16)).pack(pady=20)

root.mainloop()

# ✅ 18. Multi-User Login Panel
# Objective: Switch between multiple users via dialog.
# Requirements:
# •	Frame with current user info.
# •	Button to “Switch User” opens a custom dialog (Toplevel()).
# •	Dialog: username selection, login button.
# •	Menu: User > Logout, Exit.

import tkinter as tk
from tkinter import messagebox

users = {
    "admin": "admin123",
    "john": "john456",
    "alice": "alice789"
}

current_user = tk.StringVar(value="Not logged in")

def switch_user_dialog():
    dialog = tk.Toplevel(root)
    dialog.title("Switch User")
    dialog.geometry("300x150")
    dialog.grab_set()

    tk.Label(dialog, text="Username:").pack(pady=5)
    username_var = tk.StringVar()
    username_menu = tk.OptionMenu(dialog, username_var, *users.keys())
    username_menu.pack()

    tk.Label(dialog, text="Password:").pack(pady=5)
    password_entry = tk.Entry(dialog, show="*")
    password_entry.pack()

    def attempt_login():
        username = username_var.get()
        password = password_entry.get()
        if users.get(username) == password:
            current_user.set(username)
            messagebox.showinfo("Success", f"Logged in as {username}")
            dialog.destroy()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    tk.Button(dialog, text="Login", command=attempt_login).pack(pady=10)

def logout():
    if current_user.get() != "Not logged in":
        confirmed = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?")
        if confirmed:
            current_user.set("Not logged in")
            messagebox.showinfo("Logged Out", "You have been logged out.")

def exit_app():
    root.quit()

root = tk.Tk()
root.title("Multi-User Login Panel")
root.geometry("350x200")

# Menu bar
menu_bar = tk.Menu(root)
user_menu = tk.Menu(menu_bar, tearoff=0)
user_menu.add_command(label="Logout", command=logout)
user_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="User", menu=user_menu)
root.config(menu=menu_bar)

# Main Frame
frame = tk.Frame(root)
frame.pack(pady=30)

tk.Label(frame, text="Current User:", font=("Arial", 12)).pack()
tk.Label(frame, textvariable=current_user, font=("Arial", 14), fg="blue").pack(pady=5)

tk.Button(root, text="Switch User", command=switch_user_dialog).pack(pady=10)

root.mainloop()

# ✅ 16. Theme Switcher App
# Objective: Toggle between Light and Dark modes.
# Requirements:
# •	Menu: View > Light / Dark Theme.
# •	Toolbar: Theme switch button.
# •	Frame layout for main content.
# •	Apply theme by changing widget styles and colors.

import tkinter as tk

def apply_theme(theme):
    colors = {
        "light": {"bg": "#ffffff", "fg": "#000000"},
        "dark": {"bg": "#2e2e2e", "fg": "#ffffff"}
    }
    current = colors[theme]
    root.config(bg=current["bg"])
    content_frame.config(bg=current["bg"])
    label.config(bg=current["bg"], fg=current["fg"])
    theme_btn.config(bg=current["bg"], fg=current["fg"], activebackground=current["bg"])

def toggle_theme():
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    apply_theme(current_theme)

root = tk.Tk()
root.title("Theme Switcher App")
root.geometry("400x300")

current_theme = "light"

# Menu
menu_bar = tk.Menu(root)
view_menu = tk.Menu(menu_bar, tearoff=0)
view_menu.add_command(label="Light Theme", command=lambda: apply_theme("light"))
view_menu.add_command(label="Dark Theme", command=lambda: apply_theme("dark"))
menu_bar.add_cascade(label="View", menu=view_menu)
root.config(menu=menu_bar)

# Toolbar
toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)
theme_btn = tk.Button(toolbar, text="Switch Theme", command=toggle_theme)
theme_btn.pack(side=tk.LEFT, padx=2, pady=2)
toolbar.pack(side=tk.TOP, fill=tk.X)

# Main content
content_frame = tk.Frame(root)
content_frame.pack(fill=tk.BOTH, expand=True)

label = tk.Label(content_frame, text="Welcome to the Theme Switcher App", font=("Arial", 14))
label.pack(pady=50)

apply_theme(current_theme)
root.mainloop()

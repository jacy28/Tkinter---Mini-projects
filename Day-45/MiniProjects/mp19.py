# 🔰 19. Resume Builder (Text + File Save)
# Goal: Fill out personal info and export resume.
# Requirements:
# •	Fields: Name, Skills, Experience.
# •	Save as .txt file.
# •	Use dialogs to select save path.

import tkinter as tk
from tkinter import filedialog, messagebox

def save_resume():
    name = name_var.get().strip()
    skills = skills_text.get("1.0", tk.END).strip()
    experience = experience_text.get("1.0", tk.END).strip()
    if not name:
        messagebox.showerror("Missing Info", "Name is required.")
        return
    content = f"Name: {name}\n\nSkills:\n{skills}\n\nExperience:\n{experience}"
    path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if path:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        messagebox.showinfo("Success", "Resume saved successfully.")

root = tk.Tk()
root.title("Resume Builder")
root.geometry("400x500")

name_var = tk.StringVar()

tk.Label(root, text="Name").pack(anchor="w", padx=10, pady=(10, 0))
tk.Entry(root, textvariable=name_var).pack(fill="x", padx=10)

tk.Label(root, text="Skills").pack(anchor="w", padx=10, pady=(10, 0))
skills_text = tk.Text(root, height=5)
skills_text.pack(fill="both", padx=10)

tk.Label(root, text="Experience").pack(anchor="w", padx=10, pady=(10, 0))
experience_text = tk.Text(root, height=10)
experience_text.pack(fill="both", padx=10)

tk.Button(root, text="Save Resume", command=save_resume).pack(pady=15)

root.mainloop()

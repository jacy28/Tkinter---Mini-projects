# 🧩 Miscellaneous
# 46. Resume Builder with Template Export
# •	Input fields: name, skills, experience, education
# •	Choose template
# •	Preview resume
# •	Export as .pdf
# •	Save draft for later editing

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
import json
import os

def export_pdf(data, template):
    filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF", "*.pdf")])
    if not filename:
        return

    c = canvas.Canvas(filename, pagesize=LETTER)
    width, height = LETTER

    y = height - 50
    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, y, data["name"])
    y -= 30

    c.setFont("Helvetica", 12)
    if template == "Modern":
        c.setFillColorRGB(0.2, 0.4, 0.6)

    for section in ["education", "experience", "skills"]:
        c.drawString(50, y, section.capitalize() + ":")
        y -= 20
        lines = data[section].split("\n")
        for line in lines:
            c.drawString(70, y, line.strip())
            y -= 15
        y -= 10

    c.save()
    messagebox.showinfo("Success", f"Resume saved as {filename}")

def save_draft(data):
    filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON", "*.json")])
    if filename:
        with open(filename, "w") as f:
            json.dump(data, f)
        messagebox.showinfo("Saved", "Draft saved successfully.")

def load_draft():
    filename = filedialog.askopenfilename(filetypes=[("JSON", "*.json")])
    if filename and os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
        name_var.set(data.get("name", ""))
        skills_text.delete("1.0", tk.END)
        skills_text.insert(tk.END, data.get("skills", ""))
        edu_text.delete("1.0", tk.END)
        edu_text.insert(tk.END, data.get("education", ""))
        exp_text.delete("1.0", tk.END)
        exp_text.insert(tk.END, data.get("experience", ""))

def preview_resume():
    preview.delete("1.0", tk.END)
    preview.insert(tk.END, f"Name: {name_var.get()}\n\n")
    preview.insert(tk.END, "Education:\n" + edu_text.get("1.0", tk.END) + "\n")
    preview.insert(tk.END, "Experience:\n" + exp_text.get("1.0", tk.END) + "\n")
    preview.insert(tk.END, "Skills:\n" + skills_text.get("1.0", tk.END))

def collect_data():
    return {
        "name": name_var.get(),
        "education": edu_text.get("1.0", tk.END).strip(),
        "experience": exp_text.get("1.0", tk.END).strip(),
        "skills": skills_text.get("1.0", tk.END).strip()
    }

# ---------- GUI ---------- #
root = tk.Tk()
root.title("Resume Builder")
root.geometry("800x600")

name_var = tk.StringVar()

tk.Label(root, text="Full Name:").grid(row=0, column=0, sticky="w")
tk.Entry(root, textvariable=name_var, width=50).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Education:").grid(row=1, column=0, sticky="nw")
edu_text = tk.Text(root, height=5, width=60)
edu_text.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Experience:").grid(row=2, column=0, sticky="nw")
exp_text = tk.Text(root, height=5, width=60)
exp_text.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Skills:").grid(row=3, column=0, sticky="nw")
skills_text = tk.Text(root, height=5, width=60)
skills_text.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Template:").grid(row=4, column=0, sticky="w")
template_var = tk.StringVar(value="Basic")
ttk.Combobox(root, textvariable=template_var, values=["Basic", "Modern"], width=20).grid(row=4, column=1, sticky="w")

tk.Button(root, text="Preview", command=preview_resume).grid(row=5, column=0, pady=10)
tk.Button(root, text="Export to PDF", command=lambda: export_pdf(collect_data(), template_var.get())).grid(row=5, column=1, sticky="w", pady=10)
tk.Button(root, text="Save Draft", command=lambda: save_draft(collect_data())).grid(row=6, column=0, pady=5)
tk.Button(root, text="Load Draft", command=load_draft).grid(row=6, column=1, sticky="w", pady=5)

tk.Label(root, text="Preview:").grid(row=7, column=0, sticky="nw")
preview = tk.Text(root, height=10, width=100, bg="#f0f0f0")
preview.grid(row=7, column=1, padx=10, pady=10)

root.mainloop()

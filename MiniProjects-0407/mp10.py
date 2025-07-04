# 10. User Profile Card Generator
# Objective: Create a visual user profile summary.
# Features:
# •	Entry fields for name, age, email.
# •	Profile card drawn on Canvas with custom shapes and text.
# •	Use .insert() and .get() to retrieve inputs.
# •	Layout using pack() in Frames

import tkinter as tk

def generate_card():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()

    canvas.delete("all")  

    canvas.create_rectangle(20, 20, 380, 180, fill="#d0f0c0", outline="#4caf50", width=2)

    canvas.create_oval(30, 40, 90, 100, fill="#81c784", outline="#388e3c")

    canvas.create_text(110, 50, anchor="nw", text=f"Name: {name}", font=("Arial", 12, "bold"))
    canvas.create_text(110, 80, anchor="nw", text=f"Age: {age}", font=("Arial", 12))
    canvas.create_text(110, 110, anchor="nw", text=f"Email: {email}", font=("Arial", 12))

root = tk.Tk()
root.title("User Profile Card Generator")
root.geometry("420x320")

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Name:").pack()
name_entry = tk.Entry(input_frame, width=30)
name_entry.pack()
name_entry.insert(0, "Christy")  

tk.Label(input_frame, text="Age:").pack()
age_entry = tk.Entry(input_frame, width=30)
age_entry.pack()
age_entry.insert(0, "25")  

tk.Label(input_frame, text="Email:").pack()
email_entry = tk.Entry(input_frame, width=30)
email_entry.pack()
email_entry.insert(0, "christy@example.com")  
generate_btn = tk.Button(root, text="Generate Card", command=generate_card)
generate_btn.pack(pady=10)

canvas_frame = tk.Frame(root)
canvas_frame.pack()
canvas = tk.Canvas(canvas_frame, width=400, height=200, bg="white")
canvas.pack()

root.mainloop()

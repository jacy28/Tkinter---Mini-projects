import tkinter as tk
from tkinter import messagebox
import re

# Email Validation 
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

def submit_form():
    name=name_entry.get()
    email=email_entry.get()
    age=age_spinbox.get()
    about=about_text.get("1.0", tk.END).strip()

    if not name or not email or not age or not about:
        messagebox.showerror("Input Error", "Please fill in all required fields.")
        return

    if not is_valid_email(email):
        messagebox.showerror("Invalid email", "Please enter valid email.")
        return
    
    result=f"Name: {name}\nEmail: {email}\nAge: {age}\nAbout: {about}"
    output_label.config(text=result)

root=tk.Tk()

root.title("Personal Information Form")
root.geometry("400x500")

frame=tk.LabelFrame(root, text="Enter your details", padx=10, pady=10)
frame.grid(row=0, column=0, padx=20, pady=20)

name_label=tk.Label(frame,text="Name:", padx=5, pady=5)
name_label.grid(row=0, column=0)
name_entry=tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1, pady=5)

email_lable=tk.Label(frame, text="Email:", padx=5, pady=5)
email_lable.grid(row=1, column=0)
email_entry=tk.Entry(frame, width=30)
email_entry.grid(row=1, column=1, pady=5)

phone_lable=tk.Label(frame, text="Phone:", padx=5, pady=5)
phone_lable.grid(row=2, column=0)
phone_entry=tk.Entry(frame, width=30)
phone_entry.grid(row=2, column=1, pady=5)

age_label=tk.Label(frame, text="Age:", padx=5, pady=5)
age_label.grid(row=3, column=0)
age_spinbox=tk.Spinbox(frame, from_=15, to=50, width=5)
age_spinbox.grid(row=3, column=1, pady=5)

about_label=tk.Label(frame, text="About You:", padx=5, pady=5)
about_label.grid(row=4, column=0)
about_text=tk.Text(frame, width=25, height=5)
about_text.grid(row=4, column=1, pady=5)

submit_btn=tk.Button(root, text="Submit", command=submit_form)
submit_btn.grid(row=1, column=0, pady=10)

output_frame=tk.Frame(root)
output_frame.grid(row=2, column=0, padx=20, pady=10)

output_label=tk.Label(output_frame, text="")
output_label.grid(row=0, column=0)

root.mainloop()


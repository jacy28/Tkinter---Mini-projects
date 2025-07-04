# 14. Feedback Form with Rating
# Objective: Collect user feedback and store/display it.
# Features:	
# •	Entry for name/email, Text for comments.
# •	Spinbox for rating (1-10).
# •	Button saves feedback to Listbox.
# •	Scrollbar for Listbox.
# •	Show thank-you message in a Label.

import tkinter as tk

def submit_feedback():
    name = name_entry.get()
    email = email_entry.get()
    comment = comment_text.get("1.0", tk.END).strip()
    rating = rating_spinbox.get()

    if name and email and comment:
        entry = f"{name} ({email}) - Rating: {rating}\nComment: {comment}"
        feedback_listbox.insert(tk.END, entry)
        thank_you_label.config(text="Thank you for your feedback!")
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        comment_text.delete("1.0", tk.END)
        rating_spinbox.delete(0, tk.END)
        rating_spinbox.insert(0, 5)
    else:
        thank_you_label.config(text="Please fill all fields.")

root = tk.Tk()
root.title("Feedback Form")
root.geometry("450x450")

form_frame = tk.Frame(root)
form_frame.pack(pady=10)

tk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(form_frame, text="Email:").grid(row=1, column=0, sticky="w")
email_entry = tk.Entry(form_frame, width=30)
email_entry.grid(row=1, column=1, pady=5)

tk.Label(form_frame, text="Comments:").grid(row=2, column=0, sticky="nw")
comment_text = tk.Text(form_frame, width=30, height=5)
comment_text.grid(row=2, column=1, pady=5)

tk.Label(form_frame, text="Rating (1-10):").grid(row=3, column=0, sticky="w")
rating_spinbox = tk.Spinbox(form_frame, from_=1, to=10, width=5)
rating_spinbox.grid(row=3, column=1, sticky="w")
rating_spinbox.delete(0, tk.END)
rating_spinbox.insert(0, 5)

submit_btn = tk.Button(root, text="Submit Feedback", command=submit_feedback)
submit_btn.pack(pady=10)

thank_you_label = tk.Label(root, text="", fg="green")
thank_you_label.pack()

list_frame = tk.Frame(root)
list_frame.pack(pady=10)

feedback_listbox = tk.Listbox(list_frame, width=60, height=10)
feedback_listbox.pack(side="left", fill="y")

scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=feedback_listbox.yview)
scrollbar.pack(side="right", fill="y")
feedback_listbox.config(yscrollcommand=scrollbar.set)

root.mainloop()

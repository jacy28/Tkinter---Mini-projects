# import sqlite3
# import tkinter as tk
# from tkinter import messagebox, filedialog
# import csv

# # 16.	Connect to a SQLite database and create a table named students with name, age, and grade.
# def init_db():
#     conn = sqlite3.connect("students.db")
#     c = conn.cursor()
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS students (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             age INTEGER,
#             grade TEXT,
# 30.	Prevent duplicate email insertions using UNIQUE constraints.
#             email TEXT UNIQUE,
#             gpa REAL
#         )
#     """)
#     conn.commit()
#     return conn, c

# conn, cur = init_db()

# # 18.	On clicking “Save”, insert the values into the SQLite database.
# def save_record():
#     try:
#         cur.execute("INSERT INTO students (name, age, grade, email, gpa) VALUES (?, ?, ?, ?, ?)",
#                     (name_var.get(), age_var.get(), grade_var.get(), email_var.get(), gpa_var.get()))
#         conn.commit()

# # 19.	After saving, display “Record Saved!” in a Label.
#         status_label.config(text="Record Saved!", fg="green")
#         clear_fields()
#         view_all()
#     except sqlite3.IntegrityError as e:
#         messagebox.showerror("Error", str(e))

# # 20.	Add a “View All” button to fetch and show all records in a Text or Listbox.
# def view_all():
#     student_list.delete(0, tk.END)
#     cur.execute("SELECT name, age, grade FROM students")
#     rows = cur.fetchall()
#     for row in rows:
#         student_list.insert(tk.END, row)
#     update_count()

# # 21.	Add a Clear button to clear all fields.
# def clear_fields():
#     name_var.set("")
#     age_var.set("")
#     grade_var.set("")
#     email_var.set("")
#     gpa_var.set("")
#     status_label.config(text="")

# # 22.	Create a form with Update and Delete buttons for student records.
# # 33.	Show messagebox confirmation before deleting a record.
# def delete_record():
#     if messagebox.askyesno("Confirm", "Delete this record?"):
#         cur.execute("DELETE FROM students WHERE name=?", (name_var.get(),))
#         conn.commit()
#         clear_fields()
#         view_all()

# def update_record():
#     cur.execute("UPDATE students SET age=?, grade=?, email=?, gpa=? WHERE name=?",
#                 (age_var.get(), grade_var.get(), email_var.get(), gpa_var.get(), name_var.get()))
#     conn.commit()
#     status_label.config(text="Record Updated", fg="blue")
#     view_all()

# # 27.	Show the selected record details in entry fields for editing.
# def show_selected(event):
#     selected = student_list.get(tk.ANCHOR)
#     cur.execute("SELECT * FROM students WHERE name=?", (selected[0],))
#     record = cur.fetchone()
#     if record:
#         name_var.set(record[1])
#         age_var.set(record[2])
#         grade_var.set(record[3])
#         email_var.set(record[4])
#         gpa_var.set(record[5])

# # 24.	Add a search function to find students by name using LIKE.
# def search_name():
#     student_list.delete(0, tk.END)
#     keyword = search_var.get()
#     cur.execute("SELECT name, age, grade FROM students WHERE name LIKE ?", ('%' + keyword + '%',))
#     rows = cur.fetchall()
#     for row in rows:
#         student_list.insert(tk.END, row)

# # 25.	Display total student count from the database in a Label.
# def update_count():
#     cur.execute("SELECT COUNT(*) FROM students")
#     count = cur.fetchone()[0]
#     count_label.config(text=f"Total Students: {count}")

# # 26.	Insert dummy data using a loop and display it in a scrollable Listbox.
# def add_dummy():
#     for i in range(5):
#         try:
#             cur.execute("INSERT INTO students (name, age, grade, email, gpa) VALUES (?, ?, ?, ?, ?)",
#                         (f"Dummy{i}", 20+i, "A", f"dummy{i}@mail.com", 4.0))
#         except:
#             continue
#     conn.commit()
#     view_all()

# # 34.	Export all records to a .txt file from the database using File Dialog.
# def export_txt():
#     file = filedialog.asksaveasfilename(defaultextension=".txt")
#     cur.execute("SELECT * FROM students")
#     rows = cur.fetchall()
#     with open(file, "w") as f:
#         for row in rows:
#             f.write(str(row) + "\n")
#     messagebox.showinfo("Exported", "Data exported to text file.")

# # 35.	Import student records from a .csv and store them in the SQLite table.
# def import_csv():
#     file = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
#     with open(file, newline='') as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             try:
#                 cur.execute("INSERT INTO students (name, age, grade, email, gpa) VALUES (?, ?, ?, ?, ?)",
#                             (row['name'], row['age'], row['grade'], row['email'], row['gpa']))
#             except:
#                 continue
#     conn.commit()
#     view_all()

# root = tk.Tk()
# root.title("Student Records")
# root.geometry("700x600")

# name_var = tk.StringVar()
# age_var = tk.StringVar()
# grade_var = tk.StringVar()
# email_var = tk.StringVar()
# gpa_var = tk.StringVar()
# search_var = tk.StringVar()

# tk.Label(root, text="Name").grid(row=0, column=0)
# tk.Entry(root, textvariable=name_var).grid(row=0, column=1)

# tk.Label(root, text="Age").grid(row=1, column=0)
# tk.Entry(root, textvariable=age_var).grid(row=1, column=1)

# tk.Label(root, text="Grade").grid(row=2, column=0)
# tk.Entry(root, textvariable=grade_var).grid(row=2, column=1)

# tk.Label(root, text="Email").grid(row=3, column=0)
# tk.Entry(root, textvariable=email_var).grid(row=3, column=1)

# tk.Label(root, text="GPA").grid(row=4, column=0)
# tk.Entry(root, textvariable=gpa_var).grid(row=4, column=1)

# tk.Button(root, text="Save", command=save_record).grid(row=5, column=0, pady=5)
# tk.Button(root, text="Update", command=update_record).grid(row=5, column=1)
# tk.Button(root, text="Delete", command=delete_record).grid(row=5, column=2)
# tk.Button(root, text="Clear", command=clear_fields).grid(row=5, column=3)

# student_list = tk.Listbox(root, width=60)
# student_list.grid(row=6, column=0, columnspan=4, pady=10)
# student_list.bind("<<ListboxSelect>>", show_selected)

# tk.Entry(root, textvariable=search_var).grid(row=7, column=0)
# tk.Button(root, text="Search", command=search_name).grid(row=7, column=1)
# tk.Button(root, text="View All", command=view_all).grid(row=7, column=2)
# tk.Button(root, text="Add Dummy", command=add_dummy).grid(row=7, column=3)

# tk.Button(root, text="Export TXT", command=export_txt).grid(row=8, column=0)
# tk.Button(root, text="Import CSV", command=import_csv).grid(row=8, column=1)

# count_label = tk.Label(root, text="Total Students: 0", fg="blue")
# count_label.grid(row=9, column=0, columnspan=2)

# status_label = tk.Label(root, text="", fg="green")
# status_label.grid(row=10, column=0, columnspan=4)

# view_all()
# root.mainloop()

# # 28.	Create a login system (username, password) using SQLite authentication.
# def create_login_table():
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL
#         )
#     """)
#     conn.commit()

# def register_user():
#     username = username_var.get()
#     password = password_var.get()
#     if username and password:
#         try:
#             cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
#             conn.commit()
#             messagebox.showinfo("Success", "User registered.")
#         except sqlite3.IntegrityError:
# 29.	Show error if username already exists (validate before insert).
#             messagebox.showerror("Error", "Username already exists.")
#     else:
#         messagebox.showwarning("Missing", "Enter username and password.")

# def login_user():
#     username = username_var.get()
#     password = password_var.get()
#     cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
#     result = cur.fetchone()
#     if result:
#         messagebox.showinfo("Login Success", f"Welcome {username}")
#         login_frame.pack_forget()
#         main_frame.pack()
#     else:
#         messagebox.showerror("Login Failed", "Invalid credentials.")

# # 31.	Create a real-time GPA calculator that stores results in SQLite.
# def calculate_gpa():
#     try:
#         scores = list(map(float, gpa_input_var.get().split(",")))  # Ex: "3.0,3.5,4.0"
#         gpa = round(sum(scores) / len(scores), 2)
#         gpa_var.set(gpa)
#         messagebox.showinfo("GPA", f"Calculated GPA: {gpa}")
#     except:
#         messagebox.showerror("Error", "Invalid input. Enter comma-separated numbers.")

# # 32.	Build a feedback form with rating and comment fields and store them in DB.
# def create_feedback_table():
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS feedback (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             rating INTEGER,
#             comment TEXT
#         )
#     """)
#     conn.commit()

# def submit_feedback():
#     rating = feedback_rating.get()
#     comment = feedback_comment.get()
#     if rating:
#         cur.execute("INSERT INTO feedback (rating, comment) VALUES (?, ?)", (rating, comment))
#         conn.commit()
#         messagebox.showinfo("Thanks!", "Feedback submitted.")
#         feedback_rating.set("")
#         feedback_comment.set("")

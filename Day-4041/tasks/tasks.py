# # 1.	Create a Tkinter window with three labels stacked vertically using pack().
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# name_label=tk.Label(root, text="Name:")
# name_label.pack(pady=10)
# email_label=tk.Label(root, text="Email:")
# email_label.pack(pady=10)
# phone_label=tk.Label(root, text="Phone no:")
# phone_label.pack(pady=10)
# root.mainloop()

# # 2.	Create a horizontal layout using pack(side="left") for three buttons.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# btn1=tk.Button(root, text="Button1")
# btn1.pack(side="left", padx=5)
# btn2=tk.Button(root, text="Button2")
# btn2.pack(side="left", padx=5)
# btn3=tk.Button(root, text="Button3")
# btn3.pack(side="left", padx=5)
# root.mainloop()

# # 3.	Build a login form with two labels and two entry fields using grid().
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# name_label=tk.Label(root, text="User Name:")
# name_label.grid(row=0, column=0, padx=5, pady=5)
# name_entry=tk.Entry(root)
# name_entry.grid(row=0, column=1, padx=5, pady=5)
# pw_label=tk.Label(root, text="Password:")
# pw_label.grid(row=1, column=0, padx=5, pady=5)
# pw_entry=tk.Entry(root)
# pw_entry.grid(row=1, column=1, padx=5, pady=5)
# root.mainloop()

# # 4.	Design a 3x3 button matrix using grid() (like a calculator layout).
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# frame=tk.Frame(root)
# frame.grid(row=0, column=0, padx=10, pady=10)
# buttons=[
#     ("1", 0, 0), ("2", 0, 1), ("3", 0, 2),
#     ("4", 1, 0), ("5", 1, 1), ("6", 1, 2),
#     ("7", 2, 0), ("8", 2, 1), ("9", 2, 2)
# ]
# for text, row, col in buttons:
#     btn=tk.Button(frame, text=text, width=10, height=3)
#     btn.grid(row=row, column=col, padx=5, pady=5)
# root.mainloop()

# # 5.	Use grid(sticky='E') to align a label to the right.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# name_label=tk.Label(root, text="Name:")
# name_label.grid(row=0, column=0, sticky="E", pady=10)
# email_label=tk.Label(root, text="Email:")
# email_label.grid(row=1, column=0, sticky="E", pady=10)
# phone_label=tk.Label(root, text="Phone no:")
# phone_label.grid(row=2, column=0, sticky="E", pady=10)
# root.mainloop()

# # 6.	Create a window where one label uses place() at (50, 50), and another at the center using relx and rely.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# name_label=tk.Label(root, text="Name:")
# name_label.place(x=50, y=50)
# email_label=tk.Label(root, text="Email:")
# email_label.place(relx=0.5, rely=0.5, anchor="center")
# root.mainloop()

# # 7.	Combine pack() for the title and grid() for form layout (demonstrate mixed geometry error).
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# root.title("Combine Pack and Grid")
# title=tk.Label(root, text="Form")
# title.pack(padx=10, pady=10)
# name_label=tk.Label(root, text="Name:")
# name_label.grid(row=0, column=0, padx=5, pady=5)
# name_entry=tk.Entry(root)
# name_entry.grid(row=0, column=1, padx=5, pady=5)
# email_label=tk.Label(root, text="Email:")
# email_label.grid(row=1, column=0, pady=5, padx=5)
# email_entry=tk.Entry(root)
# email_entry.grid(row=1, column=2, padx=5, pady=5)
# btn=tk.Button(root, text="Submit")
# btn.grid(row=2, padx=5, pady=5)
# root.mainloop()
# TclErrror


# # 8.	Make a form using grid() and add padding using padx and pady.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# name_label=tk.Label(root, text="Name:")
# name_label.grid(row=0, column=0, padx=5, pady=10)
# name_entry=tk.Entry(root)
# name_entry.grid(row=0, column=1, padx=5, pady=10)
# email_label=tk.Label(root, text="Email:")
# email_label.grid(row=1, column=0, pady=5, padx=10)
# email_entry=tk.Entry(root)
# email_entry.grid(row=1, column=1, padx=5, pady=10)
# btn=tk.Button(root, text="Submit")
# btn.grid(row=2, column=1, pady=15)
# root.mainloop()

# # 9.	Create a form with place() to precisely position username, password, and login button.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# name_label=tk.Label(root, text="User Name:")
# name_label.place(x=50, y=20)
# name_entry=tk.Entry(root)
# name_entry.place(x=150, y=20)
# pw_label=tk.Label(root, text="Password:")
# pw_label.place(x=50, y=60)
# pw_entry=tk.Entry(root)
# pw_entry.place(x=150, y=60)
# btn=tk.Button(root, text="Submit")
# btn.place(x=150, y=100)
# root.mainloop()

# # 10.	Create a sidebar layout using pack(side="left", fill="y") and main content area using pack(fill="both", expand=True).
# import tkinter as tk
# root = tk.Tk()
# root.geometry("500x300")
# root.title("Sidebar Layout")
# sidebar = tk.Frame(root, bg="lightgray", width=120)
# sidebar.pack(side="left", fill="y")
# sidebar.pack_propagate(False)
# sidebar_label=tk.Label(sidebar, text="Sidebar", bg="lightgray")
# sidebar_label.pack(pady=10)
# btn1=tk.Button(sidebar, text="Dashboard")
# btn1.pack(fill="x", padx=10, pady=5)
# btn2=tk.Button(sidebar, text="Settings")
# btn2.pack(fill="x", padx=10, pady=5)
# main_content = tk.Frame(root, bg="white")
# main_content.pack(side="left", fill="both", expand=True)
# tk.Label(main_content, text="Main content example", bg="white", font=("Arial", 14)).pack(pady=20)
# root.mainloop()

# 🧩 Section 2: Event Handling (Button, Keyboard, Mouse)
# # 11.	Create a button that prints a message when clicked.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def print_message():
#     print("Button Clicked!")
# btn=tk.Button(root, text="Print", command=print_message)
# btn.pack(padx=10, pady=10)
# root.mainloop()

# # 12.	Bind a keyboard event to the root window to print the key pressed.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def key_pressed(event):
#     print("Key Pressed:", event.char)
# root.bind("<Key>", key_pressed)
# root.mainloop()

# # 13.	Bind a mouse click event to a label that changes its text on click.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def change_text(event):
#     label.config(text="Changed Text.")
# label=tk.Label(root, text="Original text")
# label.pack(padx=10, pady=10)  
# label.bind("<Button-1>", change_text)
# root.mainloop()

# # 14.	Create a button that changes the background color of the window.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def change_bg():
#     root.config(bg="red")
# btn=tk.Button(root, text="Change", command=change_bg)
# btn.pack(padx=10, pady=10)
# root.mainloop()

# # 15.	Create an Entry field and a button to display the entered text using command=.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def display_text():
#     entered_text=entry.get()
#     label.config(text=entered_text)
# entry=tk.Entry(root)
# entry.pack(padx=10, pady=10)
# label=tk.Label(root, text="Display")
# label.pack(padx=10, pady=10)
# btn=tk.Button(root, text="Click", command=display_text)
# btn.pack(padx=10, pady=10)
# root.mainloop()

# # 16.	Create a button that opens a message box when clicked.
# import tkinter as tk
# from tkinter import messagebox
# root=tk.Tk()
# root.geometry("300x300")
# def open_msg():
#     messagebox.showinfo("open", "Opens messagebox when button is clicked.")
# btn=tk.Button(root, text="Click", command=open_msg)
# btn.pack(padx=10, pady=10)
# root.mainloop()

# # 17.	Create an entry widget that triggers an event when Enter key is pressed (<Return>).
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def key_pressed(event):
#     text=entry.get()
#     print("You Entered:", text)
# entry=tk.Entry(root)
# entry.pack(padx=10, pady=10)
# entry.bind("<Return>", key_pressed)
# root.mainloop()

# # 18.	Bind the arrow keys (<Up>, <Down>) to update a label with the direction.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def update_direction(event):
#     if event.keysym=="Up":
#         label.config(text="Up arrow pressed.")
#     elif event.keysym=="Down":
#         label.config(text="Down arrow pressed.")
# label=tk.Label(root, text="Press an arrow")
# label.pack(padx=10, pady=10)
# root.bind("<Up>", update_direction)
# root.bind("<Down>", update_direction)
# root.mainloop()

# # 19.	Track and display mouse position using <Motion> event.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def mouse_position(event):
#     x, y=event.x, event.y
#     label.config(text=f"Mouse coordinates: {x}, {y}")
# label=tk.Label(root, text="Display mouse position")
# label.pack(padx=10, pady=10)
# root.bind("<Motion>", mouse_position)
# root.mainloop()

# # 20.	Change button text on hover using <Enter> and <Leave> events.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def on_enter(event):
#     btn.config(text="Changed Button")
# def on_leave(event):
#     btn.config(text="Hover Me")
# btn=tk.Button(root, text="Hover Me")
# btn.pack(padx=10, pady=10)
# btn.bind("<Enter>", on_enter)
# btn.bind("<Leave>", on_leave)
# root.mainloop()

# # 21.	Create a window with a fixed size of 400x300 using geometry() and resizable(False, False).
# import tkinter as tk
# root=tk.Tk()
# root.geometry("400x300")
# root.resizable(False, False)
# root.mainloop()

# # 22.	Change the title of the window to “My First GUI App”.
# import tkinter as tk
# root=tk.Tk()
# root.title("My First GUI App")
# root.geometry("400x300")
# root.mainloop()

# # 23.	Set a custom icon for the window (use .ico file).
# import tkinter as tk
# root=tk.Tk()
# root.title("My First GUI App")
# root.geometry("400x300")
# root.iconbitmap("icon.ico")
# root.mainloop()

# # 24.	Create a window at position (200, 100) using geometry("300x200+200+100").
# import tkinter as tk
# root=tk.Tk()
# root.title("My First GUI App")
# root.geometry("300x200+200+100")
# root.mainloop()

# # 25.	Display the current window width and height dynamically using a Label.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def display_size(event):
#     width=root.winfo_width()
#     height=root.winfo_height()
#     label.config(text=f"Width: {width}, Height: {height}")
# label=tk.Label(root, text="")
# label.pack(padx=10, pady=10)
# root.bind("<Configure>", display_size)
# root.mainloop()

# # 26.	Disable only horizontal resizing (resizable(False, True)).
# import tkinter as tk
# root=tk.Tk()
# root.geometry("400x300")
# root.resizable(False, True)
# root.mainloop()

# 27.	Create a resizable notepad-style window using Text widget with dynamic resizing.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("400x300")
# root.resizable(False, False)
# root.mainloop()

# # 28.	Create a centered window on screen by calculating screen width and height.
# import tkinter as tk
# root=tk.Tk()
# window_width=400
# window_height=300
# screen_width=root.winfo_screenwidth()
# screen_height=root.winfo_screenheight()
# x=(screen_width // 2)-(window_width // 2)
# y=(screen_height // 2)-(window_height // 2)
# root.geometry(f"{window_width}x{window_height}+{x}+{y}")
# root.mainloop()

# # 29.	Make a splash screen that disappears after 3 seconds.
# import tkinter as tk
# splash=tk.Tk()
# splash.title("Splash Screen")
# splash_width=300
# splash_height=200
# screen_width=splash.winfo_screenwidth()
# screen_height=splash.winfo_screenheight()
# x=(screen_width // 2)-(splash_width // 2)
# y=(screen_height // 2)-(splash_height // 2)
# splash.geometry(f"{splash_width}x{splash_height}+{x}+{y}")
# splash.overrideredirect(True)
# label=tk.Label(splash, text="Splash label")
# label.pack(expand=True)
# splash.after(2000, splash.destroy)
# splash.mainloop()
# root=tk.Tk()
# root.title("Main App")
# root.geometry("400x300")
# label=tk.Label(root, text="Main label")
# label.pack(expand=True)
# root.mainloop()

# # 30.	Create a window that opens in maximized mode using zoomed state if on Windows.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("400x300")
# root.state("zoomed")
# root.mainloop()

# # 31.	Create a form with name, email Entry widgets and a submit button.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("400x300")
# name_label=tk.Label(root, text="Name:")
# name_label.grid(row=0, column=0, padx=10, pady=20)
# name_entry=tk.Entry(root)
# name_entry.grid(row=0, column=1, padx=10, pady=20)
# email_label=tk.Label(root, text="Email:")
# email_label.grid(row=1, column=0, padx=10, pady=20)
# email_entry=tk.Entry(root)
# email_entry.grid(row=1, column=1, padx=10, pady=20)
# btn=tk.Button(root, text="Submit")
# btn.grid(row=2, column=1, padx=10, pady=20)
# root.mainloop()

# # 32.	Retrieve and print the name and email entered by the user.
# import tkinter as tk
# from tkinter import messagebox
# root=tk.Tk()
# root.geometry("400x300")
# def submit_form():
#     name=name_entry.get()
#     email=email_entry.get()
#     messagebox.showinfo("Form Submitted",f"Name: {name}\nEmail: {email}")
# name_label=tk.Label(root, text="Name:")
# name_label.grid(row=0, column=0, padx=10, pady=20)
# name_entry=tk.Entry(root)
# name_entry.grid(row=0, column=1, padx=10, pady=20)
# email_label=tk.Label(root, text="Email:")
# email_label.grid(row=1, column=0, padx=10, pady=20)
# email_entry=tk.Entry(root)
# email_entry.grid(row=1, column=1, padx=10, pady=20)
# btn=tk.Button(root, text="Submit", command=submit_form)
# btn.grid(row=2, column=1, padx=10, pady=20)
# root.mainloop()

# # 33.	Use insert() to pre-fill an entry with "Enter Name".
# import tkinter as tk
# from tkinter import messagebox
# root=tk.Tk()
# root.geometry("400x300")
# name_entry=tk.Entry(root)
# name_entry.pack(pady=30)
# name_entry.insert(0, "Enter Name:")
# root.mainloop()

# # 34.	Use delete() to clear the Entry field on button click.
# import tkinter as tk
# from tkinter import messagebox
# root=tk.Tk()
# root.geometry("400x300")
# def submit_form():
#     name=name_entry.get()
#     email=email_entry.get()
#     messagebox.showinfo("Form Submitted",f"Name: {name}\nEmail: {email}")
#     name_entry.delete(0, tk.END)
#     email_entry.delete(0, tk.END)
# name_label=tk.Label(root, text="Name:")
# name_label.grid(row=0, column=0, padx=10, pady=20)
# name_entry=tk.Entry(root)
# name_entry.grid(row=0, column=1, padx=10, pady=20)
# email_label=tk.Label(root, text="Email:")
# email_label.grid(row=1, column=0, padx=10, pady=20)
# email_entry=tk.Entry(root)
# email_entry.grid(row=1, column=1, padx=10, pady=20)
# btn=tk.Button(root, text="Submit", command=submit_form)
# btn.grid(row=2, column=1, padx=10, pady=20)
# root.mainloop()

# # 35.	Validate if the name field is not empty before submitting.
# def validate_name():
#     name = name_entry.get()
#     if not name.strip():
#         messagebox.showerror("Error", "Please enter the name.")
#         return False
#     return True
# def submit_form():
#     if not validate_name():
#         return 

# # 36.	Validate email format using regex (as in your example).
# import tkinter as tk
# import re
# from tkinter import messagebox
# root=tk.Tk()
# root.geometry("400x300")
# def validate_email(email):
#     regex=r'^[\w\.-]+@[\w\.-]+\.\w+$'
#     return re.match(regex, email)
# def submit_form():
#     email=email_entry.get()
#     if validate_email(email):
#        messagebox.showinfo("Submitted", f"Form submitted successfully. Email: {email}")
#     else:
#         messagebox.showerror("Invalid Email", "Please enter a valid email address.")
# email_label=tk.Label(root, text="Email:")
# email_label.grid(row=0, column=0, padx=10, pady=20)
# email_entry=tk.Entry(root)
# email_entry.grid(row=0, column=1, padx=10, pady=20)
# btn=tk.Button(root, text="Submit", command=submit_form)
# btn.grid(row=1, column=1, padx=10, pady=20)
# root.mainloop()

# # 37.	Create a password entry field with show="*".
# import tkinter as tk
# root=tk.Tk()
# root.geometry("400x300")
# pw_label=tk.Label(root, text="Password:")
# pw_label.grid(row=0, column=0, padx=10, pady=20)
# pw_entry=tk.Entry(root, show="*")
# pw_entry.grid(row=0, column=1, padx=10, pady=20)
# root.mainloop()

# # 38.	Create a login form and print “Login Success” if username and password match predefined values.
# import tkinter as tk
# from tkinter import messagebox
# root=tk.Tk()
# root.geometry("400x300")
# valid_username="admin"
# valid_pw="1234"
# def login():
#     username=name_entry.get()
#     pw=pw_entry.get()
#     if username==valid_username and pw==valid_pw:
#         messagebox.showinfo("Login", "Login Success.")
#     else:
#         messagebox.showerror("Login failed", "Invalid username & password.")
# name_label=tk.Label(root, text="User Name:")
# name_label.grid(row=0, column=0, padx=10, pady=20)
# name_entry=tk.Entry(root)
# name_entry.grid(row=0, column=1, padx=10, pady=20)
# pw_label=tk.Label(root, text="Password:")
# pw_label.grid(row=1, column=0, padx=10, pady=20)
# pw_entry=tk.Entry(root, show="*")
# pw_entry.grid(row=1, column=1, padx=10, pady=20)
# btn=tk.Button(root, text="Submit", command=login)
# btn.grid(row=2, column=1, padx=10, pady=20)
# root.mainloop()

# # 39.	Display a warning message if the email is invalid or empty.
# import tkinter as tk
# import re
# from tkinter import messagebox
# root=tk.Tk()
# root.geometry("400x300")
# def validate_email(email):
#     regex=r'^[\w\.-]+@[\w\.-]+\.\w+$'
#     return re.match(regex, email)
# def submit_form():
#     email=email_entry.get()
#     if not email.strip():  
#         messagebox.showerror("Invalid Email", "Email field cannot be empty.")
#     elif not validate_email(email):
#         messagebox.showerror("Invalid Email", "Please enter a valid email address.")
#     else:
#         messagebox.showinfo("Submitted", f"Form submitted successfully.\nEmail: {email}")
# email_label=tk.Label(root, text="Email:")
# email_label.grid(row=0, column=0, padx=10, pady=20)
# email_entry=tk.Entry(root)
# email_entry.grid(row=0, column=1, padx=10, pady=20)
# btn=tk.Button(root, text="Submit", command=submit_form)
# btn.grid(row=1, column=1, padx=10, pady=20)
# root.mainloop()

# # 40.	Allow only numeric input using regex validation.
# import tkinter as tk
# import re
# root=tk.Tk()
# root.geometry("400x300")
# def is_numeric(input):
#     return re.fullmatch(r'\d*', input) is not None
# vcmd=root.register(is_numeric)
# entry = tk.Entry(root, validate="key", validatecommand=(vcmd, '%P'))
# entry.pack(pady=40)
# root.mainloop()


# # 41.	Create a Text widget for notes and a button to save content to a file.
# import tkinter as tk
# from tkinter import messagebox
# root=tk.Tk()
# root.geometry("400x300")
# def save_content():
#     content=text.get("1.0", tk.END).strip()
#     if content:
#         try:
#             with open("notes.txt","w") as file:
#                 file.write(content)
#             messagebox.showinfo("Saved", "File saved successfully.")
#         except Exception as e:
#             messagebox.showerror("Error", "File not saved.")
#     else:
#         messagebox.showerror("Empty", "Nothing to save!")
# text=tk.Text(root, width=30, height=5)
# text.pack(expand=True)
# btn=tk.Button(root, text="Save", command=save_content)
# btn.pack(padx=30, pady=20)
# root.mainloop()

# # 42.	Insert a sample paragraph into the Text widget using insert().
# import tkinter as tk
# root = tk.Tk()
# root.geometry("400x300")
# text = tk.Text(root,wrap="word", width=40, height=10)
# text.pack(pady=20)
# paragraph = "This is the sample paragraph entered into the text widget."
# text.insert("1.0", paragraph)
# root.mainloop()

# # 43.	Use get() to print the entire content of the Text widget.
# import tkinter as tk
# root = tk.Tk()
# root.geometry("400x300")
# def print_text():
#     content=text.get("1.0", tk.END)
#     print(f"Content:\n{content}")
# text = tk.Text(root,wrap="word", width=40, height=10)
# text.pack(pady=20)
# btn = tk.Button(root, text="Print Text", command=print_text)
# btn.pack(pady=10)
# root.mainloop()

# # 44.	Clear the Text content on button click using delete().
# import tkinter as tk
# root = tk.Tk()
# root.geometry("400x300")
# def clear_text():
#     text.delete("1.0", tk.END)
# text = tk.Text(root,wrap="word", width=40, height=10)
# text.pack(pady=20)
# btn = tk.Button(root, text="Clear Text", command=clear_text)
# btn.pack(pady=10)
# root.mainloop()

# # 45.	Display the number of characters or words typed in the Text widget.
# import tkinter as tk
# root = tk.Tk()
# root.geometry("400x300")
# def count_char():
#     content=text.get("1.0", tk.END).strip()
#     count_char=len(content)
#     print(f"Words Count: {count_char}")
# text = tk.Text(root,wrap="word", width=40, height=10)
# text.pack(pady=20)
# btn = tk.Button(root, text="Count", command=count_char)
# btn.pack(pady=10)
# root.mainloop()

# # 46.	Add a scrollbar to the Text widget for easier navigation.
# import tkinter as tk
# root = tk.Tk()
# root.geometry("400x300")
# frame = tk.Frame(root)
# frame.pack(padx=10, pady=10, fill="both", expand=True)
# text = tk.Text(frame, wrap="word")
# text.pack(side="left", fill="both", expand=True)
# scrollbar = tk.Scrollbar(frame, command=text.yview)
# scrollbar.pack(side="right", fill="y")
# text.config(yscrollcommand=scrollbar.set)
# root.mainloop()

# # 47.	Auto-save the Text widget content every 5 seconds using after().
# import tkinter as tk
# import time
# root = tk.Tk()
# root.geometry("400x300")
# def auto_save():
#     content=text.get("1.0", tk.END).strip()
#     with open("autosave.txt", "w") as file:
#         file.write(content)
#     print(f"Autosaved at {time.strftime('%H:%M:%S')}")
#     root.after(5000, auto_save)
# text = tk.Text(root,wrap="word", width=40, height=10)
# text.pack(pady=20)
# auto_save()
# root.mainloop()

# # 48.	Highlight specific keywords in the Text widget using tags.
# import tkinter as tk
# root = tk.Tk()
# root.geometry("400x300")
# text = tk.Text(root, wrap="word", width=40, height=10)
# text.pack(pady=20)
# sample = "Python is powerful. Tkinter makes GUI easy. Python is fun."
# text.insert("1.0", sample)
# def highlight():
#     text.tag_remove("highlight", "1.0", tk.END)
#     keyword = "Python"
#     start = "1.0"
#     while True:
#         pos = text.search(keyword, start, stopindex=tk.END)
#         if not pos:
#             break
#         end = f"{pos}+{len(keyword)}c"
#         text.tag_add("highlight", pos, end)
#         start = end
#     text.tag_config("highlight", background="yellow", foreground="black")
# btn = tk.Button(root, text="Highlight 'Python'", command=highlight)
# btn.pack(pady=10)
# root.mainloop()

# # 49.	Load text from a file and display it in the Text widget.
# import tkinter as tk
# from tkinter import filedialog
# root=tk.Tk()
# root.geometry("400x300")
# def load_file():
#     file_path=filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
#     if file_path:
#         with open(file_path, "r", encoding="utf-8") as file:
#             content=file.read()
#             text.delete("1.0", tk.END)
#             text.insert("1.0", content)
# text=tk.Text(root, wrap="word", width=30, height=5)
# text.pack(padx=10, pady=20)
# btn=tk.Button(root, text="Load File", command=load_file)
# btn.pack(padx=30, pady=20)
# root.mainloop()

# 50.	Create a mini diary app with Text widget input and date-based saving.
import tkinter as tk
from datetime import datetime
root = tk.Tk()
root.geometry("400x300")
root.title("Mini Diary App")
text = tk.Text(root, wrap="word", width=40, height=10)
text.pack(pady=20)
def save_entry():
    date = datetime.now().strftime("%Y-%m-%d")
    filename = f"diary_{date}.txt"
    content = text.get("1.0", tk.END).strip()
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
btn = tk.Button(root, text="Save Entry", command=save_entry)
btn.pack(pady=10)
root.mainloop()


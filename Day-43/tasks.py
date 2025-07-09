# # 🔷 Section 1: Frames (Tasks 1–15)
# # 1.	Create a Frame widget and place a label inside it.
# import tkinter as tk
# root=tk.Tk()
# frame=tk.Frame(root)
# frame.pack()
# label=tk.Label(frame, text="Label inside frame")
# label.pack(pady=20)
# root.mainloop()

# # 2.	Add three Buttons inside a Frame using pack().
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# frame=tk.Frame(root)
# frame.pack(pady=20)
# btn1=tk.Button(frame, text="Button-1")
# btn1.pack(pady=20)
# btn2=tk.Button(frame, text="Button-2")
# btn2.pack(pady=20)
# btn3=tk.Button(frame, text="Button-3")
# btn3.pack(pady=20)
# root.mainloop()

# # 3.	Add a Label, Entry, and Button inside a Frame using grid().
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# frame=tk.Frame(root)
# frame.grid(row=0, column=0, padx=5, pady=5)
# label=tk.Label(frame, text="Sample")
# label.grid(row=0, column=0, padx=5, pady=5)
# entry=tk.Entry(frame)
# entry.grid(row=0, column=1, padx=5, pady=5)
# button=tk.Button(frame, text="Click")
# button.grid(row=1, column=1, padx=5, pady=5)
# root.mainloop()

# # 4.	Nest a Frame inside another Frame.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# outer_frame=tk.Frame(root, bg="green", width=200, height=200)
# outer_frame.pack()
# outer_frame.pack_propagate(False)
# inner_frame=tk.Frame(outer_frame, bg="red", width=150, height=150)
# inner_frame.pack()
# root.mainloop()

# # 5.	Set the background color and fixed size of a Frame.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# frame=tk.Frame(root, bg="green", width=200, height=200)
# frame.pack()
# root.mainloop()

# 6.	Use pack_propagate(False) and test resizing behavior.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# frame=tk.Frame(root, bg="green", width=200, height=200)
# frame.pack()
# frame.pack_propagate(False)
# root.mainloop()


# # 7.	Create multiple frames (header, content, footer).
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# header_frame=tk.Frame(root, bg="green", width=200, height=200)
# header_frame.pack()
# header_label=tk.Frame(header_frame, bg="green")
# header_label.pack()
# content_frame=tk.Frame(root, bg="green", width=200, height=200)
# content_frame.pack()
# content_label=tk.Frame(content_frame, bg="white")
# content_label.pack()
# footer_frame=tk.Frame(root, bg="black", width=200, height=200)
# footer_frame.pack()
# footer_label=tk.Frame(footer_frame, bg="black")
# footer_label.pack()
# root.mainloop()


# # 8.	Align multiple frames horizontally using pack(side="left").
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# header_frame=tk.Frame(root, bg="green", width=200, height=200)
# header_frame.pack(side="left")
# header_frame.pack_propagate(False)
# content_frame=tk.Frame(root, bg="lightblue", width=200, height=200)
# content_frame.pack(side="left")
# content_frame.pack_propagate(False)
# footer_frame=tk.Frame(root, bg="black", width=200, height=200)
# footer_frame.pack(side="left")
# footer_frame.pack_propagate(False)
# root.mainloop()

# # 9.	Create a left sidebar Frame for navigation buttons.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("500x500")
# sidebar=tk.Frame(root, bg="lightgray", width=150)
# sidebar.pack(side="left", fill="y")
# sidebar.pack_propagate(False)
# nav1=tk.Button(sidebar, text="Home")
# nav1.pack(fill="x", padx=10, pady=10)
# nav2=tk.Button(sidebar, text="About")
# nav2.pack(fill="x", padx=10, pady=10)
# nav3=tk.Button(sidebar, text="Contact")
# nav3.pack(fill="x", padx=10, pady=10)
# main=tk.Frame(root)
# main.pack(side="left", expand=True, fill="both")
# label=tk.Label(main, text="Main Content")
# label.pack(pady=20)
# root.mainloop()

# # 10.	Add form fields in one frame and result display in another.
# import tkinter as tk
# def display_result():
#     name = name_entry.get()
#     age = age_entry.get()
#     result_label.config(text=f"Name: {name}, Age: {age}")
# root = tk.Tk()
# root.title("Task 10 - Form and Result")
# root.geometry("400x250")
# form_frame = tk.Frame(root, bg="lightyellow")
# form_frame.pack(pady=20)
# tk.Label(form_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
# name_entry = tk.Entry(form_frame)
# name_entry.grid(row=0, column=1, padx=5, pady=5)
# tk.Label(form_frame, text="Age:").grid(row=1, column=0, padx=5, pady=5)
# age_entry = tk.Entry(form_frame)
# age_entry.grid(row=1, column=1, padx=5, pady=5)
# submit_btn = tk.Button(form_frame, text="Submit", command=display_result)
# submit_btn.grid(row=2, column=0, columnspan=2, pady=10)
# result_frame = tk.Frame(root, bg="lightblue", height=50)
# result_frame.pack(fill="x")
# result_label = tk.Label(result_frame, text="Result will appear here.")
# result_label.pack(pady=10)
# root.mainloop()


# # 11.	Combine pack() and grid() using different frames.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# main_frame=tk.Frame(root)
# main_frame.pack(padx=10, pady=10)
# pack_frame=tk.Frame(main_frame)
# pack_frame.pack()
# pack_label=tk.Label(pack_frame, text="Pack Example")
# pack_label.pack(padx=10, pady=10)
# grid_frame=tk.Frame(main_frame)
# grid_frame.grid(row=1, column=0, padx=10, pady=10)
# grid_label=tk.Label(grid_frame, text="Grid Example")
# grid_label.grid(row=0, column=0, padx=10, pady=10)
# root.mainloop()

# # 12.	Use Frame to create a login form layout.
# import tkinter as tk
# from tkinter import messagebox
# root=tk.Tk()
# root.geometry("300x300")
# USER_NAME="admin"
# PASSWORD="1234"
# def login():
#     name=name_entry.get()
#     password=password_entry.get()
#     if not name or not password:
#         messagebox.showerror("Error", "Please fill all fields.")
#         return
#     if name==USER_NAME and password==PASSWORD:
#         messagebox.showinfo("Success", "Login successfully.")
#     else:
#         messagebox.showerror("Login Falied", "Invalid username & password.")
# form_frame=tk.Frame(root)
# form_frame.grid(row=0, column=0, padx=5, pady=5)
# tk.Label(form_frame, text="User Name:").grid(row=0, column=0, padx=5, pady=5)
# name_entry=tk.Entry(form_frame)
# name_entry.grid(row=0, column=1, padx=5, pady=5)
# tk.Label(form_frame, text="Password:").grid(row=1, column=0, padx=5, pady=5)
# password_entry=tk.Entry(form_frame)
# password_entry.grid(row=1, column=1)
# btn=tk.Button(form_frame, text="Login", command=login)
# btn.grid(row=2, column=0, columnspan=2, pady=10)
# root.mainloop()


# # 13.	Use Frame to group widgets by section (personal info vs contact info).
# import tkinter as tk
# root = tk.Tk()
# root.geometry("400x300")
# personal_frame = tk.LabelFrame(root, text="Personal Information", padx=10, pady=10)
# personal_frame.pack(padx=10, pady=10, fill="x")
# tk.Label(personal_frame, text="First Name:").grid(row=0, column=0, sticky="w")
# tk.Entry(personal_frame).grid(row=0, column=1)
# tk.Label(personal_frame, text="Last Name:").grid(row=1, column=0, sticky="w")
# tk.Entry(personal_frame).grid(row=1, column=1)
# contact_frame = tk.LabelFrame(root, text="Contact Information", padx=10, pady=10)
# contact_frame.pack(padx=10, pady=10, fill="x")
# tk.Label(contact_frame, text="Email:").grid(row=0, column=0, sticky="w")
# tk.Entry(contact_frame).grid(row=0, column=1)
# tk.Label(contact_frame, text="Phone:").grid(row=1, column=0, sticky="w")
# tk.Entry(contact_frame).grid(row=1, column=1)
# root.mainloop()


# # 14.	Style a Frame with borders, padding, and relief.
# import tkinter as tk
# root = tk.Tk()
# root.geometry("400x300")
# frame=tk.Frame(root, borderwidth=5, bg="green", relief="groove", padx=10, pady=10,  width=250, height=150 )
# frame.pack(padx=10, pady=10)
# frame.pack_propagate(False)
# tk.Label(frame, text="Styled Frame ex").pack(padx=10, pady=10)
# root.mainloop()

# # 15.	Place a Frame at a specific location using place().
# import tkinter as tk
# root = tk.Tk()
# root.geometry("400x300")
# root.title("Place Frame")
# place_frame = tk.Frame(root, bg="lightblue", width=150, height=100)
# place_frame.place(x=100, y=80)  
# tk.Label(place_frame, text="Placed Frame", bg="lightblue").place(relx=0.5, rely=0.5, anchor="center")
# root.mainloop()

# # 16.	Create a horizontal PanedWindow with two frames.
# import tkinter as tk
# root = tk.Tk()
# root.geometry("400x200")
# root.title("Horizontal PanedWindow")
# pane = tk.PanedWindow(root, orient=tk.HORIZONTAL)
# pane.pack(fill=tk.BOTH, expand=1)
# left = tk.Frame(pane, bg="lightblue", width=150, height=200)
# right = tk.Frame(pane, bg="lightgreen", width=250, height=200)
# pane.add(left)
# pane.add(right)
# root.mainloop()


# # 17.	Create a vertical PanedWindow with a text area and a form.
# import tkinter as tk
# root = tk.Tk()
# root.geometry("400x300")
# root.title("Vertical PanedWindow")
# pane = tk.PanedWindow(root, orient=tk.VERTICAL)
# pane.pack(fill=tk.BOTH, expand=True)
# text = tk.Text(pane, height=5)
# pane.add(text)
# form_frame = tk.Frame(pane)
# tk.Label(form_frame, text="Name:").grid(row=0, column=0)
# tk.Entry(form_frame).grid(row=0, column=1)
# pane.add(form_frame)
# root.mainloop()


# # 18.	Add a Label on each side of the PanedWindow.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("400x300")
# pane=tk.PanedWindow(root, orient=tk.HORIZONTAL)
# pane.pack(fill=tk.BOTH, expand=True)
# left=tk.Label(pane, text="Left label", bg="skyblue")
# right=tk.Label(pane, text="Right label", bg="lightcoral")
# pane.add(left)
# pane.add(right)
# root.mainloop()

# # 19.	Embed a scrollable Text widget inside one PanedWindow pane.
# import tkinter as tk
# root = tk.Tk()
# root.geometry("400x300")
# pane = tk.PanedWindow(root)
# pane.pack(fill=tk.BOTH, expand=True)
# text_frame = tk.Frame(pane)
# scroll = tk.Scrollbar(text_frame)
# text = tk.Text(text_frame, yscrollcommand=scroll.set)
# scroll.config(command=text.yview)
# scroll.pack(side=tk.RIGHT, fill=tk.Y)
# text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
# label=tk.Label(pane, text="Other Pane")
# pane.add(text_frame)
# pane.add(label)
# root.mainloop()


# # 20.	Allow user to resize a drawing area (Canvas) using PanedWindow.
# import tkinter as tk
# root = tk.Tk()
# root.geometry("500x300")
# pane = tk.PanedWindow(root)
# pane.pack(fill=tk.BOTH, expand=True)
# canvas = tk.Canvas(pane, bg="white")
# pane.add(canvas)
# controls = tk.Frame(pane)
# tk.Button(controls, text="Draw").pack(pady=10)
# pane.add(controls)
# root.mainloop()


# # 21.	Split the window into 3 resizable panes using nested PanedWindows.
# import tkinter as tk
# root = tk.Tk()
# root.geometry("600x300")
# main_pane = tk.PanedWindow(root, orient=tk.HORIZONTAL)
# main_pane.pack(fill=tk.BOTH, expand=True)
# left = tk.Label(main_pane, text="Left", bg="lightblue", width=100)
# main_pane.add(left)
# middle_pane = tk.PanedWindow(main_pane, orient=tk.VERTICAL)
# top = tk.Label(middle_pane, text="Top-Mid", bg="lightgreen")
# bottom = tk.Label(middle_pane, text="Bottom-Mid", bg="lightyellow")
# middle_pane.add(top)
# middle_pane.add(bottom)
# main_pane.add(middle_pane)
# right = tk.Label(main_pane, text="Right", bg="salmon", width=100)
# main_pane.add(right)
# root.mainloop()


# # 22.	Add a resizable file explorer pane on the left.
# import tkinter as tk
# root = tk.Tk()
# root.geometry("500x300")
# pane = tk.PanedWindow(root, orient=tk.HORIZONTAL)
# pane.pack(fill=tk.BOTH, expand=True)
# file_explorer = tk.Listbox(pane)
# file_explorer.insert(0, "File 1", "File 2", "File 3")
# pane.add(file_explorer)
# preview = tk.Text(pane)
# pane.add(preview)
# root.mainloop()


# # 23.	Use different background colors in each pane.
# import tkinter as tk
# root = tk.Tk()
# root.geometry("400x200")
# pane = tk.PanedWindow(root, orient=tk.HORIZONTAL)
# pane.pack(fill=tk.BOTH, expand=True)
# pane.add(tk.Label(pane, text="Red", bg="red", width=20))
# pane.add(tk.Label(pane, text="Green", bg="green", width=20))
# pane.add(tk.Label(pane, text="Blue", bg="blue", fg="white", width=20))
# root.mainloop()


# # 24.	Add widgets like Entry, Listbox, or Canvas to different panes.
# import tkinter as tk
# root = tk.Tk()
# root.geometry("500x300")
# pane = tk.PanedWindow(root)
# pane.pack(fill=tk.BOTH, expand=True)
# entry = tk.Entry(pane)
# listbox = tk.Listbox(pane)
# canvas = tk.Canvas(pane, bg="white")
# pane.add(entry)
# pane.add(listbox)
# pane.add(canvas)
# root.mainloop()

# # 25.	Combine Frame and PanedWindow to build a 3-column layout.
# import tkinter as tk
# root = tk.Tk()
# root.geometry("600x300")
# root.title("3-Column Layout")
# pane = tk.PanedWindow(root, orient=tk.HORIZONTAL)
# pane.pack(fill=tk.BOTH, expand=True)
# left_frame = tk.Frame(pane, bg="lightgray", width=150)
# middle_frame = tk.Frame(pane, bg="white", width=300)
# right_frame = tk.Frame(pane, bg="lightblue", width=150)
# pane.add(left_frame)
# pane.add(middle_frame)
# pane.add(right_frame)
# tk.Label(left_frame, text="Left Sidebar").pack(pady=10)
# tk.Label(middle_frame, text="Main Content").pack(pady=10)
# tk.Label(right_frame, text="Right Panel").pack(pady=10)
# root.mainloop()

# # 26.	Create a basic Menu bar with File and Edit menus.
# import tkinter as tk
# root = tk.Tk()
# root.title("Menu Example")
# root.geometry("400x300")
# menubar = tk.Menu(root)
# file_menu = tk.Menu(menubar, tearoff=0)
# edit_menu = tk.Menu(menubar, tearoff=0)
# menubar.add_cascade(label="File", menu=file_menu)
# menubar.add_cascade(label="Edit", menu=edit_menu)
# root.config(menu=menubar)
# root.mainloop()


# 27.	Add an “Open” command to the File menu that prints to console.
# def open_file():
#     print("Open selected")
# file_menu.add_command(label="Open", command=open_file)

# 28.	Add an “Exit” option to close the window using root.quit().
# file_menu.add_command(label="Exit", command=root.quit)

# 29.	Add a separator between menu items.
# file_menu.insert_separator(1)  

# # 30.	Create a Help menu with “About” dialog using messagebox.showinfo().
# from tkinter import messagebox
# help_menu = tk.Menu(menubar, tearoff=0)
# help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Tkinter Menu Example"))
# menubar.add_cascade(label="Help", menu=help_menu)

# 31.	Use add_cascade() to attach a submenu to the main menu.
# menubar.add_cascade(label="File", menu=file_menu)

# 32.	Add multiple submenus (File → New, Open, Save).
# file_menu.delete(0, tk.END)  
# file_menu.add_command(label="New", command=lambda: print("New File"))
# file_menu.add_command(label="Open", command=open_file)
# file_menu.add_command(label="Save", command=lambda: print("Save File"))
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)

# 33.	Bind keyboard shortcuts (e.g., Ctrl+O for Open).
# root.bind('<Control-o>', lambda event: open_file())

# 34.	Disable a menu item (e.g., “Save” initially).
# file_menu.entryconfig("Save", state="disabled")

# 35.	Dynamically update menu contents at runtime (e.g., recent files).
# recent_files = ["project1.txt", "report.docx", "notes.md"]
# def update_recent_menu():
#     recent_menu.delete(0, tk.END)
#     for f in recent_files:
#         recent_menu.add_command(label=f, command=lambda file=f: print("Opening", file))
# recent_menu = tk.Menu(file_menu, tearoff=0)
# file_menu.add_cascade(label="Recent Files", menu=recent_menu)
# update_recent_menu()

# # 36.	Create a toolbar at the top of the window using Frame.
# import tkinter as tk
# root = tk.Tk()
# root.title("Toolbar Example")
# root.geometry("400x300")
# toolbar = tk.Frame(root, bg="lightgray")
# toolbar.pack(side="top", fill="x")
# root.mainloop()

# 37.	Add "Open" and "Save" Buttons with icons or text.
# open_btn = tk.Button(toolbar, text="Open")
# open_btn.pack(padx=2, pady=2)
# save_btn = tk.Button(toolbar, text="Save")
# save_btn.pack(padx=2, pady=2)

# 38.	Align buttons horizontally using pack(side=LEFT).
# open_btn = tk.Button(toolbar, text="Open")
# open_btn.pack(side="left", padx=2, pady=2)
# save_btn = tk.Button(toolbar, text="Save")
# save_btn.pack(side="left", padx=2, pady=2)

# 39.	Create a toolbar with Buttons that perform different actions.
# def open_file():
#     print("Opening file...")
# def save_file():
#     print("Saving file...")
# open_btn.config(command=open_file)
# save_btn.config(command=save_file)


# 40.	Hide and show the toolbar dynamically with a toggle button.
# def toggle_toolbar():
#     if toolbar.winfo_ismapped():
#         toolbar.pack_forget()
#         toggle_btn.config(text="Show Toolbar")
#     else:
#         toolbar.pack(side="top", fill="x")
#         toggle_btn.config(text="Hide Toolbar")
# toggle_btn = tk.Button(root, text="Hide Toolbar", command=toggle_toolbar)
# toggle_btn.pack(pady=10)

# # 41.	Use messagebox.showinfo() to display an info message.
# import tkinter as tk
# from tkinter import messagebox
# def show_info():
#     messagebox.showinfo("Info", "This is an information message.")
# root = tk.Tk()
# tk.Button(root, text="Show Info", command=show_info).pack(pady=10)
# root.mainloop()

# # 42.	Use messagebox.askokcancel() to confirm closing the app.
# import tkinter as tk
# from tkinter import messagebox
# def on_closing():
#     if messagebox.askokcancel("Quit", "Do you really want to quit?"):
#         root.destroy()
# root = tk.Tk()
# root.protocol("WM_DELETE_WINDOW", on_closing)
# root.mainloop()


# # 43.	Use messagebox.askquestion() for yes/no confirmation.
# import tkinter as tk
# from tkinter import messagebox
# root=tk.Tk()
# def confirm_delete():
#     result = messagebox.askquestion("Delete", "Are you sure you want to delete this?")
#     if result == 'yes':
#         print("Deleted.")
#     else:
#         print("Cancelled.")
# tk.Button(root, text="Delete", command=confirm_delete).pack(pady=10)
# root.mainloop()

# 44.	Create a button that triggers showwarning().
# def warn_user():
#     messagebox.showwarning("Warning", "This action may be risky!")

# tk.Button(root, text="Show Warning", command=warn_user).pack(pady=10)


# 45.	Use a dialog to confirm data submission in a form.
# def submit_form():
#     name = entry.get()
#     if not name:
#         messagebox.showerror("Error", "Name cannot be empty.")
#         return
#     if messagebox.askokcancel("Confirm", f"Submit name: {name}?"):
#         messagebox.showinfo("Submitted", "Form submitted successfully!")

# tk.Label(root, text="Enter Name:").pack()
# entry = tk.Entry(root)
# entry.pack()
# tk.Button(root, text="Submit", command=submit_form).pack(pady=10)

# 46.	Create a Toplevel() custom dialog for name input.
# import tkinter as tk
# def open_name_dialog():
#     dialog = tk.Toplevel(root)
#     dialog.title("Enter Name")
#     dialog.geometry("250x100")
#     tk.Label(dialog, text="Name:").pack(pady=5)
#     tk.Entry(dialog).pack(pady=5)
#     tk.Button(dialog, text="Close", command=dialog.destroy).pack(pady=5)
# root = tk.Tk()
# tk.Button(root, text="Open Name Dialog", command=open_name_dialog).pack(pady=20)
# root.mainloop()

# # 47.	Pass data from a dialog back to the main window.
# import tkinter as tk
# def open_dialog():
#     def submit():
#         user_name = entry.get()
#         name_label.config(text=f"Name: {user_name}")
#         dialog.destroy()
#     dialog = tk.Toplevel(root)
#     tk.Label(dialog, text="Enter your name:").pack()
#     entry = tk.Entry(dialog)
#     entry.pack()
#     tk.Button(dialog, text="Submit", command=submit).pack()
# root = tk.Tk()
# name_label = tk.Label(root, text="Name: ")
# name_label.pack(pady=10)
# tk.Button(root, text="Enter Name", command=open_dialog).pack()
# root.mainloop()

# # 48.	Add a submit and cancel button to the dialog.
# import tkinter as tk
# def open_dialog():
#     def submit():
#         name_label.config(text=f"Name: {entry.get()}")
#         dialog.destroy()
#     def cancel():
#         dialog.destroy()
#     dialog = tk.Toplevel(root)
#     tk.Label(dialog, text="Enter Name:").pack()
#     entry = tk.Entry(dialog)
#     entry.pack(pady=5)
#     btn_frame = tk.Frame(dialog)
#     btn_frame.pack(pady=5)
#     tk.Button(btn_frame, text="Submit", command=submit).pack(side="left", padx=5)
#     tk.Button(btn_frame, text="Cancel", command=cancel).pack(side="left", padx=5)
# root = tk.Tk()
# name_label = tk.Label(root, text="Name: ")
# name_label.pack(pady=10)
# tk.Button(root, text="Open Dialog", command=open_dialog).pack()
# root.mainloop()


# # 49.	Center the dialog window using geometry().
# import tkinter as tk
# def center_dialog(win, w=250, h=100):
#     screen_w = win.winfo_screenwidth()
#     screen_h = win.winfo_screenheight()
#     x = (screen_w // 2) - (w // 2)
#     y = (screen_h // 2) - (h // 2)
#     win.geometry(f"{w}x{h}+{x}+{y}")
# def open_dialog():
#     dialog = tk.Toplevel(root)
#     dialog.title("Centered Dialog")
#     center_dialog(dialog, 300, 120)
#     tk.Label(dialog, text="This dialog is centered").pack(pady=20)
#     tk.Button(dialog, text="Close", command=dialog.destroy).pack()
# root = tk.Tk()
# tk.Button(root, text="Open Centered Dialog", command=open_dialog).pack(pady=20)
# root.mainloop()

# # 50.	Open a custom dialog that validates email before accepting.
# import tkinter as tk
# import re
# from tkinter import messagebox
# def is_valid_email(email):
#     return re.match(r"[^@]+@[^@]+\.[^@]+", email)
# def open_email_dialog():
#     def submit():
#         email = entry.get()
#         if is_valid_email(email):
#             email_label.config(text=f"Email: {email}")
#             dialog.destroy()
#         else:
#             messagebox.showerror("Invalid Email", "Please enter a valid email address.")
#     dialog = tk.Toplevel(root)
#     dialog.title("Enter Email")
#     tk.Label(dialog, text="Email:").pack()
#     entry = tk.Entry(dialog)
#     entry.pack(pady=5)
#     tk.Button(dialog, text="Submit", command=submit).pack(pady=5)
# root = tk.Tk()
# email_label = tk.Label(root, text="Email:")
# email_label.pack(pady=10)
# tk.Button(root, text="Enter Email", command=open_email_dialog).pack()
# root.mainloop()



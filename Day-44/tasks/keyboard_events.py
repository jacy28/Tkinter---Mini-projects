# # 26.	Bind <KeyPress> to the main window and log the pressed key.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def key_pressed(event):
#     print("Key Pressed:", event.char)
# root.bind("<KeyPress>", key_pressed)
# root.mainloop()

# # 27.	Show key name (event.keysym) in a Label when any key is pressed.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def show_keyname(event):
#     label.config(text=f"Key Pressed: {event.keysym}")
# label=tk.Label(root, text="")
# label.pack(padx=10, pady=10)
# root.bind("<KeyPress>", show_keyname)
# root.mainloop()

# # 28.	Create a login form where pressing Enter (<Return>) submits the form.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def submit(event=None):
#     username=name_entry.get()
#     password=pw_entry.get()
#     if not username or not password:
#         print("Please enter Username & Password.")
#         return
#     else:
#         print("Login Successfully.")
# name_label=tk.Label(root, text="User Name:")
# name_label.grid(row=0, column=0, padx=5, pady=10)
# name_entry=tk.Entry(root)
# name_entry.grid(row=0, column=1, padx=5, pady=10)
# pw_label=tk.Label(root, text="Password:")
# pw_label.grid(row=1, column=0, padx=5, pady=10)
# pw_entry=tk.Entry(root)
# pw_entry.grid(row=1, column=1, padx=5, pady=10)
# btn=tk.Button(root, text="Submit", command=submit)
# btn.grid(row=2, column=1, pady=20)
# root.bind("<Return>", submit)
# root.mainloop()

# # 29.	Use arrow key bindings (<Left>, <Right>) to move a shape on a canvas.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# canvas=tk.Canvas(root, width=300, height=300, bg="white")
# canvas.pack(pady=20)
# shape=canvas.create_oval(140, 140, 160, 160, fill="red")
# def move_shape(event):
#     if event.keysym=="Left":
#         canvas.move(shape, 0, -10)
#     elif event.keysym=="Right":
#         canvas.move(shape, 0, 10)
# root.bind("<Left>", move_shape)
# root.bind("<Right>", move_shape)
# root.mainloop()

# # 30.	Bind a key to toggle background color (B = black, W = white).
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def toggle_bg(event):
#     key=event.keysym.lower()
#     if key=="b":
#         root.config(bg="black")
#     elif key=="w":
#         root.config(bg="white")
# root.bind("<Key>", toggle_bg)
# root.mainloop()

# # 31.	Use <KeyRelease> to track when a specific key (like Shift) is released.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def key_released(event):
#     print("Key Released:", event.keysym)
# root.bind("<KeyRelease>", key_released)
# root.mainloop()

# # 32.	Pressing Esc closes the application (root.destroy()).
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# root.bind("<Escape>", lambda event: root.destroy())
# root.mainloop()

# # 33.	Bind Ctrl+S (<Control-s>) to simulate saving.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def save(event=None):
#     print("Data Saved!")
# root.bind("<Control-s>", save)
# root.mainloop()

# # 34.	Use function keys (e.g., <F1>) to display help in a dialog.
# import tkinter as tk
# from tkinter import messagebox
# root = tk.Tk()
# root.geometry("300x300")
# def show_help(event=None):
#     messagebox.showinfo("Help", "This is a help dialog. Press F1 anytime!")
# root.bind("<F1>", show_help)
# label = tk.Label(root, text="Press F1 for help", font=("Arial", 14))
# label.pack(padx=10, pady=10)
# root.mainloop()

# # 35.	Build a text entry that capitalizes all characters typed using key bindings.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# entry=tk.Entry(root)
# entry.pack(padx=10, pady=10)
# def capital_text(event):
#     if event.char.isprintable():
#         entry.insert("insert", event.char.upper())
#         return "break"
# root.bind("<KeyPress>", capital_text)
# root.mainloop() 
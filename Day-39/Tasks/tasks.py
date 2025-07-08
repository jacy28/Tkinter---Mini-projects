# 1.	Check Tkinter Installation:
# Write a Python script to import Tkinter and confirm it’s installed without errors.
# import tkinter 


# # 2.	Create a Basic Window:
# # Create a Tkinter window with a title and a specific size.
# import tkinter as tk
# root=tk.Tk()
# root.title("Basic Window")
# root.geometry("300x300")
# root.mainloop()


# # 3.	Change Window Title:
# # Modify your window’s title to something different.
# import tkinter as tk
# root=tk.Tk()
# root.title("Basic Window")
# root.geometry("300x300")
# def change_title():
#     root.title("Tkinter Window")
# root.after(2000, change_title)
# root.mainloop()


# # 4.	Resize the Window:
# # Adjust the window size using .geometry().
# import tkinter as tk
# root=tk.Tk()
# root.title("Basic Window")
# root.geometry("300x300")
# def change_size():
#     root.geometry("500x400")
# button=tk.Button(root, text="Resize window", command=change_size)
# button.pack(padx=10, pady=10)
# root.mainloop()


# 5.	Add a Label Widget:
# Place a label widget in the window that displays “Welcome to Tkinter!”.
# import tkinter as tk
# root=tk.Tk()
# root.title("Tkinter Window")
# root.geometry("300x300")
# label=tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 12))
# label.pack(padx=30, pady=30)
# root.mainloop()

# # 6. Add an Entry Widget:
# # Add a single-line text entry box beneath your label.
# import tkinter as tk
# root=tk.Tk()
# root.title("Tkinter Window")
# root.geometry("300x300")
# label=tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 12))
# label.pack(padx=30, pady=30)
# entry=tk.Entry(root)
# entry.pack()
# root.mainloop()


# # 7.	Add a Button Widget:
# # Add a button that does nothing when clicked (for now).
# import tkinter as tk
# root=tk.Tk()
# root.title("Tkinter Window")
# root.geometry("300x300")
# button=tk.Button(root, text="Click")
# button.pack()
# root.mainloop()

# # 8.	Get Text from Entry:
# # Write a function that retrieves text from the entry widget.
# import tkinter as tk
# root=tk.Tk()
# root.title("Tkinter Window")
# root.geometry("300x300")
# entry=tk.Entry(root)
# entry.pack(padx=30, pady=30)
# def get_text():
#     user_input=entry.get()
#     print(f"You typed: {user_input}")
# button=tk.Button(root, text="Get Text", command=get_text)
# button.pack()
# root.mainloop()


# # 9.	Update Label Text:
# # Use a button to update the label’s text with whatever is typed in the entry box.
# import tkinter as tk
# root=tk.Tk()
# root.title("Tkinter Window")
# root.geometry("300x300")
# label=tk.Label(root, text="Hello, Tkinter!", pady=20, font=12)
# label.pack()
# entry=tk.Entry(root)
# entry.pack(padx=30, pady=30)
# def update_label():
#     user_input=entry.get()
#     label.config(text=f"Hello, {user_input}")
# button=tk.Button(root, text="Update Label", command=update_label)
# button.pack()
# root.mainloop()


# # 10.	Create a Multi-line Text Widget:
# # Add a Text widget to your window for multi-line input.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# text=tk.Text(root, height=5, width=25)
# text.pack(pady=20)
# root.mainloop()

# # 11.	Read from Text Widget:
# # Write a function to extract and print the contents of the Text widget.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# text=tk.Text(root, height=5, width=25)
# text.pack(pady=20)
# def print_content():
#     content=text.get("1.0", tk.END).strip()
#     print("Content:", content)
# button=tk.Button(root, text="Print text", command=print_content)
# button.pack()
# root.mainloop()


# # 12.	Experiment with pack():
# # Arrange three different widgets vertically using the pack() layout manager.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# label=tk.Label(root, text="Sample experiment using pack.")
# label.pack(pady=20)
# entry=tk.Entry(root)
# entry.pack(pady=20)
# button=tk.Button(root, text="Click Me")
# button.pack(pady=20)
# root.mainloop()

# # 13.	Experiment with grid():
# # Arrange a label and an entry widget side by side using grid().
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# label=tk.Label(root, text="Name:")
# label.grid(row=0, column=0, padx=20, pady=20)
# entry=tk.Entry(root)
# entry.grid(row=0, column=1)
# root.mainloop()


# # 14.	Experiment with place():
# # Position a button at coordinates (100, 50) using place().
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# button=tk.Button(root, text="Cick Me")
# button.place(x=100, y=50)
# root.mainloop()


# # 15.	Mix Layout Managers (pack and grid):
# # Try to use pack() and grid() in the same frame and observe what happens.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# frame=tk.Frame(root)
# frame.pack(padx=10, pady=10)
# btn1=tk.Button(frame, text="Pack Btn")
# btn1.pack()
# btn2=tk.Button(frame, text="Grid Btn")
# btn2.grid(row=0, column=0)
# root.mainloop()
# Got an ERROR: _tkinter.TclError: cannot use geometry manager grid inside .!frame which already has slaves managed by pack


# # 16.	Create a Frame Widget:
# # Add a frame to your main window.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# frame=tk.Frame(root)
# frame.pack(padx=10, pady=10)
# root.mainloop()

# # 17.	Add Widgets to Frame:
# # Place at least two widgets inside the frame.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# frame=tk.Frame(root)
# frame.pack(padx=10, pady=10)
# label=tk.Label(frame, text="Inside Frame")
# label.pack()
# btn=tk.Button(frame, text="Click Me", pady=10)
# btn.pack()
# root.mainloop()

# # 18.	Multiple Frames:
# # Create two frames and add different widgets to each.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# frame1=tk.Frame(root, bg="lightblue", width=200, height=100)
# frame1.pack(padx=10, pady=10)
# frame1.pack_propagate(False)
# label=tk.Label(frame1, text="Inside Frame")
# label.pack()
# frame2=tk.Frame(root, bg="red", width=200, height=100)
# frame2.pack(padx=10, pady=10)
# frame2.pack_propagate(False)
# btn=tk.Button(frame2, text="Click Me", pady=10)
# btn.pack()
# root.mainloop()


# # 19.	Label Font and Color:
# # Change the font size and foreground color of a label.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# label=tk.Label(root, text="Hello, Tkinter!", font=14, fg="red")   # fg ---- text color
# label.pack()
# root.mainloop()

# # 20.	Button Command:
# # Make the button print a message to the console when clicked.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def print_msg():
#     print("Welcome to Tkinter!")
# btn=tk.Button(root, text="print", command=print_msg)
# btn.pack(pady=30)
# root.mainloop()


# # 21.	Disable/Enable Button:
# # Add a checkbox that enables or disables the button.
# import tkinter as tk
# root=tk.Tk()
# root.title("Disable/Enable Button")
# root.geometry("300x300")
# def toggle_btn():
#     if var.get()==1:
#         btn.config(state="normal")
#     else:
#         btn.config(state="disabled")
# var=tk.IntVar()
# checkBtn=tk.Checkbutton(root, text="Enable button", variable=var, command=toggle_btn)
# checkBtn.pack(pady=10)
# btn=tk.Button(root, text="Click me", state="disabled")
# btn.pack(pady=10)
# root.mainloop()


# # 22.	Set Default Entry Text:
# # Pre-fill the entry widget with default text.
# import tkinter as tk
# root=tk.Tk()
# root.title("Default Entry Text")
# root.geometry("300x300")
# entry=tk.Entry(root)
# entry.pack()
# entry.insert(0, "Enter your name")
# root.mainloop()

# # 23.	Clear Entry/Text Widget:
# # Add a button that clears the entry or text widget contents.
# import tkinter as tk
# root=tk.Tk()
# root.title("Default Entry Text")
# root.geometry("300x300")
# entry=tk.Entry(root)
# entry.pack()
# entry.insert(0, "Enter your name")
# def clear_entry():
#     entry.delete(0, tk.END)
# btn=tk.Button(root, text="Clear Entry", command=clear_entry)
# btn.pack(pady=10)
# root.mainloop()


# # 24.	Window Icon:
# # Change the window icon (if on a supported OS).
# import tkinter as tk
# root=tk.Tk()
# root.title("Window icon")
# root.geometry("300x300")
# root.iconbitmap("icon.ico")
# root.mainloop()

# # 25.	Window Resizability:
# # Set the window to be non-resizable.
# import tkinter as tk
# root=tk.Tk()
# root.title("Window Resizability")
# root.geometry("300x300")
# root.resizable(False, False)
# root.mainloop()

# # 26.	Custom Window Size on Startup:
# # Start the window maximized or minimized.
# import tkinter as tk
# root=tk.Tk()
# root.title("Custom Window Size")
# root.state("zoomed")
# root.mainloop()

# # 27.	Label with Image:
# # Add an image to a label widget.
# import tkinter as tk
# from PIL import Image, ImageTk
# root=tk.Tk()
# root.title("Label with Image")
# image=Image.open("cherry.png")
# photo=ImageTk.PhotoImage(image)
# label=tk.Label(root, image=photo)
# label.pack(pady=20)
# label.image=photo
# root.mainloop()

# # 28.	Entry Validation:
# # Use .get() and logic to restrict entry to numbers only.
# import tkinter as tk
# from tkinter import messagebox
# root=tk.Tk()
# root.geometry("300x300")
# entry=tk.Entry(root)
# entry.pack()
# def validate():
#     value=entry.get()
#     if value.isdigit():
#         messagebox.showinfo("Success", f"Valid number: {value}")
#     else:
#         messagebox.showerror("Error", "Please enter numbers only.")
# btn=tk.Button(root, text="Validate", command=validate)
# btn.pack(pady=20)
# root.mainloop()

# # 29.	Button with Keyboard Shortcut:
# # Bind a keyboard shortcut (e.g., Enter) to the button click event.
# import tkinter as tk
# root = tk.Tk()
# root.title("Keyboard Shortcut")
# root.geometry("400x300")
# def submit(event=None):
#     print("Button clicked.")
# btn=tk.Button(root, text="Click", command=submit)
# btn.pack(pady=30)
# root.bind("<Return>", submit)
# root.mainloop()

# # 30.	Text Widget Scrollbar:
# # Attach a vertical scrollbar to the Text widget.
# import tkinter as tk
# root = tk.Tk()
# root.title("Text with Scrollbar")
# root.geometry("400x300")
# frame = tk.Frame(root)
# frame.pack(padx=10, pady=10, fill="both", expand=True)
# scrollbar = tk.Scrollbar(frame)
# scrollbar.pack(side="right", fill="y")
# text= tk.Text(frame, wrap="word", yscrollcommand=scrollbar.set)
# text.pack(side="left", fill="both", expand=True)
# scrollbar.config(command=text.yview)
# root.mainloop()

# # 31. Frame Border and Relief:
# # Add a border and a relief style (e.g., sunken) to a frame.
# import tkinter as tk
# root=tk.Tk()
# root.title("Frame border")
# root.geometry("300x300")
# frame=tk.Frame(root, borderwidth=5, relief="sunken")
# frame.pack(padx=0, pady=10)
# label = tk.Label(frame, text="Inside a sunken frame")
# label.pack()
# root.mainloop()

# # 32.	Pack Side Option:
# # Use pack(side=LEFT) and pack(side=RIGHT) to see the effect.
# import tkinter as tk
# root=tk.Tk()
# root.title("Pack Side")
# root.geometry("300x300")
# label1 = tk.Label(root, text="Label-1")
# label1.pack(side="left")
# label2 = tk.Label(root, text="Label-2")
# label2.pack(side="right")
# root.mainloop()

# # 33.	Grid Row/Column Span:
# # Make a widget span multiple columns or rows using grid().
# import tkinter as tk
# root=tk.Tk()
# root.title("Pack Side")
# root.geometry("300x300")
# label1 = tk.Label(root, text="Label-1 (Columnspan=2)", bg="lightblue")
# label1.grid(row=0, column=0, columnspan=2)
# label2 = tk.Label(root, text="Label-2", bg="lightgreen")
# label2.grid(row=1, column=0)
# label3 = tk.Label(root, text="Label-3", bg="lightyellow")
# label3.grid(row=1, column=1)
# root.mainloop()

# # 34.	Closing the Window:
# # Add a button that closes the window when clicked using root.destroy().
# import tkinter as tk
# root=tk.Tk()
# root.title("Closing the Window")
# root.geometry("300x300")
# btn=tk.Button(root, text="Close", command=root.destroy)
# btn.pack(pady=20)
# root.mainloop()

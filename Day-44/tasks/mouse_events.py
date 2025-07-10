# # 16.	Bind <Button-1> to a button and print the mouse coordinates.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def on_click(event):
#     print("Mouse coordinates:", event.x, event.y)
# btn=tk.Button(root, text="Click Me")
# btn.pack(padx=10, pady=10)
# btn.bind("<Button-1>", on_click)
# root.mainloop()

# # 17.	Bind <Enter> and <Leave> to a label to change its color on hover.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# label=tk.Label(root, text="Welcome, tkinter!")
# label.pack(padx=10, pady=10)
# def enter_event(event):
#     label.config(fg="red")
# def leave_event(event):
#     label.config(fg="black")
# label.bind("<Enter>", enter_event)
# label.bind("<Leave>", leave_event)
# root.mainloop()

# # 18.	Create a button that moves to a random location inside the window on click.
# import tkinter as tk
# import random
# root=tk.Tk()
# root.geometry("300x300")
# def move_btn():
# Get window size
#     win_width=root.winfo_width()
#     win_height=root.winfo_height()
    # Define max position (prevent button from going outside window)
#     max_x=win_width-btn.winfo_width()
#     max_h=win_height-btn.winfo_height()
    # Generate random (x, y) within bounds
#     new_x=random.randint(0, max_x)
#     new_y=random.randint(0, max_h)
    # Move button
#     btn.place(x=new_x, y=new_y)
# btn=tk.Button(root, text="Catch Me", command=move_btn)
# btn.place(x=100, y=100)
# root.mainloop()

# # 19.	Implement a right-click (<Button-3>) to display a popup message.
# import tkinter as tk
# from tkinter import messagebox
# root=tk.Tk()
# root.geometry("300x300")
# def show_popup(event):
#     messagebox.showinfo("Right click", "You right_clicked.")
# root.bind("<Button-3>", show_popup)
# root.mainloop()

# # 20.	Display tooltip text using <Enter> and <Leave> events with a Label.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# label=tk.Label(root, text="Hover me")
# label.pack(padx=10, pady=40)
# tooltip=tk.Label(root, text="This is tooltip")
# tooltip.place_forget()
# def show_tooltip(event):
#     tooltip.place(x=100, y=100)
# def hide_tooltip(event):
#     tooltip.place_forget()
# label.bind("<Enter>", show_tooltip)
# label.bind("<Leave>", hide_tooltip)
# root.mainloop()

# # 21.	Use mouse double-click (<Double-Button-1>) on a label to change its text.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def change_text(event):
#     label.config(text="Happy Learning!")
# label=tk.Label(root, text="Welcome to Tkinter")
# label.pack(padx=10, pady=10)
# label.bind("<Double-Button-1>", change_text)
# root.mainloop()

# # 22.	Click on a canvas to draw a small circle at the mouse position.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# canvas=tk.Canvas(root, bg="white")
# canvas.pack(fill="both", expand=True)
# def draw_circle(event):
#     r=5
#     x, y=event.x, event.y
#     canvas.create_oval(x-r, y-r, x+r, y+r, fill="red")
# canvas.bind("<Button-1>", draw_circle)
# root.mainloop()

# # 23.	Draw a rectangle on canvas by clicking two points (first click = start, second = end).
# import tkinter as tk
# root = tk.Tk()
# root.geometry("400x400")
# canvas = tk.Canvas(root, bg="white")
# canvas.pack(fill="both", expand=True)
# start_point = {}
# def on_click(event):
#     global start_point
#     if not start_point:
#         # First click
#         start_point = {'x': event.x, 'y': event.y}
#     else:
#         # Second click: draw rectangle
#         canvas.create_rectangle(start_point['x'], start_point['y'], event.x, event.y, outline="red")
#         start_point = {}  # reset
# canvas.bind("<Button-1>", on_click)
# root.mainloop()


# # 24.	Log all mouse events in a Text widget (hover, enter, click).
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# text=tk.Text(root, height=10)
# text.pack(fill="x")
# def log_event(event):
#     msg=f" {event.type} at ({event.x}, {event.y})"
#     text.insert("end", msg)
#     text.see("end")
# text.bind("<Enter>", log_event)
# text.bind("<Leave>", log_event)
# text.bind("<Motion>", log_event)
# text.bind("<Button-1>", log_event)
# text.bind("<Button-3>", log_event)
# root.mainloop()

# # 25.	Change the border color of an Entry widget on mouse hover.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# entry=tk.Entry(root, highlightbackground="green", highlightthickness=3)
# entry.pack(padx=10, pady=20)
# def on_enter(event):
#     entry.config(highlightbackground="red")
# def on_leave(event):
#     entry.config(highlightbackground="green")
# entry.bind("<Enter>", on_enter)
# entry.bind("<Leave>", on_leave)
# root.mainloop()
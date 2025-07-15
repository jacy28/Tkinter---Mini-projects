# 🎨 Drawing & Shapes
# import tkinter as tk

# root = tk.Tk()
# root.title("Canvas Drawing")

# # Create a canvas
# canvas = tk.Canvas(root, width=400, height=400, bg="white")
# canvas.pack()

# # 1.	Create a canvas and draw a rectangle.
# canvas.create_rectangle(50, 50, 150, 120, fill="skyblue", outline="black")

# # 2. Draw a circle (oval) using bounding box
# canvas.create_oval(200, 50, 300, 150, fill="lightgreen", outline="black")

# # 3. Draw a line from (50, 200) to (300, 200)
# canvas.create_line(50, 200, 300, 200, fill="red", width=2)

# # 4. Draw a polygon (triangle)
# canvas.create_polygon(100, 300, 150, 250, 200, 300, fill="orange", outline="black")

# # 5. Fill shapes with different colors 

# # Start the GUI event loop
# root.mainloop()

# 🧩 Positioning & Dimensions
# import tkinter as tk

# def resize_canvas():
#     try:
#         new_width = int(entry_width.get())
#         new_height = int(entry_height.get())
#         canvas.config(width=new_width, height=new_height)
#     except ValueError:
#         print("Please enter valid numbers for width and height.")

# # Main window
# root = tk.Tk()

# #6. Canvas with custom width and height 
# canvas_width = 500
# canvas_height = 400
# canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
# canvas.pack(pady=10)

# #9. Variables for dynamic positioning 
# x1, y1 = 50, 50
# x2, y2 = 150, 100

# #8. Draw multiple shapes 
# canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black")
# canvas.create_oval(x1+200, y1, x2+200, y2+50, fill="lightgreen", outline="black")
# canvas.create_line(x1, y2+100, x2+200, y2+100, fill="purple", width=2)
# canvas.create_polygon(250, 250, 300, 200, 350, 250, fill="orange", outline="black")

# #7. Write text 
# canvas.create_text(250, 20, text="Canvas Drawing Demo", font=("Arial", 16), fill="blue")

# #10. Inputs to dynamically resize the canvas 
# controls_frame = tk.Frame(root)
# controls_frame.pack()

# tk.Label(controls_frame, text="Canvas Width:").grid(row=0, column=0)
# entry_width = tk.Entry(controls_frame)
# entry_width.insert(0, str(canvas_width))
# entry_width.grid(row=0, column=1)

# tk.Label(controls_frame, text="Canvas Height:").grid(row=0, column=2)
# entry_height = tk.Entry(controls_frame)
# entry_height.insert(0, str(canvas_height))
# entry_height.grid(row=0, column=3)

# resize_button = tk.Button(controls_frame, text="Resize Canvas", command=resize_canvas)
# resize_button.grid(row=0, column=4, padx=10)

# root.mainloop()

# # 11.	Animate a rectangle moving left to right.
# import tkinter as tk
# root=tk.Tk()
# def move_rectangle():
#     canvas.move(rect, 60, 0)
#     if canvas.coords(rect)[2]<canvas.winfo_width():
#         root.after(1000, move_rectangle)
# canvas=tk.Canvas(root, width=400, height=200, bg="white")
# canvas.pack()
# rect=canvas.create_rectangle(10, 50, 60, 100, fill="blue")
# move_rectangle()
# root.mainloop()

# # 12.	Animate a circle bouncing off canvas borders.
# import tkinter as tk

# # Setup main window
# root = tk.Tk()
# root.title("Bouncing Circle")

# # Create canvas
# canvas_width = 400
# canvas_height = 300
# canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
# canvas.pack()

# # Create a circle (oval)
# radius = 20
# x, y = 50, 50
# dx, dy = 10, 5  # Change in position per frame (speed)
# circle = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="red")

# def move_circle():
#     global dx, dy
#     # Move the circle
#     canvas.move(circle, dx, dy)
#     # Get new coordinates
#     x1, y1, x2, y2 = canvas.coords(circle)
#     # Bounce off left/right walls
#     if x1 <= 0 or x2 >= canvas_width:
#         dx = -dx
#     # Bounce off top/bottom walls
#     if y1 <= 0 or y2 >= canvas_height:
#         dy = -dy

#     # Schedule next move
#     root.after(20, move_circle)

# # Start animation
# move_circle()
# root.mainloop()

# # 13.	Animate multiple shapes at different speeds.
# import tkinter as tk
# # Setup main window
# root = tk.Tk()
# root.title("Multiple Shapes Animation")
# # Create canvas
# canvas = tk.Canvas(root, width=500, height=400, bg="white")
# canvas.pack()
# # Define shapes with their speed and direction
# shapes = [
#     {"id": canvas.create_oval(50, 50, 90, 90, fill="red"), "dx": 2, "dy": 3},
#     {"id": canvas.create_rectangle(100, 150, 160, 180, fill="blue"), "dx": 4, "dy": 2},
#     {"id": canvas.create_oval(200, 250, 230, 280, fill="green"), "dx": 1, "dy": 5},
# ]
# canvas_width = 500
# canvas_height = 400
# def animate_shapes():
#     for shape in shapes:
#         canvas.move(shape["id"], shape["dx"], shape["dy"])
#         x1, y1, x2, y2 = canvas.coords(shape["id"])
#         # Bounce off left/right
#         if x1 <= 0 or x2 >= canvas_width:
#             shape["dx"] *= -1
#         # Bounce off top/bottom
#         if y1 <= 0 or y2 >= canvas_height:
#             shape["dy"] *= -1
#     # Schedule next frame
#     root.after(30, animate_shapes)
# # Start animation
# animate_shapes()
# root.mainloop()

# # 14.	Animate an object and stop animation on button click.
# import tkinter as tk
# # Setup main window
# root = tk.Tk()
# root.title("Stop Animation Example")
# # Create canvas
# canvas = tk.Canvas(root, width=400, height=300, bg="white")
# canvas.pack()
# # Create a moving rectangle
# rect = canvas.create_rectangle(10, 100, 60, 150, fill="purple")
# dx = 5  # Speed
# # Animation control flag
# animation_running = True
# def move_object():
#     global dx  # Declare at the top of the function
#     if animation_running:
#         canvas.move(rect, dx, 0)
#         x1, y1, x2, y2 = canvas.coords(rect)
#         # Bounce off walls
#         if x2 >= canvas.winfo_width() or x1 <= 0:
#             dx = -dx
#         # Continue animation
#         root.after(30, move_object)
# def stop_animation():
#     global animation_running
#     animation_running = False
# # Stop button
# stop_button = tk.Button(root, text="Stop Animation", command=stop_animation)
# stop_button.pack(pady=10)
# # Start animation
# move_object()
# root.mainloop()

# # 15.	Animate an object along a diagonal path.
# import tkinter as tk
# # Create main window
# root = tk.Tk()
# root.title("Diagonal Animation")
# # Create canvas
# canvas = tk.Canvas(root, width=400, height=300, bg="white")
# canvas.pack()
# # Create an object (e.g., a circle)
# obj = canvas.create_oval(20, 20, 60, 60, fill="orange")
# # Diagonal movement speed
# dx = 3
# dy = 3
# def move_diagonal():
#     global dx, dy  # Declare both at the top before usage
#     canvas.move(obj, dx, dy)
#     x1, y1, x2, y2 = canvas.coords(obj)
#     # Bounce off canvas edges
#     if x2 >= canvas.winfo_width() or x1 <= 0:
#         dx = -dx
#     if y2 >= canvas.winfo_height() or y1 <= 0:
#         dy = -dy
#     # Repeat movement
#     root.after(30, move_diagonal)
# # Start animation
# move_diagonal()
# root.mainloop()


# # 🖱️ Event Binding
# # 16.	Bind a left mouse click (<Button-1>) to draw a circle where clicked.
# import tkinter as tk
# def draw_circle(event):
#     x, y = event.x, event.y
#     r = 20  # radius of the circle
#     canvas.create_oval(x - r, y - r, x + r, y + r, fill='blue')
# root = tk.Tk()
# root.title("Click to Draw Circle")
# canvas = tk.Canvas(root, width=400, height=400, bg='white')
# canvas.pack()
# # Bind left mouse click to draw_circle function
# canvas.bind("<Button-1>", draw_circle)
# root.mainloop()


# # 17.	Bind a double-click to draw a rectangle.
# import tkinter as tk
# def draw_rectangle(event):
#     x, y = event.x, event.y
#     w, h = 40, 30  # width and height of the rectangle
#     canvas.create_rectangle(x - w/2, y - h/2, x + w/2, y + h/2, fill='green')
# root = tk.Tk()
# root.title("Double-Click to Draw Rectangle")
# canvas = tk.Canvas(root, width=400, height=400, bg='white')
# canvas.pack()
# # Bind double-click (left mouse button) to draw_rectangle function
# canvas.bind("<Double-Button-1>", draw_rectangle)
# root.mainloop()


# # 18.	Show the mouse coordinates on the canvas when clicked.
# import tkinter as tk
# def show_coordinates(event):
#     x, y = event.x, event.y
#     coords_text = f"({x}, {y})"
#     canvas.create_text(x, y, text=coords_text, fill="black", font=("Arial", 10))
# root = tk.Tk()
# root.title("Click to Show Coordinates")
# canvas = tk.Canvas(root, width=400, height=400, bg='white')
# canvas.pack()
# # Bind left mouse click to show_coordinates function
# canvas.bind("<Button-1>", show_coordinates)
# root.mainloop()

# # 19.	Move a shape to the clicked position.
# import tkinter as tk
# def move_shape(event):
#     x, y = event.x, event.y
#     r = 20  # radius of the circle
#     canvas.coords(circle, x - r, y - r, x + r, y + r)
# root = tk.Tk()
# root.title("Move Shape to Clicked Position")
# canvas = tk.Canvas(root, width=400, height=400, bg='white')
# canvas.pack()
# # Create a circle initially at the center
# r = 20
# circle = canvas.create_oval(200 - r, 200 - r, 200 + r, 200 + r, fill='red')
# # Bind left click to move the circle
# canvas.bind("<Button-1>", move_shape)
# root.mainloop()

# # 20.	Change shape color when hovered over (use tag_bind()).
# import tkinter as tk

# def on_enter(event):
#     canvas.itemconfig("my_shape", fill="orange")

# def on_leave(event):
#     canvas.itemconfig("my_shape", fill="blue")

# root = tk.Tk()
# root.title("Hover to Change Shape Color")

# canvas = tk.Canvas(root, width=400, height=400, bg='white')
# canvas.pack()

# # Create a rectangle with a tag
# rect = canvas.create_rectangle(150, 150, 250, 250, fill="blue", tags="my_shape")

# # Bind mouse enter/leave to the tag
# canvas.tag_bind("my_shape", "<Enter>", on_enter)
# canvas.tag_bind("my_shape", "<Leave>", on_leave)

# root.mainloop()


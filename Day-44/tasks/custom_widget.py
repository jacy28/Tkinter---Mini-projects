# # 36.	Create a custom widget (class) that displays a label and a button.
# import tkinter as tk
# class LabelButton(tk.Frame):
#     def __init__(self, master, text="Label", btn_text="Click Me"):
#         super().__init__(master)
#         self.label = tk.Label(self, text=text)
#         self.label.pack(side="left", padx=5)
#         self.button = tk.Button(self, text=btn_text, command=self.on_click)
#         self.button.pack(side="left")
#     def on_click(self):
#         print("Button clicked!")
# root = tk.Tk()
# lb = LabelButton(root, "Hello", "Greet")
# lb.pack(pady=10)
# root.mainloop()


# # 37.	Build a custom widget with a label and an entry. When user types, the label updates live.
# import tkinter as tk
# class LiveLabelEntry(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master)
#         self.label = tk.Label(self, text="Type something")
#         self.label.pack()
#         self.entry = tk.Entry(self)
#         self.entry.pack()
#         self.entry.bind("<KeyRelease>", self.update)
#     def update(self, event):
#         self.label.config(text=self.entry.get())
# root = tk.Tk()
# lle = LiveLabelEntry(root)
# lle.pack(pady=10)
# root.mainloop()


# # 38.	Design a custom widget that combines two buttons (OK, Cancel) and handles clicks.
# import tkinter as tk
# class OKCancel(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master)
#         tk.Button(self, text="OK", command=self.ok).pack(side="left", padx=5)
#         tk.Button(self, text="Cancel", command=self.cancel).pack(side="left", padx=5)

#     def ok(self):
#         print("OK pressed")

#     def cancel(self):
#         print("Cancel pressed")

# root = tk.Tk()
# ok_cancel = OKCancel(root)
# ok_cancel.pack(pady=10)
# root.mainloop()


# # 39.	Create a SearchBox custom widget with Entry + Search button.
# import tkinter as tk
# class SearchBox(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master)
#         self.entry = tk.Entry(self)
#         self.entry.pack(side="left")
#         tk.Button(self, text="Search", command=self.search).pack(side="left")

#     def search(self):
#         print("Searching for:", self.entry.get())

# root = tk.Tk()
# sb = SearchBox(root)
# sb.pack(pady=10)
# root.mainloop()


# # 40.	Build a calculator row widget (2 entries + operator + result label).
# import tkinter as tk
# class CalcRow(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master)
#         self.e1 = tk.Entry(self, width=5)
#         self.e2 = tk.Entry(self, width=5)
#         self.result = tk.Label(self, text="= ?")
#         self.e1.pack(side="left")
#         tk.Label(self, text="+").pack(side="left")
#         self.e2.pack(side="left")
#         tk.Button(self, text="=", command=self.calculate).pack(side="left")
#         self.result.pack(side="left")

#     def calculate(self):
#         try:
#             total = int(self.e1.get()) + int(self.e2.get())
#             self.result.config(text=f"= {total}")
#         except:
#             self.result.config(text="= Error")

# root = tk.Tk()
# calc = CalcRow(root)
# calc.pack(pady=10)
# root.mainloop()


# # 41.	Make a reusable custom login widget (username + password + submit).
# import tkinter as tk
# class LoginWidget(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master)
#         tk.Label(self, text="Username:").grid(row=0, column=0)
#         tk.Label(self, text="Password:").grid(row=1, column=0)
#         self.username = tk.Entry(self)
#         self.password = tk.Entry(self, show="*")
#         self.username.grid(row=0, column=1)
#         self.password.grid(row=1, column=1)
#         tk.Button(self, text="Login", command=self.login).grid(row=2, column=1)

#     def login(self):
#         print("Logged in:", self.username.get())

# root = tk.Tk()
# login = LoginWidget(root)
# login.pack(pady=10)
# root.mainloop()


# # 42.	Create a reusable rating bar (5 stars) using buttons or labels inside a frame.
# import tkinter as tk
# class RatingBar(tk.Frame):
#     def __init__(self, master, max_stars=5):
#         super().__init__(master)
#         self.stars = []
#         for i in range(max_stars):
#             btn = tk.Button(self, text="☆", command=lambda i=i: self.rate(i+1))
#             btn.pack(side="left")
#             self.stars.append(btn)

#     def rate(self, value):
#         for i, btn in enumerate(self.stars):
#             btn.config(text="★" if i < value else "☆")
#         print("Rated:", value)

# root = tk.Tk()
# rb = RatingBar(root)
# rb.pack(pady=10)
# root.mainloop()


# # 43.	Embed a custom color picker with Buttons to choose predefined colors.
# import tkinter as tk
# class ColorPicker(tk.Frame):
#     def __init__(self, master, colors=["red", "green", "blue"]):
#         super().__init__(master)
#         self.label = tk.Label(self, text="Pick a color", width=20)
#         self.label.pack()
#         for color in colors:
#             tk.Button(self, bg=color, width=5, command=lambda c=color: self.set_color(c)).pack(side="left")

#     def set_color(self, color):
#         self.label.config(bg=color)

# root = tk.Tk()
# cp = ColorPicker(root)
# cp.pack(pady=10)
# root.mainloop()


# # 44.	Create a reusable toolbar widget with configurable buttons (Open, Save, Exit).
# import tkinter as tk
# class Toolbar(tk.Frame):
#     def __init__(self, master, actions):
#         super().__init__(master)
#         for name, command in actions.items():
#             tk.Button(self, text=name, command=command).pack(side="left")

# root = tk.Tk()
# tb = Toolbar(root, {"Open": lambda: print("Open"),
#                     "Save": lambda: print("Save"),
#                     "Exit": root.quit})
# tb.pack(pady=10)
# root.mainloop()


# # 45.	Use class inheritance to create a LabeledEntry widget with custom styles.
# import tkinter as tk
# class LabeledEntry(tk.Frame):
#     def __init__(self, master, label_text):
#         super().__init__(master)
#         tk.Label(self, text=label_text).pack(side="left")
#         self.entry = tk.Entry(self)
#         self.entry.pack(side="left")

#     def get(self):
#         return self.entry.get()

# root = tk.Tk()
# le = LabeledEntry(root, "Email:")
# le.pack(pady=10)
# root.mainloop()

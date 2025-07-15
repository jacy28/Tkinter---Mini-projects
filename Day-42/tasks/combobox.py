# # 31.	Create a Combobox with fruits: Apple, Banana, Cherry.
# import tkinter as tk
# from tkinter import ttk
# root = tk.Tk()
# root.geometry("400x300")
# root.title("Fruit Combobox")
# # Label
# label = tk.Label(root, text="Select a fruit:")
# label.pack(pady=10)
# # Combobox with fruits
# combo = ttk.Combobox(root, values=["Apple", "Banana", "Cherry"])
# combo.pack(pady=5)
# # Optional: Set default value
# combo.set("Apple")
# root.mainloop()

# # 32.	Print selected value when changed using a button or callback.
# import tkinter as tk
# from tkinter import ttk
# def show_selection():
#     print("Selected fruit:", combo.get())
# root = tk.Tk()
# root.geometry("400x300")
# root.title("Combobox Selection")
# # Combobox
# combo = ttk.Combobox(root, values=["Apple", "Banana", "Cherry"])
# combo.set("Apple")  # Optional default
# combo.pack(pady=10)
# # Button to print selected value
# btn = tk.Button(root, text="Show Selection", command=show_selection)
# btn.pack(pady=5)
# root.mainloop()

# # 33.	Set a default selected value using current().
# import tkinter as tk
# from tkinter import ttk
# root = tk.Tk()
# root.geometry("400x300")
# root.title("Default Combobox Selection")
# # Create Combobox
# combo = ttk.Combobox(root, values=["Apple", "Banana", "Cherry"])
# combo.pack(pady=10)
# combo.current(1)
# root.mainloop()

# # 34.	Allow typing a custom value into the Combobox.
# import tkinter as tk
# from tkinter import ttk
# root = tk.Tk()
# root.geometry("400x300")
# root.title("Custom Combobox Input")
# # Create Combobox (default state allows typing)
# combo = ttk.Combobox(root, values=["Apple", "Banana", "Cherry"])
# combo.pack(pady=10)
# # Optional: Set a default value
# combo.set("Type or choose...")
# root.mainloop()


# # 35.	Disable editing in the Combobox (readonly mode).
# import tkinter as tk
# from tkinter import ttk
# root = tk.Tk()
# root.geometry("400x300")
# root.title("Readonly Combobox")
# # Create Combobox (default state allows typing)
# combo = ttk.Combobox(root, values=["Apple", "Banana", "Cherry"], state="readonly")
# combo.pack(pady=10)
# root.mainloop()

# # 36.	Update the options in a Combobox using a button click.
# import tkinter as tk
# from tkinter import ttk
# def update_options():
#     new_fruits = ["Mango", "Pineapple", "Grapes"]
#     combo['values'] = new_fruits
#     combo.set('')  # Optional: clear current selection
# root = tk.Tk()
# root.geometry("400x300")
# root.title("Update Combobox Options")
# # Initial Combobox
# combo = ttk.Combobox(root, values=["Apple", "Banana", "Cherry"])
# combo.pack(pady=10)
# combo.current(0)
# # Button to update options
# btn = tk.Button(root, text="Update Options", command=update_options)
# btn.pack(pady=5)
# root.mainloop()

# # 37.	Create a dependent dropdown: Select “Country” then update “City”.
# import tkinter as tk
# from tkinter import ttk
# def update_cities(event):
#     selected_country = country_combo.get()
#     cities = country_city_map.get(selected_country, [])
#     city_combo['values'] = cities
#     city_combo.set('')  # Clear previous selection
# root = tk.Tk()
# root.geometry("400x300")
# root.title("Country → City Dropdown")
# # Country to City mapping
# country_city_map = {
#     "USA": ["New York", "Los Angeles", "Chicago"],
#     "India": ["Delhi", "Mumbai", "Bangalore"],
#     "Japan": ["Tokyo", "Osaka", "Kyoto"]
# }
# # Country Combobox
# ttk.Label(root, text="Select Country:").pack(pady=5)
# country_combo = ttk.Combobox(root, values=list(country_city_map.keys()), state='readonly')
# country_combo.pack(pady=5)
# country_combo.bind("<<ComboboxSelected>>", update_cities)
# # City Combobox (will be updated based on country)
# ttk.Label(root, text="Select City:").pack(pady=5)
# city_combo = ttk.Combobox(root, state='readonly')
# city_combo.pack(pady=5)
# root.mainloop()

# # 38.	Clear selection and reset Combobox to default.
# import tkinter as tk
# from tkinter import ttk
# def clear_selection():
#     combo.set('')  # Clears selection (shows empty)
# def reset_to_default():
#     combo.current(0)  # Reset to first item
# root = tk.Tk()
# root.geometry("400x300")
# root.title("Clear / Reset Combobox")
# combo = ttk.Combobox(root, values=["Apple", "Banana", "Cherry"], state='readonly')
# combo.pack(pady=10)
# combo.current(1)  # Set default to Banana initially
# btn_clear = tk.Button(root, text="Clear Selection", command=clear_selection)
# btn_clear.pack(pady=5)
# btn_reset = tk.Button(root, text="Reset to Default (Apple)", command=reset_to_default)
# btn_reset.pack(pady=5)
# root.mainloop()


# # 39.	Show selected item in a Label on selection.
# import tkinter as tk
# from tkinter import ttk
# def show_selection(event):
#     selected = combo.get()
#     label.config(text=f"Selected: {selected}")
# root = tk.Tk()
# root.geometry("400x300")
# root.title("Show Selection in Label")
# # Combobox
# combo = ttk.Combobox(root, values=["Apple", "Banana", "Cherry"], state="readonly")
# combo.pack(pady=10)
# combo.current(0)  # Optional default selection
# # Bind selection event
# combo.bind("<<ComboboxSelected>>", show_selection)
# # Label to display selected item
# label = tk.Label(root, text="Selected: None")
# label.pack(pady=10)
# root.mainloop()

# # 40.	Create a search bar using Combobox where typing filters options.
# import tkinter as tk
# from tkinter import ttk
# def filter_options(event):
#     typed = combo.get()
#     if typed == "":
#         combo['values'] = fruits
#     else:
#         filtered = [item for item in fruits if typed.lower() in item.lower()]
#         combo['values'] = filtered
#         combo.event_generate('<Down>')  # Auto-show dropdown
# root = tk.Tk()
# root.geometry("400x300")
# root.title("Searchable Combobox")
# # Full list of items
# fruits = ["Apple", "Banana", "Cherry", "Date", "Dragonfruit", "Grapes", "Guava", "Mango", "Orange", "Papaya", "Pineapple", "Strawberry"]
# # Create editable Combobox
# combo = ttk.Combobox(root)
# combo['values'] = fruits
# combo.pack(pady=20)
# # Bind key release to filter
# combo.bind("<KeyRelease>", filter_options)
# root.mainloop()






# 34. Form Autofill Desktop App
# •	Input form templates with field mappings
# •	Save/load profile data
# •	Paste into browser using hotkey or pyautogui
# •	Delay options to avoid detection
# •	Optional: multiple profiles

import tkinter as tk
from tkinter import filedialog, messagebox
import pyautogui
import time
import json
import threading
import keyboard

class AutofillApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Form Autofill App")

        self.fields = ["Name", "Email", "Phone", "Address", "Comments"]
        self.entries = {}
        self.delay = tk.DoubleVar(value=0.5)

        self.create_form()
        self.setup_buttons()

        # Register hotkey
        keyboard.add_hotkey('ctrl+alt+f', self.autofill)

    def create_form(self):
        for i, field in enumerate(self.fields):
            tk.Label(self.root, text=field).grid(row=i, column=0, sticky='w')
            entry = tk.Entry(self.root, width=40)
            entry.grid(row=i, column=1)
            self.entries[field] = entry

        tk.Label(self.root, text="Delay between fields (sec):").grid(row=len(self.fields), column=0, sticky='w')
        tk.Entry(self.root, textvariable=self.delay).grid(row=len(self.fields), column=1)

    def setup_buttons(self):
        tk.Button(self.root, text="Autofill (Alt+Ctrl+F)", command=self.autofill).grid(row=6, column=0)
        tk.Button(self.root, text="Save Profile", command=self.save_profile).grid(row=6, column=1)
        tk.Button(self.root, text="Load Profile", command=self.load_profile).grid(row=7, column=1)

    def autofill(self):
        def do_autofill():
            time.sleep(3)  # Time to switch to browser
            for field in self.fields:
                value = self.entries[field].get()
                pyautogui.write(value)
                pyautogui.press('tab')
                time.sleep(self.delay.get())

        threading.Thread(target=do_autofill).start()

    def save_profile(self):
        data = {field: self.entries[field].get() for field in self.fields}
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, "w") as f:
                json.dump(data, f)
            messagebox.showinfo("Saved", "Profile saved successfully.")

    def load_profile(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, "r") as f:
                data = json.load(f)
            for field in self.fields:
                self.entries[field].delete(0, tk.END)
                self.entries[field].insert(0, data.get(field, ""))

if __name__ == "__main__":
    root = tk.Tk()
    app = AutofillApp(root)
    root.mainloop()

# 23. Weather Forecast App with Charted Temperature
# •	Input city name
# •	Fetch weather using OpenWeatherMap API
# •	Show temperature, humidity, description
# •	5-day forecast with bar chart (matplotlib)
# •	Add save location and search history

import tkinter as tk
from tkinter import ttk, messagebox
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime

API_KEY = '#'  

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast App")
        self.city_name = tk.StringVar()
        self.history = []

        self.build_ui()

    def build_ui(self):
        # Input frame
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=10)

        ttk.Label(input_frame, text="City:").pack(side='left')
        ttk.Entry(input_frame, textvariable=self.city_name, width=20).pack(side='left', padx=5)
        ttk.Button(input_frame, text="Search", command=self.fetch_weather).pack(side='left')

        # Current weather
        self.info_label = ttk.Label(self.root, text="", font=("Arial", 12))
        self.info_label.pack(pady=5)

        # Forecast chart
        self.fig, self.ax = plt.subplots(figsize=(6, 3))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()

        # History
        self.history_list = tk.Listbox(self.root, height=5)
        self.history_list.pack(pady=5, fill='x')
        self.history_list.bind("<<ListboxSelect>>", self.on_history_select)

    def fetch_weather(self):
        city = self.city_name.get().strip()
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name.")
            return

        url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
        try:
            response = requests.get(url)
            data = response.json()

            if data.get("cod") != "200":
                raise Exception(data.get("message", "Unknown error"))

            # Add to history
            if city not in self.history:
                self.history.append(city)
                self.history_list.insert(tk.END, city)

            # Current weather (first item)
            current = data["list"][0]
            temp = current["main"]["temp"]
            humidity = current["main"]["humidity"]
            description = current["weather"][0]["description"].capitalize()
            self.info_label.config(text=f"{city.title()}: {description}, {temp:.1f}°C, {humidity}% humidity")

            # 5-day forecast (get 1 value per day at 12:00)
            dates = []
            temps = []
            for item in data["list"]:
                dt = datetime.datetime.fromtimestamp(item["dt"])
                if dt.hour == 12:
                    dates.append(dt.strftime("%a"))
                    temps.append(item["main"]["temp"])

            self.plot_forecast(dates, temps)

        except Exception as e:
            print("Error:", e)
            messagebox.showerror("API Error", f"Failed to fetch weather data.\n{e}")

    def plot_forecast(self, dates, temps):
        self.ax.clear()
        self.ax.bar(dates, temps, color='skyblue')
        self.ax.set_title("5-Day Forecast (12:00 PM)")
        self.ax.set_ylabel("Temperature (°C)")
        self.canvas.draw()

    def on_history_select(self, event):
        if not self.history_list.curselection():
            return
        index = self.history_list.curselection()[0]
        city = self.history_list.get(index)
        self.city_name.set(city)
        self.fetch_weather()

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

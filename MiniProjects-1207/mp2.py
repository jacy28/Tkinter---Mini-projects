# 2. Live Stock Market Tracker using APIs
# •	Input stock symbols
# •	Fetch live data using financial APIs (like Alpha Vantage)
# •	Show live price, change %, and volume
# •	Use after() to update every 60 seconds
# •	Line chart of price trend (last hour/day)

import tkinter as tk
from tkinter import ttk, messagebox
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
import pandas as pd

API_KEY = 'VUZSJ55FK8TQ66CB'

class StockTracker:
    def __init__(self, root):
        self.root = root
        self.ts = TimeSeries(key=API_KEY, output_format='pandas')
        self.symbol = tk.StringVar()
        self.prices = []
        self.timestamps = []
        self.updating = False
        self.build_ui()

    def build_ui(self):
        self.root.title("Live Stock Market Tracker")
        frame = ttk.Frame(self.root); frame.pack(pady=10)

        ttk.Label(frame, text="Symbol:").pack(side='left')
        ttk.Entry(frame, textvariable=self.symbol, width=8).pack(side='left', padx=5)
        ttk.Button(frame, text="Start", command=self.start).pack(side='left', padx=5)
        ttk.Button(frame, text="Stop", command=self.stop).pack(side='left')

        self.fig, self.ax = plt.subplots(figsize=(6, 3))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()

        self.info = ttk.Label(self.root, text="", font=("Arial", 10))
        self.info.pack(pady=5)

    def start(self):
        symbol = self.symbol.get().strip().upper()
        if not symbol:
            messagebox.showwarning("Warning", "Enter stock symbol")
            return
        self.symbol.set(symbol)
        self.prices.clear()
        self.timestamps.clear()
        self.updating = True
        self.update()

    def stop(self):
        self.updating = False

    def update(self):
        if not self.updating:
            return

        try:
            data, _ = self.ts.get_quote_endpoint(symbol=self.symbol.get())
            print("Raw API response:", data)  # Debug print

            price = float(data['05. price'].iloc[0])
            change_pct = float(data['10. change percent'].iloc[0].rstrip('%'))
            vol = int(data['06. volume'].iloc[0])

            self.prices.append(price)
            self.timestamps.append(datetime.now().strftime("%H:%M:%S"))

            # Keep only last 60 data points
            if len(self.prices) > 60:
                self.prices = self.prices[-60:]
                self.timestamps = self.timestamps[-60:]

            self.ax.clear()
            self.ax.plot(self.timestamps, self.prices, marker='o', color='blue')
            self.ax.set_title(self.symbol.get())
            self.ax.set_xlabel("Time (updated every 60s)")
            self.ax.set_ylabel("Price")
            self.ax.tick_params(axis='x', rotation=45)
            self.fig.tight_layout()

            self.canvas.draw()
            self.info.config(text=f"Price: {price:.2f}  Δ%: {change_pct:.2f}%  Vol: {vol}")

        except Exception as e:
            print("Error fetching data:", e)
            self.info.config(text="Error fetching data. Check console or API limits.")

        self.root.after(60000, self.update)  # Call again in 60 seconds

if __name__ == "__main__":
    root = tk.Tk()
    app = StockTracker(root)
    root.mainloop()

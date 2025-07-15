# 🖥️ System Monitoring
# 41. Network Speed Monitor with History Graph
# •	Check upload/download speed (use speedtest-cli)
# •	Show result every X seconds
# •	Line chart for history
# •	Export data to CSV
# •	Alert if speed drops below threshold

import tkinter as tk
from tkinter import messagebox, filedialog
import speedtest
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import time
import csv

class NetworkSpeedMonitor:
    def __init__(self, root):
        self.root = root
        self.root.title("📶 Network Speed Monitor")

        # UI Config
        self.interval = tk.IntVar(value=10)  # seconds
        self.threshold = tk.DoubleVar(value=5.0)  # Mbps
        self.running = False
        self.data = []  # (timestamp, download, upload)

        # GUI Layout
        tk.Label(root, text="Check Interval (sec):").pack()
        tk.Entry(root, textvariable=self.interval).pack()

        tk.Label(root, text="Alert if Download < Mbps:").pack()
        tk.Entry(root, textvariable=self.threshold).pack()

        tk.Button(root, text="▶ Start Monitoring", command=self.start_monitoring).pack(pady=5)
        tk.Button(root, text="💾 Export CSV", command=self.export_csv).pack()

        # Matplotlib Chart
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack()

    def start_monitoring(self):
        if not self.running:
            self.running = True
            self.monitor_loop()

    def monitor_loop(self):
        if self.running:
            threading.Thread(target=self.perform_speedtest).start()
            self.root.after(self.interval.get() * 1000, self.monitor_loop)

    def perform_speedtest(self):
        try:
            st = speedtest.Speedtest()
            download = round(st.download() / 1_000_000, 2)  # Mbps
            upload = round(st.upload() / 1_000_000, 2)  # Mbps
            timestamp = time.strftime("%H:%M:%S")

            self.data.append((timestamp, download, upload))
            print(f"{timestamp} - ↓ {download} Mbps, ↑ {upload} Mbps")

            if download < self.threshold.get():
                messagebox.showwarning("⚠ Low Speed", f"Download speed is {download} Mbps")

            self.update_plot()
        except Exception as e:
            print("Speedtest Error:", e)

    def update_plot(self):
        times = [row[0] for row in self.data[-20:]]
        downloads = [row[1] for row in self.data[-20:]]
        uploads = [row[2] for row in self.data[-20:]]

        self.ax.clear()
        self.ax.plot(times, downloads, label="Download ↓", color='blue')
        self.ax.plot(times, uploads, label="Upload ↑", color='green')
        self.ax.set_title("Network Speed (Mbps)")
        self.ax.set_ylabel("Speed (Mbps)")
        self.ax.set_xlabel("Time")
        self.ax.legend()
        self.ax.grid(True)
        self.fig.autofmt_xdate()
        self.canvas.draw()

    def export_csv(self):
        if not self.data:
            messagebox.showinfo("No Data", "No data to export.")
            return

        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if filename:
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Time", "Download (Mbps)", "Upload (Mbps)"])
                writer.writerows(self.data)
            messagebox.showinfo("Exported", f"Exported {len(self.data)} entries to {filename}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkSpeedMonitor(root)
    root.mainloop()

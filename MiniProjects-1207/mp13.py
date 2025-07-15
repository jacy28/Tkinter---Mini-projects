# 33. Web Scraper with Keyword Filter and Export
# •	Input URL and keyword
# •	Scrape text content using requests + BeautifulSoup
# •	Filter matches
# •	Export results to .txt or .csv
# •	Optional: scrape multiple pages

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

class WebScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Scraper with Keyword Filter")

        self.build_ui()

    def build_ui(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        tk.Label(frame, text="URL:").grid(row=0, column=0, sticky="e")
        self.url_entry = tk.Entry(frame, width=60)
        self.url_entry.grid(row=0, column=1, columnspan=3)

        tk.Label(frame, text="Keyword:").grid(row=1, column=0, sticky="e")
        self.keyword_entry = tk.Entry(frame, width=30)
        self.keyword_entry.grid(row=1, column=1)

        self.follow_links_var = tk.IntVar()
        tk.Checkbutton(frame, text="Scrape linked pages", variable=self.follow_links_var).grid(row=1, column=2)

        tk.Button(frame, text="Scrape", command=self.scrape).grid(row=2, column=1, pady=10)
        tk.Button(frame, text="Export", command=self.export_results).grid(row=2, column=2, pady=10)

        self.text = tk.Text(self.root, wrap="word", width=100, height=25)
        self.text.pack(padx=10, pady=10)

        self.results = []

    def scrape(self):
        url = self.url_entry.get().strip()
        keyword = self.keyword_entry.get().strip().lower()

        if not url or not keyword:
            messagebox.showerror("Error", "Please enter both URL and keyword.")
            return

        self.results.clear()
        self.text.delete(1.0, tk.END)

        try:
            self.scrape_url(url, keyword)

            if self.follow_links_var.get():
                # Scrape links from base page
                links = self.extract_links(url)
                for link in links:
                    self.scrape_url(link, keyword)

            if self.results:
                self.text.insert(tk.END, "\n\n".join(self.results))
                messagebox.showinfo("Done", f"Found {len(self.results)} matching lines.")
            else:
                self.text.insert(tk.END, "No matching results.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to scrape: {e}")

    def scrape_url(self, url, keyword):
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            for s in soup(["script", "style"]):
                s.decompose()

            visible_text = soup.get_text(separator="\n").splitlines()
            for line in visible_text:
                if keyword in line.lower():
                    self.results.append(f"[{url}]\n{line.strip()}")
        except Exception as e:
            print(f"Error scraping {url}: {e}")

    def extract_links(self, base_url):
        try:
            response = requests.get(base_url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            base = response.url  # handles redirects
            links = set()
            for a in soup.find_all("a", href=True):
                full_url = urljoin(base, a['href'])
                if full_url.startswith("http"):
                    links.add(full_url)
            return list(links)
        except:
            return []

    def export_results(self):
        if not self.results:
            messagebox.showwarning("No data", "There is nothing to export.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text File", "*.txt"), ("CSV File", "*.csv")])
        if file_path.endswith(".csv"):
            with open(file_path, "w", newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Source", "Line"])
                for r in self.results:
                    lines = r.split("\n", 1)
                    if len(lines) == 2:
                        writer.writerow([lines[0].strip("[]"), lines[1]])
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("\n\n".join(self.results))

        messagebox.showinfo("Exported", f"Results saved to {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WebScraperApp(root)
    root.mainloop()

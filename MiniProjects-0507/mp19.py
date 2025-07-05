# 🟢 19. Library Book Manager
# Goal: Add/remove books with search feature.
# Requirements:
# •	Entry for book name.
# •	Add to Listbox using Button.
# •	Scrollbar for Listbox.
# •	Search book using another Entry.
# •	Use .bind() to filter matching titles.

import tkinter as tk

def add_book():
    book = book_entry.get()
    if book:
        books.append(book)
        update_listbox(books)
        book_entry.delete(0, tk.END)

def update_listbox(book_list):
    book_listbox.delete(0, tk.END)
    for b in book_list:
        book_listbox.insert(tk.END, b)

def search_books(event):
    query = search_entry.get().lower()
    filtered = [b for b in books if query in b.lower()]
    update_listbox(filtered)

root = tk.Tk()
root.title("Library Book Manager")
root.geometry("400x400")

books = []

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

book_label = tk.Label(input_frame, text="Book Name:")
book_label.grid(row=0, column=0)
book_entry = tk.Entry(input_frame, width=25)
book_entry.grid(row=0, column=1)
add_button = tk.Button(input_frame, text="Add Book", command=add_book)
add_button.grid(row=0, column=2, padx=5)

search_label = tk.Label(root, text="Search:")
search_label.pack()
search_entry = tk.Entry(root, width=30)
search_entry.pack()
search_entry.bind("<KeyRelease>", search_books)

list_frame = tk.Frame(root)
list_frame.pack(pady=10)

scrollbar = tk.Scrollbar(list_frame, orient="vertical")
book_listbox = tk.Listbox(list_frame, width=45, height=10, yscrollcommand=scrollbar.set)
scrollbar.config(command=book_listbox.yview)

book_listbox.grid(row=0, column=0)
scrollbar.grid(row=0, column=1, sticky="ns")

root.mainloop()

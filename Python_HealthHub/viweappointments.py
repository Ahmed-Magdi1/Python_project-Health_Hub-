import csv
import tkinter as tk
from tkinter import ttk

headers = ['Name', 'Date', 'Time']

def read_csv(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(list(row.values()))
    return data

def update_table(tree, data):
    for row in tree.get_children():
        tree.delete(row)
    for i, item in enumerate(data):
        tree.insert('', i, values=item)

def save_data(data):
    with open('appointments.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow({'Name': row[0], 'Date': row[1], 'Time': row[2]})

def appoint():
    root = tk.Tk()
    root.title("Appointments")
    root.geometry("600x200")


    tree = ttk.Treeview(root, columns=headers, show='headings')
    for col in headers:
        tree.heading(col, text=col)
    tree.grid(row=0, column=0, sticky='nsew')


    data = read_csv('appointments.csv')


    update_table(tree, data)

   
    scrollbar = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')
    tree.configure(yscrollcommand=scrollbar.set)

    root.mainloop()

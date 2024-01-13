import tkinter as tk
from tkinter import ttk, messagebox
from pat_page import *
import csv

def exit_program():
    root.destroy()

def load_patient_specific_data(username):
    try:
        with open('patient_data.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                # Check if the row has enough elements
                if len(row) >= 1 and row[0].strip().lower() == username.strip().lower():
                    return row
    except FileNotFoundError:
        messagebox.showerror("Error", "Patient data file not found.")
        return None
    return None

def patient_info(username):
    global root, table
    root = tk.Tk()
    root.title("Your Medical Information")

    # Treeview widget setup
    table = ttk.Treeview(root, columns=('Name', 'Number', 'Medical Information', 'Age', 'Gender'), show='headings')
    table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Setup columns and headings
    table.heading('Name', text='Name')
    table.heading('Number', text='Number')
    table.heading('Medical Information', text='Medical Information')
    table.heading('Age', text='Age')
    table.heading('Gender', text='Gender')

    # Load specific patient data
    patient_data = load_patient_specific_data(username)
    if patient_data:
        table.insert('', 'end', values=patient_data)
    else:
        print(f"No data found for username: {username}")
        # Exit button setup
    exit_button = tk.Button(root, text="Exit", command=exit_program)
    exit_button.pack(side=tk.BOTTOM, fill=tk.X)

    # Start the main application loop
    root.mainloop()



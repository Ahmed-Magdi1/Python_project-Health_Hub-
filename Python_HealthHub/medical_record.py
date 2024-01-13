import tkinter as tk
from tkinter import ttk
from tkinter import ttk, messagebox
from doc_page import *
import csv

def exit_program():
    root.destroy()

def add_patient_data():
    # Retrieve data from entries
    name = name_entry.get()
    number = number_entry.get()
    medical_info = medical_info_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()

    # Check if all fields are filled
    if name and number and medical_info and age and gender:
        # Insert data into the table
        table.insert('', 'end', values=(name, number, medical_info, age, gender))
        # Save data to a CSV file
        with open('patient_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, number, medical_info, age, gender])

        # Clear the entries after insertion
        name_entry.delete(0, tk.END)
        number_entry.delete(0, tk.END)
        medical_info_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        gender_entry.delete(0, tk.END)
    else:
        print("Warning", "Please fill all the fields.")
        messagebox.showerror("Error", "Please fill all the fields.")


def load_patient_data():
    try:
        with open('patient_data.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                table.insert('', 'end', values=row)
    except FileNotFoundError:
        # File not found, which means no data has been saved yet
        pass

def medical_info():
    global root, name_entry, number_entry, medical_info_entry, age_entry, gender_entry, table
    root = tk.Tk()
    root.title("Patient Informations")

    # Create a frame for the Entry widgets and Add button
    entry_frame = tk.Frame(root)
    entry_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

    # Entry widgets and their labels
    tk.Label(entry_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(entry_frame)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(entry_frame, text="Number:").grid(row=1, column=0, padx=5, pady=5)
    number_entry = tk.Entry(entry_frame)
    number_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(entry_frame, text="Medical Information:").grid(row=2, column=0, padx=5, pady=5)
    medical_info_entry = tk.Entry(entry_frame)
    medical_info_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(entry_frame, text="Age:").grid(row=3, column=0, padx=5, pady=5)
    age_entry = tk.Entry(entry_frame)
    age_entry.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(entry_frame, text="Gender:").grid(row=4, column=0, padx=5, pady=5)
    gender_entry = tk.Entry(entry_frame)
    gender_entry.grid(row=4, column=1, padx=5, pady=5)

    # Add button to insert data into the table
    add_button = tk.Button(entry_frame, text="Add Patient", command=add_patient_data)
    add_button.grid(row=5, column=0, columnspan=2, pady=5)

    # Treeview widget to display the medical records
    table = ttk.Treeview(root, columns=('Name', 'Number', 'Medical Information', 'Age', 'Gender'))
    table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    table['columns'] = ('Name', 'Number', 'Medical Information', 'Age', 'Gender')
    table.heading("Name", text="Name", anchor=tk.W)
    table.column("Name", anchor=tk.W, width=200)

    table.heading("Number", text="Number", anchor=tk.W)
    table.column("Number", anchor=tk.W, width=200)

    table.heading("Medical Information", text="Medical Information", anchor=tk.W)
    table.column("Medical Information", anchor=tk.W, width=200)

    table.heading("Age", text="Age", anchor=tk.W)
    table.column("Age", anchor=tk.W, width=200)

    table.heading("Gender", text="Gender", anchor=tk.W)
    table.column("Gender", anchor=tk.W, width=200)

    load_patient_data()

    exit_button = tk.Button(root, text="Exit", bg="red", fg="white", font=("Helvetica", 14), command=exit_program)
    exit_button.pack(side=tk.BOTTOM, fill=tk.X)
    exit_button.config(bg='blue', fg='red')

    root.mainloop()


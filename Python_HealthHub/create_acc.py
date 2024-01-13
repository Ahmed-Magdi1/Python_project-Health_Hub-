import csv
import tkinter as tk
from tkinter import messagebox

class createaccount:
    def __init__(self, root):
        self.root = root
        self.root.title('New_Account')
        # Create the input fields and labels
        self.username_label = tk.Label(root, text="Username:")
        self.username_entry = tk.Entry(root)
        self.password_label = tk.Label(root, text="Password:")
        self.password_entry = tk.Entry(root)
        self.role_label = tk.Label(root, text="Role:")
        self.role_entry = tk.Entry(root)

        # Create the "Add User Data" button
        self.add_user_data_button = tk.Button(root, text="Create Account", command=self.add_user_data)

        # Position the widgets on the screen
        self.username_label.grid(row=0, column=0)
        self.username_entry.grid(row=0, column=1)
        self.password_label.grid(row=1, column=0)
        self.password_entry.grid(row=1, column=1)
        self.role_label.grid(row=2, column=0)
        self.role_entry.grid(row=2, column=1)
        self.add_user_data_button.grid(row=3, column=1)

    def add_user_data(self):
        # Get the user data from the entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_entry.get()

        # Check if all the fields are filled in
        if not username or not password or not role:
            messagebox.showwarning("Error", "Please complete all the fields.")
            return

        # Open the file in append mode ('a') and create a new CSV writer object
        with open('users.csv', 'a', newline='') as csvfile:
            user_writer = csv.writer(csvfile)

            # Write the user data as a new row in the CSV file
            user_writer.writerow([username, password, role])

        # Show a success message box
        messagebox.showinfo("Success", f"Added user {username} with role {role}!")

        # Close the GUI window
        self.root.destroy()


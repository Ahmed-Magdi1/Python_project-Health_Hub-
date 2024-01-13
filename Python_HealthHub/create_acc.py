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


        self.add_user_data_button = tk.Button(root, text="Create Account", command=self.add_user_data)


        self.username_label.grid(row=0, column=0)
        self.username_entry.grid(row=0, column=1)
        self.password_label.grid(row=1, column=0)
        self.password_entry.grid(row=1, column=1)
        self.role_label.grid(row=2, column=0)
        self.role_entry.grid(row=2, column=1)
        self.add_user_data_button.grid(row=3, column=1)

    def add_user_data(self):

        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_entry.get()


        if not username or not password or not role:
            messagebox.showwarning("Error", "Please complete all the fields.")
            return


        with open('users.csv', 'a', newline='') as csvfile:
            user_writer = csv.writer(csvfile)


            user_writer.writerow([username, password, role])


        messagebox.showinfo("Success", f"Added user {username} with role {role}!")


        self.root.destroy()


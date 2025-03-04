# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 17:36:52 2025

@author: user
"""

import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

# Path to save the contact data
contact_file = "contacts.json"

# Function to load contacts from the file
def load_contacts():
    if os.path.exists(contact_file):
        with open(contact_file, "r") as file:
            return json.load(file)
    return []

# Function to save contacts to the file
def save_contacts():
    with open(contact_file, "w") as file:
        json.dump(contacts, file, indent=4)

# Initialize the contact list
contacts = load_contacts()

# Function to add a contact
def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    address = entry_address.get().strip()

    if name and phone and email and address:
        if not phone.isdigit() or len(phone) != 10:
            messagebox.showwarning("Input Error", "Phone number must be 10 digits.")
            return
        if "@" not in email or "." not in email:
            messagebox.showwarning("Input Error", "Please enter a valid email address.")
            return

        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        save_contacts()
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields.")

# Function to update the contact list display
def update_contact_list():
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to search a contact by name or phone
def search_contact():
    search_term = entry_search.get().lower()
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['phone'].lower():
            listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to update selected contact
def update_contact():
    selected_contact_index = listbox_contacts.curselection()
    if selected_contact_index:
        index = selected_contact_index[0]
        contact = contacts[index]
        entry_name.delete(0, tk.END)
        entry_name.insert(0, contact['name'])
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, contact['phone'])
        entry_email.delete(0, tk.END)
        entry_email.insert(0, contact['email'])
        entry_address.delete(0, tk.END)
        entry_address.insert(0, contact['address'])
        
        # Remove the old contact
        del contacts[index]
        save_contacts()
        update_contact_list()

# Function to delete selected contact
def delete_contact():
    selected_contact_index = listbox_contacts.curselection()
    if selected_contact_index:
        index = selected_contact_index[0]
        del contacts[index]
        save_contacts()
        update_contact_list()

# Function to clear all input fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# Setting up the main window
window = tk.Tk()
window.title("Contact Management System")
window.geometry("600x500")
window.configure(bg="#f0f0f0")

# Styling
style = ttk.Style()
style.configure("TButton", padding=5, relief="flat", background="#ccc")
style.configure("TFrame", background="#f0f0f0")
style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
style.configure("TEntry", font=("Arial", 10))

# Contact Form Section
frame_form = ttk.Frame(window)
frame_form.pack(padx=10, pady=10, fill="x")

label_name = ttk.Label(frame_form, text="Name:")
label_name.grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_name = ttk.Entry(frame_form, width=40)
entry_name.grid(row=0, column=1)

label_phone = ttk.Label(frame_form, text="Phone:")
label_phone.grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_phone = ttk.Entry(frame_form, width=40)
entry_phone.grid(row=1, column=1)

label_email = ttk.Label(frame_form, text="Email:")
label_email.grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_email = ttk.Entry(frame_form, width=40)
entry_email.grid(row=2, column=1)

label_address = ttk.Label(frame_form, text="Address:")
label_address.grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_address = ttk.Entry(frame_form, width=40)
entry_address.grid(row=3, column=1)

# Buttons Section
frame_buttons = ttk.Frame(window)
frame_buttons.pack(padx=10, pady=10, fill="x")

button_add = ttk.Button(frame_buttons, text="Add Contact", command=add_contact)
button_add.grid(row=0, column=0, padx=5, pady=5)

button_update = ttk.Button(frame_buttons, text="Update Contact", command=update_contact)
button_update.grid(row=0, column=1, padx=5, pady=5)

button_delete = ttk.Button(frame_buttons, text="Delete Contact", command=delete_contact)
button_delete.grid(row=0, column=2, padx=5, pady=5)

button_clear = ttk.Button(frame_buttons, text="Clear Fields", command=clear_entries)
button_clear.grid(row=0, column=3, padx=5, pady=5)

# Search Section
frame_search = ttk.Frame(window)
frame_search.pack(padx=10, pady=10, fill="x")

label_search = ttk.Label(frame_search, text="Search (Name/Phone):")
label_search.grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_search = ttk.Entry(frame_search, width=30)
entry_search.grid(row=0, column=1, padx=5, pady=5)

button_search = ttk.Button(frame_search, text="Search", command=search_contact)
button_search.grid(row=0, column=2, padx=5, pady=5)

# Contact List Section
frame_list = ttk.Frame(window)
frame_list.pack(padx=10, pady=10, fill="both", expand=True)

label_contacts = ttk.Label(frame_list, text="Contact List:")
label_contacts.grid(row=0, column=0, sticky="w", padx=5, pady=5)

listbox_contacts = tk.Listbox(frame_list, height=10, width=50, selectmode=tk.SINGLE)
listbox_contacts.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

# Scrollbar for the contact list
scrollbar = ttk.Scrollbar(frame_list, orient="vertical", command=listbox_contacts.yview)
scrollbar.grid(row=1, column=1, sticky="ns")
listbox_contacts.configure(yscrollcommand=scrollbar.set)

# Start the Tkinter event loop
update_contact_list()  # Load the contact list initially
window.mainloop()
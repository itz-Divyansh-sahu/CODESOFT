import customtkinter as ctk
from tkinter import messagebox
from assets.contact_manager import add_contact, generate_new_id


def open_add_contact(app, refresh_callback):
    add_window = ctk.CTkToplevel(app)
    add_window.title("Add Contact")
    add_window.geometry("450x520")
    add_window.grab_set()

    ctk.CTkLabel(
        add_window,
        text="Add New Contact",
        font=("Arial", 22, "bold")
    ).pack(pady=15)

    # ---------------- INPUTS ----------------
    name_entry = ctk.CTkEntry(add_window, placeholder_text="Name", width=300)
    name_entry.pack(pady=10)

    phone_entry = ctk.CTkEntry(add_window, placeholder_text="Phone", width=300)
    phone_entry.pack(pady=10)

    email_entry = ctk.CTkEntry(add_window, placeholder_text="Email", width=300)
    email_entry.pack(pady=10)

    address_box = ctk.CTkTextbox(add_window, width=300, height=100)
    address_box.pack(pady=10)

    # ---------------- STATUS LABEL ----------------
    status_label = ctk.CTkLabel(add_window, text="", text_color="green")
    status_label.pack(pady=5)

    # ---------------- SAVE FUNCTION ----------------
    def save_contact():

        name = name_entry.get().strip()
        phone = phone_entry.get().strip()
        email = email_entry.get().strip()
        address = address_box.get("1.0", "end").strip()

        if not all([name, phone, email, address]):
            status_label.configure(text="All fields are required", text_color="red")
            return

        new_contact = {
            "id": generate_new_id(),
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }

        add_contact(new_contact)

        refresh_callback()

        status_label.configure(text="✓ Contact Added Successfully", text_color="lightgreen")

        add_window.after(1000, add_window.destroy)

    # ---------------- BUTTON ----------------
    ctk.CTkButton(
        add_window,
        text="Add Contact",
        command=save_contact
    ).pack(pady=20)
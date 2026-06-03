import customtkinter as ctk
from tkinter import messagebox
from assets.contact_manager import update_contact


def open_edit_contact(app, contact, refresh_callback):
    edit_window = ctk.CTkToplevel(app)
    edit_window.title("Edit Contact")
    edit_window.geometry("450x520")
    edit_window.grab_set()

    ctk.CTkLabel(
        edit_window,
        text="Edit Contact",
        font=("Arial", 22, "bold")
    ).pack(pady=15)

    # ---------------- INPUTS ----------------
    name_entry = ctk.CTkEntry(edit_window, width=300)
    name_entry.pack(pady=10)
    name_entry.insert(0, contact["name"])

    phone_entry = ctk.CTkEntry(edit_window, width=300)
    phone_entry.pack(pady=10)
    phone_entry.insert(0, contact["phone"])

    email_entry = ctk.CTkEntry(edit_window, width=300)
    email_entry.pack(pady=10)
    email_entry.insert(0, contact["email"])

    address_box = ctk.CTkTextbox(edit_window, width=300, height=100)
    address_box.pack(pady=10)
    address_box.insert("1.0", contact["address"])

    # ---------------- STATUS ----------------
    status_label = ctk.CTkLabel(edit_window, text="", text_color="green")
    status_label.pack(pady=5)

    # ---------------- SAVE CHANGES ----------------
    def save_changes():

        updated_contact = {
            "id": contact["id"],
            "name": name_entry.get().strip(),
            "phone": phone_entry.get().strip(),
            "email": email_entry.get().strip(),
            "address": address_box.get("1.0", "end").strip()
        }

        if not all([
            updated_contact["name"],
            updated_contact["phone"],
            updated_contact["email"],
            updated_contact["address"]
        ]):
            status_label.configure(text="All fields are required", text_color="red")
            return

        update_contact(updated_contact)

        refresh_callback()

        status_label.configure(text="✓ Updated Successfully", text_color="lightgreen")

        edit_window.after(1000, edit_window.destroy)

    # ---------------- BUTTON ----------------
    ctk.CTkButton(
        edit_window,
        text="Save Changes",
        command=save_changes
    ).pack(pady=20)
import customtkinter as ctk

from tkinter import messagebox
from assets.contact_manager import load_contacts
from assets.contact_manager import search_contacts
from assets.contact_manager import delete_contact  # optional if you add delete
from assets.add_page import open_add_contact
from assets.edit_page import open_edit_contact
from PIL import Image


edit_icon = ctk.CTkImage(
light_image=Image.open("assets/edit.png"),
dark_image=Image.open("assets/edit.png"),
size=(18, 18)
)

# ---------------- SETTINGS ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---------------- APP WINDOW ----------------
app = ctk.CTk()
app.title("Contact Book")
app.geometry("950x750")
app.configure(fg_color="#1d2430")


# ---------------- MAIN FRAME ----------------
main_frame = ctk.CTkFrame(
    app,
    width=600,
    height=550,
    fg_color="#ebe4c6",
    corner_radius=10
)
main_frame.place(relx=0.5, rely=0.5, anchor="center")


# ---------------- TITLE ----------------
title_label = ctk.CTkLabel(
    app,
    text="Contact Book",
    font=("Comic Sans MS", 36, "bold"),
    text_color="white"
)
title_label.place(relx=0.5, y=60, anchor="center")


# ---------------- CONTACT LABEL ---------------- 
contacts_label = ctk.CTkLabel( main_frame, text="Contacts", 
                              font=("Komika Axis", 29, "bold"), 
                              text_color="black" ) 
contacts_label.place(x=65, y=16)

tooltip_label = ctk.CTkLabel(
    app,
    text="",
    fg_color="#222222",
    text_color="white",
    corner_radius=6,
    padx=2,
    pady=2
)

tooltip_label.place_forget()
tooltip_label.lift()
# ---------------- SEARCH ----------------
search_entry = ctk.CTkEntry(
    main_frame,
    width=160,
    height=40,
    placeholder_text="Search contact",
    fg_color="white",
    text_color="black",
    placeholder_text_color="gray",
    border_width=0
)
search_entry.place(x=340, y=25)

total_label = ctk.CTkLabel(
    main_frame,
    text="Total: 0",
    font=("Bahnschrift", 14, "bold"),
    text_color="black"
)
total_label.place(x=60, y=70)

# ---------------- CONTACT FRAME ----------------
contacts_frame = ctk.CTkScrollableFrame(
    main_frame,
    width=480,
    height=390,
    fg_color="#dcdcdc"
)
contacts_frame.place(x=60, y=100)

def show_tooltip(widget, text):
    tooltip_label.configure(text=text)

    widget.update_idletasks()

    x = widget.winfo_rootx() + widget.winfo_width()
    y = widget.winfo_rooty()

    tooltip_label.place(x=x, y=y)


def hide_tooltip(event=None):
    tooltip_label.place_forget()

# ---------------- REFRESH FUNCTION ----------------
def refresh_contacts(contact_list=None):

    for widget in contacts_frame.winfo_children():
        widget.destroy()

    if contact_list is None:
        contact_list = load_contacts()

    if not contact_list:
        ctk.CTkLabel(
            contacts_frame,
            text="No Contacts Found",
            text_color="gray30"
        ).pack(pady=20)
        return
    
    total_label.configure(
    text=f"Total Contacts: {len(contact_list)}"
    )

    for contact in contact_list:

        card = ctk.CTkFrame(
            contacts_frame,
            fg_color="white",
            corner_radius=8
        )
        card.pack(fill="x", padx=5, pady=5)


        # ---------------- NAME ----------------
        ctk.CTkLabel(
            card,
            text=contact["name"],
            font=("Arial", 15, "bold"),
            text_color="black"
        ).pack(side="left", padx=10)


        # ---------------- RIGHT SIDE BUTTON HOLDER ----------------
        btn_frame = ctk.CTkFrame(card, fg_color="transparent")
        btn_frame.pack(side="right", padx=5)


        # ---------------- EDIT BUTTON ----------------
        edit_btn = ctk.CTkButton(
            btn_frame,
            image=edit_icon,
            text="",
            width=28,
            height=28,
            fg_color="transparent",
            text_color="black",
            hover_color="#e0e0e0",
            command=lambda c=contact: open_edit_contact(app, c, refresh_contacts)
        )
        edit_btn.pack(side="left", padx=2)
        edit_btn.bind("<Enter>", lambda e, b=edit_btn: show_tooltip(b, "Edit Contact"))
        edit_btn.bind("<Leave>", hide_tooltip)


        # ---------------- DELETE BUTTON ----------------
        delete_btn = ctk.CTkButton(
            btn_frame,
            text="🗑",
            width=28,
            height=28,
            fg_color="red",
            hover_color="#cc0000",
            command=lambda cid=contact["id"]: remove_contact(cid, refresh_contacts)
        )
        delete_btn.pack(side="left", padx=2)
        delete_btn.bind("<Enter>", lambda e, b=delete_btn: show_tooltip(b, "Delete Contact"))
        delete_btn.bind("<Leave>", hide_tooltip)

# ---------------- DELETE WRAPPER ----------------


def remove_contact(contact_id, refresh_callback):

    confirm = messagebox.askyesno(
        "Delete Contact",
        "Are you sure you want to delete this contact?"
    )

    if confirm:
        delete_contact(contact_id)
        refresh_callback()


# ---------------- SEARCH FUNCTION ----------------
def on_search(event=None):

    query = search_entry.get()

    results = search_contacts(query)

    refresh_contacts(results)


search_entry.bind("<KeyRelease>", on_search)


# ---------------- ADD BUTTON ----------------
add_btn = ctk.CTkButton(
    main_frame,
    text="+",
    font=("Comic Sans MS", 25, "bold"),
    width=50,
    height=38,
    fg_color="black",
    command=lambda: open_add_contact(app, refresh_contacts)
)
add_btn.place(x=510, y=25)
add_btn.bind("<Enter>", lambda e: show_tooltip(add_btn, "Add Contact"))
add_btn.bind("<Leave>", hide_tooltip)



# ---------------- INITIAL LOAD ----------------
refresh_contacts()

app.mainloop()
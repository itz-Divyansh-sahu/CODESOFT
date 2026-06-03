import json
import customtkinter as ctk

FILE_NAME = "contacts.json"


# ---------------- JSON ----------------

def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# ---------------- ID ----------------

def generate_new_id():

    contacts = load_contacts()

    return max(
        [contact["id"] for contact in contacts],
        default=0
    ) + 1


# ---------------- CRUD ----------------

def add_contact(contact):

    contacts = load_contacts()

    contacts.append(contact)

    save_contacts(contacts)


def update_contact(updated_contact):

    contacts = load_contacts()

    for i, contact in enumerate(contacts):

        if contact["id"] == updated_contact["id"]:
            contacts[i] = updated_contact
            break

    save_contacts(contacts)


def delete_contact(contact_id):

    contacts = load_contacts()

    contacts = [
        contact
        for contact in contacts
        if contact["id"] != contact_id
    ]

    save_contacts(contacts)



# ---------------- SEARCH ----------------

def search_contacts(query):

    contacts = load_contacts()

    if not query:
        return contacts

    return [
        contact
        for contact in contacts
        if query.lower() in contact["name"].lower()
    ]
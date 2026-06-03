from customtkinter import *
import customtkinter as ctk

root = ctk.CTk()

root.title("Rock Paper Scissors Game")
root.geometry("800x400")

frame = CTkFrame(master=root)
frame.pack(pady=20, padx=20)
frame.place(relx=0.5, rely=0.5)
label = CTkLabel(
    master=root,
    text="Welcome !!",
    font=("Bloody", 40)
)
label.pack()

label2 = CTkLabel(
    master=frame,
    text="Rock Paper Scissors Game",
    font=("Arial", 30)
)
label2.pack(pady=(20,10))

root.mainloop()
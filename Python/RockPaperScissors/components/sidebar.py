import sys
import customtkinter as ctk
class Sidebar(ctk.CTkFrame):

    def __init__(self, master, controller):
        super().__init__(
            master,
            width=180,
            fg_color="#111111",
            border_width=2,
            border_color="#FFFFFF"
        )

        self.controller = controller

        self.pack_propagate(False)

        # -----------------------------
        # Title
        # -----------------------------
        title = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=(30, 50))

        # -----------------------------
        # Navigation Frame
        # -----------------------------
        nav_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        nav_frame.pack(expand=True)

        # -----------------------------
        # Buttons
        # -----------------------------
        self.buttons = {}

        menu_items = [
            ("Home", "home"),
            ("Game", "game"),
            ("History", "history"),
            ("About", "about")
        ]

        for text, page in menu_items:

            btn = ctk.CTkButton(
                nav_frame,
                text=text,
                width=140,
                height=45,
                corner_radius=12,
                fg_color="transparent",
                border_width=1,
                border_color="#444444",
                hover_color="#2563EB",
                font=("Comic Sans MS", 16, "bold"),
                command=lambda p=page: self.navigate(p)
            )

            btn.pack(pady=10)

            self.buttons[page] = btn

        exit_btn = ctk.CTkButton(
        self,
        text="Exit",
        width=140,
        height=45,
        corner_radius=12,
        fg_color="#DC2626",        # red color
        hover_color="#B91C1C",     # darker red on hover
        text_color="white",
        font=("Arial", 16, "bold"),
        command=self.exit_app
        )

        exit_btn.pack(pady=(30, 10))    

    # ==================================
    # Navigation
    # ==================================

    def navigate(self, page_name):

        self.controller.show_page(page_name)

        self.highlight_button(page_name)

    # ==================================
    # Active Button Highlight
    # ==================================

    def highlight_button(self, active_page):

        for page, button in self.buttons.items():

            if page == active_page:

                button.configure(
                    fg_color="#2563EB",
                    border_color="#2563EB"
                )

            else:

                button.configure(
                    fg_color="transparent",
                    border_color="#444444"
                )

    def exit_app(self):
     self.controller.destroy()            
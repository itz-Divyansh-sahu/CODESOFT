import customtkinter as ctk


class HomePage(ctk.CTkFrame):

    def __init__(self, master, controller):
        super().__init__(master, fg_color="#26477E")

        self.controller = controller

        # store selected button safely
        self.selected_button = None
        self.selected_round_value = None

        self.create_widgets()

    # ================= UI =================

    def create_widgets(self):

        # TITLE
        ctk.CTkLabel(
            self,
            text="WELCOME TO !!",
            font=("Arial", 42, "bold"),
            text_color="black"
        ).pack(pady=(40, 5))

        ctk.CTkLabel(
            self,
            text="ROCK PAPER SCISSORS GAME",
            font=("Arial Rounded MT Bold", 34),
            text_color="white"
        ).pack()

        # SPACER
        ctk.CTkFrame(self, fg_color="transparent", height=60).pack()

        # SELECT LABEL
        ctk.CTkLabel(
            self,
            text="Select Round",
            font=("Cascadia Code", 32, "bold"),
            text_color="white"
        ).pack(pady=20)

        # ROUND FRAME
        round_frame = ctk.CTkFrame(self, fg_color="transparent")
        round_frame.pack(pady=20)

        # BUTTONS
        self.btn5 = self.create_round_button(round_frame, "5", 0, 5)
        self.btn10 = self.create_round_button(round_frame, "10", 1, 10)
        self.btn12 = self.create_round_button(round_frame, "12", 2, 12)

        # NEXT BUTTON
        self.next_btn = ctk.CTkButton(
            self,
            text="NEXT",
            width=180,
            height=50,
            font=("Arial", 22, "bold"),
            fg_color="#1E293B",
            state="disabled",
            command=self.start_game
        )
        self.next_btn.pack(pady=50)

        # RULES
        rules_frame = ctk.CTkFrame(
            self,
            fg_color="#000000",
            corner_radius=15
        )
        rules_frame.pack(side="bottom", pady=25, padx=25, fill="x")

        ctk.CTkLabel(
            rules_frame,
            text="Rules",
            font=("Arial", 20, "bold")
        ).pack(pady=(10, 5))

        ctk.CTkLabel(
            rules_frame,
            text="• Rock beats Scissors\n• Scissors beats Paper\n• Paper beats Rock",
            justify="left",
            font=("Arial", 16)
        ).pack(pady=(0, 15))

    # ================= BUTTON FACTORY =================

    def create_round_button(self, parent, text, col, value):

        btn = ctk.CTkButton(
            parent,
            text=text,
            width=90,
            height=90,
            corner_radius=45,
            font=("Arial", 28, "bold"),
            fg_color="white",
            text_color="black",
            command=lambda: self.select_round(value)
        )

        btn.grid(row=0, column=col, padx=30)

        return btn

    # ================= ROUND SELECTION =================

    def select_round(self, rounds):

        # save selected value
        self.controller.selected_rounds = rounds
        self.selected_round_value = rounds

        # reset all buttons
        for btn in [self.btn5, self.btn10, self.btn12]:
            btn.configure(fg_color="white", text_color="black",hover_color="#e4e189")

        # highlight selected
        selected_map = {
            5: self.btn5,
            10: self.btn10,
            12: self.btn12
        }

        selected_map[rounds].configure(
            fg_color="#22C55E",
            text_color="white"
        )

        self.next_btn.configure(state="normal")

    # ================= START GAME =================

    def start_game(self):

        if not self.controller.selected_rounds:
            return

        self.controller.reset_game()
        self.controller.current_round = 1   # IMPORTANT

        self.controller.show_page("game")
    def reset_selection(self):

        self.selected_round_value = None

        for btn in [self.btn5, self.btn10, self.btn12]:
            btn.configure(
                fg_color="white",
                text_color="black"
            )

        self.next_btn.configure(
            state="disabled"
        )   
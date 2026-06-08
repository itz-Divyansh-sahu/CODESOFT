import customtkinter as ctk
import webbrowser


class AboutPage(ctk.CTkFrame):

    def __init__(self, master, controller):
        super().__init__(master, fg_color="#1E293B")

        self.controller = controller
        self.create_ui()

    # ================= LINKS =================

    def open_linkedin(self):
        webbrowser.open("https://www.linkedin.com/in/coder-divyansh-sahu")

    def open_github(self):
        webbrowser.open("https://github.com/itz-Divyansh-sahu")

    def open_email(self):
        webbrowser.open("mailto:divyanshsahuf@gmail.com")

    # ================= UI =================

    def create_ui(self):

        # TITLE
        title = ctk.CTkLabel(
            self,
            text="ABOUT THE GAME",
            font=("Segoe UI Variable", 34, "bold"),
            text_color="white"
        )
        title.pack(pady=(30, 10))

        # DESCRIPTION BOX
        desc_frame = ctk.CTkFrame(
            self,
            fg_color="#111827",
            corner_radius=15
        )
        desc_frame.pack(pady=20, padx=30, fill="x")

        desc_text = (
            "Rock Paper Scissors is a simple yet classic hand game "
            "played between you and the computer. This game is built "
            "using Python and CustomTkinter with a modern UI design.\n"
            "The goal is to win more rounds than the AI opponent. "
            "Each round is unpredictable as the AI makes random moves."
        )

        ctk.CTkLabel(
            desc_frame,
            text=desc_text,
            font=("Segoe UI Variable", 16),
            justify="left",
            wraplength=800
        ).pack(padx=20, pady=20)

        # RULES SECTION
        rules_title = ctk.CTkLabel(
            self,
            text="GAME RULES",
            font=("Segoe UI Variable", 26, "bold"),
            text_color="white"
        )
        rules_title.pack(pady=(20, 10))

        rules_frame = ctk.CTkFrame(
            self,
            fg_color="#111827",
            corner_radius=15
        )
        rules_frame.pack(padx=30, fill="x")

        rules = (
            "• Rock beats Scissors\n"
            "• Scissors beats Paper\n"
            "• Paper beats Rock\n"
            "• Same choice results in a Tie\n"
            "• Each match has selected number of rounds\n"
            "• Player with highest score wins the match"
        )

        ctk.CTkLabel(
            rules_frame,
            text=rules,
            font=("Segoe UI Variable", 16),
            justify="left"
        ).pack(padx=20, pady=20)

        # HOW TO PLAY
        guide_title = ctk.CTkLabel(
            self,
            text="HOW TO PLAY",
            font=("Segoe UI Variable", 26, "bold"),
            text_color="white"
        )
        guide_title.pack(pady=(20, 10))

        guide_frame = ctk.CTkFrame(
            self,
            fg_color="#111827",
            corner_radius=15
        )
        guide_frame.pack(padx=30, fill="x")

        guide = (
            "1. Select number of rounds from Home page\n"
            "2. Click 'Next' to start the game\n"
            "3. Choose Rock, Paper, or Scissors in each round\n"
            "4. AI will automatically make its move\n"
            "5. Result and score will update instantly\n"
            "6. After all rounds, final winner will be shown\n"
            "7. You can view match history anytime"
        )

        ctk.CTkLabel(
            guide_frame,
            text=guide,
            font=("Segoe UI Variable", 16),
            justify="left"
        ).pack(padx=20, pady=20)

        # ================= FOOTER =================

        footer_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        footer_frame.pack(pady=30)

        footer = ctk.CTkLabel(
            footer_frame,
            text="Built using Python • CustomTkinter • PIL",
            font=("Segoe UI Variable", 14),
            text_color="gray"
        )
        footer.pack()

        author = ctk.CTkLabel(
            footer_frame,
            text="MADE BY: DIVYANSH SAHU",
            font=("Segoe UI Variable", 15, "bold"),
            text_color="white"
        )
        author.pack(pady=(8, 12))

        # Social Links
        links_frame = ctk.CTkFrame(
        footer_frame,
        fg_color="transparent"
        )

        ctk.CTkButton(
            links_frame,
            text="LinkedIn",
            width=5,
            command=self.open_linkedin
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            links_frame,
            text="GitHub",
            width=5,
            command=self.open_github
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            links_frame,
            text="Email",
            width=5,
            command=self.open_email
        ).pack(side="left", padx=5)
        links_frame.pack(pady=2)
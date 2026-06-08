import customtkinter as ctk


class HistoryPage(ctk.CTkFrame):

    def __init__(self, master, controller):
        super().__init__(
            master,
            fg_color="#26477E"
        )

        self.controller = controller

        self.create_ui()

    # ==========================================
    # UI
    # ==========================================

    def create_ui(self):

        # TITLE

        title = ctk.CTkLabel(
            self,
            text="MATCH HISTORY",
            font=("Arial", 34, "bold"),
            text_color="white"
        )

        title.pack(pady=(20, 10))

        # SCROLLABLE AREA

        self.scroll_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            width=750,
            height=550
        )

        self.scroll_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.load_history()

    # ==========================================
    # REFRESH
    # ==========================================

    def refresh(self):
        self.load_history()

    # ==========================================
    # LOAD HISTORY
    # ==========================================

    def load_history(self):

        # clear old cards

        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        # no matches

        if not self.controller.match_history:

            empty = ctk.CTkLabel(
                self.scroll_frame,
                text="No Matches Played Yet",
                font=("Arial", 24, "bold"),
                text_color="white"
            )

            empty.pack(pady=50)

            return

        # newest first

        history = list(reversed(self.controller.match_history))

        for index, match in enumerate(history, start=1):

            result = match["result"]

            # -----------------------------
            # CARD COLOR
            # -----------------------------

            if "YOU WON" in result:

                card_color = "#0FDC5A"
                status = "WON"

            elif "DRAW" in result:

                card_color = "#F7C636"
                status = "DRAW"

            else:

                card_color = "#F92E2E"
                status = "DEFEAT"

            # -----------------------------
            # CARD
            # -----------------------------

            card = ctk.CTkFrame(
                self.scroll_frame,
                fg_color=card_color,
                corner_radius=20,
                height=150
            )

            card.pack(
                fill="x",
                padx=20,
                pady=10
            )

            # MATCH NUMBER

            ctk.CTkLabel(
                card,
                text=f"Match : {len(history) - index + 1}",
                font=("Arial", 20, "bold"),
                text_color="white"
            ).pack(
                anchor="w",
                padx=20,
                pady=(15, 5)
            )

            # STATUS

            ctk.CTkLabel(
                card,
                text=status,
                font=("Arial", 28, "bold"),
                text_color="white"
            ).pack()

            # ROUND

            ctk.CTkLabel(
                card,
                text=f"Round : {match['rounds']}",
                font=("Arial", 18, "bold"),
                text_color="white"
            ).pack()

            # SCORE

            ctk.CTkLabel(
                card,
                text=f"You : {match['player']}      Computer: {match['ai']}",
                font=("Arial", 18, "bold"),
                text_color="white"
            ).pack(
                pady=(5, 15)
            )
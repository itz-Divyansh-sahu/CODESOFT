import customtkinter as ctk
from PIL import Image
from utils.game_logic import get_ai_choice, decide_winner
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def asset_path(filename):
    return os.path.join(BASE_DIR, "assets", filename)


class GamePage(ctk.CTkFrame):

    def __init__(self, master, controller):
        super().__init__(master, fg_color="#26477E")

        self.controller = controller
        self.end_panel = None

        self.load_images()
        self.create_ui()

    # ================= IMAGES =================
    def load_images(self):

        self.rock_img = ctk.CTkImage(Image.open(asset_path("fist.png")), size=(120, 120))
        self.paper_img = ctk.CTkImage(Image.open(asset_path("paper.png")), size=(120, 120))
        self.scissor_img = ctk.CTkImage(Image.open(asset_path("scissor.png")), size=(120, 120))

        self.choice_images = {
            "Rock": self.rock_img,
            "Paper": self.paper_img,
            "Scissors": self.scissor_img
        }

    # ================= UI =================
    def create_ui(self):

        self.round_lbl = ctk.CTkLabel(
            self,
            text="Round 1",
            font=("Lucida Sans Unicode", 28, "bold"),
            text_color="white"
        )
        self.round_lbl.pack(pady=(20, 10))

        score_frame = ctk.CTkFrame(self, fg_color="transparent")
        score_frame.pack(pady=10)

        self.player_score_lbl = ctk.CTkLabel(score_frame, text="Player : 0", font=("Lucida Sans Unicode", 22, "bold"),bg_color="black")
        self.player_score_lbl.grid(row=0, column=0, padx=80)

        self.ai_score_lbl = ctk.CTkLabel(score_frame, text="COMP : 0", font=("Lucida Sans Unicode", 22, "bold"),bg_color="black")
        self.ai_score_lbl.grid(row=0, column=1, padx=80)

        # DISPLAY
        display_frame = ctk.CTkFrame(self, fg_color="transparent")
        display_frame.pack(pady=20)

        ctk.CTkLabel(display_frame, text="PLAYER",font=("Lucida Sans Unicode",18,"bold")).grid(row=0, column=0)

        self.player_choice_lbl = ctk.CTkLabel(
            display_frame,
            text="?",
            width=140,
            height=140,
            corner_radius=70,
            fg_color="white",
            text_color="black",
            font=("Arial", 50, "bold")
        )
        self.player_choice_lbl.grid(row=1, column=0, padx=50)

        ctk.CTkLabel(display_frame, text="VS", font=("Lucida Sans Unicode",18,"bold")).grid(row=1, column=1)

        ctk.CTkLabel(display_frame, text="COMP",font=("Lucida Sans Unicode",18,"bold")).grid(row=0, column=2)

        self.ai_choice_lbl = ctk.CTkLabel(
            display_frame,
            text="?",
            width=140,
            height=140,
            corner_radius=70,
            fg_color="white",
            text_color="black",
            font=("Arial", 50, "bold")
        )
        self.ai_choice_lbl.grid(row=1, column=2, padx=50)

        # BUTTONS
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack()

        ctk.CTkButton(btn_frame, image=self.rock_img, text="", command=lambda: self.make_move("Rock")).grid(row=0, column=0, padx=15)
        ctk.CTkButton(btn_frame, image=self.paper_img, text="", command=lambda: self.make_move("Paper")).grid(row=0, column=1, padx=15)
        ctk.CTkButton(btn_frame, image=self.scissor_img, text="", command=lambda: self.make_move("Scissors")).grid(row=0, column=2, padx=15)

        # RESULT
        self.result_frame = ctk.CTkFrame(self, width=700, height=120, fg_color="#1E293B")
        self.result_frame.pack(pady=25)
        self.result_frame.pack_propagate(False)

        self.result_lbl = ctk.CTkLabel(self.result_frame, text="Make your move!", font=("Arial", 18, "bold"))
        self.result_lbl.pack(expand=True)

    # ================= DISPLAY UPDATE =================
    def update_display(self, player, ai, result):

        self.player_choice_lbl.configure(image=self.choice_images[player], text="")
        self.ai_choice_lbl.configure(image=self.choice_images[ai], text="")

        if result == "Tie":
            msg = f"{player} vs {ai}\nIt's a Tie!"
        elif result == "Player":
            msg = f"{player} beats {ai}\nYOU Win!"
        else:
            msg = f"{ai} beats {player}\nCOMPUTER Win!"

        self.result_lbl.configure(text=msg)

        self.player_score_lbl.configure(text=f"Player : {self.controller.player_score}")
        self.ai_score_lbl.configure(text=f"COMPUTER : {self.controller.ai_score}")

    # ================= MOVE =================
    def make_move(self, player):

        if self.controller.game_over:
            return

        if not self.controller.selected_rounds:
            return

        if self.controller.current_round > self.controller.selected_rounds:
            return

        ai = get_ai_choice()
        result = decide_winner(player, ai)

        if result == "Player":
            self.controller.player_score += 1
        elif result == "AI":
            self.controller.ai_score += 1

        # UPDATE UI
        self.update_display(player, ai, result)

        # CHECK END FIRST
        if self.controller.current_round == self.controller.selected_rounds:
            self.end_game()
            return

        # INCREMENT ONCE ONLY
        self.controller.current_round += 1

        self.round_lbl.configure(
            text=f"Round {self.controller.current_round} / {self.controller.selected_rounds}"
        )

    # ================= END GAME =================
    def end_game(self):

        self.controller.game_over = True

        p = self.controller.player_score
        a = self.controller.ai_score

        if p > a:
            result = "YOU WON THE MATCH!"
        elif a > p:
            result = "COMPUTER WON THE MATCH!"
        else:
            result = "MATCH DRAW!"

        self.controller.save_match(result)
        self.show_end_panel(result)

    # ================= END PANEL =================
    def show_end_panel(self, text):

        if self.end_panel:
            self.end_panel.destroy()

        self.end_panel = ctk.CTkFrame(self, fg_color="#111111",width=45,height=45)
        self.end_panel.pack(pady=15,padx=15)

        ctk.CTkLabel(self.end_panel, text=text, font=("Arial", 22, "bold")).pack(pady=10)

        ctk.CTkButton(self.end_panel, text="Play Again", command=self.restart_game).pack(pady=5)
        ctk.CTkButton(self.end_panel, text="History", command=lambda: self.controller.show_page("history")).pack(pady=5)

    # ================= RESTART =================
    def restart_game(self):

        self.controller.reset_game()
        self.controller.game_over = False
        self.controller.current_round = 1

        self.reset_ui()
        self.controller.show_page("home")

    # ================= RESET UI =================
    def reset_ui(self):

        if self.end_panel:
            self.end_panel.destroy()
            self.end_panel = None

        self.player_choice_lbl.configure(image=None, text="?")
        self.ai_choice_lbl.configure(image=None, text="?")

        self.player_score_lbl.configure(text="Player : 0")
        self.ai_score_lbl.configure(text="COMP : 0")

        self.round_lbl.configure(text="Round 1")
        self.result_lbl.configure(text="Make your move!")
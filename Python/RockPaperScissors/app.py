import customtkinter as ctk

from pages.home_page import HomePage
from pages.game_page import GamePage
from pages.history_page import HistoryPage
from pages.about_page import AboutPage
from components.sidebar import Sidebar

from utils.game_logic import get_ai_choice, decide_winner


class RockPaperScissorsApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        # ==========================================
        # WINDOW
        # ==========================================
        self.title("Rock Paper Scissors")
        self.geometry("1100x700")
        self.minsize(1000, 650)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # ==========================================
        # GAME STATE
        # ==========================================
        self.selected_rounds = None

        self.current_round = 1
        self.player_score = 0
        self.ai_score = 0

        self.game_over = False

        # history
        self.match_history = []
        self.match_number = 1

        # ==========================================
        # SIDEBAR
        # ==========================================
        self.sidebar = Sidebar(self, self)
        self.sidebar.pack(side="left", fill="y")

        # ==========================================
        # MAIN CONTAINER
        # ==========================================
        self.container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        self.container.pack(
            side="right",
            fill="both",
            expand=True
        )

        # ==========================================
        # PAGES
        # ==========================================
        self.pages = {}

        self.create_pages()

        self.show_page("home")

    # ==========================================
    # CREATE PAGES
    # ==========================================
    def create_pages(self):

        self.pages["home"] = HomePage(
            self.container,
            self
        )

        self.pages["game"] = GamePage(
            self.container,
            self
        )

        self.pages["history"] = HistoryPage(
            self.container,
            self
        )

        self.pages["about"] = AboutPage(
            self.container,
            self
        )

        for page in self.pages.values():
            page.place(
                relwidth=1,
                relheight=1
            )

    # ==========================================
    # NAVIGATION
    # ==========================================
    def show_page(self, page_name):

        # block direct game access
        if page_name == "game" and self.selected_rounds is None:
            return

        self.pages[page_name].tkraise()

        self.sidebar.highlight_button(page_name)

        # always refresh history
        if page_name == "history":
            self.pages["history"].load_history()

    # ==========================================
    # GAME ROUND
    # ==========================================
    def play_round(self, player_choice):

        if self.game_over:
            return None, None, None

        ai_choice = get_ai_choice()

        result = decide_winner(
            player_choice,
            ai_choice
        )

        if result == "Player":
            self.player_score += 1

        elif result == "AI":
            self.ai_score += 1

        return (
            player_choice,
            ai_choice,
            result
        )

    # ==========================================
    # RESET GAME
    # ==========================================
    def reset_game(self):

        self.current_round = 1

        self.player_score = 0
        self.ai_score = 0

        self.game_over = False

    # ==========================================
    # LOCK GAME
    # ==========================================
    def lock_game(self):

        self.game_over = True

    # ==========================================
    # SAVE MATCH
    # ==========================================
    def save_match(self, result_text):

        self.match_history.append(
            {
                "match": self.match_number,
                "rounds": self.selected_rounds,
                "player": self.player_score,
                "ai": self.ai_score,
                "result": result_text
            }
        )

        self.match_number += 1
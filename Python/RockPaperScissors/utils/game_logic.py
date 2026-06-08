import random

CHOICES = ["Rock", "Paper", "Scissors"]


def get_ai_choice():
    return random.choice(CHOICES)


def decide_winner(player, ai):

    if player == ai:
        return "Tie"

    if (
        (player == "Rock" and ai == "Scissors") or
        (player == "Paper" and ai == "Rock") or
        (player == "Scissors" and ai == "Paper")
    ):
        return "Player"

    return "AI"


def update_score(result, score):
    player_score, ai_score = score

    if result == "Player":
        player_score += 1
    elif result == "AI":
        ai_score += 1

    return player_score, ai_score
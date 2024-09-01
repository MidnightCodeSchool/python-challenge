import pytest


def test_file_exists():
    global rock_paper_scissors
    try:
        from p003_if_elif_else import rock_paper_scissors
    except ModuleNotFoundError as e:
        fname = str(e).split(" ")[-1]
        raise FileNotFoundError(
            f"{fname} not found. Are you naming the file correctly?"
        )


def test_rock_paper_scissors_draw():
    assert rock_paper_scissors("rock", "rock") == "draw"
    assert rock_paper_scissors("paper", "paper") == "draw"
    assert rock_paper_scissors("scissors", "scissors") == "draw"


def test_rock_paper_scissors_player1_wins():
    assert rock_paper_scissors("rock", "scissors") == "player_1_wins"
    assert rock_paper_scissors("paper", "rock") == "player_1_wins"
    assert rock_paper_scissors("scissors", "paper") == "player_1_wins"


def test_rock_paper_scissors_player2_wins():
    assert rock_paper_scissors("scissors", "rock") == "player_2_wins"
    assert rock_paper_scissors("rock", "paper") == "player_2_wins"
    assert rock_paper_scissors("paper", "scissors") == "player_2_wins"


def test_rock_paper_scissors_invalid_choice():
    with pytest.raises(ValueError):
        rock_paper_scissors("rock", "invalid")
    with pytest.raises(ValueError):
        rock_paper_scissors("invalid", "scissors")
    with pytest.raises(ValueError):
        rock_paper_scissors("invalid", "invalid")

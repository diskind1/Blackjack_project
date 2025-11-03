

def ask_player_action() -> str:

    player_choice = ""
    while player_choice.lower() != "h" and player_choice.lower() != "s":
        player_choice = input("Enter your choice ('H' / 'S':    ")

    if player_choice.lower() == "h":
        return "H"
    else:
        return "S"



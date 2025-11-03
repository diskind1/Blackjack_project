from deck import card_value
from player_io import ask_player_action


def calculate_hand_value(hand: list[dict]) -> int:

    hand_value = 0
    for card in hand:
        value = card_value(card)
        hand_value += value

    return hand_value


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player["hand"] = [deck.pop(),deck.pop()]
    dealer["hand"] = [deck.pop(),deck.pop()]
    print(player,dealer)





def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while sum(dealer) <= 17:
        dealer["hand"] = [deck.pop()]
    if sum(dealer) > 21:
        return False
    return True



def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck,player,dealer)
    while ask_player_action().upper() == "H":
        player["hand"] = [deck.pop()]
        calculate_hand_value(player["hand"])
        if sum(player["hand"]) > 21:
            print("Player disqualified, dealer wins")
            break
        else:
            continue
     dealer_play(deck)
    if player["hand"] > dealer["hand"]:
        print("Player wins, dealer disqualified")
    if dealer["hand"]: > player["hand"]:
        print("Player disqualified, dealer wins")


    return None

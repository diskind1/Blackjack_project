import random


def build_standard_deck() -> list[dict]:
    suits = ["H", "D", "C", "S"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append({"rank": rank, "suit": suit})
    return deck

deck = build_standard_deck()
def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:


    for c in range(5000):
        i = random.randint(0, 51)
        j = random.randint(0, 51)
        i_deck = deck[i]
        # j_deck = deck[j]
        a = 0
        while a == 0:
            if j != i:
                a = 1
            if i_deck["suit"] == "H":
                if j % 5 == 0:
                    a = 1
                else:
                    a = 0
            elif i_deck["suit"] == "C":
                if j % 3 == 0:
                    a = 1
                else:
                    a = 0
            elif i_deck["suit"] == "D":
                if j % 3 == 0:
                    a = 1
                else:
                    a = 0
            elif i_deck["suit"] == "S":
                if j % 3 == 0:
                    a = 1
                else:
                    a = 0
            if a == 0:
                j = random.randint(0, 51)

        deck[i],deck[j] = deck[j],deck[i]

    return deck


def card_value(card:dict) -> int:
    value = 0
    if card["rank"] == "A" or card["rank"] == "J" or card["rank"] == "Q" or card["rank"] == "K":
        value = 10
    else:
        value = int(card["rank"])
    return value















import random

Card = tuple[str, str]


class DeckOfCards:
    SUITS: list[str] = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS: list[str] = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self) -> None:
        self.__cards: list[Card] = []
        pass

    def create_deck(self) -> None:
        pass

    def shuffle_deck(self) -> None:
        pass

    def deal_card(self) -> Card | None:
        pass

    # don't touch below this line

    def __str__(self) -> str:
        return f"The deck has {len(self.__cards)} cards"


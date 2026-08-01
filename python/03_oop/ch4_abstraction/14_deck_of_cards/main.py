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
        self.create_deck()        
    def create_deck(self) -> None:
        
        for s in self.SUITS:
            for r in self.RANKS:
                self.__cards.append((r,s))

    def shuffle_deck(self) -> None:
        random.shuffle(self.__cards)

    def deal_card(self) -> Card | None:
        if len(self.__cards):
            return self.__cards.pop()
        return None

    # don't touch below this line

    def __str__(self) -> str:
        return f"The deck has {len(self.__cards)} cards"


SUITS: list[str] = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS: list[str] = [
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
    "Ace",
]


class Card:
    

    def __init__(self, rank: str, suit: str) -> None:
        self.rank=rank
        self.suit=suit
        self.rank_index=RANKS.index(rank)
        self.suit_index=SUITS.index(suit)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other,Card):
            return False
        return self.rank_index==other.rank_index and self.suit_index==other.suit_index
    def __lt__(self, other: "Card") -> bool:
        if self.rank_index<other.rank_index:
            return True
        if self.rank_index==other.rank_index and self.suit_index<other.suit_index:
            return True
        return False


    def __gt__(self, other: "Card") -> bool:
        if self.rank_index>other.rank_index:
            return True
        if self.rank_index==other.rank_index and self.suit_index>other.suit_index:
            return True
        return False

    # don't touch below this line

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
class Round:
    def resolve_round(self) -> int:
        raise NotImplementedError("Subclasses must implement resolve_round()")


# Don't touch above this line
"""
We will be building a simple game where we compare two cards and depending on the round (high or low) determine the winner.

    HighCardRound: The highest card wins
    LowCardRound: The lowest card wins

    Complete the HighCardRound class that inherits from Round:
        Create a constructor that takes two cards (card1 and card2) and stores them as instance variables.
        Implement the resolve_round(self) -> int method that returns an integer:
            1 if card1 is higher than card2
            2 if card2 is higher than card1
            0 if the cards are equal
    Complete the LowCardRound class that inherits from Round:
        Create a constructor that takes two cards (card1 and card2) and stores them as instance variables.
        Implement a resolve_round(self) -> int method that returns an integer:
            1 if card1 is lower than card2
            2 if card2 is lower than card1
            0 if the cards are equal

"""

class HighCardRound(Round):
    def __init__(self,card1 :"Card",card2 :"Card"):
        self.card1=card1
        self.card2=card2
    def resolve_round(self) -> int:
        if self.card1>self.card2:
            return 1 
        if self.card1<self.card2:
            return 2
        return 0


class LowCardRound(Round):
    def __init__(self,card1 :"Card",card2 :"Card"):
        self.card1=card1
        self.card2=card2
    def resolve_round(self) -> int:
        if self.card1<self.card2:
            return 1 
        if self.card1>self.card2:
            return 2
        return 0


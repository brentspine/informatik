from enum import Enum
import random


class UnoCard:
    def __init__(self, display):
        self.display = display


class UnoCards(Enum):
    GP2 = UnoCard("Green +2")
    GReverse = UnoCard("Green Reverse")
    GExpose = UnoCard("Green Expose")
    G0 = UnoCard("Green 0")
    G1 = UnoCard("Green 1")
    G2 = UnoCard("Green 2")
    G3 = UnoCard("Green 3")
    G4 = UnoCard("Green 4")
    G5 = UnoCard("Green 5")
    G6 = UnoCard("Green 6")
    G7 = UnoCard("Green 7")
    G8 = UnoCard("Green 8")
    G9 = UnoCard("Green 9")

    YP2 = UnoCard("Yellow +2")
    YReverse = UnoCard("Yellow Reverse")
    YExpose = UnoCard("Yellow Expose")
    Y0 = UnoCard("Yellow 0")
    Y1 = UnoCard("Yellow 1")
    Y2 = UnoCard("Yellow 2")
    Y3 = UnoCard("Yellow 3")
    Y4 = UnoCard("Yellow 4")
    Y5 = UnoCard("Yellow 5")
    Y6 = UnoCard("Yellow 6")
    Y7 = UnoCard("Yellow 7")
    Y8 = UnoCard("Yellow 8")
    Y9 = UnoCard("Yellow 9")

    BP2 = UnoCard("Blue +2")
    BReverse = UnoCard("Blue Reverse")
    BExpose = UnoCard("Blue Expose")
    B0 = UnoCard("Blue 0")
    B1 = UnoCard("Blue 1")
    B2 = UnoCard("Blue 2")
    B3 = UnoCard("Blue 3")
    B4 = UnoCard("Blue 4")
    B5 = UnoCard("Blue 5")
    B6 = UnoCard("Blue 6")
    B7 = UnoCard("Blue 7")
    B8 = UnoCard("Blue 8")
    B9 = UnoCard("Blue 9")

    RP2 = UnoCard("Red +2")
    RReverse = UnoCard("Red Reverse")
    RExpose = UnoCard("Red Expose")
    R0 = UnoCard("Red 0")
    R1 = UnoCard("Red 1")
    R2 = UnoCard("Red 2")
    R3 = UnoCard("Red 3")
    R4 = UnoCard("Red 4")
    R5 = UnoCard("Red 5")
    R6 = UnoCard("Red 6")
    R7 = UnoCard("Red 7")
    R8 = UnoCard("Red 8")
    R9 = UnoCard("Red 9")

    SWish = UnoCard("Wish")
    Swish4 = UnoCard("Wish +4")

    Empty = UnoCard("Empty")


def generate_random():
    return random.randint(0, len([e.value for e in UnoCards.value]) - 1)

# Fixed card drawing program

import itertools
import random

def build_deck() -> list[tuple[int, str]]:
    """Create a standard 52-card deck."""
    suits = ['Spade', 'Heart', 'Diamond', 'Club']
    values = range(1, 14)
    return list(itertools.product(values, suits))

def rank_to_name(value: int) -> str:
    """Map card numeric value to human-readable rank."""
    return {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}.get(value, str(value))


def draw_cards(count: int = 5) -> list[tuple[int, str]]:
    """Shuffle and draw a number of cards from the deck."""
    deck = build_deck()
    random.shuffle(deck)
    if not 0 < count <= len(deck):
        raise ValueError('count must be between 1 and 52')
    return deck[:count]


def main() -> None:
    print('You got:')
    for value, suit in draw_cards(5):
        print(f"{rank_to_name(value)} of {suit}")


if __name__ == '__main__':
    main()

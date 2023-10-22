from app_poker.core.hand_calculator import HandCalculator
from app_poker.model.hand import Hand
from app_poker.model.card import Card
from app_poker.model.suit import Suit
from app_poker.config.standard.hand_rank import HandRank
from app_poker.config.standard.card_ranks import card_ranks
from app_poker.model.card_values import (
    ace_card_value,
    king_card_value,
    queen_card_value,
    jack_card_value,
    ten_card_value,
)

hand_calculator = HandCalculator()


def test_calculate_highest_hand_rank_returns_royal_flush_for_diamonds():
    suit = Suit.Diamonds
    cards = [
        Card(ace_card_value, suit, card_ranks[ace_card_value]),
        Card(king_card_value, suit, card_ranks[king_card_value]),
        Card(queen_card_value, suit, card_ranks[queen_card_value]),
        Card(jack_card_value, suit, card_ranks[jack_card_value]),
        Card(ten_card_value, suit, card_ranks[ten_card_value]),
    ]
    hand = Hand(cards)
    expected_result = HandRank.ROYAL_FLUSH

    assert expected_result == hand_calculator.calculate_highest_hand_rank(hand)


def test_calculate_highest_hand_rank_returns_royal_flush_for_clubs():
    suit = Suit.Clubs
    cards = [
        Card(ace_card_value, suit, card_ranks[ace_card_value]),
        Card(king_card_value, suit, card_ranks[king_card_value]),
        Card(queen_card_value, suit, card_ranks[queen_card_value]),
        Card(jack_card_value, suit, card_ranks[jack_card_value]),
        Card(ten_card_value, suit, card_ranks[ten_card_value]),
    ]
    hand = Hand(cards)
    expected_result = HandRank.ROYAL_FLUSH

    assert expected_result == hand_calculator.calculate_highest_hand_rank(hand)


def test_calculate_highest_hand_rank_returns_royal_flush_for_hearts():
    suit = Suit.Hearts
    cards = [
        Card(ace_card_value, suit, card_ranks[ace_card_value]),
        Card(king_card_value, suit, card_ranks[king_card_value]),
        Card(queen_card_value, suit, card_ranks[queen_card_value]),
        Card(jack_card_value, suit, card_ranks[jack_card_value]),
        Card(ten_card_value, suit, card_ranks[ten_card_value]),
    ]
    hand = Hand(cards)
    expected_result = HandRank.ROYAL_FLUSH

    assert expected_result == hand_calculator.calculate_highest_hand_rank(hand)


def test_calculate_highest_hand_rank_returns_royal_flush_for_spades():
    suit = Suit.Spades
    cards = [
        Card(ace_card_value, suit, card_ranks[ace_card_value]),
        Card(king_card_value, suit, card_ranks[king_card_value]),
        Card(queen_card_value, suit, card_ranks[queen_card_value]),
        Card(jack_card_value, suit, card_ranks[jack_card_value]),
        Card(ten_card_value, suit, card_ranks[ten_card_value]),
    ]
    hand = Hand(cards)
    expected_result = HandRank.ROYAL_FLUSH

    assert expected_result == hand_calculator.calculate_highest_hand_rank(hand)

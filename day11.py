from art11 import logo
from random import choice


def deal_card():
    """Return a new card from the deck (list)"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card


def calculate_score(list_of_cards):
    """Take a list of cards and return the score of it"""
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0
    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    return sum(list_of_cards)


def compare(user_scores, computer_scores):
    if user_scores == computer_scores:
        return 'Draw'
    elif computer_scores == 0:
        return 'You lose, opponent has BlackJack'
    elif user_scores == 0:
        return 'You won with BlackJack'
    elif user_scores > 21:
        return 'You went over, you lose'
    elif computer_scores > 21:
        return 'The computer went over, you won'
    elif user_scores > computer_scores:
        return 'You win'
    else:
        return 'You lose'


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f'Your cards: {user_cards}, current score: {user_score}')
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input('Type "y" to get another card, type "n" to pass: ')
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f'Your final hand is: {user_cards}, your final score is: {user_score}')
    print(f"Computer's final hand is: {computer_cards}, its final score is: {computer_score}")
    print(compare(user_score, computer_score))


while input('Do you want to play a game of BlackJack? Type "y" or "n": ') == 'y':
    play_game()

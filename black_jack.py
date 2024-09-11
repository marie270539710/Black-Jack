import random
import os

_MESSAGE_WIN = "Congratulations!!! You win!!!"
_MESSAGE_LOSE = "You lose. So Sorry."

# flowers (Flowers) and Card values
flowers = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
card_numbers = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
                'A': 11}


# Function to clear the console (works for both Windows and Unix-based systems)
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to deal a random card with its suit
def deal_card():
    """Returns a tuple representing a card (value, suit)."""
    card = random.choice(list(card_numbers.keys()))
    suit = random.choice(flowers)
    return card, suit


# Function to calculate the score of a hand
def calculate_score(hand):
    """Returns the score calculated from a hand."""
    score = 0
    ace_count = 0
    for card, suit in hand:
        score += card_numbers[card]
        if card == 'A':
            ace_count += 1

    # Adjust for Aces (count Ace as 1 if score > 21)
    while score > 21 and ace_count:
        score -= 10
        ace_count -= 1

    return score


# Function to display a deck/hand (with flowers)
def display_hand(hand):
    """This area displays the hand as card values with its corresponding flowers."""
    return ', '.join([f"{card} of {suit}" for card, suit in hand])


# Function to compare scores
def compare(player_score, ai_score):
    """Compares the scores and determines the result."""
    if player_score == ai_score:
        return "It's a draw! You got a tie!"
    elif ai_score == 0:
        return "Computer has a Blackjack! "+_MESSAGE_LOSE
    elif player_score == 0:
        return "You have a Blackjack! "+_MESSAGE_WIN
    elif player_score > 21:
        return "You went over 21. "+_MESSAGE_LOSE
    elif ai_score > 21:
        return "Computer went over 21. "+_MESSAGE_WIN
    elif player_score > ai_score:
        return "Congratulations!!!You win!!!"
    else:
        return "You lose. So Sorry."


# Main game function
def blackjack_game():
    print("***---Welcome to FishOn's Blackjack Game!---***")

    while True:
        # Deal initial cards
        user_hand = [deal_card(), deal_card()]
        computer_hand = [deal_card(), deal_card()]

        game_over = False

        while not game_over:
            player_score = calculate_score(user_hand)
            ai_score = calculate_score(computer_hand)

            print(f"\nYour cards on deck: {display_hand(user_hand)}, current score: {player_score}")
            print(f"Computer's first card on deck: {computer_hand[0][0]} of {computer_hand[0][1]}")

            # Check for blackjack or if user goes over 21
            if player_score == 0 or ai_score == 0 or player_score > 21:
                game_over = True
            else:
                # Ask the user if they want to draw another card
                user_should_continue = input("\nType 'y' to get another card, 'n' to pass: ").lower()
                if user_should_continue == 'y':
                    user_hand.append(deal_card())
                else:
                    game_over = True

        # Computer's turn: Keep drawing if score is less than or equal to 16
        while ai_score != 0 and ai_score < 17:
            computer_hand.append(deal_card())
            ai_score = calculate_score(computer_hand)

        # Display final hands and scores
        print(f"\nYour final hand on deck: {display_hand(user_hand)}, final score: {player_score}")
        print(f"Computer's final hand on deck: {display_hand(computer_hand)}, final score: {ai_score}")
        print(compare(player_score, ai_score))

        # Ask the user if they want to play again
        play_again = input("\nDo you want to play again? Type 'y' or 'n': ").lower()
        if play_again == 'y':
            clear_console()  # Clear the console for a fresh start
        else:
            print("***---Thank you for playing!---***")
            break

# Run the game
blackjack_game()

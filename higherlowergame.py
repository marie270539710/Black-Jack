import random

# Data for the game
data = [
    {'name': 'Instagram', 'follower_count': 346, 'description': 'Social media platform', 'country': 'United States'},
    {'name': 'Cristiano Ronaldo', 'follower_count': 215, 'description': 'Footballer', 'country': 'Portugal'},
    {'name': 'Ariana Grande', 'follower_count': 183, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Dwayne Johnson', 'follower_count': 181, 'description': 'Actor and professional wrestler', 'country': 'United States'},
    {'name': 'Selena Gomez', 'follower_count': 174, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Kylie Jenner', 'follower_count': 172, 'description': 'Reality TV personality and businesswoman and Self-Made Billionaire', 'country': 'United States'},
    # More data entries here...
]

def get_random_account():
    """Returns a random account from the data."""
    return random.choice(data)

def format_account(account):
    """Formats the account data for display."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}"

def play_game():
    score = 0
    account_a = get_random_account()
    account_b = get_random_account()

    # Make sure A and B are different
    while account_a == account_b:
        account_b = get_random_account()

    game_should_continue = True
    while game_should_continue:
        print(f"Compare A: {format_account(account_a)}")
        print("vs")
        print(f"Compare B: {format_account(account_b)}")

        # Ask the user for a guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Get follower count
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        # Check if user is correct
        is_correct = (guess == "a" and a_follower_count > b_follower_count) or (guess == "b" and b_follower_count > a_follower_count)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
            account_a = account_b  # Move account B to account A for the next round
            account_b = get_random_account()

            # Ensure account_b is different from account_a
            while account_a == account_b:
                account_b = get_random_account()

        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")

# Start the game
play_game()

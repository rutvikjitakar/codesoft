import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def play_round(user_score, computer_score):
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()

    computer_choice = get_computer_choice()
    print(f"Computer chose {computer_choice}")

    winner = get_winner(user_choice, computer_choice)
    if winner == 'user':
        print("You win!")
        user_score += 1
    elif winner == 'computer':
        print("You lose!")
        computer_score += 1
    else:
        print("It's a tie!")

    return user_score, computer_score

def main():
    user_score = 0
    computer_score = 0
    play_again = 'y'

    while play_again.lower() == 'y':
        user_score, computer_score = play_round(user_score, computer_score)
        print(f"Score: You {user_score} - Computer {computer_score}")
        play_again = input("Do you want to play another round? (Y/N): ")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()

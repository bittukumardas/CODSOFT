import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors):  ").lower()
    options = ["rock", "paper", "scissors"]
    if player_choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return get_choices()
    computer_choice = random.choice(options)
    return {"player": player_choice, "computer": computer_choice}

def check_win(player, computer):
    print(f"You chose: {player}, computer chose: {computer}")
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return f"{player.capitalize()} beats {computer}! You win!"
    else:
        return f"{computer.capitalize()} beats {player}! You lose."

def play_game():
    while True:
        choices = get_choices()
        result = check_win(choices["player"], choices["computer"])
        print(result)

        con = input("Do you want to continue (Y for yes/N for no)?: ").strip().upper()
        if con == 'N':
            print("THANK YOU!")
            break
        elif con != 'Y':
            print("Invalid input, exiting the game.")
            break

if __name__ == "__main__":
    play_game()

exit()


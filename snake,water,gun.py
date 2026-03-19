print("Welcome To The Snake,Water,Gun game!\n")
print("Description: ")
print("You all have played rock, paper ,scissors Game in your childhood.\nThis Game is completely similar to it.\n")
import random
import time

choices = ["snake","water","gun"]
round_number = 0
computer_points = 0
player_points = 0

emojis = {
    "snake" : "🐍",
    "water" : "🌊",
    "gun"   : "🔫"
}
while True:
    computer = random.choice(choices)
    round_number += 1
    print(f"Round: {round_number}")
    player = input("Enter Your Choice(snake or water or gun): ").lower()
    if player not in choices:
        print("Invalid choice!")

    else:
        print(f"Player choice: {player} {emojis[player]}\n")
        print("Computer is choosing...")
        time.sleep(2)
        print(f"Computer choice: {computer} {emojis[computer]}\n")
        if player == computer:
            print("It's a draw!")

        elif player == "snake" and computer == "water":
            print("Player won!")
            player_points += 1

        elif player == "gun" and computer == "snake":
            print("Player won!")
            player_points += 1

        elif player == "water" and computer == "gun":
            print("Player won!")
            player_points += 1

        elif player == "snake" and computer == "gun":
            print("Computer won!")
            computer_points += 1

        elif player == "water" and computer == "snake":
            print("Computer won!")
            computer_points += 1

        else:
            print("Computer won!")
            computer_points += 1
        play_again = input("Wanna play again?(yes/no): ").lower()
        print()
        if play_again == "no":
            break
        elif play_again == "yes":
            continue
        else:
            print("Invalid Play again choice!")
print(f"Player Total Points: {player_points}")
print(f"Computer Total Points: {computer_points}\n")
if player_points > computer_points:
    print("🙌 You Won The Game!")
elif computer_points > player_points:
    print("💻 Computer Won The Game!")
else:
    print("🤝 Game is a Draw!")
print()
print("Thank You For Playing The Game. Hope You Enjoyed It!")
print("Goodbye!")
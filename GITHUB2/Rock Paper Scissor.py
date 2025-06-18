import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors Game!")
    options = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    while True:
        print("\nChoose: rock, paper, scissors or type 'exit' to quit.")
        user_choice = input("Your choice: ").lower()

        if user_choice == "exit":
            print("\nFinal Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

        if user_choice not in options:
            print("Invalid choice. Try again.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

rock_paper_scissors()

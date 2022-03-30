



from random import choice


def determine_winner(user_choice, computer_choice):




if __name__ == "__main__":
    #
    # USER SELECTION
    #
    valid_selections = ["rock", "paper", "scissors"]

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in valid_selections:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(valid_selections)
    #the rock paper scissors list is a duplicate from line 13, we shouldn't have duplication
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    if u == "rock" and c == "rock":
        print("It's a tie!")
    elif u == "rock" and c == "paper":
        print("The computer wins")
    elif u == "rock" and c == "scissors":
        print("The user wins")

    elif u == "paper" and c == "rock":
        print("The computer wins")
    elif u == "paper" and c == "paper":
        print("It's a tie!")
    elif u == "paper" and c == "scissors":
        print("The user wins")

    elif u == "scissors" and c == "rock":
        print("The computer wins")
    elif u == "scissors" and c == "paper":
        print("The user wins")
    elif u == "scissors" and c == "scissors":
        print("It's a tie!")
    
    winner = determine_winner(u,c)
    if winner = 

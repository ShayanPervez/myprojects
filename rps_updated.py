print("**** ROCK, PAPER, SCISSOR GAME****\n Player vs Computer\n\n")


from random import randint
player_wins = 0
comp_wins = 0
winning_score = 3
while (player_wins < winning_score) and (comp_wins<winning_score):
    print(f'computer score {comp_wins} , player score {player_wins}')
    player = input("Player , make your move: ").lower()
    if player== "quit" or player == "q":
        break
    rand_num = randint(0,2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissor"
    print(f"computer plays: {computer}")

    if player == computer:
        print("It's a tie")
    elif player == "rock":
        if computer == "scissor":
             print("Player, wins")
             player_wins += 1
        else:
            print("computer, wins")
            comp_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("Player , wins")
            player_wins += 1
        else:
            print("computer, wins")
            comp_wins += 1
    elif player == "scissor":
        if computer =="rock":
            print("computer , wins")
            comp_wins += 1
        else:
            print("Player, wins ")
            player_wins += 1

    else:
        print("Please enter a valid move")
if player_wins >comp_wins:
    print("CONGRATS, You Won!!")

elif player_wins == comp_wins:
    print("IT'S A TIE")

else:
    print("OH NO :( THE COMPUTER WON")

print(f'FINAL SCORE: computer score {comp_wins} , player score {player_wins}')

import random
import math

def play_RPS():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors ")
    user = user.lower() #we wanna make sure if doesn't go wrong even with upper case so converting everything to lower case

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return(0,user, computer) #computer and user ties
    if is_win(user,computer):
        return(1,user, computer)#user wins this round
    else:
        return(-1,user, computer) #user loses this round

def is_win(player, opponent):
    if ((player =="p" and opponent =="r") or (player == "r" and opponent =="s") or (player =="s" and opponent =="p")):
        return True
    return False

def majority_wins(n):
    no_of_player_wins = 0
    no_of_computer_wins = 0
    no_of_wins_necessary = math.ceil(n/2)
    total_games = 0
    while (no_of_computer_wins < no_of_wins_necessary) and (no_of_player_wins < no_of_wins_necessary) and (total_games < how_many_games):
        result,user,computer = play_RPS()
        total_games +=1
        if result == 0:
            print("You and computer tied you chose {} and computer chose {}".format(user,computer))
        elif result == 1:
            no_of_player_wins +=1
            print("You won, you chose {} and computer chose {}".format(user,computer))
        else:
            print("You lose, you chose {} and computer chose {}".format(user,computer))
            no_of_computer_wins += 1
    # print(no_of_computer_wins)
    # print(no_of_player_wins)


    if no_of_player_wins > no_of_computer_wins:
        print("You won best out of {} games! Congrats :) ".format(n))
    elif no_of_player_wins == no_of_computer_wins:
        print("You and computer drawd this match out of {} games! Haha wanna play again? :) ".format(n))   
    else:
        print("Oh no the computer has won the best out of {} games! Better luck next time :) ".format(n))

how_many_games = int(input("How many games do you wanna play "))
majority_wins(how_many_games)

    



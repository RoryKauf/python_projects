import random

d = {1: "rock", 2: "paper", 3: "scissors"}

def who_won(user_win_counter, comp_win_counter):
    if user_win_counter > comp_win_counter:
        print (f"The final score is {user_win_counter} to you and {comp_win_counter} to the computer. You won!! Bye")
    elif user_win_counter == comp_win_counter:
        print (f"The final score is {user_win_counter} to you and {comp_win_counter} to the computer. It's a draw! Bye")
    else:
        print(f"The final score is {user_win_counter} to you and {comp_win_counter} to the computer. You lost!! Bye")

def inner_game(user_choice, comp_choice, user_win_counter, comp_win_counter):
    if (user_choice.lower() == "rock" and comp_choice == "scissors") or (
            user_choice.lower() == "paper" and comp_choice == "rock") or (
            user_choice.lower() == "scissors" and comp_choice):
        print(f"The computer chose {comp_choice}. You've won!")
        user_win_counter += 1
        print(f"The score is {user_win_counter} to you, {comp_win_counter} to the computer\n")
    elif user_choice.lower() == comp_choice:
        print(f"The computer chose {comp_choice}. It's a draw!")
        print(f"The score is {user_win_counter} to you, {comp_win_counter} to the computer\n")
    else:
        print(f"The computer chose {comp_choice}. You've lost")
        comp_win_counter += 1
        print(f"The score is {user_win_counter} to you, {comp_win_counter} to the computer\n")
    return user_win_counter, comp_win_counter

def rps_game(user_choice):
    comp_choice = d[random.randint(1, 3)]
    user_win_counter = 0
    comp_win_counter = 0
    user_win_counter, comp_win_counter = inner_game(user_choice, comp_choice, user_win_counter, comp_win_counter)
    while True:
        try:
            another_game_q = input("Would you like to play again? Y/N\n")
            while another_game_q.lower() == "y":
                while True:
                    try:
                        comp_choice = d[random.randint(1, 3)]
                        user_choice = input("Please type rock, paper or scissors\n")
                        if user_choice.lower() in d.values():
                            user_win_counter, comp_win_counter = inner_game(user_choice, comp_choice, user_win_counter,
                                                                            comp_win_counter)
                            break
                        else:
                            print("please only enter rock paper or scissors\n")
                    except:
                        break
                another_game_q = input("Would you like to play again? Y/N\n")
            if another_game_q.lower() == "n":
                who_won(user_win_counter, comp_win_counter)
                break
            else:
                print("Please only enter y or n\n")
                continue
        except:
            continue

while True:
    try:
        user_choice = input("Please type rock, paper or scissors\n")
        if user_choice.lower() in d.values():
            rps_game(user_choice)
            break
        else:
            print("please only enter rock paper or scissors\n")
    except:
        continue
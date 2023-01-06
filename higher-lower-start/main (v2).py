import random
import os
from art import logo
from art import vs
from game_data import data

def main():
    print(logo)
    
    game_start()
    
    print("You are correct!")
    print(f"Your current score is: {player_score}")

        start_again = input(f"Game over. Your score is {player_score}. Want to try again? y/n: ")
    if start_again == "y":
        os.system('clear')
        main()

def game_start():
    a = rand_name(data)
    b = rand_name(data)
    
    print(f"Compare A: {a['name']}, a {a['description']} from {a['country']}")
    print(vs)
    print(f"With B: {b['name']}, a {b['description']} from {b['country']}")
    
    
    guess = input(f"{b['name']}'s follower count is '<' or '>' than {a['name']}: ")

    guess_correct = guess_check(a['follower_count'], b['follower_count'], guess) 
    
    if guess_correct == True:
        print(logo)
        os.system('clear')
        print(logo)

        game_start()
        
    
    else:
        return False



def rand_name(dictionary):
    return random.choice(dictionary)

def guess_check(followers_a,followers_b,user_guess):
    """
    Check if user correctly guessed that B is higher or lower than A
    """
    #Win-lose conditions
    if followers_b > followers_a and user_guess == ">":
        return True
    elif followers_b < followers_a and user_guess == "<":
        return True
    else:
        print("You are wrong.")
        return False

def add_score(guess_correct, player_score):
    if guess_correct == True:
        return player_score + 1
        

main()
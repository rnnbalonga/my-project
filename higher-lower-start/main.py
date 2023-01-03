import random
import os
from art import logo
from art import vs
from game_data import data

def main():
    print(logo)
    
    #Initialize game. This section should keep going as long as player guesses correctly.
    game_end = False
    player_score = 0
    
    while game_end == False:
        a, b, guess = game()

        answer_correct = check_guess(a, b, guess)

        if answer_correct == True:
            player_score = add_current_score(answer_correct, player_score)
            os.system('clear')
            print(logo)
            print(f"Your current score is: {player_score} \n")

        else:
            game_end = True
            print(f"Game over. Your score is: {player_score}. \n")
            if input("Want to start a new game? y/n: ") == "y":
                os.system('clear')
                main()
            

def game():
    """
    Print related gaming text using the values of a and b. Returns values of person_a, person_b, and guess.
    """
    rand_dict = rand_people()
    person_a = rand_dict['a']
    person_b = rand_dict['b']
    
    print(f"Compare A: {person_a['name']}, a {person_a['description']} from {person_a['country']}")
    print(vs)
    print(f"With B: {person_b['name']}, a {person_b['description']} from {person_b['country']}\n")

    guess = input(f"Is {person_a['name']}'s follower count higher or lower than {person_b['name']}'s? Type 'h' for higher and 'l' for lower: ")
    
    return person_a, person_b, guess
    

def rand_people():
    person_a = rand_name(data)
    person_b = rand_name(data)

    if person_a == person_b:
        person_a = rand_name(data)
        person_b = rand_name(data)

    return {
        'a': person_a,
        'b': person_b
    }

def rand_name(dictionary):
    return random.choice(dictionary)
    
def check_guess(person_a, person_b,guess):
    """
    Check the follower counts of a and b. Evaluate whether guess == True or Guess == False. Returns True or False
    """
    
    if person_a['follower_count'] > person_b['follower_count'] and guess == "h":
        return True
    elif person_a['follower_count'] < person_b['follower_count'] and guess == "l":
        return True
    else:
        return False

def add_current_score(answer_is_correct, current_score):
    """
    This will evaluate if the answer is correct and add the score if needed. Returns new current score.
    """
    if answer_is_correct == True:
        return current_score + 1
    else:
        return current_score

main()
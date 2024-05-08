#Rules:
# The game starts with a pile of 20 stones between the players
# The two players alternate turns
# On a given turn, a player may take either 1 or 2 stone from the center pile
# The two players continue until the center pile has run out of stones.
# The last player to take a stone loses.

#Requirements:
# Start with 20 stones - create variable remaining stones
# Two players - track which one is being asked for an input
# Get input - make sure that the player only enters either 1 or 2
# Subtract player input from the remaining stones
# Track if game has ended - game will end when remaining stones <= 0
# 

def get_player_choice(player):
    """
    This function will get the player's choice.
    """
    while True:
        player_choice = input(f"Player {player} would you like to remove 1 or 2 stones? ")
        #Check if player_choice is an int or not.
        player_choice = is_int(player_choice)
        break
    if is_1_or_2(player_choice):
            return player_choice
    #Issue is it will only ask player to enter 1 or 2 just once. If the player insists on entering some other int, it will proceed to use that input.
    #Need to find a solution.
    else:
        player_choice = ask_again()
        return player_choice

def is_int(choice):
    """
    Check if player's choice is an integer.
    """
    if type(choice) == int:
        return True
    else:
        return False


def is_1_or_2(choice):
    """
    Check if player's choice is 1 or 2.
    """
    if choice == 1 or choice == 2:
        return True
    else:
        return False

def check_if_valid(choice):
    if is_int(choice) and is_1_or_2(choice):
        return True
    else:
        return False

def ask_again():
    while True:
        player_choice = (input("Please enter 1 or 2: "))
        player_choice = is_int(player_choice)
        if player_choice == 1 or player_choice == 2:
            return player_choice

# def main():
#     """
#     You should write your code here. 
#     """
#     #Create starting variables based on requirements
#     remaining_stones = 20
#     player = 1

#     while remaining_stones > 0:
#         #Ask player how many stones to subtract
#         print(f'There are {remaining_stones} stones left.')
#         subtract = get_player_choice(player)
#         #Substract input from remaining stones
#         remaining_stones -= subtract
#         #Switch player
#         if player == 1:
#             player += 1
#         else:
#             player -= 1
#     print(f"Player {player} wins!")
        
def main():
    print(check_if_valid(3)) #expected answer False
    print(check_if_valid('hey')) #expected answer False
    print(check_if_valid(1)) #expect True
    print(check_if_valid(2)) #expect True
 
 

if __name__ == '__main__':
    main()
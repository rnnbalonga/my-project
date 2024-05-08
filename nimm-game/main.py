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
        user_choice = input(f"Player {player} would you like to remove 1 or 2 stones? ")
        #Check if user_choice is an int or not.
        try:
            user_choice = int(user_choice)
            break
        except ValueError:
            print("Nope")
    if user_choice == 1 or user_choice == 2:
                print("\n")
                return user_choice
    else:
        user_choice = int(input("Please enter 1 or 2: "))
        print("\n")
        return user_choice



def main():
    """
    You should write your code here. 
    """
    #Create starting variables based on requirements
    remaining_stones = 20
    player = 1

    while remaining_stones > 0:
        #Ask player how many stones to subtract
        print(f'There are {remaining_stones} stones left.')
        subtract = get_player_choice(player)
        #Substract input from remaining stones
        remaining_stones -= subtract
        #Switch player
        if player == 1:
            player += 1
        else:
            player -= 1
    print(f"Player {player} wins!")
        
        
 

if __name__ == '__main__':
    main()
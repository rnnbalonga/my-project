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

def main():
    """
    You should write your code here. 
    """
    #Create starting variables based on requirements
    remaining_stones = 20
    player = 1
    game_over = False 

    while not game_over:
        print(f'There are {remaining_stones} stones left')
        game_over = True
        
 

if __name__ == '__main__':
    main()
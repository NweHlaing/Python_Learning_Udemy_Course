#game list declare
game_list = ['0','1','2']

#display function
def display_gamelist(game_list):
    print("Here is current game list")
    print(game_list)
display_gamelist(game_list)

#position choice function
def position_choice():
    choice = 'wrong'
    while choice not in ['0','1','2']:
        choice = input("Pick a position to replace (0,1,2): ")
        if choice not in ['0','1','2']:
            print("Sorry, invalid choice")
    return int(choice)
position_choice()

#replace value function
def replacement_choice(game_list,position):
    user_placement = input("Type a string to place at the position: ")
    game_list[position] = user_placement
    return game_list
replacement_choice(game_list,1)
print("Current game list..",game_list)

#game on function
def gameon_choice():
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input("Would you like to keep playing? Y or N ")
        if choice not in ['Y','N']:
            print("Please make sure to choose Y or N.")
    if choice == "Y":
        # Game is still on
        return True
    else:
        # Game is over
        return False
gameon_choice()

# Variable to keep game playing
game_on = True

game_list = [0,1,2]
while game_on:
    display_gamelist(game_list)
    #Player choose position
    position = position_choice()
    # Rewrite that position and update game_list
    game_list = replacement_choice(game_list, position)
    # Clear Screen and show the updated game list
    display_gamelist(game_list)
    # Ask if you want to keep playing
    game_on = gameon_choice()


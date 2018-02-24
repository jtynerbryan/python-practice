import random
import os

# draw grid
# pick random location for player, exit door, and monster
# draw player in the grid
# take input for movement
# move player unless move is invalid
# check for win or loss
# clear screen and redraw grid

CELLS = [(0,0), (1, 0), (2,0), (3,0), (4,0),
         (0,1), (1, 1), (2,1), (3,1), (4,1),
         (0,2), (1, 2), (2,2), (3,2), (4,2),
         (0,3), (1, 3), (2,3), (3,3), (4,3),
         (0,4), (1, 4), (2,4), (3,4), (4,4)
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_locations():
    return random.sample(CELLS, 3)

def move_player(player, move):
    x, y = player
    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "UP":
        y -= 1
    if move == "DOWN":
        y += 1

    return x, y

def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    x, y = player
    if x == 0:
        moves.remove("LEFT")
    elif x == 4:
        moves.remove("RIGHT")
    elif y == 0:
        moves.remove("UP")
    elif y == 4:
        moves.remove("DOWN")
    return moves

def draw_map(player):
    print(" _"*5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format('X')
            else:
                output = tile.format('_')
        else:
            line_end = '\n'
            if cell == player:
                output = tile.format('X|')
            else:
                output = tile.format('_|')
        print(output, end=line_end)

def win(door, player):
    if player == door:
        return True
    else:
        return False

def lose(monster, player):
    if player == monster:
        return True
    else:
        return False

def play_again():
    play_again = input("Would you like to play again? y/n ")
    if play_again.upper() == "Y":
        return True
    else:
        return False

def game_loop():
    monster, door, player = get_locations()
    while True:
        print(monster, door, player)
        draw_map(player)
        valid_moves = get_moves(player)

        print(f"You're currently in room {player}") # fill with player position
        print(f"You can move {(', ').join(valid_moves)}") # fill with available moves
        print("Enter QUIT to quit")

        move = input ("> ")
        move = move.upper()

        if move == 'QUIT':
            break
        if move in valid_moves:
            player = move_player(player, move)
        else:
            input("Walls are hard, don't run into them!")
        clear_screen()

        if win(door, player):
            print("You found the door out of the dungeon! YOU WIN")
            break
        elif lose(monster, player):
            print("The monster got you! GAME OVER")
            break

    if play_again() == True:
        game_loop()
    else:
        return



clear_screen()
print("Welcome to the dungeon")
input("Press return to start!")
clear_screen()
game_loop()

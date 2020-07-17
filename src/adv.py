from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player('Wade_Watts', room['outside'].name)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

def print_location(room_desc, room_name):
    print(textwrap.fill(f'\n{player1.name} is currently {player1.current_room}.'))

def print_quit():
    print('\n You were not prepared!')

def print_invalid_direction():
    print('\n Nope.')

def move_foyer(move):
    if move == 's':
        foyer_move_s = room["foyer"].s_to
        player1.current_room = foyer_move_s.name
        print_location(foyer_move_s.description, "outside")
    elif move == 'e':
        foyer_move_e = room[player1.current_room.lower()].e_to
        player1.current_room = foyer_move_e.name
        print_location(foyer_move_e.description, "narrow")
    elif move == 'n':
        foyer_move_n = room[player1.current_room.lower()].n_to
        player1.current_room = foyer_move_n.name
        print_location(foyer_move_n.description, "overlook")
    elif move == 'i':
        get_and_drop(room['foyer'])
    elif move != 's' or 'e' or 'n' or 'i':
        print_invalid_direction()

def move_overlook(move):
    if move == 's':
        overlook_move_s = room["overlook"].s_to
        player1.current_room = overlook_move_s.name
        print_location(overlook_move_s.description,"foyer" )
    elif move == 'i':
        get_and_drop(room['overlook'])
    elif move != 's' or 'i':
        print_invalid_direction()

def move_narrow(move):
    if move == 'w':
        narrow_move_w = room["narrow"].w_to
        player1.current_room = narrow_move_w.name
        print_location(narrow_move_w.description, "foyer")
    elif move == 'n':
        narrow_move_n = room["narrow"].n_to
        player1.current_room = narrow_move_n.name
        print_location(narrow_move_n.description, "treasure")
    elif move == 'i':
        get_and_drop(room['narrow'])
    elif move != 'w' or 'n' or 'i':
        print_invalid_direction()

def move_treasure(move):
    if move == 's':
        treasure_move_s = room["treasure"].s_to
        player1.current_room = treasure_move_s.name
        print_location(treasure_move_s.description, "narrow")
    elif move == 'i':
        get_and_drop(room['treasure'])
    elif move != 's' or 'i':
        print_invalid_direction()

def move_outside(move):
    if move == 'n':
        print('\nSo you choose Adventure.')
        new_room = room['outside'].n_to
        player1.current_room = new_room.name
        print_location(new_room.description, "foyer")
    elif move == 'i':
        get_and_drop(room['outside'])
    elif move != 'i' or 'n':
        print('\nYou must not deny destiny, the only path forward is North. Accept faith by choosing n for North')

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


print_location(room['outside'].description, "outside")
while True:
    try:
        
        choices = ['n', 's', 'e', 'w', 'i']
        next_move = input('\n Keep going?')
        print(f"PLAYER.CURRENT_ROOM: {player1.current_room}")
        if next_move == 'q':
            print_quit()
            break 
        if player1.current_room == 'Outside Cave Entrance' or player1.current_room == 'outside' and next_move in choices:
            move_outside(next_move)
            continue
        if player1.current_room == 'Foyer' and next_move in choices:
            move_foyer(next_move)
            continue
        if player1.current_room == 'Grand Overlook' and next_move in choices:
            move_overlook(next_move)
            continue
        if player1.current_room == 'Narrow Passage' and next_move in choices:
            move_narrow(next_move)
            continue
        if player1.current_room == 'Treasure Chamber' and next_move in choices:
            move_treasure(next_move)
            continue

        if next_move not in choices:
            print(f'\n You may only move in the four cardinal directions: n for North, s for South, e for East, w for West')
            continue
    except:
        pass

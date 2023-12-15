"""
Pentominoes game bot.
"""

import random
from logging import DEBUG, debug, getLogger

getLogger().setLevel(DEBUG)


def field_information():
    """
    Parse the info about the field.

    However, the function doesn't do anything with it. Since the height of the field is
    hard-coded later, this bot won't work with maps of different height.

    The input may look like this:

    Plateau 15 17:
    """
    field_info = input()[:-1].split()
    return int(field_info[1]), int(field_info[2])


def parse_field(height: int, length: int):
    """
    Parse the field.

    First of all, this function is also responsible for determining the next
    move. Actually, this function should rather only parse the field, and return
    it to another function, where the logic for choosing the move will be.

    Also, the algorithm for choosing the right move is wrong. This function
    finds the first position of _our_ character, and outputs it. However, it
    doesn't guarantee that the figure will be connected to only one cell of our
    territory. It can not be connected at all (for example, when the figure has
    empty cells), or it can be connected with multiple cells of our territory.
    That's definitely what you should address.

    Also, it might be useful to distinguish between lowecase (the most recent piece)
    and uppercase letters to determine where the enemy is moving etc.

    The input may look like this:

        01234567890123456
    000 .................
    001 .................
    002 .................
    003 .................
    004 .................
    005 .................
    006 .................
    007 ..O..............
    008 ..OOO............
    009 .................
    010 .................
    011 .................
    012 ..............X..
    013 .................
    014 .................

    :param player int: Represents whether we're the first or second player
    """
    _ = input()
    field = []
    for _ in range(height):
        field += [list(input()[4:])]
    return field

def parse_figure():
    """
    Parse the figure.

    The function parses the height of the figure (maybe the width would be
    useful as well), and then reads it.
    It would be nice to save it and return for further usage.

    The input may look like this:

    Piece 2 2:
    **
    ..
    """
    figure = []
    h = int(input().split(' ')[1])
    for _ in range(h):
        figure += [list(input())]
    return figure

def all_possible_moves(player: int, deck: list, figure: list, h_map, l_map):
    if player == 1:
        player1 = 'O'
        player2 = 'X'
    else:
        player1 = 'X'
        player2 = 'O'
    figure1 = []
    for i in figure:
        a1_1=[]
        for j in i:
            a1_1+=[j.replace('*',player1)]
        figure1 += [a1_1]
    figure = figure1
    poss_moves = []
    for i in range(h_map-len(figure)+1):
        for j in range(l_map-len(figure[0])+1):
            count = 0
            trueth = 1
            for h in range(len(figure)):
                for l in range(len(figure[0])): 
                    if deck[i+h][j+l] == player1 and deck[i+h][j+l] == figure[h][l]: count += 1
                    elif deck[i+h][j+l] == player2 and figure[h][l] == player1: trueth = 0
            if count == 1 and trueth==1: poss_moves += [[i, j]]
    return poss_moves




def step(player: int):
    """
    Perform one step of the game.

    :param player int: Represents whether we're the first or second player
    """
    h, w = field_information()
    field = parse_field(h, w)
    moves = all_possible_moves(player, field, parse_figure(), h, w)
    if moves:  # Check if there are valid moves
        rand = [0,1]
        random_move = random.choice(rand)
        move_now = sorted(moves)[-random_move]
        return move_now
    else:
        debug("No valid moves found.")
        return None


def play(player: int):
    """
    Main game loop.

    :param player int: Represents whether we're the first or second player
    """
    while True:
        move = step(player)
        if move is not None:  # Check if move is not None
            print(*move)
        else:
            break  # Exit the loop if there are no valid moves


def parse_info_about_player():
    """
    This function parses the info about the player

    It can look like this:

    $$$ exec p2 : [./player1.py]
    """
    i = input()
    return 1 if "p1 :" in i else 2


def main():
    player = parse_info_about_player()
    try:
        play(player)
    except EOFError:
        debug("Cannot get input. Seems that we've lost ):")


if __name__ == "__main__":
    main()

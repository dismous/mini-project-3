"""
Pentominoes game bot.
"""

from logging import DEBUG, debug, getLogger
getLogger().setLevel(DEBUG)


def get_field_info():
    """
    Parse the field information from the input.
    """
    field_info = input()[:-1].split()
    return int(field_info[1]), int(field_info[2])


def get_field(height, length):
    """
    Parse the field from the input.
    """
    _ = input()
    field = [list(input()[4:]) for _ in range(height)]
    return field


def get_figure():
    """
    Parse the figure from the input.
    """
    figure = []
    figure_height = int(input().split(' ')[1])
    figure = [list(input()) for _ in range(figure_height)]
    return figure


def calculate_possible_moves(player, field, figure, field_height, field_length):
    """
    Calculate all possible moves for the given player, field, and figure.
    Prioritize moves that are closer to the center of the board and block the opponent.
    In the late game, prioritize moves that block the most possible moves for the opponent.
    """
    player1, player2 = ('O', 'X') if player == 1 else ('X', 'O')

    figure = [[cell.replace('*', player1) for cell in row] for row in figure]

    blocking_moves = []
    other_moves = []

    center = [field_height // 2, field_length // 2]

    for i in range(field_height - len(figure) + 1):
        for j in range(field_length - len(figure[0]) + 1):
            count = sum(field[i+h][j+l] == player1 and field[i+h][j+l] == figure[h][l] 
                        for h in range(len(figure)) 
                        for l in range(len(figure[0])))

            is_valid = all(field[i+h][j+l] != player2 or figure[h][l] != player1 
                           for h in range(len(figure)) 
                           for l in range(len(figure[0])))
            
            if count == 1 and is_valid:
                is_blocking = any(field[i+h][j+l] == player2 
                                  for h in range(-1, len(figure)+1) 
                                  for l in range(-1, len(figure[0])+1) 
                                  if 0 <= i+h < field_height and 0 <= j+l < field_length)
                if is_blocking:
                    blocking_moves.append([i, j])
                else:
                    other_moves.append([i, j])

    if abs(center[0] - i) <= 1 and abs(center[1] - j) <= 1:

        blocking_moves.sort(key=lambda move: sum(field[move[0]+h][move[1]+l] == player2 for h in range(-1, len(figure)+1) 
                                                 for l in range(-1, len(figure[0])+1) 
                                                 if 0 <= move[0]+h < field_height and 0 <= move[1]+l < field_length), reverse=True)
    else:
        blocking_moves.sort(key=lambda move: abs(move[0] - center[0]) + abs(move[1] - center[1]))
        other_moves.sort(key=lambda move: abs(move[0] - center[0]) + abs(move[1] - center[1]))

    return blocking_moves + other_moves

def make_move(player):
    """
    Perform a move for the given player.
    """
    field_height, field_length = get_field_info()
    field = get_field(field_height, field_length)
    moves = calculate_possible_moves(player, field, get_figure(), field_height, field_length)
    if moves:
        chosen_move = moves[0]
        return chosen_move
    else:
        debug("No valid moves found.")
        return None


def start_game(player):
    """
    Start the game for the given player.
    """
    while True:
        move = make_move(player)
        if move is not None:
            print(*move)
        else:
            break


def get_player_info():
    """
    Parse the player information from the input.
    """
    i = input()
    return 1 if "p1 :" in i else 2


def main():
    """
    Main function to start the game.
    """
    player = get_player_info()
    try:
        start_game(player)
    except EOFError:
        debug("Cannot get input. lose")


if __name__ == "__main__":
    main()

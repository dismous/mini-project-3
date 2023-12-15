"""
Pentomino game bot.
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
    Prioritize moves that are in the direction of the opponent's territory and expands throughout the lategame.
    """
    player1, player2 = ('O', 'X') if player == 1 else ('X', 'O')

    figure = [[cell.replace('*', player1) for cell in row] for row in figure]

    possible_moves = []

    opponent_positions = [(i, j) for i in range(field_height) for j in range(field_length) if field[i][j] == player2]

    for i in range(field_height - len(figure) + 1):
        for j in range(field_length - len(figure[0]) + 1):
            count = sum(field[i+h][j+l] == player1 and field[i+h][j+l] == figure[h][l] 
                        for h in range(len(figure)) 
                        for l in range(len(figure[0])))

            is_valid = all(field[i+h][j+l] != player2 or figure[h][l] != player1 
                           for h in range(len(figure))
                           for l in range(len(figure[0])))
            
            if count == 1 and is_valid:
                move = [i, j]
                distance_to_opponent = min(abs(i-x) + abs(j-y) for x, y in opponent_positions)
                is_boundary = any(field[i+di][j+dj] == player2 for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)] if 0 <= i+di < field_height and 0 <= j+dj < field_length)
                weight = 0.5 if is_boundary else 1
                possible_moves.append((move, weight * distance_to_opponent))

    possible_moves.sort(key=lambda x: x[1])
    return [move for move, _ in possible_moves]

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

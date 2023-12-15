"""
mini-project-3
player_Oleksa_Khita.py
"""
import random
from logging import DEBUG, debug, getLogger

getLogger().setLevel(DEBUG)

def parse_field_info():
    """
    Parse info about the field
    """
    field_info = input()[:-1].split()
    return int(field_info[1]), int(field_info[2])


def parse_field(height: int, length: int):
    """
    Parse the field
    """
    _ = input()
    return [list(input()[4:]) for _ in range(height)]


def parse_figure():
    """
    Parse the figure
    """
    h = int(input().split(' ')[1])
    return [list(input()) for _ in range(h)]


def moves(player):
    """
    Find the best move possible and perform it for the given player.
    """

    height, length = parse_field_info()
    field = parse_field(height, length)
    figure = parse_figure()

    opponent, player = ('X', 'O') if player == 1 else ('O', 'X')

    figure = [[i.replace('*', player) for i in row] for row in figure[:]]

    figure_height, figure_width = len(figure), len(figure[0])

    player_position = {(i, j) for i in range(height) for j in range(length) if field[i][j] == player}

    secondary_moves = []

    total_pieces = sum(1 for row in field for cell in row if cell != '.')

    possible_moves = []
    non_adjacent_moves = []

    opponent_position = [(i, j) for i in range(height) for j in range(length) if field[i][j] == opponent]

    for i in range(height - figure_height + 1):
        for j in range(length - figure_width + 1):
            same_count = sum((i + h, j + w) in player_position and figure[h][w] == player for h in range(figure_height) for w in range(figure_width))

            if same_count != 1:
                continue

            possible_moves.append((i, j))

    for i, j in possible_moves:
        is_valid_placement = all(field[i + h][j + w] != opponent or figure[h][w] != player for h in range(figure_height) for w in range(figure_width))

        if is_valid_placement:
            is_adjacent = any(field[i + h][j + w] == opponent for h in range(-1, figure_height + 1) for w in range(-1, figure_width + 1) if 0 <= i + h < height and 0 <= j + w < length)
            if is_adjacent:
                return [i, j]
            else:
                non_adjacent_moves.append((i, j))

    if non_adjacent_moves:
        target = max(opponent_position, key=lambda pos: abs(pos[0] - i) + abs(pos[1] - j))
        best_move = min(non_adjacent_moves, key=lambda move: abs(move[0] - target[0]) + abs(move[1] - target[1]))
        return list(best_move)

    try:
        return possible_moves[0] if possible_moves else None
    except:
        try:
            return random.choice(possible_moves)
        except:
            return random.choice(possible_moves)



def play(player: int):
    """
    Main game loop.
    """
    while True:
        move = moves(player)
        print(*move if move != None else "No valid moves found.")


def parse_info_about_player():
    """
    Parse info about the player
    """
    return 1 if "p1" in input() else 2


def main():
    player = parse_info_about_player()
    try:
        play(player)
    except EOFError:
        debug("Cannot get input. Game over.")

if __name__ == "__main__":
    main()

# ruby ./filler_vm -f ./map01 -p1 "py ./player_Khita_Oleksa.py" -p2 "py ./player_Popov_Bohdan.py" | py visualizer.py
# ruby ./filler_vm -f ./map01 -p1 "py ./player_Popov_Bohdan.py" -p2 "py ./player_Khita_Oleksa.py" | py visualizer.py
# ruby ./filler_vm -f ./map01 -p1 "py ./panama_bot.py" -p2 "py ./player_K.py" | py visualizer.py 
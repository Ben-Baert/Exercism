def board(white, black):
    check_positions(white, black)
    return [''.join("W"
        if (row, column) == white else ("B" if (row, column) == black else "_")
        for column in range(8)) for row in range(8)]

def can_attack(white, black):
    check_positions(white, black)
    white_x, black_x = white
    white_y, black_y = black
    white_difference = white_x - white_y if white_x >= white_y else white_y - white_x
    black_difference = black_x - black_y if black_x >= black_y else black_y - black_x
    return white_difference == black_difference or white_difference == 0 or black_difference == 0

def check_positions(white, black):
    if white == black or not all(0 <= x <= 7 for x in white + black):
        raise ValueError("Invalid position")
import numpy as np

def board(board):
    np_board = np.array([[char for char in row] for row in board])
    try:
        top_and_bottom_border = np.append(np_board[0], np_board[-1])
        side_borders = np.append(np_board[1:-1,0], np_board[1:-1,-1])
    except IndexError:
        raise ValueError("Rows are of different length")
    relevant = np_board[1:-1,1:-1]
    if (any(item not in "+-" for item in top_and_bottom_border) or
        any(item not in "|" for item in side_borders) or
        any(item not in " *" for item in relevant.flatten())):
        raise ValueError("Faulty border")
    board[1:-1] =  ["|" + ''.join(str(sum("*" == relevant[max(row_index-1,0):row_index+2, max(column_index-1,0):column_index+2].flatten()) or " ") if value != "*" else "*" for column_index, value in enumerate(row)) + "|" for row_index, row in enumerate(relevant)]
    return board
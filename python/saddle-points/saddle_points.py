def saddle_points(matrix):
    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise ValueError("Only supported for regular matrices")
    return set((row_index, column_index)
        for row_index, row in enumerate(matrix)
        for column_index, cell_value in enumerate(row)
        for column in zip(*matrix)
        if cell_value == max(row) and cell_value == min(column))
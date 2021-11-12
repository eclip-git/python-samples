

def route_exists(from_row, from_column, to_row, to_column, map_matrix):

    rows = len(map_matrix)
    cols = len(map_matrix[0])

    if from_row >= rows or from_row < 0 or from_column >= cols or from_column < 0:
        return False

    if visited[from_row][from_column]:
        return False

    visited[from_row][from_column] = True

    if map_matrix[from_row][from_column] is False:
        return False

    if from_column == to_column and from_row == to_row:
        return True

    if route_exists(from_row+1, from_column, to_row, to_column, map_matrix) is False:
        if route_exists(from_row-1, from_column, to_row, to_column, map_matrix) is False:
            if route_exists(from_row, from_column-1, to_row, to_column, map_matrix) is False:
                if route_exists(from_row, from_column+1, to_row, to_column, map_matrix) is False:
                    return False
                else:
                    return True
            else:
                return True
        else:
            return True
    else:
        return True


if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ];

    visited = []
    for i in range(len(map_matrix)):
        row = []
        for j in range(len(map_matrix[0])):
            row.append(False)
        visited.append(row)

    print(route_exists(0, 0, 0, 2, map_matrix))

    print(visited)

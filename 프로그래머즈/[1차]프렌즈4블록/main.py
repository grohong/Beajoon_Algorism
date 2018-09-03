def delete_point(m, n, board):
    dx = [1, 0, 1]
    dy = [0, 1, 1]

    delete = []
    for row_idx, row in enumerate(board):
        for col_idx, col in enumerate(row):

            if col == '0':
                continue

            flag = True
            for x, y in zip(dx, dy):
                tmp_x = col_idx+x
                tmp_y = row_idx+y

                if tmp_x >= n or tmp_y >= m:
                    flag = False
                    break

                if col != board[tmp_y][tmp_x]:
                    flag = False
                    break

            if flag == True:
                delete.append([col_idx, row_idx])

    return delete

def delete_process(deletes, board):
    dx = [1, 0, 1]
    dy = [0, 1, 1]

    for delete in deletes:
        tmp = list(board[delete[1]])
        tmp[delete[0]] = "0"
        board[delete[1]] = "".join(tmp)
        for x, y in zip(dx, dy):
            tmp = list(board[delete[1]+y])
            tmp[delete[0]+x] = "0"
            board[delete[1]+y] = "".join(tmp)

    tmp_board = [[] for _ in range(len(board[0]))]
    for row_idx, row in enumerate(board):
        for col_idx, col in enumerate(row):
            tmp_board[col_idx].append(col)

    result_board = []
    for row in tmp_board:
        zero_remove = list(filter(lambda x: x!= "0", row))
        tmp = "".join(zero_remove).zfill(len(board))
        result_board.append(tmp)

    tmp_board = [[] for _ in range(len(board))]
    for row_idx, row in enumerate(result_board):
        for col_idx, col in enumerate(row):
            tmp_board[col_idx].append(col)

    result_board = []
    for tmp in tmp_board:
        result_board.append("".join(tmp))

    return result_board



def solution(m, n, board):
    answer = 0

    while(True):

        delete = delete_point(m, n, board)

        if len(delete) != 0:
            board = delete_process(delete, board)
        else:
            break

    for row in board:
        answer += row.count('0')

    return answer

# print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
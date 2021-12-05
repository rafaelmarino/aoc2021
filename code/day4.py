#!/usr/bin/python3


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def check_bingo(board_marks):
    """Check if a board of markings (1/0) wins Bingo by rows or cols"""
    for i, row in enumerate(board_marks):
        if sum(row) == 5:
            return {"type": "row_bingo", "id": i}
    for i in range(5):
        if sum(list(zip(*board_marks))[i]) == 5:
            return {"type": "col_bingo", "id": i}
    return False


def compute_score(draw, board, markings):
    """Sum of all unmarked numbers times the draw number that won the bingo"""
    markings = [int(d) for row in markings for d in row]
    unmarkings = [1 if d == 0 else 0 for d in markings]
    total = 0
    for i in range(len(unmarkings)):
        total += unmarkings[i] * int(board[i])
    return total * int(draw)


def play_bingo(data):
    """--- Day 4: Giant Squid ---"""
    dim = [5, 5]  # rows, cols
    draws = data[0].split(",")
    draws[0]
    boards = [row for row in data[2:] if row != ""]
    boards_ = [boards[i : i + 5] for i in range(0, len(boards), 5)]
    boards_ = list(chunks(boards, dim[0]))
    boards__ = [" ".join(b).split() for b in boards_]
    # check that each board has 25 unique numbers
    # len(boards_)  # 100
    # assert sum([len(set(b)) for b in boards__]) == 5 * 5 * 100
    board_marks = {i: [[0] * 5 for _ in range(5)] for i in range(len(boards_))}
    for draw in draws:
        for i, board in enumerate(boards__):
            if draw in board:
                # print(draw in board, draw, i, board)
                array_pos = board.index(draw)
                row_id, col_id = array_pos // dim[0], array_pos % dim[1]
                board_marks[i][row_id][col_id] = 1
                bingo = check_bingo(board_marks[i])
                if bingo:
                    # print(draw, i, bingo, board_marks[i])  # board_marks[i]
                    return compute_score(draw, boards__[i], board_marks[i])
        # print(draw)
        # break  # apply all markings for a single draw


if __name__ == "__main__":
    file_path = "input/day4.txt"
    with open(file_path, "r") as f:
        data = f.read().splitlines()
        winning_score = play_bingo(data)
        print(f"Winning score from first-winning bingo board: {winning_score}")

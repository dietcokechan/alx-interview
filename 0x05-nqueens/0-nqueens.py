#!/usr/bin/python3
import sys


def printBoard(board):
    if any(1 in x for x in board):
        print([[idx, board[idx].index(1)] for idx, val in enumerate(board)])


def isSafe(row, square, chess_board, N, diagonal):
    if chess_board[row][square]:
        return False
    if square - diagonal >= 0 and chess_board[row][square - diagonal]:
        return False
    if square + diagonal < (N) and chess_board[row][square + diagonal]:
        return False
    if row == 0:
        return True
    return isSafe(row - 1, square, chess_board, N, diagonal + 1)


def placeSquare(row, position, chess_board, N):
    for square in range(position, N):
        if 1 in chess_board[row]:
            return 0
        if not isSafe(row - 1, square, chess_board, N, 1):
            continue
        chess_board[row][square] = 1
        return
    return 1


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

if not str.isdigit(N):
    print("N must be a number")
    sys.exit(1)

N = int(N)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = 0

while queen != N:
    chess_board = [[0 for x in range(N)] for x in range(N)]
    chess_board[0][queen] = 1
    position = 0
    row = 1
    while row < N:
        if placeSquare(row, position, chess_board, N):
            row -= 1
            position = chess_board[row].index(1)
            chess_board[row][position] = 0
            position += 1
            if not row:
                break
        else:
            row += 1
            position = 0
    printBoard(chess_board)
    queen += 1

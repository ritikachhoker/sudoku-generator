import random
def print_board(board):
    for row in board:
        print("".join(map(str,row)))
def is_valid_move(board, row, col, num):
    if num in board[row] or num in[board[i][col] for i in range(9)]:
        return False
    start_row, start_col = 3*(row//3), 3*(col//3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col+j]==num:
               return False
    return True
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col]==0:
                for num in range(1,10):
                    if is_valid_move(board, row, col, num):
                        board[row][col]=num
                        if solve_sudoku(board):
                            return True
                        board[row][col]=0
                        return False
                return True
def generate_sudoku():
    base=[[0]*9 for _ in range(9)]
    solve_sudoku(base)
    for _ in range(20):
        row, col= random.randint(0,8), random.randint(0,8)
        base[row][col]= 0
    return base
if __name__=="__main__":
    sudoku_board= generate_sudoku()
    print("Generated sudoku puzzle")
    print_board(sudoku_board)


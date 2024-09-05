# func_py_solve_n_queens.py
def func_py_solve_n_queens(n):
    def solve(row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if col not in columns and row - col not in diagonals1 and row + col not in diagonals2:
                board[row] = col
                columns.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)
                solve(row + 1)
                columns.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)
    
    result = []
    board = [-1] * n
    columns = set()
    diagonals1 = set()
    diagonals2 = set()
    solve(0)
    return result

print(func_py_solve_n_queens(4))

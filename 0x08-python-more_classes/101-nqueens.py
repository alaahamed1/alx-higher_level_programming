#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col].
    
    This function checks if a queen can be placed on the board at the given 
    row and column without being attacked by any other queen. It checks:
    1. The row on the left side.
    2. The upper diagonal on the left side.
    3. The lower diagonal on the left side.
    
    Parameters:
    board (list of list of int): The chessboard.
    row (int): The row index where the queen is to be placed.
    col (int): The column index where the queen is to be placed.
    N (int): The size of the board (N x N).
    
    Returns:
    bool: True if it's safe to place the queen, False otherwise.
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens_util(board, col, N, solutions):
    """
    Utility function to solve the N Queens problem using backtracking.
    
    This function attempts to place queens on the board, column by column. 
    If it successfully places a queen in each column, it records the solution.
    
    Parameters:
    board (list of list of int): The chessboard.
    col (int): The current column index to place a queen.
    N (int): The size of the board (N x N).
    solutions (list of list of list of int): The list to store all valid solutions.
    
    Returns:
    None
    """
    if col >= N:
        # All queens are placed, add the solution to the list
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return
    
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1  # Place queen
            solve_nqueens_util(board, col + 1, N, solutions)
            board[i][col] = 0  # Backtrack

def solve_nqueens(N):
    """
    Solve the N Queens problem and return all possible solutions.
    
    This function initializes the board and calls the recursive utility function 
    to find all solutions to the N Queens problem.
    
    Parameters:
    N (int): The size of the board (N x N).
    
    Returns:
    list of list of list of int: A list of all possible solutions, where each 
    solution is represented as a list of [row, column] pairs.
    """
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    return solutions

def main():
    """
    Main function to handle input and output.
    
    This function processes command-line arguments, validates the input, 
    and then solves the N Queens problem by printing all possible solutions.
    
    Returns:
    None
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()

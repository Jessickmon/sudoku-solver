from __future__ import print_function
#  kylie ying on youtube was used for the back tracking algorithm and parts of the valid assignment function


class solveSudokuBoard:

    def __init__(self, game_board):
        self.board = game_board

    def check_empty(self):
        board = self.board

        row_number = 0  # indexes start at 0 for lists
        col_number = 0

        for row in board:  # iterate through each row then through each column in each row
            for col in board:
                if board[row_number][col_number % 9] == 0:  # check if it equals 0 which is denoted as an empty cell
                    return row_number, col_number % 9
                col_number += 1
            row_number += 1

        return False  # if no indexes equal 0 (empty), then we return false

    def valid_assignment(self, guess):

        if self.check_empty():  # checks if the puzzle is empty which means it is not false
            assignment_row = self.check_empty()[0]
            assignment_col = self.check_empty()[1]

            row_checked = self.board[assignment_row]  # indexing each row, then checking if our guess is in there

            if guess in row_checked:
                return False

            col_checked = [self.board[i][assignment_col] for i in range(9)]  # same as the row but with columns

            if guess in col_checked:  # iteration above for column is called list comprehension
                return False

            square_row = ((assignment_row // 3) * 3)  # find the starting positions for the row, col for the 3x3
            square_col = ((assignment_col // 3) * 3)

            for r in range(square_row, square_row + 3):  # iterate through start position to end position (itself + 3)
                for c in range(square_col, square_col + 3):
                    if self.board[r][c] == guess:
                        return False  # if the guess equals any of the row, col, or 3x3, then we return false

            return True  # otherwise, true is returned because the guess fits the rules of sudoku

        return None  # if the puzzle is filled, then none is returned

    def solve_puzzle(self):
        board = self.board

        if self.check_empty() is False:  # checks if board is empty. if not, then solve_puzzle function is true/done
            return True

        solving_row_index, solving_col_index = self.check_empty()  # calling checking empty function for row/col values

        for cell_num in range(1, 10):  # iterates from 1 to 9 for guesses on the sudoku puzzle
            guess = cell_num
            if self.valid_assignment(guess):  # if the guess is in a valid spot, then the index equals the guess
                board[solving_row_index][solving_col_index] = guess
                if self.solve_puzzle():  # if the puzzle is solved (ie returns true), then return the board
                    return board

            board[solving_row_index][solving_col_index] = 0  # otherwise, we backtrack by setting the position to 0 and
                                                             # attempt the next number in the iteration

        return False  # if the board is not empty, then we return false


inserted_board = solveSudokuBoard([
    [0, 0, 7, 4, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 9, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 8],
    [0, 4, 0, 0, 6, 5, 0, 3, 0],
    [3, 0, 8, 0, 2, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 5, 0, 0, 3, 0, 0],
    [0, 0, 1, 7, 0, 3, 0, 5, 0]])

print(*solveSudokuBoard.solve_puzzle(inserted_board), sep='\n')

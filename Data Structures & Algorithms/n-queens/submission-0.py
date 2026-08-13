class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        # initialize empty board with '.'
        board = [['.' ] * n for _ in range(n)]

        def is_valid(board, row, col):
            # check column upward
            for i in range(row, -1, -1):
                if board[i][col] == 'Q':
                    return False

            # check left diagonal upward
            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # check right diagonal upward
            i, j = row, col
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def solve(board, row):
            # base case: all rows filled → valid solution found
            if row == n:
                # convert board to list of strings and store
                result.append(["".join(r) for r in board])
                return

            # try placing queen in every column of current row
            for col in range(n):
                if is_valid(board, row, col):
                    board[row][col] = 'Q'   # place queen
                    solve(board, row + 1)    # recurse to next row
                    board[row][col] = '.'    # backtrack, remove queen

        solve(board, 0)
        return result
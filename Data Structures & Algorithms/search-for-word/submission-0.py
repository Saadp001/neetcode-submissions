class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def find(i, j, idx):
            # base case: all characters matched
            if idx == len(word):
                return True

            # out of bounds or already visited or wrong character
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            if board[i][j] == 'v':
                return False
            if board[i][j] != word[idx]:
                return False

            # mark as visited
            temp = board[i][j]
            board[i][j] = 'v'

            # explore all 4 directions
            for di, dj in directions:
                if find(i + di, j + dj, idx + 1):
                    return True

            # backtrack — restore cell
            board[i][j] = temp
            return False

        # try starting from every cell
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and find(i, j, 0):
                    return True

        return False
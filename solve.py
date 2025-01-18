class Solve:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sqr = [[set() for _ in range(3)] for _ in range(3)]

        # Populates sets
        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n == '.':
                    continue

                rows[i].add(n)
                cols[j].add(n)
                sqr[i//3][j//3].add(n)

        def candidates(i, j):
            cand = []
            for k in range(1, 10):
                s = str(k)
                if s not in rows[i] and s not in cols[j] and s not in sqr[i//3][j//3]:
                    cand.append(s)

            return cand

        def backtrack(i=0, j=0):
            while i < len(board) and board[i][j] != '.':
                j += 1
                if j == len(board):
                    j = 0
                    i += 1

            if i == len(board):
                return True

            cand = candidates(i, j)

            for c in cand:
                board[i][j] = c
                rows[i].add(c)
                cols[j].add(c)
                sqr[i//3][j//3].add(c)

                if backtrack(i, j):
                    return True

                board[i][j] = '.'
                rows[i].remove(c)
                cols[j].remove(c)
                sqr[i//3][j//3].remove(c)
            return False

        return backtrack(0, 0)

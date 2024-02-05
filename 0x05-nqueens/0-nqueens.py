#!/usr/bin/python3
import sys

class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [['.'] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = [[i, board[i].index('Q')] for i in range(n)]
                res.append(copy)
                return

            for c in range(n):
                if c not in col and (r + c) not in posDiag and (r - c) not in negDiag:
                    col.add(c)
                    posDiag.add(r + c)
                    negDiag.add(r - c)
                    board[r][c] = "Q"
                    backtrack(r + 1)

                    col.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
                    board[r][c] = '.'

        backtrack(0)
        return res
def main():
    if len(sys.argv) != 2:
        print("Usage: script_name.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions_instance = Solution()
    result = solutions_instance.totalNQueens(N)

    for solution in result:
        print(solution)

if __name__ == "__main__":
    main()
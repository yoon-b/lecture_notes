# NeetCode
class Solution:
    def solveNQueens(self, n : int):
        # placing only one queen in a row
        # no need to check row validity
        # just check the queen is safe in [col & positive diagonal & negative diagonal]-wise
        col = set()
        posDiag = set()
        negDiag = set()

        rlt = []
        board = [ ["."] * n for i in range(n)]  # empty cell expressed as "."

        def backtrack(r):
            if r == n:  # successfully place all n queens
                copy = ["".join(row) for row in board]  # creating a copy for printing the result
                rlt.append(copy)
                return
            
            for c in range(n):  # traverse columns
                # if there's any queen attacking c, the current queen candidate
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue  # skip this one and go to the next column
                
                # if c is safe, mark the queen's position
                col.add(c) 
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)  # go to the next row

                # if all the queens are placed, this functon will be terminated, returning the rlt.
                # below is executed when solution isn't found.
                # therefore, remove c's traces (cuz it's not valid) 
                # and update c with the for loop above.
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
            
        backtrack(0)  # start from the first row
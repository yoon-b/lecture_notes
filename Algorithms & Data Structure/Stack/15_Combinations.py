"""
Given two integers n and k, 
return all possible combinations of k numbers out of the range [1, n]
"""


def combine(n: int, k: int):  # -> List[List[int]]
    rlt = []

    def backtrack(start, comb):
        if len(comb) == k:
            rlt.append(comb.copy())
            return
        
        for i in range(start, n+1):
            comb.append(i)
            backtrack(i + 1, comb)
            comb.pop()
    
    backtrack(1, [])  # start with an empty combination
    
    return rlt

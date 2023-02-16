"""
< Subsets - Backtracking >
Given an integer array nums, 
return all possible subsets (the power set).

The solution set must not contain duplicate subsets.
(this is not a permutation)
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rlt = []

        subset = []
        def dfs(i):  # the index of the value that we're making a decision on.
            
            # base case
            if i >= len(nums):
                # subset if going to be modified, so instead of the reference, 
                # we need to append the actual instance of each modified subset 'subset.copy'
                rlt.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i]
            # pop the element we just appeneded 
            subset.pop()
            dfs(i + 1)
        
        # starting from the first element
        dfs(0)
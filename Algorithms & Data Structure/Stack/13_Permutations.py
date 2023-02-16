"""
Given an array nums of distinct integers,
return all the possible permutations.
"""
class Solution:
    def permute(self, nums: List[int]) -> List[[List]]:
        result = []

        # base case
        if len(nums) == 1:  # having 1 value -> having 1 permutation only
            return [nums[:]]  # this is faster than [nums.copy()]
                              # return as a list in a list (hint from the problem)

        for i in range(len(nums)):  # traverse every value in nums
            n = nums.pop(0)
            perms = self.permute(nums)  # recursive call. has 1 less value than the original

            # going through each permutation
            for perm in perms:
                perm.append(n)  # adding back the popped value from above
            
            result.extend(perms)
            nums.append(n)  # clean up
        
        return result
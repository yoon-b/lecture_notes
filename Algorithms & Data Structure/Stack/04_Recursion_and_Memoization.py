# fibbonacci function with recursion


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# fibbonacci with memoization

nums = dict()  # use a global variable
def fib2(n):
    if n <= 2:
        return 1
    
    if n in nums:
        return nums[n]
    else:
        num = fib(n-1) + fib(n-2)
        nums[n] = num
        return num

'''
< Memoization >
- stores the previously calculated result of the subproblem
and uses the stored result for the same subproblem.
- speed up computer programs
'''
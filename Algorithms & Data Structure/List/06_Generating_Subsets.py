#generating subsets(combinations) using bitewise operations

def sub_sets(arr):
    N = len(arr)
    allSubs = [[0] for _ in range(2**N)]
    
    for i in range(1<<N): # number of subsets possible
        subset = []
        for j in range(N):
            # check if the bit is set at each position in the mask
            if i & (1<<j):
                subset.append(arr[j])
        allSubs[i] = subset
    
    return allSubs
    
    ##
    # for subset in allSubs:
    #     print(subset)
    # return

# example
lst = [1, 2]
print(sub_sets(lst))

## see the ouput paired w/ ##
# sub_sets(lst)
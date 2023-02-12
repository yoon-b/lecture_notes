#generating subsets(combinations) using bitewise operations

def sub_sets(arr):
    N = len(arr)
    allSubs = []
    
    for i in range(1<<N): # number of subsets possible
        subset = []
        for j in range(N):
            # check if the bit is set at each position in the mask
            if i & (1<<j):
                subset.append(arr[j])
        allSubs.append(subset)
    
    for subset in allSubs:
        print(subset)
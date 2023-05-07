def candidate_generation(input_set):
    
    #initialize an empty set for storing the subsets
    
    subsets=[]
    
    #iterate through all possible subsets
    
    for i in range(2**len(input_set)):
        
        #initialize the element subset
        subset = []
        
        #iterate through all the input sets
        for j in range(len(input_set)):
            
            # check the jth bit in the set
            if i&(1<<j):
                subset.append(input_set[j])
                subsets.append(subset)
    return subsets

input_set = str(input('enter the set - ').strip())
subsets = candidate_generation(input_set)

print(subsets)
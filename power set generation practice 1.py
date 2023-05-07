def power_set(input_set):
    
    result = [[]]
    
    for x in input_set:
        
        for subset in result[:]:
            result.append(subset+[x])
            
    return result

input_set = set(input("enter input set seperated by space").split())

Output_set = power_set(input_set)

print(Output_set)
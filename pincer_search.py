def pincer_search(words, max_distance):
    
    upper_bounds = [len(word) + max_distance for word in words]
    lower_bounds = [len(word) - max_distance for word in words]
    
    candidates = set()
    confirmed_pairs = set()
    
    for i, word1 in enumerate(words):
        
        for j in range(i + 1, len(words)):
            if len(words[j]) > upper_bounds[i]:
                break
            if len(words[j]) >= lower_bounds[i]:
                diff_count = sum(1 for c1, c2 in zip(word1, words[j]) if c1 != c2)
                if diff_count <= max_distance:
                    candidates.add((word1, words[j]))
        
        for j in range(i - 1, -1, -1):
            if len(words[j]) < lower_bounds[i]:
                break
            if len(words[j]) <= upper_bounds[i]:
                diff_count = sum(1 for c1, c2 in zip(word1, words[j]) if c1 != c2)
                if diff_count <= max_distance:
                    candidates.add((word1, words[j]))
        
        for candidate in candidates:
            for j, word2 in enumerate(candidate):
                # Check upper bounds of the confirmed word
                upper_bound = len(word2) + max_distance
                for k in range(j + 1, len(candidate)):
                    if len(candidate[k]) > upper_bound:
                        break
                    if len(candidate[k]) >= lower_bounds[i]:
                        diff_count = sum(1 for c1, c2 in zip(word2, candidate[k]) if c1 != c2)
                        if diff_count <= max_distance:
                            confirmed_pairs.add(candidate)
                            break
                # Check lower bounds of the confirmed word
                lower_bound = len(word2) - max_distance
                for k in range(j - 1, -1, -1):
                    if len(candidate[k]) < lower_bound:
                        break
                    if len(candidate[k]) <= upper_bounds[i]:
                        diff_count = sum(1 for c1, c2 in zip(word2, candidate[k]) if c1 != c2)
                        if diff_count <= max_distance:
                            confirmed_pairs.add(candidate)
                            break
    
    return confirmed_pairs

# Take input from the user
words_str = input("Enter a list of words (separated by spaces): ")
words = words_str.split()
max_distance = int(input("Enter the maximum edit distance: "))

pairs = pincer_search(words, max_distance)
print("Pairs within edit distance of", max_distance, ":")
for pair in pairs: 
    print(pair)

def generate_candidates(words, max_distance):
    candidates = set()
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words[i+1:], start=i+1):
            if abs(j - i) > max_distance:
                break
            if len(word1) == len(word2):
                diff_count = sum(1 for c1, c2 in zip(word1, word2) if c1 != c2)
                if diff_count <= max_distance:
                    candidates.add((word1, word2))
    return candidates

words = input("Enter a list of words (separated by spaces): ").split()
max_distance = int(input("Enter the maximum edit distance: "))

candidates = generate_candidates(words, max_distance)
print("Candidates within edit distance of", max_distance, ":")
for candidate in candidates:
    print(candidate)

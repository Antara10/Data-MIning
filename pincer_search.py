from collections import defaultdict
import csv
from itertools import combinations

def read_csv_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        transactions = []
        for row in reader:
            transactions.append([int(item) for item in row[1].split(',')])
        return transactions


def pincer_search(transactions, min_sup):
    
    itemsets = defaultdict(int)
    frequent_itemsets = []
    n = len(transactions)
    m = len(transactions[0])
    start = 0
    end = m - 1
    
    # Phase 1: forward pincer movement
    while start < n and end >= 0:
        
        count = defaultdict(int)
        for i in range(start, n):
            for j in range(end, -1, -1):
                items = transactions[i][j:]
                for k in range(len(items)):
                    itemset = tuple(sorted(items[:k] + items[k+1:]))
                    count[itemset] += 1

        
        infrequent_itemsets = set(itemset for itemset, freq in count.items() if freq < min_sup)
        for itemset in infrequent_itemsets:
            del count[itemset]

        
        frequent_itemsets.extend(count.keys())
        itemsets.update(count)

        
        if end > 0:
            end -= 1
        else:
            start += 1

    # Phase 2: backward pincer movement
    for i in range(n):
        for j in range(m):
            items = transactions[i][:j+1]
            for k in range(len(items)):
                itemset = tuple(sorted(items[:k] + items[k+1:]))
                if itemset in itemsets and itemsets[itemset] >= min_sup:
                    frequent_itemsets.append(itemset)

    
    rules = []
    for itemset in frequent_itemsets:
        for i in range(1, len(itemset)):
            for antecedent in combinations(itemset, i):
                antecedent = tuple(sorted(antecedent))
                consequent = tuple(sorted(set(itemset) - set(antecedent)))
                support = itemsets[itemset] / float(n)
                confidence = itemsets[itemset] / float(itemsets[antecedent])
                lift = confidence / (itemsets[consequent] / float(n))
                if confidence >= min_conf:
                    rules.append((antecedent, consequent, support, confidence, lift))

    return frequent_itemsets, rules



filename = 'transactionsint.csv'
min_sup = 3
min_conf = 0.5
transactions = read_csv_file(filename)
frequent_itemsets, rules = pincer_search(transactions, min_sup)

print("Frequent itemsets:")
for itemset in frequent_itemsets:
    print(list(itemset),end=',')

print("Association rules:")
for antecedent, consequent, support, confidence, lift in rules:
    print(list(antecedent), "->", list(consequent), "Support:", round(support, 2), "Confidence:", round(confidence, 2))
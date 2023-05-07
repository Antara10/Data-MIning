import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

df = pd.read_csv('new.csv')


items = df['Items Purchased'].str.split(',', expand=True)

df = pd.get_dummies(items.stack()).sum(level=0)

num_partitions = 2


partitions = [df[i:i+len(df)//num_partitions] for i in range(0, len(df), len(df)//num_partitions)]

for i, partition in enumerate(partitions):
    frequent_itemsets = apriori(partition, min_support=0.3, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.15)
    print(f"Partition {i+1}:")
    print(frequent_itemsets)
    print(rules)
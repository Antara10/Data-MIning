import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

df = pd.read_csv(r'C:\Users\bipro\OneDrive\Documents\Data Mining\practical\practical\transactionsint.csv')

one_hot_encoded = df['Items Purchased'].str.get_dummies(sep=',')


frequent_itemsets = apriori(one_hot_encoded, min_support=0.4, use_colnames=True)

association_rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.35)

print("Frequent Itemsets:")
print(frequent_itemsets)
print("\nAssociation Rules:")
print(association_rules)
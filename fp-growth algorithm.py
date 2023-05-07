class Node:
    def __init__(self, item, count, parent):
        self.item = item
        self.count = count
        self.parent = parent
        self.children = {}
        self.next = None

    def increment_count(self, count):
        self.count += count

def insert_tree(root, transaction, count):
    node = root
    for item in transaction:
        if item in node.children:
            child = node.children[item]
        else:
            child = Node(item, 0, node)
            node.children[item] = child
            if node.next is None:
                node.next = child
            else:
                while node.next is not None and node.next.item != item:
                    node = node.next
                if node.next is None:
                    node.next = child
                else:
                    node.next.increment_count(count)
                    child.next = node.next
                    node.next = child
        node = child
        node.increment_count(count)

def build_tree(transactions, min_support):
    root = Node(None, 0, None)
    item_counts = {}
    for transaction in transactions:
        for item in transaction:
            if item not in item_counts:
                item_counts[item] = 0
            item_counts[item] += 1
    for item in item_counts:
        if item_counts[item] >= min_support:
            root.children[item] = Node(item, item_counts[item], root)
    for transaction in transactions:
        transaction = [item for item in transaction if item in root.children]
        transaction.sort(key=lambda item: root.children[item].count, reverse=True)
        insert_tree(root, transaction, 1)
    return root

def find_frequent_itemsets(root, min_support, itemset, freq_itemsets):
    for item in root.children:
        count = root.children[item].count
        if count >= min_support:
            new_itemset = itemset.copy()
            new_itemset.append(item)
            freq_itemsets[tuple(new_itemset)] = count
            conditional_tree = build_conditional_tree(root.children[item], min_support)
            find_frequent_itemsets(conditional_tree, min_support, new_itemset, freq_itemsets)

def build_conditional_tree(node, min_support):
    transactions = []
    counts = {}
    while node is not None:
        transaction = []
        count = node.count
        while node.parent is not None:
            transaction.append(node.item)
            node = node.parent
        if len(transaction) > 0:
            transactions.append(transaction)
            counts[tuple(transaction)] = count
        node = node.next
    return build_tree(transactions, min_support)

def fptree():
    transactions = []
    while True:
        transaction_str = input("Enter a transaction (comma-separated items): ")
        if transaction_str == "":
            break
        transaction = [int(item) for item in transaction_str.split(",")]
        transactions.append(transaction)

    min_support = int(input("Enter the minimum support count: "))

    root = build_tree(transactions, min_support)
    freq_itemsets = {}
    find_frequent_itemsets(root, min_support, [], freq_itemsets)
    return freq_itemsets

freq_itemsets = fptree()
print(freq_itemsets)



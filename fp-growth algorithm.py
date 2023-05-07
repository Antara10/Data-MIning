import numpy as np
import pandas as pd
import pyfpgrowth

transactions = [['cheese', 'butter', 'egg'],
                ['butter', 'sugar'],
                ['butter', 'milk'],
                ['cheese', 'butter', 'paneer'],
                ['cheese', 'milk'],
                ['butter', 'milk'],
                ['cheese', 'milk'],
                ['cheese', 'butter', 'paneer', 'egg'],
                ['cheese', 'butter', 'paneer']]

patterns = pyfpgrowth.find_frequent_patterns(transactions, 2)

rules = pyfpgrowth.generate_association_rules(patterns, 0.7)


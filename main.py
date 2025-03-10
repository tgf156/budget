import pandas as pd

data = pd.read_csv("Data/Monzo Data Export - CSV (Friday, March 7th, 2025).csv")
expense = data[data['Amount'] < 0]
income = data[data['Type'] == 'Income']
transfer = data[data['Type'] == 'Pot transfer']
print(transfer)

#Transaction ID,Date,Time,Type,Name,Emoji,Category,Amount,Currency,Local amount,Local currency,Notes and #tags,Address,Receipt,Description,Category split,Money Out,Money In
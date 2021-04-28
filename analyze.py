import pandas as pd

dataset = pd.read_csv('data_csv.csv')
dataset.head(n=4)
# print(dataset)
#  dropping the columns (Year of graduation, graduation month)
dataset.dropna(axis=1, inplace=True)

dataset.to_csv('Data analyst assignment dataset.csv', index=False)

read = pd.read_csv('Data analyst assignment dataset.csv')

print(read.info())

import pandas as pd

df = pd.read_csv('../sample_data/02 Introduction to Pandas/intel.csv')
print(df.head())

print(type(df))
print(df.shape)
print(df.describe())
print(df.info())
print(df.loc[:3, 'Date':'Low'])

print(df.iloc[1:3, 1:3])

print(df[['Date', 'Close']].head())

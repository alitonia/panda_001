import pandas as pd

df = pd.read_csv('../sample_data/02 Introduction to Pandas/intel.csv')
print(df.shape)

condition = []
for x in range(len(df['Open'])):
    if df['Open'][x] > 55 and df['Low'][x] > 56:
        condition.append(True)
    else:
        condition.append(False)

# condition = pd.DataFrame(data=condition)
print(df[condition])


open_series = df['Open']
print(type(df))
print(type(df['Open']))
print(type(df['Open'].values))

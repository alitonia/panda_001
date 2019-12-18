
import pandas as pd
import numpy as np
df = pd.read_csv('../sample_data/02 Introduction to Pandas/intel.csv')
# print(df.head())
# pd.DataFrame()


# personal_data = dict(name=['Bob', 'Tom', 'Chicken'], age=[10, 15, 18], job=[
#                      'dev', 'unemployed', 'pet'], married_status=[False, False, True])

# # Change column name to capital
# df = pd.DataFrame(personal_data)
# new_name = [chr(ord(x[0])-32) + x[1:] for x in df.columns]

# for i in range(len(df.columns)):
#     df.columns.values[i] = new_name[i]

name = ['Bob', 'Tom', 'Chicken']
age = [10, 15, 18]
job = ['dev', 'unemployed', 'pet']
married_status = [False, False, True]

column_name = ['name', 'age', 'job', 'married_status']

column_name = [x[0].upper()+x[1:] for x in column_name]
data = [name, age, job, married_status]

personal_data = dict(zip(column_name, data))

df = pd.DataFrame(personal_data)
print(df)

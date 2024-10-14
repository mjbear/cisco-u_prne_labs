import pandas

with open('router_info.csv') as csv_file:
    df = pandas.read_csv(csv_file)
print(df)
print()
print(df['ip'])
print()
print(df.loc[[0]])
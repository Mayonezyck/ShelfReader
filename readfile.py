import pandas


df = pandas.read_csv('example.csv', index_col='barcode')

print(df)

import pandas as pd


#df = pandas.read_csv('example.csv', names=['call number','x','title','barcode','xx','xxx','xxxx'])

d = pd.DataFrame(pd.read_excel('shelflist.xlsx'))
print(d)

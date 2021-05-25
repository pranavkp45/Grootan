import pandas as pd

data = pd.read_csv (r'C:\Users\Desktop\Test\Bank records.csv')   
df = pd.DataFrame(data, columns= ['Date','Descrption','Deposits','Withdrawl','Balance'])

print(df)
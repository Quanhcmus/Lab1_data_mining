from deleteColumn import deleteColumn
import pandas as pd
Ob=deleteColumn('input/house-prices.csv')
Ob.writeFile()

df=pd.read_csv('output/deleteColumn.csv')

print(df.shape)





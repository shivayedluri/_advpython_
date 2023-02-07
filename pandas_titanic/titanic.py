import pandas as pd
df=pd.read_csv('../data/tips.csv')
print(df)
#df.drop(['smoker'],axis=1,inplace=True)
#print(df)
#df.fillna(method='sex',inplace=True)
#print(df)
print(pd.pivot_table(df,index=['sex','Age'],aggfunc=np.sum))
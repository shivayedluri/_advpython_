import pandas as pd
d={'team':["ind","eng","nz"],'rank':[1,2,3]}
df=pd.DataFrame(d)
print(df)
df.drop([0,1],axis=0,inplace=True)
print(df)
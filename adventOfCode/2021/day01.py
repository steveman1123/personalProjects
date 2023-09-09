import pandas as pd
df = pd.DataFrame()
#read from csv (no header, so specify that)
df['data'] = pd.read_csv("./day01in.txt",header=None)

#pt 1

#get the change
df = df.assign(delta=df['data'].diff())

print(">0",sum(df['delta']>0))


#pt 2
df = df.assign(win3=df['data']+df['data'].shift(1)+df['data'].shift(2))
df = df.assign(dif3=df['win3'].diff())

print("win3 >0",sum(df['dif3']>0))
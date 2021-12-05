import pandas as pd
df = pd.DataFrame()
#read from csv (no header, so specify that)
df = pd.read_csv("./day02in.txt",header=None,sep=" ",engine="python")

#pt 1
df['h'] = df[1]*(df[0]=="forward")
df['v'] = (df[1]*(df[0]=="down"))-(df[1]*(df[0]=="up"))

print(df)
totv = sum(df['v'])
toth = sum(df['h'])
print("total v:",totv)
print("total h:",toth)
print("product:",totv*toth)
print()

#pt 2
#h=sum(forward), v=aim*forward
df['aim'] = df['v'].cumsum()
df['newh'] = df['h']
df['newv'] = (df['aim']*(df[1]*(df[0]=='forward')))

print(df)
newtoth=sum(df['newh'])
newtotv=sum(df['newv'])
print("new total h",newtoth)
print("new total v",newtotv)
print("pruduct",newtoth*newtotv)
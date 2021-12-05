import pandas as pd
df = pd.DataFrame()
#read from csv (no header, so specify that)
df = pd.read_csv("./day03in.txt",header=None,sep=" ",engine="python")

#pt 1

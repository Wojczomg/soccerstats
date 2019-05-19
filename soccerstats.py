import os
import pandas as pd
import numpy as np

os.chdir("C:\\Users\\Wojcz\\gigaprojekt\\")
from tablesmaker3000 import registry
df2 = pd.DataFrame()

for r in [5,6,7,8,9]:
	register = registry()
	path = "C:\\Users\\Wojcz\\PycharmProjects\\scrapyta\\scrapyta\\['england']\\"
	df=pd.read_csv(path+"['201{}'].csv".format(r),names=[i for i in range(5)],engine="python")

	haha=df.iloc[:,0].map(lambda x: x[:x.find(" -")].strip())
	hehe=df.iloc[:,0].map(lambda x: x[x.find(" -")+2:].strip())	

	dfnew = pd.concat([haha,hehe,df.iloc[:,[1,2,3,4]].astype(float)],axis=1)
	dfnew.columns = [i for i in range(6)]

	for k in dfnew[:-160:-1].itertuples(index=False,name=None):
		for j in register["writer"]:
			j(k)
	for k in dfnew[-160::-1].itertuples(index=False,name=None):
		df2=df2.append([register["reader"](k)],ignore_index=True)
		for j in register["writer"]:
				j(k)


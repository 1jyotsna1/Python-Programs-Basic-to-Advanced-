import pandas as pd
import numpy as np
from tabulate import tabulate

Img_=pd.read_excel(r"C:\Users\Jyotsna\Desktop\img.xlsx")
Img=Img_.values
print("i","\t","j","\t","value")
for i in range(0,Img.shape[0]):
		for j in range(0,Img.shape[1]):
		      if Img[i][j]>=0:
			      print(i,"\t",j,"\t",Img[i][j])


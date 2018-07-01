import pandas as pd
import numpy as np

data =pd.read_csv('train.csv')

ID = data.pop('ID')

col = list(data)
nul_ = data.isnull().sum()
ddd = data.dtypes

target = data['target']

Cor__ = []s
for i in data.columns[1:]:
    ind = i
    Cor__.append(data['target'].corr(data[i]))


#Cor__ = np.array(Cor__)
#arr = Cor__[~np.isnan(Cor__)]


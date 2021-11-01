# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 18:18:48 2021

@author: User
"""

#eksik veriler
#sci -kit learn
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#kodlar
#veri yükleme
veriler=pd.read_csv("eksikveriler.csv")
print(veriler)

from sklearn.impute import SimpleImputer

imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
Yas = veriler.iloc[:,1:4].values
print(Yas)
imputer=imputer.fit(Yas[:,1:4])
Yas[:,1:4]=imputer.transform(Yas[:,1:4])
print(Yas)
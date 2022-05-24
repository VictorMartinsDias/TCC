# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 14:11:32 2021

@author: vmd01
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_excel('D:/Python__/Artigo_TCC/Grafico_artigo.xlsx')


fig = plt.figure(figsize=(7.5, 4.5), dpi=1000)

plt.scatter(df['T'], df['ln(Deff) 3'], marker='s', color='black', alpha=0.9)

z = np.polyfit(df['T'], df['ln(Deff) 3'], 1)
p = np.poly1d(z)
plt.plot(df['T'],p(df['T']),"--", color='black')

plt.xlabel("1/T (1/K)")
plt.ylabel("ln Deff (m²/s)")
plt.show()
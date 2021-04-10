# število vseh kaznivih dejanj po letih ter narisano povprečje

from pridobivanje_podatkov import *
import pandas as pd #uvedemo novo knjižnico za branje excelovih datotek
import operator
import matplotlib.pyplot as plt
import numpy as np
import os

seznam_datotek = ['KD2009.csv','kd2010.csv','kd2011.csv','kd2012.csv','kd2013.csv','kd2014.csv','kd2015.csv','kd2016.csv','kd2017.csv','kd2018.csv','kd2019.csv']

slovar_primerov = {}

for leto in seznam_datotek:
    df = pd.read_csv(leto, sep=';', encoding = 'Windows-1250', low_memory = False)
    df.drop_duplicates(subset =["UraStoritve", 'DanVTednu', 'ZaporednaStevilkaKD'],
                      keep = False, inplace = True) #znebimo se odvečnih ponovitev
    slovar_primerov[leto[2:-4]] = df.shape[0]
    
    sorted_slovar_primerov = sorted(slovar_primerov.items(), key = operator.itemgetter(1), reverse = True)
    sortirani = {k: v for k, v in sorted_slovar_primerov}
# print(sortirani)
# print(slovar_primerov)


x = slovar_primerov.keys()
y = slovar_primerov.values()
povprecje = round(sum(y) / len(slovar_primerov))
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
        marker='o', markerfacecolor='blue', markersize=12, label = 'št. obravnavanih primerov')
plt.axhline(y = povprecje, color = 'red', linestyle = 'solid', linewidth = 3, label = 'povprečje')  

plt.ylim()
plt.xlim()
  
#poimenujemo x-os
plt.xlabel('leta')
#poimenujemo y-os
plt.ylabel('število obravnavanih primerov')
  
# naslov grafa
plt.title('Število vseh kaznivih dejanj po letih 2009-2019')
plt.legend()  

plt.show()
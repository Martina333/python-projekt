# koda nariše tortni prikaz za prisotnost mamil

from pridobivanje_podatkov import *
import pandas as pd
import operator
import matplotlib.pyplot as plt


seznam_datotek = ['KD2009.csv','kd2010.csv','kd2011.csv','kd2012.csv','kd2013.csv','kd2014.csv','kd2015.csv','kd2016.csv','kd2017.csv','kd2018.csv','kd2019.csv']


seznam_vseh_slovarjev= []
for eksel in seznam_datotek:
    df = pd.read_csv(eksel, sep=';', encoding = 'Windows-1250',low_memory=False)
    seznam_mamil = df['VplivMamil']

    slovar_mamil = {}
    for mamilo in seznam_mamil:
        if mamilo in slovar_mamil:
            slovar_mamil[mamilo] += 1
        else:
            slovar_mamil[mamilo] = 1
    sorted_slovar_mamil = sorted(slovar_mamil.items(), key = operator.itemgetter(1), reverse = True)
    sortirani = {k: v for k, v in sorted_slovar_mamil}

    
    del sortirani['NN']

    seznam_vseh_slovarjev.append(sortirani)
    
    total_tabela = []
    total_da = sum([item['DA'] for item in seznam_vseh_slovarjev])
    total_ne = sum([item['NE'] for item in seznam_vseh_slovarjev])
    total = total_da + total_ne
    total_da1 = round((total_da / total) * 100, 2)
    total_ne2 = round((total_ne / total) * 100, 2)
    total_tabela.append(total_da1)
    total_tabela.append(total_ne2)
    
    nov_slov = dict()
    nov_slov['DA'] = total_da1
    nov_slov['NE'] = total_ne2
          
     
x_os = nov_slov.keys()

y_os = nov_slov.values()

barve = ['r', 'y']

plt.pie(y_os, labels = x_os, colors=barve, 
        startangle=0, shadow = True, explode = (0.1, 0.01),
        radius = 1.5, autopct = '%1.1f%%')

plt.legend()
plt.title('Prisotnost mamil')
plt.show()
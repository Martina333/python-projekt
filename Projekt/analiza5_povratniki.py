# koda izriše tortni prikaz glede na excel-podatke ali je oseba prvič storila kaznivo dejanje ali ne

from pridobivanje_podatkov import *
import pandas as pd
import operator
import matplotlib.pyplot as plt
import os


seznam_datotek = ['KD2009.csv','kd2010.csv','kd2011.csv','kd2012.csv','kd2013.csv','kd2014.csv','kd2015.csv','kd2016.csv','kd2017.csv','kd2018.csv','kd2019.csv']

    
seznam_vseh_slovarjev= []
for eksel in seznam_datotek:
    df = pd.read_csv(eksel, sep=';', encoding = 'Windows-1250',low_memory=False)
    seznam_povrata = df['Povratnik']
    slovar_povratnikov = {}
    for povratnik in seznam_povrata:
        if povratnik in slovar_povratnikov:
            slovar_povratnikov[povratnik] += 1
        else:
            slovar_povratnikov[povratnik]  = 1
    sorted_slovar_povrat = sorted(slovar_povratnikov.items(), key = operator.itemgetter(1), reverse = True)
    sortirani = {k: v for k, v in sorted_slovar_povrat}
    
    seznam_vseh_slovarjev.append(sortirani)
#print(seznam_vseh_slovarjev)
    total_tabela = []
    total_da = sum([item['DA'] for item in seznam_vseh_slovarjev])
    total_ne = sum([item['NE'] for item in seznam_vseh_slovarjev])
    total = total_da + total_ne
    total_da1 = round((total_da / total) * 100, 2) #seštejemo vse 'da' in delimo z vsemi podatki da dobimo procente
    total_ne2 = round((total_ne / total) * 100, 2)
    total_tabela.append(total_da1)
    total_tabela.append(total_ne2)
    
    nov_slov = dict()
    nov_slov['DA'] = total_da1
    nov_slov['NE'] = total_ne2
#print(nov_slov)    
x_os = nov_slov.keys()
y_os = nov_slov.values()
    
colors = ['y', 'b']
    
plt.pie(y_os, labels = x_os, colors=colors, 
    startangle=90, shadow = True, explode = (0,0.1),
    radius = 1.2, autopct = '%1.1f%%')
  

plt.legend()

plt.title('Procentni delež povratnikov v obdobju 2009-2019')

plt.show()
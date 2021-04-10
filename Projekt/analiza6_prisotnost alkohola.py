# KODA NARIŠE HISTOGRAM GLEDE NA PODATKE, ALI JE ALKOHOL BIL PRISOTEN PRI KAZNIVEM DEJANJU ALI NE

from pridobivanje_podatkov import *
import pandas as pd #knjižnica za branje podatkov
import operator #knjižnica, ki nam pomaga sortirati podatke
import matplotlib.pyplot as plt #knjižnica za risanje histograma


seznam_datotek = ['KD2009.csv','kd2010.csv','kd2011.csv','kd2012.csv','kd2013.csv','kd2014.csv','kd2015.csv','kd2016.csv','kd2017.csv','kd2018.csv','kd2019.csv']

seznam_vseh_slovarjev= []
for eksel in seznam_datotek:
    df = pd.read_csv(eksel, sep=';', encoding = 'Windows-1250',low_memory=False)
    seznam_alko = df['VplivAlkohola']
#preberemo vse datoteke, pri tem gledamo le stolpec s podatki o alkoholu
    
    slovar_alko = {}
    for alkohol in seznam_alko:
        if alkohol in slovar_alko:
            slovar_alko[alkohol] += 1
        else:
            slovar_alko[alkohol] = 1
    sorted_slovar_alko = sorted(slovar_alko.items(), key = operator.itemgetter(1), reverse = True)
    sortirani = {k: v for k, v in sorted_slovar_alko}
    #uredimo elemente slovarja po velikosti
#print(sortirani)
    
    del sortirani['NN'] #iz slovarja zbrišemo ključ 'NN', osredotočimo se le na ključa 'NE' in 'DA'

    seznam_vseh_slovarjev.append(sortirani)
    
    total_tabela = []
    total_da = sum([item['DA'] for item in seznam_vseh_slovarjev]) #seštejemo vse 'DA'
    total_ne = sum([item['NE'] for item in seznam_vseh_slovarjev]) #seštejemo vse 'NE'
    total = total_da + total_ne #seštejemo vse podatke za 'DA' in 'NE'
    total_da1 = round((total_da / total) * 100, 2) #izračunamo procente
    total_ne2 = round((total_ne / total) * 100, 2)
    total_tabela.append(total_da1)
    total_tabela.append(total_ne2)
    
    nov_slov = dict()
    nov_slov['DA'] = total_da1  # v novi slovar dodamo ključa 'DA' in 'NE' ter jima priredimo vrednosti
    nov_slov['NE'] = total_ne2
    

    
x_os = nov_slov.keys() #na x-osi damo 'DA' in 'NE'
y_os = nov_slov.values() #njune vrednosti damo na y-os

    
barve = ['red','green'] #določimo barve
plt.bar(x_os, y_os, color = barve, width = 0.5) #naredimo histogram
    
plt.xlabel('Prisotnost alkohola')
plt.ylabel('Procenti')
plt.title('Prisotnost alkohola izražen v procentih za leta 2009 - 2019')
plt.show()
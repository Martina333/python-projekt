# v kateri upravni enoti je največ kriminalnih dejanj in kako se ta spreminjajo po letih

from pridobivanje_podatkov import *
import pandas as pd #uvedemo novo knjižnico za branje excelovih datotek
import operator
import matplotlib.pyplot as plt


seznam_vseh_slovarjev = []

seznam_datotek_storitve = ['kd2010.csv','kd2011.csv','kd2012.csv','kd2013.csv','kd2014.csv','kd2015.csv','kd2016.csv','kd2017.csv','kd2018.csv','kd2019.csv']
for eksel in seznam_datotek_storitve:
    df = pd.read_csv(eksel, sep=';', encoding = 'Windows-1250',low_memory=False)
    df.drop_duplicates(subset =["UraStoritve", 'DanVTednu', 'ZaporednaStevilkaKD'],
                      keep = False, inplace = True)
    seznam_ue = df['UpravnaEnotaStoritve']


    slovar_ue = {}
    for kraj in seznam_ue: # sprehodimo se po parih iz seznama
        if kraj in slovar_ue: # če smo našli novega 
            slovar_ue[kraj] += 1 # je potrebno narediti nov vnos v slovar
        else:
            slovar_ue[kraj] = 1
    sorted_slovar_ue = sorted(slovar_ue.items(), key = operator.itemgetter(1), reverse = True)
    sortirani = {k: v for k, v in sorted_slovar_ue}
    seznam_vseh_slovarjev.append(sortirani)
    
nova_tabela = [] 
for sortirani in seznam_vseh_slovarjev: #sprehodimo se po vseh slovarjih naše tabele vseh slovarjev
    
    nova_tabela.append(next(iter(sortirani.items()))) #dodamo samo prvi ključ



y_os = [par[1] for par in nova_tabela]

x_os = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']

x = x_os
y = y_os


plt.plot(x, y, color='blue', linestyle='solid', linewidth = 3,
         marker='o', markerfacecolor='red', markersize=12)
  

plt.ylim()
plt.xlim()
  

plt.xlabel('leta')

plt.ylabel('število obravnavanih primerov')
  
plt.title('Število vseh kaznivih dejanj v Ljubljani po letih 2010-2019')

plt.show()

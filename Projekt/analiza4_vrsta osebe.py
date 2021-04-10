# prikažemo razmerje oseb udeleženih v kaznivem dejanju glede na to ali je oseba žrtev ali storilec

from pridobivanje_podatkov import *
import pandas as pd #uvedemo novo knjižnico za branje excelovih datotek
import operator
import matplotlib.pyplot as plt
import numpy as np
import os

seznam_datotek= ['KD2009.csv','kd2010.csv','kd2011.csv','kd2012.csv','kd2013.csv','kd2014.csv','kd2015.csv','kd2016.csv','kd2017.csv','kd2018.csv','kd2019.csv']

seznam_vseh_slovarjev = []
    
for eksel in seznam_datotek:
    df = pd.read_csv(eksel, sep=';', encoding = 'Windows-1250',low_memory=False)
    seznam_oseb = df['VrstaOsebe']
    
    slovar_oseb = {}
    for oseba in seznam_oseb:
        if oseba in slovar_oseb:
            slovar_oseb[oseba] += 1
        else:
            slovar_oseb[oseba] = 1
    

    seznam_vseh_slovarjev.append(slovar_oseb)


nova_tabela = [] 
for slovar_oseb in seznam_vseh_slovarjev: #sprehodimo se po vseh slovarjih naše tabele vseh slovarjev
    res = {kljuc: slovar_oseb[kljuc] for kljuc in slovar_oseb.keys()
                               & {'ŽRTEV', 'OVADENI OSUMLJENEC', 'NEOVADENI OSUMLJENEC (ARHIV)'}}
    # gledamo samo ključe 'žrtev', 'ovadeni osumljenec', 'neovadeni osumljenec (arhiv)'
    nova_tabela.append(res)
    

tab1 = []
tab2 = []
tab3 = []
for res in nova_tabela:
    zrtev = {kljuc: res[kljuc] for kljuc in res.keys()
                               & {'ŽRTEV'}}
    tab1.append(zrtev) #naredimo tabelo katere elementi so ključ 'žrtev' in njegove vrednosti
    
    ov_osumljenec = {kljuc: res[kljuc] for kljuc in res.keys()
                               & {'OVADENI OSUMLJENEC'}}
    tab2.append(ov_osumljenec)
    neov_osumljenec = {kljuc: res[kljuc] for kljuc in res.keys()
                               & {'NEOVADENI OSUMLJENEC (ARHIV)'}}
    tab3.append(neov_osumljenec)

tab_1 = []
tab_2 = []
tab_3 = []

for slo_ in tab1:
    for kljuc in slo_:
        tab_1.append(slo_[kljuc]) #za ključ 'žrtev' izpišemo vrednosti v tabelo tab1

for slo_ov in tab2:
    for kljuc in slo_ov:
        tab_2.append(slo_ov[kljuc])

for slo_neov in tab3:
    for kljuc in slo_neov:
        tab_3.append(slo_neov[kljuc])


        
tab_zrtev = tab_1
tab_ov = tab_2
tab_neov = tab_3


barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))

br1 = np.arange(len(tab_zrtev))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

plt.bar(br1, tab_zrtev, color ='r', width = barWidth,
        edgecolor ='grey', label ='Žrtev')
plt.bar(br2, tab_ov, color ='g', width = barWidth,
        edgecolor ='grey', label ='Ovadeni osumljenci')
plt.bar(br3, tab_neov, color ='b', width = barWidth,
        edgecolor ='grey', label ='Neovadeni osumljenci')
 

plt.xlabel('Leta', fontweight ='bold', fontsize = 15)
plt.ylabel('Razmerje med žrtvami in osumljenci', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(tab_zrtev))],
        ['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
plt.title('Razmerje med žrtvami in osumljenci po letih v obdobju 2009-2019') 
plt.legend()
plt.show()

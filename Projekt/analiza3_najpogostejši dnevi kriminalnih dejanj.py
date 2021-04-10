#TA KODA NAM GRAFIČNO PREDSTAVI NAJPOGOSTEJŠI DAN ZA VSAKO LETO
#RDEČI STOLPEC V HISTOGRAMU PA PREDSTAVLJA NAJINO NAPOVED ZA LETO 2020 GLEDE NA NAJVEČKRAT PONOVLJEN DAN
#V LETIH 2009-2019 IN
# POVPREČNIM ŠTEVILOM PRIMEROV ZA VSA LETA

from pridobivanje_podatkov import *
import pandas as pd #uvedemo novo knjižnico za branje excelovih datotek
import operator
import matplotlib.pyplot as plt


seznam_datotek = ['KD2009.csv','kd2010.csv','kd2011.csv','kd2012.csv','kd2013.csv','kd2014.csv','kd2015.csv','kd2016.csv','kd2017.csv','kd2018.csv','kd2019.csv']
seznam_vseh_procentov = []
seznam_vseh_slovarjev = []

    
for eksel in seznam_datotek:
    df = pd.read_csv(eksel, sep=';', encoding = 'Windows-1250',low_memory=False)
    df.drop_duplicates(subset =["UraStoritve", 'DanVTednu', 'ZaporednaStevilkaKD'],
                      keep = False, inplace = True)
    seznam_dan = df['DanVTednu']
    
    slovar_dni = {}
    for dan in seznam_dan:
        if dan in slovar_dni:
            slovar_dni[dan] += 1
        else:
            slovar_dni[dan] = 1
        
    sorted_slovar_dni = sorted(slovar_dni.items(), key = operator.itemgetter(1), reverse = True)
    sortirani = {k: v for k, v in sorted_slovar_dni}       
    

    tabela_procentov = []
    vrednosti = sortirani.values()
    for vrednost_dneva in vrednosti:
        
        procent = round(vrednost_dneva / sum(vrednosti) * 100, 2)
        tabela_procentov.append(procent)
      
    seznam_vseh_procentov.append(tabela_procentov)
    seznam_vseh_slovarjev.append(sortirani)
    
#print(seznam_vseh_slovarjev)  #izpiše tabelo vseh sortiranih slovarjev za vsa leta
#print(seznam_vseh_procentov)  #izpiše vse procente za dneve za vsa leta

nova_tabela = [] 
for sortirani in seznam_vseh_slovarjev: 
    
    nova_tabela.append(next(iter(sortirani.items() ))) #prvi element vsakega slovarja dodamo v naso tabelo


tabela_imen, tabela_stevil = [],[]  #razbijemo pare v dve tabeli
for par in nova_tabela:
    tabela_imen.append(par[0])
    tabela_stevil.append(par[1])
    
najpogostejsi_dan = max(set(tabela_imen), key = tabela_imen.count)
    #kateri dan se največkrat ponovi
#print(najpogostejsi_dan) 

napoved = round(sum(tabela_stevil) / len(tabela_stevil))
    # povprečje vseh primerov

x_labels = [par[0] for par in nova_tabela]
x_labels.append(najpogostejsi_dan)
leta = ['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
leta.append('2020 - napoved') #dodamo najino napoved
z = set(zip(x_labels, leta))
x_os = sorted(z, key = lambda t: t[1])


y_labels = [par[1] for par in nova_tabela]
y_labels.append(napoved)
plt.figure(figsize = (12,6))

seznam_barv = ['blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue', 'red']

ax = pd.Series(y_labels).plot(kind = 'bar', color = seznam_barv)
ax.set_xticklabels(x_os)

rects = ax.patches

for rect, label in zip(rects, y_labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2, height + 5, label, ha='center', va='bottom', color = 'black')

plt.xlabel('dnevi')
plt.ylabel('število kriminalnih dejanj')
plt.title('Največja ponovitev kriminalnih dejanj po dnevih 2009-2019')
plt.show()

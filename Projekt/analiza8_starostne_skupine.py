# za vsa leta posebej predstavimo starostne skupine osumljencev

from pridobivanje_podatkov import *
import pandas as pd
import os
import matplotlib.pyplot as plt
import pylab as plt



def storitelji_dejanja(leto):
    '''Funkcija pogleda vse storitelje dejanja'''
    
    df = pd.read_csv(leto, sep=';', encoding='windows-1250', low_memory = False)
    df = df[['VrstaOsebe','StarostniRazred']]
    df = df[df['StarostniRazred'] != 'NI PODATKA']
    df = df[df['StarostniRazred'] != 'NI POJAVA']
    df = df[df['StarostniRazred'] != '00-07']
    df['stevilo'] = 1
    df = df.groupby(['VrstaOsebe','StarostniRazred']).count()['stevilo']['OVADENI OSUMLJENEC']
    #gledamo samo ovadene osumljence in njihovo starost
    return df

def starostne_skupine(leto):
    '''Funkcija za vsako leto vrne pripadajočo tabelo starostnih skupin'''
    
    df = pd.read_csv(leto, sep=';', encoding='windows-1250', low_memory = False)
    df = df[df['StarostniRazred'] != 'NI PODATKA']
    df = df[df['StarostniRazred'] != 'NI POJAVA']
    df = df[df['StarostniRazred'] != 'PRAVNA OSEBA']
    
    starostne_skupine = df.pivot_table(index = ['StarostniRazred'], aggfunc ='size').keys().tolist()
    return starostne_skupine

# print(starostne_skupine(os.getcwd()+ "/KD2009.csv"))

leta = ['KD2009.csv','KD2009.csv','kd2010.csv','kd2011.csv','kd2012.csv','kd2013.csv','kd2014.csv','kd2015.csv','kd2016.csv','kd2017.csv','kd2018.csv','kd2019.csv']
podatki = []
for leto in leta:
    podatki.append(storitelji_dejanja(os.getcwd()+ "/" + leto))
# print(podatki[0])


#Narišemo 11 tortnih diagramov naenkrat
fig, axs = plt.subplots(nrows=2,ncols=6)

for ax in axs.flat:
    ax.axis('off')
fig.suptitle('Prikaz starostnih skupin osumljencev v posameznih letih', fontsize=24)

axs[0, 0].pie(podatki[0], shadow=True)
axs[0, 0].set_title('2009')

axs[0, 1].pie(podatki[2], shadow=True)
axs[0, 1].set_title('2010')

axs[0, 2].pie(podatki[3], shadow=True)
axs[0, 2].set_title('2011')

axs[0, 3].pie(podatki[4], shadow=True)
axs[0, 3].set_title('2012')

axs[0, 4].pie(podatki[5],shadow=True)
axs[0, 4].set_title('2013')

axs[0, 5].pie(podatki[6], shadow=True)
axs[0, 5].set_title('2014')

#druga vrstica
axs[1, 0].pie(podatki[7], shadow=True)
axs[1, 0].set_title('2015')

axs[1, 1].pie(podatki[8], shadow=True)
axs[1, 1].set_title('2016')

axs[1, 2].pie(podatki[9], shadow=True)
axs[1, 2].set_title('2017')

axs[1, 3].pie(podatki[10], shadow=True)
axs[1, 3].set_title('2018')

axs[1, 4].pie(podatki[11], shadow=True)
axs[1, 4].set_title('2019')


axs[1, 4].legend(starostne_skupine(os.getcwd()+ "/KD2009.csv")[1:], bbox_to_anchor=(2.5,2))


plt.show()

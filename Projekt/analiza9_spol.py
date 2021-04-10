# predstavimo spol osumljencev

from pridobivanje_podatkov import *
import pandas as pd
import os
import matplotlib.pyplot as plt


def spol(leto):    
    df = pd.read_csv(leto, sep=';', encoding = 'Windows-1250', low_memory = False)
    df.drop_duplicates(subset =["UraStoritve", 'DanVTednu', 'ZaporednaStevilkaKD'],
                      keep = False, inplace = True)
    df = df[['VrstaOsebe','Spol']]  #hkrati upoštevamo oba stolpca
    df = df[df['Spol'] != 'PRAVNA OSEBA']#ne upoštevamo pravne osebe
    
    df['stevilo'] = 1
    df = df.groupby(['VrstaOsebe','Spol']).count()['stevilo']['OVADENI OSUMLJENEC']
    return df


tabela_letnic = ['KD2009.csv','kd2010.csv','kd2011.csv','kd2012.csv','kd2013.csv','kd2014.csv','kd2015.csv','kd2016.csv','kd2017.csv','kd2018.csv','kd2019.csv']
moski = []
zenske = []
for leto in tabela_letnic:
    moski.append(spol(leto)['MOŠKI'])
    zenske.append(spol(leto)['ŽENSKI'])

x_os = ['2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
df = pd.DataFrame({'MOŠKI': moski, 'ŽENSKI': zenske}, index = x_os)
# df = df.sort_index()
histogram = df.plot.bar(figsize =(13,5),color=['cyan', 'lightpink'], rot = 0, edgecolor ='black' )
histogram.set_facecolor('darkgray')
histogram.set_title('DELEŽ OSUMLJENCEV GLEDE NA SPOL') 
plt.show()    

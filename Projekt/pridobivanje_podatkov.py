# kazniva dejanja

#pridobivanje podatkov s spleta

import requests
import re
from zipfile import ZipFile
from urllib.request import urlopen
import os
import pandas as pd

url = 'https://podatki.gov.si/dataset/mnzpkazniva-dejanja-od-leta-2009-dalje'
req = requests.get(url)
page = req.text
#print(page)

url2 = 'https://www.policija.si/baza/'

datoteke = set()
for datoteka in re.findall(r'href="[^"]+?/([^/"]+\.zip)"', page):
    datoteke.add(datoteka)
for datoteka in datoteke:
    #print(datoteka)
    odpri = urlopen(url2 + datoteka)
    trenutnizip = open("tempfile.zip", "wb")
    trenutnizip.write(odpri.read())
    trenutnizip.close()
    zip_datoteka = ZipFile("tempfile.zip")
    zip_datoteka.extractall(path = os.getcwd())
    zip_datoteka.close()
    
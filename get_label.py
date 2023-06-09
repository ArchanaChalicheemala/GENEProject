# -*- coding: utf-8 -*-
"""Get label.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13KU19iT_fEs8-YuX9DCxpk1y_f93FrLP
"""

import requests
import os
import pandas as pd
from google.colab import drive
drive.mount('/content/gdrive')
#path = "/var/www/html/"
#files = os.listdir(path)
#files = os.listdir('GSE13255_RAW/')
files='/content/gdrive/My Drive/GSE13255_RAW'
name = []
label = []
fs = files#[0:20]
for i,f in enumerate(fs):
    print(i)
    a = f.replace('.txt.gz','')
    url = f'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={a}'
    print(url)
    name.append(a)
    r = requests.get(url)
    a = r.text
    label.append(a.split('DX:')[1].split('<br>')[0].replace(' ', ''))
data = {'name': name, 'DX': label}
df = pd.DataFrame.from_dict(data)
df.to_csv('lebel_DX.csv')

"""# New Section"""

import requests
import os
import pandas as pd
from google.colab import drive
drive.mount('/content/gdrive')
#path = "/var/www/html/"
#files = os.listdir(path)
#files = os.listdir('GSE13255_RAW/')
files='/content/gdrive/My Drive/GSE13255_RAW'
name = []
label = []
fs = files#[0:20]
for i,f in enumerate(fs):
    print(i)
    a = f.replace('.txt.gz','')
    url = f'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={a}'
    print(url)
    name.append(a)
    r = requests.get(url)
    a = r.text
    try:
        label.append(a.split('DX:')[1].split('<br>')[0].replace(' ', ''))
    except IndexError:
        label.append("")
data = {'name': name, 'DX': label}
df = pd.DataFrame.from_dict(data)
df.to_csv('lebel_DX.csv')

for i,f in enumerate(fs):
    print(i)
    a = f.replace('.txt.gz','')
    url = f'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={a}'
    print(url)
    name.append(a)
    r = requests.get(url)
    a = r.text
    try:
        label.append(a.split('DX:')[1].split('<br>')[0].replace(' ', ''))
    except IndexError:
        label.append("")
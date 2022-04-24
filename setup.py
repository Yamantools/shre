import os
import shutil

os.system('pip install requests')
os.system('pip install UserAgent')
os.system('pip install pystyle')

import zipfile
with zipfile.ZipFile('DATA.zip', 'r') as zip_ref:
    zip_ref.extractall('DATA')
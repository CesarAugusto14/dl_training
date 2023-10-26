# Retrieving from ftp:
url = 'https://ftp.mcs.anl.gov/pub/candle/public/benchmarks/Examples/xform-smiles-data/'

# Downloading the data:
import urllib.request
import os
import zipfile

# Download EVERYTHING from the url:

# Get the list of files:
with urllib.request.urlopen(url) as response:
    html = response.read().decode('utf-8')
    
# Get the list of files:
files = []
for line in html.split('\n'):
    if 'href' in line:
        files.append(line.split('"')[1])
        
# Download the files:
for file in files:
    print('Downloading ' + file)
    urllib.request.urlretrieve(url + file, file)
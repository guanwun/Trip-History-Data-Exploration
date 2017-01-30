import requests
from zipfile import ZipFile
from io import BytesIO
import pandas as pd

def dataframe(weblink):
    url = requests.get(weblink)
    z = ZipFile(BytesIO(url.content))
    names = z.namelist()
    if len(names) == 1:
        file = names.pop()
        df = pd.read_csv(z.open(file))
        return df   
    else:
        return pd.DataFrame()
        
#create data frames for every data in the repository
Years = ['2016-Q3','2016-Q2','2016-Q1',
         '2015-Q4','2015-Q3','2015-Q2','2015-Q1',
         '2014-Q4','2014-Q3','2014-Q2','2014-Q1',
         '2013-Q4','2013-Q3','2013-Q2','2013-Q1',
         '2012-Q4','2012-Q3','2012-Q2','2012-Q1',
         '2011-Q4','2011-Q3','2011-Q2','2011-Q1',
         '2010-Q4']
url_before = "https://s3.amazonaws.com/capitalbikeshare-data/"
url_after1 = "-cabi-trip-history-data.zip"
url_after2 = "-cabi-trips-history-data.zip"
df = {}
ToDo = []
for name in Years:
    if name in ['2016-Q3','2016-Q2']:
        url = url_before + name + url_after2
    else:
        url = url_before + name + url_after1
    print(url)
    df[name] = dataframe(url)
    if df[name].empty == True:
        ToDo.append(name)
        
#only 2016-Q3 has more than 1 csv file
url = requests.get("https://s3.amazonaws.com/capitalbikeshare-data/2016-Q3-cabi-trips-history-data.zip")
z = ZipFile(BytesIO(url.content))
names = z.namelist()
temp = {}
while names:
    file = names.pop()
    print(file)
    temp[file] = pd.read_csv(z.open(file))
    
#merge 2016-Q3 data and store back into df dictionary
frame = [temp["2016-Q3-Trips-History-Data-2.csv"],temp["2016-Q3-Trips-History-Data-1.csv"]]
df['2016-Q3'] = pd.concat(frame)
df['2016-Q3'].info()

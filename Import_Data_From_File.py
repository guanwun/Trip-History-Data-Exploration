# download all the files from https://s3.amazonaws.com/capitalbikeshare-data/index.html

import pandas as pd

Years = ['2016-Q3','2016-Q2','2016-Q1',
         '2015-Q4','2015-Q3','2015-Q2','2015-Q1',
         '2014-Q4','2014-Q3','2014-Q2','2014-Q1',
         '2013-Q4','2013-Q3','2013-Q2','2013-Q1',
         '2012-Q4','2012-Q3','2012-Q2','2012-Q1',
         '2011-Q4','2011-Q3','2011-Q2','2011-Q1',
         '2010-Q4']

file = '-Trips-History-Data.csv'
df = {}
for name in Years:
    if name in ['2016-Q3']:
        temp = {}
        temp[1] = pd.read_csv('2016-Q3-Trips-History-Data-1.csv')
        temp[2] = pd.read_csv('2016-Q3-Trips-History-Data-2.csv')
        frame = [temp[1],temp[2]]
        df[name] = pd.concat(frame)
    else:
        file_name = name + file
        df[name] = pd.read_csv(file_name)
        
# station number dictionary
station = pd.read_csv('station_status.csv')
station = station[['name','terminalName']]
station.head()

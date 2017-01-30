## manipulate columns, extend time format

# rename columns for consistent purpose

# ['Duration', 'Start date', 'End date', 'Start station', 'End station','Bike number', 'Member type']
y1 = ['2013-Q3','2013-Q2','2013-Q1','2012-Q4','2012-Q3','2012-Q2',
      '2012-Q1','2011-Q4','2011-Q3','2011-Q2','2011-Q1','2010-Q4']
# ['Duration', 'Start date', 'Start station', 'End date', 'End station','Bike number', 'Member type']
y2 = ['2014-Q4','2014-Q3','2014-Q2','2014-Q1','2013-Q4']
# ['Duration (ms)', 'Start date', 'Start station', 'End date', 'End station', 'Bike number', 'Member type']
y3 = ['2015-Q2','2015-Q1']
#['Duration (ms)', 'Start date', 'End date', 'Start station number','Start station', 'End station number', 
# 'End station', 'Bike number','Member type']
y4 = ['2016-Q3','2016-Q2','2016-Q1','2015-Q4','2015-Q3']
for i1 in y1:
    df[i1].columns = ['Duration', 'Start date', 'End date', 'Start station', 'End station', 'Bike number', 'Member type']
for i2 in y2:
    df[i2].columns = ['Duration', 'Start date', 'Start station', 'End date', 'End station', 'Bike number', 'Member type']
    df[i2] = df[i2][['Duration', 'Start date', 'End date', 'Start station', 'End station', 'Bike number', 'Member type']]
for i3 in y3:
    df[i3].columns = ['Duration (ms)', 'Start date', 'Start station', 'End date', 'End station', 'Bike number', 'Member type']
    df[i3] = df[i3][['Duration (ms)', 'Start date', 'End date', 'Start station', 'End station', 'Bike number', 'Member type']]
for i4 in y4:
    df[i4].columns = ['Duration (ms)', 'Start date', 'End date', 'Start station number','Start station', 'End station number', 
                      'End station', 'Bike number','Member type']
    df[i4] = df[i4][['Duration (ms)', 'Start date', 'End date', 'Start station number', 'End station number',
                     'Bike number', 'Member type']]

# Add Duration to years of 2015-2016

def time(ms):
    x = int(ms / 1000)
    seconds = x % 60
    x = int(x / 60)
    minutes = x % 60
    x = int(x / 60)
    hours = x
    time = str(hours) + 'h' + ' ' + str(minutes) + 'm' + ' ' + str(seconds) + 's'
    return(time)

for name in ['2016-Q3','2016-Q2','2016-Q1','2015-Q4','2015-Q3','2015-Q2','2015-Q1']:
    newcols = df[name]['Duration (ms)'].apply(time)
    df[name] = pd.concat([df[name], newcols], axis=1)
    df[name].columns = ['Duration (ms)', 'Start date', 'End date', 'Start station', 'End station',
                        'Bike number', 'Member type', 'Duration']
    df[name] = df[name][['Duration (ms)', 'Duration', 'Start date', 'End date', 
                         'Start station', 'End station','Bike number', 'Member type']]

# Add Duration (ms) to years of 2010-2014

import itertools 

def millisecond(time):
    number = ["".join(x) for _, x in itertools.groupby(time, key=str.isdigit)]
    ms = int(number[0])*3600000 + int(number[2])*60000 + int(number[4])*1000
    return(ms)

for name in ['2014-Q4','2014-Q3','2014-Q2','2014-Q1',
             '2013-Q4','2013-Q3','2013-Q2','2013-Q1',
             '2012-Q4','2012-Q3','2012-Q2','2012-Q1',
             '2011-Q4','2011-Q3','2011-Q2','2011-Q1','2010-Q4']:
    newcols = df[name]['Duration'].apply(millisecond)
    df[name] = pd.concat([df[name], newcols], axis=1)
    df[name].columns = ['Duration', 'Start date', 'End date', 'Start station', 
                        'End station','Bike number', 'Member type', 'Duration (ms)']
    df[name] = df[name][['Duration (ms)', 'Duration', 'Start date', 'End date', 
                         'Start station', 'End station','Bike number', 'Member type']]

# we only need station number

# 2010-Q4, 2011-Q1, 2011-Q2, 2011-Q3, 2011-Q4
# extract number
for name in ['2011-Q4','2011-Q3','2011-Q2','2011-Q1','2010-Q4']:
    df[name]['Start station'] = df[name]['Start station'].str.replace('.*\(', '', case = False)
    df[name]['Start station'] = df[name]['Start station'].str.replace('\)', '', case = False)
    df[name]['End station'] = df[name]['End station'].str.replace('.*\(', '', case = False)
    df[name]['End station'] = df[name]['End station'].str.replace('\)', '', case = False)
    df[name] = df[name][['Duration (ms)', 'Duration', 'Start date', 'End date', 
                         'Start station', 'End station','Bike number', 'Member type']]
    df[name].columns = ['Duration (ms)', 'Duration', 'Start date', 'End date', 
                         'Start station number', 'End station number','Bike number', 'Member type']
# 2012-Q1 to 2015-Q2
# map address to station number
for name in ['2015-Q2','2015-Q1',
             '2014-Q4','2014-Q3','2014-Q2','2014-Q1',
             '2013-Q4','2013-Q3','2013-Q2','2013-Q1',
             '2012-Q4','2012-Q3','2012-Q2','2012-Q1']:
    station.columns = ['Start station','Start station number']
    df[name] = pd.merge(df[name], station, on='Start station')
    station.columns = ['End station','End station number']
    df[name] = pd.merge(df[name], station, on='End station')
    df[name] = df[name][['Duration (ms)', 'Duration', 'Start date', 'End date', 
                         'Start station number', 'End station number','Bike number', 'Member type']]
# 2015-Q3 to 2016-Q3
# change column name
for name in ['2015-Q3','2015-Q4','2016-Q1','2016-Q2','2016-Q3']:
    df[name].columns = ['Duration (ms)', 'Duration', 'Start date', 'End date', 
                         'Start station number', 'End station number','Bike number', 'Member type']

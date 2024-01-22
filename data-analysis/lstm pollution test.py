import pandas as pd
from datetime import datetime

#combine dates
def parse(x):
	return datetime.strptime(x,"%Y %m %d %H")
dataset = pd.read_csv(r'C:\Users\user\Downloads\PRSA_data_2010.1.1-2014.12.31.csv', parse_dates = [['year', 'month', 'day', 'hour']], index_col=0, date_parser=parse)

#drop column labelled no
dataset.drop('No', axis=1, inplace=True)
#rename columns
dataset.columns = ['pollution', 'dew', 'temp', 'press', 'wnd_dir', 'wnd_spd', 'snow', 'rain']
dataset.index.name = 'date'
#fill na values with 0
dataset['pollution'].fillna(0, inplace=True)
#drop first 24 hours
print(dataset.shape)
dataset = dataset[24:]
print(dataset.head())
print(dataset.shape)
#save as pollution.csv 
dataset.to_csv('pollution.csv')

print("hi")
# Importing more than 50 files to MySQL through Python in seconds
from sqlalchemy import create_engine # Pip install sqlalchemy
import pandas as pd #pip install pandas
import os
# Note:install Pymysql if not installed
# Create a blank database where the csv files needs to be imported as a table
hostname='localhost'
username= "root"
password = "Qwert12345%40"
port=3306
database="test3"

engine=create_engine('mysql+pymysql://' +username+':'+password+'@'+hostname+':'+str(port)+'/'+database)
print(engine)

conn=engine.connect()

path=r'C:\Users\praty\Downloads\All_csv_fies'
files=os.listdir(path)

for i in files:
    data=pd.read_csv(os.path.join(path,i))
    print(i)
    data.to_sql(name=i,con=engine,index=False,if_exists='replace')
    print('Imported',i)

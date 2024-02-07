from sqlalchemy import create_engine # Pip install sqlalchemy
from sqlalchemy.engine import URL
import pandas as pd # pip install pandas
import os
import pypyodbc # Pip install pypyodbc

SERVER_NAME= 'pratyush625'
DATABASE_NAME='test_csv'

connection_string = f"""
           DRIVER={{SQL Server}};
           SERVER={SERVER_NAME};
           DATABASE={DATABASE_NAME};
           Trusted_Connection=yes;
"""

connection_url=URL.create('mssql+pyodbc', query={'odbc_connect': connection_string})
engine= create_engine(connection_url, module=pypyodbc)

path=r'C:\Users\praty\Downloads\All_csv_fies_1'
files=os.listdir(path)

for i in files:
    data=pd.read_csv(os.path.join(path,i))
    print(i)
    data.to_sql(name=i,con=engine,index=False,if_exists='replace')
    print('Imported',i)

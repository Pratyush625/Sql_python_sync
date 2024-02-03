# Sql_python_sync
"Syncing Python with SQL: Streamlining Data Integration and Management"

Importing Multiple CSV Files into MySQL and MSSQL Using Python

Introduction:
In today's data-driven landscape, efficient data management is crucial for businesses and organizations. One common scenario involves importing CSV files into databases to harness, analyze, and derive insights from data. This article explores the significance of automating this process and emphasizes the advantages of leveraging Python for seamless integration.

Importance of Automation:
Manually importing CSV files into databases can be time-consuming and error-prone. Automating this process saves time and reduces the likelihood of human errors. It allows data professionals to focus on more complex tasks like data analysis and interpretation rather than spending valuable time on routine data-loading tasks.

Benefits of Using Python:

Versatility: Python is a versatile programming language with a rich ecosystem of libraries, making it suitable for a wide range of tasks, including data manipulation, cleaning, and database interactions.

Pandas Library: Python's Pandas library provides powerful data manipulation tools, making it easy to read CSV files into DataFrames, perform data cleaning, and prepare data for insertion into databases.

SQLAlchemy for Database Interactions: Python's SQLAlchemy library simplifies database interactions by providing a unified interface for connecting to different database systems. It supports multiple database backends, including MySQL, MSSQL, PostgreSQL, and more.

Automation and Scripting: Python's scripting capabilities enable the creation of reusable scripts or workflows, allowing for the automation of repetitive tasks. This is particularly beneficial for regularly updating databases with new CSV data.

Community Support: Python has a large and active community. This means access to a wealth of resources, tutorials, and community support when facing challenges during data integration.

By combining the strengths of Python with the efficiency of automation, data professionals can enhance their workflow, reduce manual errors, and ensure a streamlined and reliable process for importing CSV files into databases.

Below are the steps to justify the above process

Setting Up the Environment:
Prerequisites required:
Python and databases such as MySQL, MSSQL, or PostgreSQL, you need to have the respective database server installed on your local machine.

Below is the code mentioned to push multiple CSV files from local to MYSQL using Python script:

from sqlalchemy import create_engine # Pip install sqlalchemy
import pandas as pd #pip install pandas
import os
# Note: install Pymysql if not installed
# Create a blank database where the CSV files need to be imported as a table

hostname='localhost'
username= "root"
password = "**********"
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
    print('Imported', I)

Below is the code mentioned to push multiple CSV files from local to MSSQL using Python script:

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
    print('Imported', i)






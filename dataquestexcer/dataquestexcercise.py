# This is an excercise to handle data base from SQl and basic manipulation of data base in python
import os
import pandas as pd
import math
import sqlite3
import numpy as np
os.chdir('/Users/khaterehmohajery1/Documents/DataScience/DataScience-PythonProjects/dataquestexcer')
conn = sqlite3.connect('factbook.db')
query = "select * from facts;"
df = pd.read_sql_query(query, con = conn)
conn.close()
# To calculate the population of a a country in n years from now based on current population and growth rate
def pop_growth(country, year):
    db = df[['name','population', 'population_growth']]
    #db = df.loc[:, ['name','population', 'population_growth']] does the same thing
    # drops the row if values in one of these two columns is nan
    db = db.dropna(subset = ['population','population_growth'])
    data = db.loc[db['name'] == str(country),:]
    future_pop = float(data['population'] * math.exp(data['population_growth'] /100 * year))
    print("The futur population of " + str(country) + " is " + str(future_pop) + " in " + str(year) + " years.")

# This function gives out the name of countries which have lower population in 35 years form now
def lower(df):
    db = df[['name','population', 'population_growth']]
    db = db.dropna(subset = ['population','population_growth'])
    db['35_population'] = db['population'] * np.exp(db['population_growth'] /100 * 35)
    #db = db.loc[db['35_population'] < db['population']]
    return db
    
#highest and lowest population density counties
def density(df):
    db = df[["name",'population','area_land']]
    db = db.dropna(subset =  ["population",'area_land'])
    db = db.loc[db['area_land'] != 0]
    db['density'] = db['population'] / db['area_land']
    db = db.sort(columns= 'density')
    lowest_density = db.iloc[0:10, 0]
    highest_density = db.iloc[len(db)-11:len(db)-1,0]
    # or instead of refering by position reset index
    #db = db.reset_index(drop = True, inplace =True)
    #lowest_density = db.loc[0:10, 'name']
    #highest_density = db.loc[len(db)-11:len(db)-1,'name']
    return(highest_density,lowest_density)


    
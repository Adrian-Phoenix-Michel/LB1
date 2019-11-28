import pandas as pandas
import numpy as numpy
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import glob as glob
import re as re

### List ###

us_census = []
files = glob.glob("states*.csv")

for states in files:
  data = pandas.read_csv(states)
  us_census.append(data)
#print(us_census)

### DataFrame ###

us_census = pandas.DataFrame(data)

### Head ###

us_census_head = us_census.head
#print(us_census_head)

### Columns ###

us_census_columns = us_census.columns
#print(us_census_columns)

### DTypes ###

us_census_dtypes = us_census.dtypes
#print(us_census_dtypes)

### Income -> Regex ###

us_census["Income"] = us_census["Income"].replace("[\$,]", "", regex=True)
us_census.Income = pandas.to_numeric(us_census["Income"])

### PopulationGender -> Regex ###

us_census_gender = us_census["GenderPop"].str.split("_")

us_census["Men"] = us_census_gender.str.get(0).replace("M", "", regex=True)
us_census["Women"] = us_census_gender.str.get(1).replace("F", "", regex=True)
#print(us_census_head)

### Scatter (or Histrogram) ###

#plt.scatter(us_census["Women"], us_census["Income"])
#plt.scatter(us_census["Men"], us_census["Income"])
#plt.show()
#plt.savefig("myhistrogram_both.png")

#plt.scatter(us_census["Men"], us_census["Income"])
#plt.show()
#plt.savefig("myhistrogram_men.png")

#plt.scatter(us_census["Women"], us_census["Income"])
#plt.show()
#plt.savefig("myhistrogram_women.png")

### Replacing the NaN's ###

us_census = us_census.fillna(0)
#print(us_census["Women"])

### Duplicates and their Drops ###

us_census_duplicates = pandas.duplicates(us_census)
#print(us_census_duplicates)
us_census_droped_duplicates = us_census.drop_duplicates


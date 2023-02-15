import pandas as pd

#Create a DataFrame out of the 2018 Census
squirrel_raw = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_unique_colors = squirrel_raw["Primary Fur Color"].unique()


squirrel_new = {
    'Fur Color': [],
    'Count': []
}
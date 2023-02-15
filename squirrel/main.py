import pandas as pd

#Create a DataFrame out of the 2018 Census
squirrel_raw = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#Get a hold of a list of all squirrel colors
squirrel_unique_colors = squirrel_raw["Primary Fur Color"].unique()
print(squirrel_unique_colors)


#Get the length of the grey squirrel list
gray_squirrel_count = int(len(squirrel_raw[squirrel_raw["Primary Fur Color"] == "Gray"]))
red_squirrel_count = int(len(squirrel_raw[squirrel_raw["Primary Fur Color"] == "Cinnamon"]))
black_squirrel_count = int(len(squirrel_raw[squirrel_raw["Primary Fur Color"] == "Black"]))
print(gray_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

#Create a dictionary to turn into DataFrame
squirrel_new = {
    'Fur Color': ["Gray", "Cinnamon", "BLack"],
    'Count': [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}


df = pd.DataFrame.from_dict(squirrel_new)
df.to_csv("squirrel_color_count.csv")

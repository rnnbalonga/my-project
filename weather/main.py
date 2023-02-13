#Without Using Pandas:

# import csv

# with open("weather_data.csv", "r") as weather_file:
#     data = csv.reader(weather_file)
#     #Get the temperatures in each line of the file as an integer and add them to the list: temperatures
#     temperatures = []
#     #Loop through each row in the file
#     for row in data:
#         #Select temperatures which is in index 1 of each row.
#         #Add an if statement to exclude the word temp
#         if row[1] != "temp":
#             #Append index [1] of each row to the temperature list as an integer
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas 

data = pandas.read_csv("weather_data.csv")

#Convert dataframe to dictionary
data_dict = data.to_dict()
# print(data_dict)

#Convert series to list
temp_list = data["temp"].to_list()
# print(temp_list)

#Get mean of series 'temp' using pandas
temp_mean = data["temp"].mean()
# print(temp_mean)

#Get max of 'temp' using pandas
# print(data["temp"].max())

#Get data in row
# print(data[data.day == "Monday"])

# #Get data of row with max 'temp'
# print(data[data.temp == data["temp"].max()])

#Get temperature of Monday and convert it to farenheight

# monday = data[data.day == "Monday"]
# monday_temp = ((monday.temp) * 1.8) + 32
# print(monday_temp)

#Create dataframe from scratch
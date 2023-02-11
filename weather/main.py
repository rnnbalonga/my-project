import csv

with open("weather_data.csv", "r") as weather_file:
    csv.reader(weather_file)
    #Get the temperatures in each line of the file as an integer and add them to the list: temperatures
    temperatures = []
    for row in weather_file:
        print(row)
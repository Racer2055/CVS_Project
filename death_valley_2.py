import csv
from datetime import datetime
import matplotlib.pyplot as plt

def main():

    open_file = open("death_valley_2018_simple.csv", "r")
    open_file1 = open("sitka_weather_2018_simple.csv", "r")

    csv_file = csv.reader(open_file, delimiter=",")
    csv_file1 = csv.reader(open_file1, delimiter = ",")

    header_row = next(csv_file)
    header_row1 = next(csv_file1)

    fig, (ax1,ax2) = plt.subplots(2, sharex = True)

    file_info = get_city_information(csv_file,get_column_locations(header_row)['high'],get_column_locations(header_row)['low'],get_column_locations(header_row)['date'],get_column_locations(header_row)['name'])
    ax2.plot(file_info['Dates'], file_info['High'], c = "red")
    ax2.plot(file_info['Dates'], file_info['Low'], c = "blue")
    ax2.set_title(file_info['Name'], fontsize = 12)
    ax2.fill_between(file_info['Dates'], file_info['High'], file_info['Low'], facecolor ='blue', alpha = 0.1)
    

    file_info1 = get_city_information(csv_file1,get_column_locations(header_row1)['high'],get_column_locations(header_row1)['low'],get_column_locations(header_row1)['date'],get_column_locations(header_row1)['name'])
    ax1.plot(file_info1['Dates'], file_info1['High'], c = "red")
    ax1.plot(file_info1['Dates'], file_info1['Low'], c = "blue")
    ax1.set_title(file_info1['Name'], fontsize = 12)
    ax1.fill_between(file_info1['Dates'], file_info1['High'], file_info1['Low'], facecolor ='blue', alpha = 0.1)
    
    fig.suptitle(f"Temperature comparision between {file_info1['Name']} and {file_info['Name']}", fontsize = 16)
 
    fig.autofmt_xdate()
    plt.show()

def get_column_locations(header_row):
    locations = {}
    for index, column_header in enumerate(header_row):
        if(column_header == "TMAX"):
            locations['high'] = index
        if(column_header == "TMIN"):
            locations['low'] = index
        if(column_header == "DATE"):
            locations['date'] = index
        if(column_header == "NAME"):
            locations['name'] = index
    return locations


def get_city_information(csv_file,high_loc,low_loc,date_loc,name_loc):
    highs = []
    dates = []
    lows = []
    names = []
    for row in csv_file:
        try:
            high = int(row[high_loc])
            low = int(row[low_loc])
            name = row[name_loc]
            current_date = datetime.strptime(row[date_loc], '%Y-%m-%d')
            
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)
            names.append(name)
    info = {'High': highs,"Low":lows,"Dates":dates,"Name":names[0]}
    return info


main()
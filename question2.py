# pandas is used for working with tables (CSV files)
# glob is used to find all CSV files in a folder
import pandas as pd
import glob
 
 
# This function losds all CSV files and combines them into one
def create_combined_data_file():
 
    # Find all CSV files inside the temperatures folder
    all_files = glob.glob("/home/loki/Desktop/CDU/SoftwareNow-HIT137/Assignment/Assignment2/codes/temperatures/*.csv")
 
    # Create an empty list to store all CSV data
    file_list = []
 
    # Loop through each CSV file
    for f in all_files:
        # Read the data of CSV file
        data = pd.read_csv(f)
        file_list.append(data)
 
    # Combining all .csv file into one
    combined_file = pd.concat(file_list, ignore_index=True)
 
    # Converting combined_file to .csv file
    #combined_file.to_csv("/home/loki/Desktop/CDU/SoftwareNow-HIT137/Assignment/Assignment2/practiceCode/temperatures/combined_files.csv")
 
    # Return the combined table so other functions can use it
    return combined_file
 
 
# List of all month columns in the dataset
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
 
 
# This function calculates the average temperature for each season
def find_seasonal_average(combined_file):
 
    # Defining Australian seasons and their months
    seasons = {
        "Summer": ["December", "January", "February"],
        "Autumn": ["March", "April", "May"],
        "Winter": ["June", "July", "August"],
        "Spring": ["September", "October", "November"]
    }
 
    # Dictionary to store the results
    results = {}
 
    # IterAting through each season
    for season, months in seasons.items():
 
        # Calculate the average temperature for that season
        season_avg = combined_file[months].mean().mean()
 
        # Store the result rounded to 2 decimal places
        results[season] = round(season_avg, 2)
 
    # Save the seasonal averages into a text file
    with open("/home/loki/Desktop/CDU/SoftwareNow-HIT137/Assignment/Assignment2/codes/temperatures/average_temp.txt", "w") as file:
        for season, avg in results.items():
            file.write(f"{season}: {avg}°C\n")


# This function finds which station has the largest temperature range
def find_temperature_range(combined_file):
 
    # Find the hottest month for each station record
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.max.html
    # MaxTemp is added column which has the highest recorded temperature of that station
    combined_file["MaxTemp"] = combined_file[months].max(axis=1)
 
    # Find the coldest month for each station record
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.min.html
    # MinTemp is added column which has the lowest recorded temperature of that station
    combined_file["MinTemp"] = combined_file[months].min(axis=1)
 
    # Grouping all records by station name and finding the highest, and the lowest temperature ever
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html
    station_data = combined_file.groupby("STATION_NAME").agg(
        MaxTempValue=("MaxTemp", "max"),
        MinTempValue=("MinTemp", "min")
    )
 
    # Calculate the temperature range
    station_data["Range"] = station_data["MaxTempValue"] - station_data["MinTempValue"]
 
    # Find the largest temperature range
    max_range = station_data["Range"].max()
 
    # Find all stations that have this largest range
    largest_range_stations = station_data[station_data["Range"] == max_range]
 
    # Save the result into a text file
    with open("/home/loki/Desktop/CDU/SoftwareNow-HIT137/Assignment/Assignment2/codes/temperatures/largest_temp_range_station.txt", "w") as file:
        for station, row in largest_range_stations.iterrows():
            file.write(
                f"{station}: Range {row['Range']:.2f}°C "
                f"(Max: {row['MaxTempValue']:.2f}°C, Min: {row['MinTempValue']:.2f}°C)\n"
            )
 
 
# This function finds the most stable and most unstable temperature stations
def find_temperature_stability(combined_file):
 
    # Converting the table from wide format to long format
    # This puts all temperatures into one column
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.melt.html
    temp_long = combined_file.melt(
        id_vars=["STATION_NAME"],
        value_vars=months,
        var_name="Month",
        value_name="Temperature"
    )
 
    # Calculating the standard deviation for each station
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html
    station_std = temp_long.groupby("STATION_NAME")["Temperature"].std()
 
    # Find the smallest and biggest standard deviation
    min_std = station_std.min()
    max_std = station_std.max()
 
    # Find the most stable station(s)
    most_stable = station_std[station_std == min_std]
 
    # Find the most variable station
    most_variable = station_std[station_std == max_std]
 
    # Saving results into a text file
    with open("/home/loki/Desktop/CDU/SoftwareNow-HIT137/Assignment/Assignment2/codes/temperatures/temperature_stability_stations.txt", "w") as file:
 
        # Write most stable station(s)
        for station, std in most_stable.items():
            file.write(f"Most Stable: {station}: StdDev {std:.2f}°C\n")
 
        # Write most variable station(s)
        for station, std in most_variable.items():
            file.write(f"Most Variable: {station}: StdDev {std:.2f}°C\n")
 
 
# Main function that runs everything
def main():
    # Loading and combining all CSV data
    combined_data = create_combined_data_file()
 
    # Calculating seasonal averages
    find_seasonal_average(combined_data)
 
    # Finding station with largest temperature range
    find_temperature_range(combined_data)
 
    # Finding most stable and most unstable stations
    find_temperature_stability(combined_data)
 
if __name__ == "__main__":
    main()
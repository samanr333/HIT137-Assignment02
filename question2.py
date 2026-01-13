# pandas is used for working with tables (CSV files)
# glob is used to find all CSV files in a folder
import pandas as pd
import glob
 
 
# This function losds all CSV files and combines them into one
def create_combined_data_file():
 
    # Find all CSV files inside the temperatures folder
    all_files = glob.glob("temperatures/*.csv")
 
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
    with open("temperatures/average_temp.txt", "w") as file:
        for season, avg in results.items():
            file.write(f"{season}: {avg}°C\n")
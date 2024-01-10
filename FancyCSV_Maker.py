import csv
import shutil
import datetime
import pandas as pd

#clientIp=172.19.131.160&clientMac=F8:4D:89:5C:58:EE

def calculate_wind_chill(temperature, wind_speed):
    """
    Calculate wind chill using the National Weather Service formula.

    :param temperature: Temperature in degrees Fahrenheit
    :param wind_speed: Wind speed in miles per hour
    :return: Wind chill in degrees Fahrenheit
    """
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
    return wind_chill

def format_DT(rowlist):
    current_year = datetime.datetime.now().year
    date_components = rowlist
    month, day, hour = map(int, date_components)
    formatted_date_time = datetime.datetime(current_year, month, day, hour)
    formatted_date_time_str = formatted_date_time.strftime("%I'%p %a")
    if formatted_date_time_str[0] == "0":
        return " " + formatted_date_time_str[1:]

    else:
        return formatted_date_time_str
    
def format_DT(rowlist):
    from datetime import datetime
    current_year = datetime.now().year
    date_components = rowlist
    month, day, hour = map(int, date_components)
    formatted_date_time = datetime(current_year, month, day, hour)
    formatted_date_time_str = formatted_date_time.strftime("%H:%M %a")
    return formatted_date_time_str
    
def wind_direction_to_cardinal(degrees):
    """
    Convert wind direction in degrees to cardinal direction.

    Parameters:
    degrees (float): Wind direction in degrees.

    Returns:
    str: Cardinal direction (e.g., N, NE, E, SE, etc.)
    """
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                  "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    index = int((degrees + 11.25) / 22.5)
    return directions[index % 16]

# Example usage




def dup_file():
    source_file = "Weather_Data.csv"
    destination_file = "Fancy_CSV.csv"

    shutil.copy(source_file, destination_file)
    return destination_file

def check_midnight(hour):
    if hour == '24':
        return '0'
    else:
        return hour

input_file = dup_file()
columns_list = []

# Open the CSV file for reading
with open(input_file, 'r') as csv_file:
    reader = csv.reader(csv_file)
    
    # Iterate through each row in the CSV file
    for row in reader:
        # Extract the first three columns (assuming zero-based indexing)
        first_three_columns = row[:3]
        columns_list.append(first_three_columns)


# Print the list of lists
daterow = []
for row in columns_list[1:]:
    row[2] = check_midnight(row[2][:-2])
    DT = format_DT(row)
    daterow.append(DT)
    #print(DT)
#print(daterow)

# Load the original CSV file
input_file = "Fancy_CSV.csv"
df = pd.read_csv(input_file)

wind_degrees = list(df['Ridge_dir'])
cardinal_directions = [wind_direction_to_cardinal(d) for d in wind_degrees]
wind_degrees = list(df['TW_Dir'])
cardinal_directions = [wind_direction_to_cardinal(d) for d in wind_degrees]

#print(cardinal_directions)

# Create a new column from the provided list
new_column_data = daterow

# Insert the new column as the first column in the DataFrame
df.drop(df.columns[7], axis=1, inplace=True)
df.insert(7, 'TW_Dir', cardinal_directions)
df.drop(df.columns[4], axis=1, inplace=True)
df.insert(4, 'Ridge_dir', cardinal_directions)
df.insert(0, 'DateTime', new_column_data)

print()

df.drop(df.columns[1], axis=1, inplace=True)
df.drop(df.columns[1], axis=1, inplace=True)
df.drop(df.columns[1], axis=1, inplace=True)
df = df[['DateTime','AVG_Temp','AVG_RH','H2O','NewSnow','ToatalSnow','Ridge_Speed','Ridge_dir','Ridge_Gust','TW_Speed','TW_Dir','TW_Gust']]
df_reversed = df.iloc[::-1].reset_index(drop=True)

# Save the updated DataFrame to a new CSV file
output_file = "Fancy_CSV.csv"
df_reversed.to_csv(output_file, index=False)

print(f"New column added as the first column, and data saved to {output_file}.")


# wind_degrees = list(df['Ridge_dir'])
# RidgeSpeed = list(df['Ridge_Speed'])
# conc_windspeed = []

# for i in range(0,(len(wind_degrees))):
#     conc_windspeed.append(f"{str(RidgeSpeed[i])} {wind_degrees[i]}")

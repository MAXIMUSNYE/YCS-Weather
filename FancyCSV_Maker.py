import pandas as pd
import csv
import shutil
import datetime

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
print(daterow)


# Load the original CSV file
input_file = "Fancy_CSV.csv"
df = pd.read_csv(input_file)

# Create a new column from the provided list
new_column_data = daterow

# Insert the new column as the first column in the DataFrame
df.insert(0, 'DateTime', new_column_data)

# Save the updated DataFrame to a new CSV file
output_file = "Fancy_CSV.csv"
df.to_csv(output_file, index=False)

print(f"New column added as the first column, and data saved to {output_file}.")



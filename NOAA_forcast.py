# import requests
# from bs4 import BeautifulSoup
# import csv

# yc = 'https://forecast.weather.gov/MapClick.php?lat=45.2258&lon=-111.3949&unit=0&lg=english&FcstType=text&TextType=1'

# url = 'https://forecast.weather.gov/MapClick.php?lon=-111.4418981802124&lat=45.242171405990916'
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# #if response.status_code == 200:
#     # Print the HTML content of the page
#     #print(response.text)
# # else:
# #     print("Failed to retrieve the web page. Status code:", response.status_code)


# soup = BeautifulSoup(response.text, 'html.parser')

# # Extract the relevant data from the HTML
# forecast_data = []
# for div in soup.find_all('div', class_='tombstone-container'):
#     period_name = (div.find('p', class_='period-name').get_text()).replace('yN', 'y N')
#     short_desc = div.find('p', class_='short-desc').get_text()
#     temp = div.find('p', class_='temp').get_text()
#     forecast_data.append([period_name, short_desc, temp])

# # Display the data as a table
# print("Period Name,Short Description,Temperature")
# for data in forecast_data:
#     print(",".join(data))

# print(forecast_data)

# data = forecast_data

# transposed_data = list(map(list, zip(*data)))

# # Create a CSV file
# csv_file = "noaa_shortcast.csv"
# with open(csv_file, 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(transposed_data)

# csv_file



import pandas as pd
from tabulate import tabulate

# Create a DataFrame from your CSV data
data = [
    ["ChristmasDay", "Rain", "High: 48 °F"],
    ["Tonight", "Rain", "Low: 47 °F"],
    ["Tuesday", "Rain", "High: 51 °F"],
    ["Tuesday Night", "Rain", "Low: 44 °F"],
    ["Wednesday", "Rain Likely", "High: 51 °F"],
    ["Wednesday Night", "Rain", "Low: 45 °F"],
    ["Thursday", "Rain", "High: 53 °F"],
    ["Thursday Night", "Chance Rain", "Low: 44 °F"],
    ["Friday", "Slight ChanceRain", "High: 53 °F"]
]

columns = ["Period Name", "Short Description", "Temperature"]
df = pd.DataFrame(data, columns=columns)

# Set "Period Name" as the index and transpose the DataFrame
df = df.set_index("Period Name").transpose()

# Display the transposed DataFrame using tabulate
table_str = tabulate(df, headers="keys", tablefmt="grid")
print(table_str)



#     <table>
#         <thead>
#             <tr>
#                 <th>Today</th>
#                 <th>Tonight</th>
#                 <th>Sunday</th>
#                 <th>Sunday Night</th>
#                 <th>NewYears'sDay</th>
#                 <th>Monday Night</th>
#                 <th>Tuesday</th>
#                 <th>Tuesday Night</th>
#                 <th>Wednesday</th>
#             </tr>
#         </thead>
#         <tbody>
#             <tr>
# <td>Mostly Sunny</td>
# <td>Mostly Cloudy</td>
# <td>Mostly Cloudy</td>
# <td>Mostly Sunny</td>
# <td>Mostly Cloudy</td>
# <td>Mostly Sunny</td>
# <td>Mostly Clear</td>
# <td>Mostly Sunny</td>
# </tr>
# <tr>
#     <td>Low: 27 °F</td>
#     <td>High: 33 °F</td>
#     <td>Low: 27 °F</td>
#     <td>High: 33 °F</td>
#     <td>Low: 27 °F</td>
#     <td>High: 33 °F</td>
#     <td>Low: 27 °F</td>
#     <td>High: 33 °F</td>
#     <td>Low: 27 °F</td>
#     <td>High: 33 °F</td>
#     </tr>
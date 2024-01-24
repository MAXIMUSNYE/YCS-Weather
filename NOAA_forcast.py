import requests
from bs4 import BeautifulSoup
import csv

yc = 'https://forecast.weather.gov/MapClick.php?lat=45.2258&lon=-111.3949&unit=0&lg=english&FcstType=text&TextType=1'

url = 'https://forecast.weather.gov/MapClick.php?lon=-111.4418981802124&lat=45.242171405990916'
#https://forecast.weather.gov/MapClick.php?lon=-111.44276842781188&lat=45.24088227128141
response = requests.get(url)

def shortcast_get():
    soup = BeautifulSoup(response.text, 'html.parser')
    print (soup)

    forecast_data = []
    for div in soup.find_all('div', class_='tombstone-container'):
        period_name = (div.find('p', class_='period-name').get_text()).replace('yN', 'y N')
        short_desc = div.find('p', class_='short-desc').get_text()
        temp = div.find('p', class_='temp').get_text()
        forecast_data.append([period_name, short_desc, temp])

    data = forecast_data
    return data

def shortcast_get():
    soup = BeautifulSoup(response.text, 'html.parser')

    forecast_data = []
    for div in soup.find_all('div', class_='tombstone-container'):
        period_name = div.find('p', class_='period-name')
        short_desc = div.find('p', class_='short-desc')
        temp = div.find('p', class_='temp')

        # Check if all elements exist
        if period_name and short_desc and temp:
            period_name_text = period_name.get_text().replace('yN', 'y N')
            short_desc_text = short_desc.get_text()
            temp_text = temp.get_text()

            forecast_data.append([period_name_text, short_desc_text, temp_text])

    return forecast_data


# def shortcast_get():
#     soup = BeautifulSoup(response.text, 'html.parser')
#     #print(soup)

#     forecast_data = []
#     for div in soup.find_all('div', class_='tombstone-container'):
#         period_name = (div.find('p', class_='period-name').get_text()).replace('yN', 'y N')
        
#         # Find short description
#         short_desc = div.find('p', class_='short-desc')
#         if short_desc:
#             short_desc = short_desc.get_text()
#         else:
#             short_desc = "N/A"  # Or any default value you want to use

#         # Find temperature
#         temp = div.find('p', class_='temp')
#         if temp:
#             temp = temp.get_text()
#         else:
#             temp = "N/A"  # Or any default value you want to use

#         forecast_data.append([period_name, short_desc, temp])

#     return forecast_data


print("NOAA weeks forcast")
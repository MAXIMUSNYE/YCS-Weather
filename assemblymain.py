import csv
import requests

def refresh_YCWD():
    url = 'https://yellowstoneclub.com/snowdata/TIM1HR.RPT'

    response = requests.get(url)
    text = (response.text)

    if response.status_code == 200:
        lines = text.strip().split('\n')
        header = ["Month","Day","Hour","Ridge_Speed","Ridge_dir","Ridge_Gust","TW_Speed","TW_Dir","TW_Gust","AVG_Temp","AVG_RH","H2O","NewSnow","ToatalSnow"]
        data_lines = [line.strip().split() for line in lines[7:]]

        with open('weather_data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerows(data_lines)
        return data_lines
    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)

refresh_YCWD()

import Wind_Rose
import matplotlib
from Multi_Graph import plot_data_from_csv
plot_data_from_csv()
import FancyCSV_Maker
from HTML_updater import get_timestamp

print("Done")


print('\n',get_timestamp(),'\n')



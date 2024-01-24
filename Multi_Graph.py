import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import io

def calculate_wind_chill(temperature, wind_speed):
    """
    Calculate wind chill using the National Weather Service formula.

    :param temperature: Temperature in degrees Fahrenheit
    :param wind_speed: Wind speed in miles per hour
    :return: Wind chill in degrees Fahrenheit
    """
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
    return wind_chill


def plot_data_from_csv():
    # Reading the data from the CSV content
    plt.rcParams['font.size'] = 10
    plt.rcParams['font.family'] = 'sans-serif'
    #plt.rcParams['font.family'] = 'Helvetica'
    data = pd.read_csv("weather_data.csv")
    hrlables = list(data['Hour'])
    data['Hour'] = range(len(data))                                   ######___-----##_

    data['Wind Chill (°C)'] = calculate_wind_chill(data['AVG_Temp'], data['Ridge_Speed'])

    # Creating a figure with 3 subplots
    fig = plt.figure(figsize=(20, 8))
    gs = fig.add_gridspec(4, hspace=0.0)
    axs = gs.subplots(sharex=True)


    # Plotting Wind Speed
    axs[0].plot(data['Hour'], data['Ridge_Speed'], marker='o', color='blue', label= 'AVG Wind')
    axs[0].plot(data['Hour'], data['Ridge_Gust'], marker='x', color='black', label= 'Gust')
    #axs[0].set_title('Ridge_Speed')
    axs[0].set_ylabel('Ridge Speed (mph)')#, rotation='horizontal', labelpad=20)
    axs[0].set_yticks([0,5,10,15,20,25,30,35,40] )
    axs[0].legend()
    axs[0].grid(True)
    

    # Plotting Temperature and Wind Chill
    axs[1].plot(data['Hour'], data['AVG_Temp'], marker='o', color='red', label='AVG_Temp')
    axs[1].plot(data['Hour'], data['Wind Chill (°C)'], marker='x', color='purple', label='Wind Chill (°F)')
    #axs[1].set_title('Temperature and Wind Chill')
    axs[1].set_ylabel('Degrees (°F)')#, rotation='horizontal', labelpad=20)
    #axs[1].set_yticks([-20,-10,0,10,20,30,40,50])
    axs[1].legend()
    axs[1].grid(True)
    #print(list(ldata['Hour']))
    


    hour = list(data['Hour'])
    avg_temp = list(data['AVG_Temp'])
    wind_chill = list(data['Wind Chill (°C)'])

    for i in range(len(hour)):
        axs[1].text(hour[i], avg_temp[i], f'{avg_temp[i]}°F', fontsize=12, va='bottom', ha='left')
        axs[1].text(hour[i], wind_chill[i], f'{int(wind_chill[i])}°F', fontsize=12, va='top', ha='right')

        #axs[1].text(hour[i], wind_chill[i], f'{wind_chill[i]}°C', fontsize=12, va='top', ha='left')
        ttlsnownum = list(data['ToatalSnow'])[-1]
        label_text = f'New Snow {list(data["NewSnow"])[-1]}"\n ttl Snow {ttlsnownum}"'
        label_color = 'black'
        bbox_props = dict(boxstyle="square,pad=0.3", edgecolor=label_color, facecolor="white")

        # Add the labeled box to the top right corner
        axs[3].text(0.99, 0.93, label_text, transform=axs[2].transAxes,
                    fontsize=12, color=label_color, ha='right', va='top', bbox=bbox_props)

    axs[2].plot(data['Hour'], data['NewSnow'], marker='o', color='green')
    axs[2].fill_between(data['Hour'], data['NewSnow'], color='green', alpha=0.3)
    axs[2].set_xlabel('Hour')
    axs[2].set_ylabel('Inches New Snow' )#, rotation='horizontal', labelpad=20)
    axs[2].set_yticks([0,5,10,15,20,25])
    axs[2].grid(True)
    axs[2].set_xticks(data['Hour'])
    axs[2].set_xticklabels(hrlables)

    axs[3].bar(data['Hour'], data['H2O'], color='red', zorder = 2 )# marker='o',

    label_text = f'Total SWE {sum(list(data["H2O"])):.2f}"'
    label_color = 'black'
    bbox_props = dict(boxstyle="square,pad=0.3", edgecolor=label_color, facecolor="white")

    axs[3].text(0.99, 0.93, label_text, transform=axs[3].transAxes,
                fontsize=12, color=label_color, ha='right', va='top', bbox=bbox_props)

    axs[3].set_ylabel('Inches SWE')

    yticks = [0.0, 0.05, 0.1, 0.15, 0.2]
    axs[3].set_yticks(yticks)

    ytick_labels = ['0.0', '0.05', '0.1', '0.15', '']
    axs[3].set_yticklabels(ytick_labels)

    axs[3].grid(True, zorder=1)

    plt.tight_layout()
    plt.savefig("meterio.jpg", format="jpeg")
    plt.show()

plot_data_from_csv()

print("Genarate Multigraph")
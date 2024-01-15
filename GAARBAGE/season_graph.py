import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import io



import pandas as pd

# Define the file path or URL to the CSV file
file_path = "/Users/maximusnye/YCSP data sheeet/GAARBAGE/History_weather.csv"
df = pd.read_csv(file_path)

print(df.head())  # This will print the first five rows of your DataFrame

























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
    data = pd.read_csv(file_path)
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

    # Plotting Precipitation with fill
    axs[2].plot(data['Hour'], data['NewSnow'], marker='o', color='green')
    axs[2].fill_between(data['Hour'], data['NewSnow'], color='green', alpha=0.3)
    #axs[2].set_title('NewSnow')
    axs[2].set_xlabel('Hour')
    axs[2].set_ylabel('Inches New Snow' )#, rotation='horizontal', labelpad=20)
    #axs[2].set_yticks([0,2,4,6,8,10,12,14,16,18,20,22,24])
    axs[2].set_yticks([0,5,10,15,20,25])
    axs[2].grid(True)

    # Setting x-axis labels for every hour
    axs[2].set_xticks(data['Hour'])
    axs[2].set_xticklabels(hrlables)

    axs[3].bar(data['Hour'], data['H2O'], color='red', zorder = 2 )# marker='o',

    label_text = f'Total SWE {sum(list(data["H2O"])):.2f}"'
    #label_text = f'Total SWE {sum(list(data["H2O"]))}"'
    label_color = 'black'
    bbox_props = dict(boxstyle="square,pad=0.3", edgecolor=label_color, facecolor="white")

    # Add the labeled box to the top right corner
    axs[3].text(0.99, 0.93, label_text, transform=axs[3].transAxes,
                fontsize=12, color=label_color, ha='right', va='top', bbox=bbox_props)


    #axs[3].set_title('Snow Water Equiv.')
    axs[3].set_ylabel('Inches SWE')#, rotation='horizontal', labelpad=20)

    # Add additional notes or text on the side of the graph
    #fig.text(0.01, 0.52, 'Your notes here', ha='left', va='center', rotation='horizontal')

  #  axs[3].set_yticks([0.0,0.025,0.05,0.075,0.1,0.125,0.15] )
    yticks = [0.0, 0.05, 0.1, 0.15, 0.2]
    axs[3].set_yticks(yticks)

    # Set custom y-tick labels with the top label left blank
    ytick_labels = ['0.0', '0.05', '0.1', '0.15', '']
    axs[3].set_yticklabels(ytick_labels)

    axs[3].grid(True, zorder=1)


    # for ax in axs:
    #     # Get the bounding box in figure coordinates
    #     bbox = ax.get_tightbbox(fig.canvas.get_renderer())
    #     x0, y0, width, height = bbox.transformed(fig.transFigure.inverted()).bounds
    #     # slightly increase the very tight bounds:
    #     xpad = 0.05 * width
    #     ypad = 0.05 * height
    #     # Add the rectangle
    #     fig.add_artist(plt.Rectangle((x0-xpad, y0-ypad), width+3.32*xpad, height+6*ypad, edgecolor='red', linewidth=2, fill=False))


    # Adjust layout
    plt.tight_layout()
    plt.savefig("meterio.jpg", format="jpeg")
    #plt.show()

plot_data_from_csv()

print("Genarate Multigraph")
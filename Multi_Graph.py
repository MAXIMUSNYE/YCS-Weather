import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import io

#plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.4, hspace=0.4)
# TODO create new snow height plus swe
#       legends horisontal in a box on side
#       fix colors
#       add 24 hour high low avrade and daily toatals
#       ** fix hour raph and color code for night
#       fix wind chill math
#       

def calculate_wind_chill(temperature, wind_speed):

    return 13.12 + 0.6215 * temperature - 11.37 * (wind_speed ** 0.16) + 0.3965 * temperature * (wind_speed ** 0.16)

def plot_data_from_csv():
    # Reading the data from the CSV content
    data = pd.read_csv("weather_data.csv")
    data['Hour'] = range(len(data))                                   ######___-----##_

    data['Wind Chill (°C)'] = calculate_wind_chill(data['AVG_Temp'], data['Ridge_Speed'])

    # Creating a figure with 3 subplots
    fig = plt.figure(figsize=(20, 8))
    gs = fig.add_gridspec(4, hspace=0)
    axs = gs.subplots(sharex=True)

    # Plotting Wind Speed
    axs[0].plot(data['Hour'], data['Ridge_Speed'], marker='o', color='blue', label= 'AVG Wind')
    axs[0].plot(data['Hour'], data['Ridge_Gust'], marker='x', color='black', label= 'Gust')
    #axs[0].set_title('Ridge_Speed')
    axs[0].set_ylabel('Speed (km/h)')
    axs[0].set_yticks([0,5,10,15,20,25,30,35,40] )
    axs[0].legend()
    axs[0].grid(True)

    # Plotting Temperature and Wind Chill
    axs[1].plot(data['Hour'], data['AVG_Temp'], marker='o', color='red', label='AVG_Temp')
    axs[1].plot(data['Hour'], data['Wind Chill (°C)'], marker='x', color='purple', label='Wind Chill (°C)')
    #axs[1].set_title('Temperature and Wind Chill')
    axs[1].set_ylabel('Degrees (°F)')
    #axs[1].set_yticks([-20,-10,0,10,20,30,40,50])
    axs[1].legend()
    axs[1].grid(True)
    #print(list(ldata['Hour']))
    


    hour = list(data['Hour'])
    avg_temp = list(data['AVG_Temp'])
    wind_chill = list(data['Wind Chill (°C)'])

    for i in range(len(hour)):
        axs[1].text(hour[i], avg_temp[i], f'{avg_temp[i]}°F', fontsize=12, va='bottom', ha='left')
        #axs[1].text(hour[i], wind_chill[i], f'{wind_chill[i]}°C', fontsize=12, va='top', ha='left')



    # Plotting Precipitation with fill
    axs[2].plot(data['Hour'], data['NewSnow'], marker='o', color='green')
    axs[2].fill_between(data['Hour'], data['NewSnow'], color='green', alpha=0.3)
    #axs[2].set_title('NewSnow')
    axs[2].set_xlabel('Hour')
    axs[2].set_ylabel('NewSnow')
    #axs[2].set_yticks([0,2,4,6,8,10,12,14,16,18,20,22,24])
    axs[2].set_yticks([0,5,10,15,20,25])
    axs[2].grid(True)

    # Setting x-axis labels for every hour
    axs[2].set_xticks(data['Hour'])


    axs[3].bar(data['Hour'], data['H2O'], color='red', zorder = 2 )# marker='o',
    #axs[3].set_title('Snow Water Equiv.')
    axs[3].set_ylabel('Inches')
#    axs[3].set_yticks([0,5,10,15,20,25,30,35,40] )
    axs[3].grid(True, zorder=1)


    # Adjust layout
    plt.tight_layout()
    plt.savefig("meterio.jpg", format="jpeg")
    #plt.show()

plot_data_from_csv()

import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
import matplotlib as mpl

mpl.rcParams['font.size'] = 18  # Adjust the font size as needed
mpl.rcParams['font.family'] = 'Helvetica'  # Use the Helvetica font family


def read_wind_data(filename):
    directions = []
    speeds = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            directions.append(float(row['Ridge_dir']))
            speed = float(row['Ridge_Speed'])
            # Cap wind speeds at 40
            if speed > 40:
                speed = 40
            speeds.append(speed)
    return np.array(directions), np.array(speeds)

def create_wind_rose(directions, speeds):
    # Subtract 180 degrees from the directions
    directions = np.radians(directions - 180)

    # Create a polar plot
    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, polar=True)

    # Define your wind speed categories and thresholds here
    thresholds = [0, 16.5, 25.5, 38.5, 42]
    speed_categories = np.digitize(speeds, thresholds)

    # Define custom categorical colors for each category
    color_mapping = {
        1: 'yellow',    # Category 1: Yellow
        2: 'orange',    # Category 2: Orange
        3: 'red',       # Category 3: Red
        4: 'black'      # Category 4: Black
    }

    # Assign a default color for values exceeding the maximum threshold
    default_color = 'gray'
    colors = [color_mapping.get(category, default_color) for category in speed_categories]

    sizes = speeds * 15  # Scale dot sizes

    # Scatter plot
    sc = ax.scatter(directions, speeds, c=colors, s=sizes, alpha=0.8, edgecolors='black',zorder=3)


    # bar_width = np.pi / 50  # Adjust the width of each bar
    # for i in range(len(directions)):
    #     ax.bar(directions[i], speeds[i], width=bar_width, color=colors[i], edgecolor='grey', alpha=0.8)

    #start_angle = 2  # Arrow starts from the center
    #start_speed = 10  # Arrow starts from the center
    #dx = np.cos(start_angle) * 5  # Smaller x component of direction vector
    #dy = np.sin(start_angle) * 5  # Smaller y component of direction vector

#    ax.quiver((list(directions)[-1]),20, color='lightgray', scale=0.5, scale_units='xy', width=0.015)
    ax.quiver(10,10, color='lightgray', scale=0.5, scale_units='xy', width=0.015)


    # for i in range(len(directions)):
    #     sc.quiver(directions,20, color='lightgray', scale=0.5, scale_units='xy', width=0.015)


    #print(directions)

    radial_values = [0, 10, 20, 30, 40]
    ax.set_yticks(radial_values)  

    # Set the label for each 45 degrees
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)  # Clockwise
    ax.set_thetagrids(np.degrees(np.arange(0, 2*np.pi, np.pi/4)), labels=['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])

    # Set fixed limits for the radial axis (wind speed)
    ax.set_ylim(0, 45)  # Set the limit of wind speed to 40

    # Set the title
    ax.set_title("", va='bottom')#"Wind Rose", va='bottom')

    # Create a legend for wind speed categories
    legend_labels = {
        1: 'LGT',
        2: 'MOD',
        3: 'STR',
        4: 'EXT'
    }

    legend_elements = [Line2D([0], [0], marker='o', color='w', label=legend_labels[i], markersize=10, markerfacecolor=color_mapping.get(i, default_color),markeredgecolor='black') for i in range(1, 5)]

    ax.legend(handles=legend_elements, loc='lower left', title='', bbox_to_anchor=(-0.2, -0.13), fancybox=False, shadow=False, frameon=False, ncol=4, columnspacing=0.1) #SWAG Wind Class


    # Save the plot as a JPEG image
    plt.savefig('wind_rose.jpeg', dpi=300)  # You can adjust the DPI (dots per inch) for image quality

    #plt.show()

# Replace 'your_data.csv' with the path to your CSV file
filename = 'weather_data.csv'
directions, speeds = read_wind_data(filename)
create_wind_rose(directions, speeds)
print("Genarate Wind Rose")


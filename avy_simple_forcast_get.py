

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os

# File to store the last checked date and avalanche rating
file_path = 'avalanche_rating.txt'

def avalanche_safety_color(rating):
    ratings = {
        "low": "green",
        "moderate": "yellow",
        "considerable": "orange",
        "high": "red",
        "very high": "black"
    }
    return ratings.get(rating.lower(), "unknown")

def get_avalanche_rating(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        div_element = soup.find('div', class_='hazard-rating-container')
        if div_element:
            line = str(div_element).split(".png")[0].split('/images/hazard_ratings/')[1]
            return line.lower()
        else:
            print('Div element not found.')
    else:
        print('Failed to fetch the web page.')
    return None

def check_and_update_rating(url, file_path):
    # Check if the file exists and is not outdated
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            last_checked_date = datetime.fromisoformat(lines[1].strip())
            if datetime.now() - last_checked_date < timedelta(days=1):
                return lines[0].strip(), last_checked_date
    
    # If file doesn't exist or data is outdated, fetch new data
    rating = get_avalanche_rating(url)
    if rating:
        with open(file_path, 'w') as file:
            file.write(f'{rating}\n')
            file.write(f'{datetime.now().isoformat()}')
        return rating, datetime.now()
    else:
        return None, None

# URL to check
url = 'https://www.mtavalanche.com/forecast/northern-gallatin'

# Check and update the rating
rating, last_checked_date = check_and_update_rating(url, file_path)
if rating:
    color = avalanche_safety_color(rating)
    print(f"Avalanche rating: {rating}, Color: {color}, Last checked: {last_checked_date}")
else:
    print("Failed to get the avalanche rating.")

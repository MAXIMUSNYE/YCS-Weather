# Created on 2023-11-25 21:34:38
#https://forecast.weather.gov/zipcity.php
#https://open-meteo.com/en/docs#latitude=44.0582,NaN&longitude=-121.3153,NaN&hourly=&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch
#https://forecast.weather.gov/zipcity.php?inputstring=BigSky&montana
#def noaa_forcast(location):

bend = "https://forecast.weather.gov/MapClick.php?lat=44.06&lon=-121.3&unit=0&lg=english&FcstType=text&TextType=1"
bozeman = "https://forecast.weather.gov/MapClick.php?lat=45.6835&lon=-111.0505&unit=0&lg=english&FcstType=text&TextType=1"
yc = 'https://forecast.weather.gov/MapClick.php?lat=45.2258&lon=-111.3949&unit=0&lg=english&FcstType=text&TextType=1'

import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage you want to scrape



url = yc

def gettext():
    text2 = ""
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find the HTML elements containing the text you want to scrape
        # For example, to scrape all text within <p> tags:
        paragraphs = soup.find_all("td")
        
        # Iterate through the paragraphs and extract the text
        for paragraph in paragraphs:
            text = paragraph.get_text()
            text2 += text
            #return text

    else:
        #print("Failed to retrieve the webpage. Status code:", response.status_code)
        return
    return text2
#print(gettext())

text = """NWS Forecast for: 4 Miles SW Big Sky MTIssued by: National Weather Service Great Falls, MTLast Update: 3:36 am MST Jan 5, 2024Today: Snow likely, mainly before 11am. The snow could be heavy at times.  Patchy fog before 7am.  Otherwise, mostly cloudy, with a high near 21. Southwest wind 9 to 18 mph becoming west northwest in the afternoon. Winds could gust as high as 28 mph.  Chance of precipitation is 70%. Total daytime snow accumulation of 1 to 3 inches possible. 

Tonight: A 10 percent chance of snow after 5am.  Partly cloudy, with a low around 5. Wind chill values as low as -10. Southwest wind 8 to 14 mph, with gusts as high as 20 mph. 

Saturday: A 40 percent chance of snow, mainly after 11am.  Mostly cloudy, with a high near 19. Wind chill values as low as -5. South southwest wind 9 to 14 mph increasing to 16 to 21 mph in the afternoon. Winds could gust as high as 31 mph.  New snow accumulation of less than a half inch possible. 

Saturday Night: Snow.  Low around 9. Wind chill values as low as -5. South southwest wind 13 to 18 mph becoming light  after midnight. Winds could gust as high as 26 mph.  Chance of precipitation is 80%. New snow accumulation of 1 to 2 inches possible. 

Sunday: Snow likely.  Mostly cloudy, with a high near 15. Light and variable wind becoming north northwest 5 to 10 mph in the morning.  Chance of precipitation is 70%. New snow accumulation of less than one inch possible. 

Sunday Night: A 20 percent chance of snow before 11pm.  Mostly cloudy, with a low around -3. North northwest wind 5 to 10 mph becoming light west  after midnight. 

Monday: Mostly sunny, with a high near 14. Light west southwest wind becoming southwest 8 to 13 mph in the morning. Winds could gust as high as 20 mph. 

Monday Night: Snow likely, mainly after 11pm.  Mostly cloudy, with a low around 4. South wind 13 to 16 mph, with gusts as high as 24 mph. 

Tuesday: Snow likely, mainly after 11am.  Mostly cloudy, with a high near 19.

Tuesday Night: Snow.  Mostly cloudy, with a low around 7.

Wednesday: Snow likely.  Mostly cloudy, with a high near 16.

Wednesday Night: Snow likely.  Mostly cloudy, with a low around 0.

Thursday: Snow likely.  Mostly cloudy, with a high near 11."""

#text = gettext()


splitrpt = text.splitlines()
print(splitrpt[0].split(":")[4].split(" ")[-1][4:])

print(splitrpt[0].split(":")[5])

print("\n\n", splitrpt[2])



day1 = splitrpt[0].split(":")[4].split(" ")[-1][4:]
cast1 = splitrpt[0].split(":")[5]
day2 = splitrpt[2].split(":")[0]
cast2 = splitrpt[2].split(":")[1]

vars = [day1,cast1,day2,cast2]

for i in vars:
    print("\n",i)

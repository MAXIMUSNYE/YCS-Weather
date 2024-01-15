import requests
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
div_element = ""
line = 0
# Define the URL of the web page containing the image
url = 'https://www.mtavalanche.com/forecast/northern-gallatin'

def avalanche_safety_color(rating):
    """
    Return the color corresponding to the avalanche safety rating.

    :param rating: A string representing the avalanche safety rating.
    :return: A string representing the corresponding color.
    """
    ratings = {
        "low": "green",
        "moderate": "yellow",
        "considerable": "orange",
        "high": "red",
        "very high": "black"
    }
    
    return ratings.get(rating.lower(), "unknown")

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the div element with the class "hazard-rating-container"
    div_element = soup.find('div', class_='hazard-rating-container')

    if div_element:
        # Print the extracted div element
        print(div_element)
        # # The HTML string
        # html_string = div_element

        # # Parse the HTML string
        # soup = BeautifulSoup(html_string, 'html.parser')

        # # Find the <img> tag within the <div> element
        # img_tag = soup.find('div', class_='hazard-rating-container').find('img')

        # # Extract the "title" attribute from the <img> tag
        # considerable_text = img_tag.get('title', '')

        # # Print the extracted text (in this case, "Considerable")
        # print(considerable_text)

    else:
        print('Div element not found.')
    print('getting avy danger')
    split2 = '/images/hazard_ratings/'
    line = str(div_element).split(".png")
    line = line[0].split(split2)[1]
    print(f'avy danger: {line}')
else:
    print('Failed to fetch the web page.')


def avalanche_safety_color(rating):
    """
    Return the color corresponding to the avalanche safety rating.

    :param rating: A string representing the avalanche safety rating.
    :return: A string representing the corresponding color.
    """
    ratings = {
        "low": "green",
        "moderate": "yellow",
        "considerable": "orange",
        "high": "red",
        "very high": "black"
    }
    
    return ratings.get(rating.lower(), "unknown")



# Example usage
rating = line.lower()
color = avalanche_safety_color(rating)




import csv

from NOAA_forcast import shortcast_get

#
#TODO make merged cells across rows for day like saterday , sundat then with the hours oin each row, then merged on headders 
#for like Ridge Wind - speed , dir, gust
#
#


def update_html_with_csv_data(csv_file_path, html_template_path, output_html_path):
    """
    Reads data from a CSV file and updates an HTML template with this data.
    Writes the updated HTML to a specified output file.

    :param csv_file_path: Path to the CSV file containing the data.
    :param html_template_path: Path to the HTML template file.
    :param output_html_path: Path where the updated HTML file will be saved.
    """
    # Read CSV data
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        csv_data = list(reader)[1:]

    # Read HTML template from file
    with open(html_template_path, 'r', encoding='utf-8') as template_file:
        html_template = template_file.read()

    # Generate HTML table rows from CSV data
    table_rows = ''
    for row in csv_data:
        table_rows += '<tr>\n'
        for cell in row:
            table_rows += f'<td>{cell}</td>\n'
        table_rows += '</tr>\n'

    # Replace placeholder in the HTML template with the table rows
    updated_html = html_template.replace("<!-- CSV_TABLE_DATA -->", table_rows)

    # Write the updated HTML to the output file
    with open(output_html_path, 'w', encoding='utf-8') as file:
        file.write(updated_html)

# Paths to your files
csv_file_path      = 'Fancy_CSV.csv'
html_template_path = 'HTML_Template.html'  # Replace with the path to your HTML template file
output_html_path   = 'modified_HTML_file.html'

update_html_with_csv_data(csv_file_path, html_template_path, output_html_path)

# Define the path to your HTML file
html_file_path = output_html_path

# Read the HTML file
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Define a function to perform text replacements and save the modified content
def replace_and_save_html(content, data):
    count = 1
    for row in data:
        content = content.replace(f"mini_fourcast_day{count}", row[0])
        content = content.replace(f"mini_fourcast_words{count}", row[1])
        content = content.replace(f"HI_LO_{count}", row[2])
        count += 1
    return content

# Get data from shortcast_get() function
# shortcast_data = [["ChristmasDay", "Rain", "High: 48 °F"],
# ["Tonight", "Rain", "Low: 47 °F"],
# ["Tuesday", "Rain", "High: 51 °F"],
# ["Tuesday Night", "Rain", "Low: 44 °F"],
# ["Wednesday", "Rain Likely", "High: 51 °F"],
# ["Wednesday Night", "Rain", "Low: 45 °F"],
# ["Thursday", "Rain", "High: 53 °F"],
# ["Thursday Night", "Chance Rain", "Low: 44 °F"],
# ["Friday", "Slight ChanceRain", "High: 53 °F"]]
shortcast_data =  shortcast_get()

# Replace placeholders and save the modified HTML content
modified_html_content = replace_and_save_html(html_content, shortcast_data)

# Write the modified HTML content back to the file
with open(html_file_path, 'w', encoding='utf-8') as file:
    file.write(modified_html_content)

print("Text replaced and HTML file saved successfully.")
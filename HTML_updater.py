import csv

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
        csv_data = list(reader)

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
csv_file_path = 'weather_data.csv'
html_template_path = 'HTML_Template.html'  # Replace with the path to your HTML template file
output_html_path = 'modified_HTML_file.html'

update_html_with_csv_data(csv_file_path, html_template_path, output_html_path)

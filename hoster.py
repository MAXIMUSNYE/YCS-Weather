import os
import sys
import threading
import time
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler
import shutil

def copy_file(source_file, destination_file):
    try:
        shutil.copy(source_file, destination_file)
        print(f"File '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"File '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def run_server(port):
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()

def run_assembly_main():
    python_executable = sys.executable
    python_file = 'assemblymain.py'
    subprocess.run([python_executable, python_file])

# Define the server and start it on a separate thread
port = 8000
server_thread = threading.Thread(target=run_server, args=(port,))
server_thread.daemon = True
server_thread.start()
print(f"Server started on port {port}...")

# Main loop
try:
    while True:
        source_file = "modified_HTML_file.html"
        destination_file = "index.html"
        refresh_interval = 21600  # Interval to refresh HTML file in seconds

        # Run assemblymain.py to refresh the HTML file
        run_assembly_main()

        # Wait a bit to ensure assemblymain.py has finished executing
        time.sleep(15)

        # Copy the refreshed HTML file
        copy_file(source_file, destination_file)

        # Wait for the specified refresh interval before refreshing again
        time.sleep(refresh_interval)

except KeyboardInterrupt:
    print("Shutting down server...")
    sys.exit(0)

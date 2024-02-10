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

def start_server(port):
    server_thread = threading.Thread(target=run_server, args=(port,))
    server_thread.daemon = True
    server_thread.start()

def run_assembly_main():
    python_executable = sys.executable
    python_file = 'assemblymain.py'
    subprocess.run([python_executable, python_file])

# Main loop
while True:
    source_file = "modified_HTML_file.html"
    destination_file = "index.html"
    port = 8000
    duration = 1500  # Duration in seconds

    # Run assemblymain.py to refresh the HTML file
    run_assembly_main()
    time.sleep(15)
    # Copy the refreshed HTML file
    copy_file(source_file, destination_file)
    # Start the server
    start_server(port)
    # Wait for the specified duration
    time.sleep(duration)

    print("Restarting server...")

import os
import sys
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
import shutil
import threading
import assemblymain

def copy_file(source_file, destination_file):
    try:
        shutil.copy(source_file, destination_file)
        print(f"File '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"File '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def start_local_server(port=8000):
    # Change to the directory where your HTML file is located
    web_dir = os.path.dirname(__file__)
    os.chdir(web_dir)

    # Start the HTTP server
    server_address = ("", port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

    # Print the URL to access the server
    url = f"http://localhost:{port}"
    print(f"Local server is running at: {url}")

    # Open the web browser to the server URL
    webbrowser.open(url)

    try:
        # Serve the files indefinitely until interrupted or for one minute
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Terminate the server when Ctrl+C is pressed
        pass

def stop_server_after_timeout(server, timeout):
    import time
    time.sleep(timeout)
    server.shutdown()
    print("Server stopped after one minute.")

if __name__ == "__main__":
    # Set the port number and duration (in seconds)
    port = 8000
    duration = 60  # One minute (60 seconds)

    # Copy the HTML file
    source_file = "modified_HTML_file.html"  # Replace with the source file path
    destination_file = "index.html"  # Replace with the destination file path
    copy_file(source_file, destination_file)

    # Start the local server in a separate thread
    server_thread = threading.Thread(target=start_local_server, args=(port,))
    server_thread.daemon = True  # Terminate the thread when the main program exits
    server_thread.start()

    # Start a timer to stop the server after the specified duration
    timer_thread = threading.Thread(target=stop_server_after_timeout, args=(HTTPServer, duration))
    timer_thread.start()

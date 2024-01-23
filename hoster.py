import os
import sys
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
import shutil
import threading
import requests
import sys
import io
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#import assemblymain
for i in range(0,9999999999999999999):
    import subprocess

    # Replace 'python_script.py' with the name of your Python file
    python_file = 'assemblymain.py'

    # Run the Python file using the terminal
    try:
        python_executable = sys.executable

# Run the Python script using the same interpreter
        subprocess.run([python_executable, python_file])
    except subprocess.CalledProcessError as e:
        print(f"Error running {python_file}: {e}")

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

        try:
            # Serve the files indefinitely until interrupted or for one minute
            httpd.serve_forever()
        except KeyboardInterrupt:
            # Terminate the server when Ctrl+C is pressed
            pass

    def stop_server_after_timeout(server, timeout):
        import time
        time.sleep(timeout)

        print("Server stopped after one minute.")


    # Set the port number and duration (in seconds)
    port = 8000
    duration = 300  # One minute (60 seconds)

    # Copy the HTML file
    source_file = "modified_HTML_file.html"  # Replace with the source file path
    destination_file = "index.html"  # Replace with the destination file path
    copy_file(source_file, destination_file)

    # Start the local server in a separate thread
    server_thread = threading.Thread(target=start_local_server, args=(port,))
    server_thread.daemon = True  # Terminate the thread when the main program exits
    server_thread.start()
    import time
    time.sleep(30)
    try:
        HTTPServer.server_close()

    except: TypeError


    # Start a timer to stop the server after the specified duration
    #timer_thread = threading.Thread(target=stop_server_after_timeout, args=(HTTPServer, duration))
    #timer_thread.start()

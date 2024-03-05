import http.server
import socketserver

# Set the directory where your index.html file is located
directory = '.'  

# Set the port number
port = 8000

# Define the handler to serve the index.html file
Handler = http.server.SimpleHTTPRequestHandler

# Create the server object
with socketserver.TCPServer(("", port), Handler) as httpd:
    print(f"Server started at http://localhost:{port}")
    # Start the server and keep it running until manually stopped
    httpd.serve_forever()

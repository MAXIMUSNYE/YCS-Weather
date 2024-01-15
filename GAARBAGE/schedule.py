import subprocess
import logging

# The command you want to run (replace with your own)
command = "pip freeze > requirements.txt"

# Run the command
try:
    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # The above line runs the command, captures its output, and checks for errors.
    
    # Print the standard output of the command
    print("requirements.txt updated")
    logging.debug("requirements.txt updated")
    
except subprocess.CalledProcessError as e:
    # Handle any errors that occur when running the command
    print(f"requirements.txt UPDATE ERROR")

# import subprocess
# import logging

# # The command you want to run (replace with your own)
# command = "pip freeze > requirements.txt"

# # Run the command
# try:
#     result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#     # The above line runs the command, captures its output, and checks for errors.
    
#     # Print the standard output of the command
#     print("requirements.txt updated")
#     logging.debug("requirements.txt updated")
    
# except subprocess.CalledProcessError as e:
#     # Handle any errors that occur when running the command
#     print(f"requirements.txt UPDATE ERROR")


"""your_project/
│
├── your_package/                   # Main package directory
│   ├── __init__.py                 # Initializes your package
│   └── module.py                   # Python code modules (can be multiple)
│
├── tests/                          # Unit tests for your package
│   ├── __init__.py                 # Initialization for tests
│   └── test_module.py              # Test files (can be multiple)
│
├── docs/                           # Documentation files
│   ├── README.md                   # Project overview and instructions
│   ├── CONTRIBUTING.md             # Contribution guidelines
│   └── LICENSE                     # Licensing information
│
├── .env                            # Environment variables
├── .gitignore                      # Specifies files to ignore in version control
├── .travis.yml                     # CI/CD configuration for Travis CI
├── config.yml                      # Additional CI/CD configurations (if needed)
├── Dockerfile                      # Docker configuration file
├── Makefile                        # Automates common tasks
├── MANIFEST.in                     # Includes additional files in your package
├── pyproject.toml                  # Build system configuration (Poetry, Flit)
├── requirements.txt                # Lists package dependencies
├── security.md                     # Security policies and procedures (if applicable)
├── setup.cfg                       # Configuration for setup.py, linters, etc.
└── setup.py                        # Package setup and distribution configuration

# Additional directories and files (if applicable)
├── config/                         # External configuration files
│   ├── config.yaml
│   └── ...
├── data/                           # Data files or datasets
│   ├── datafile.csv
│   └── ...
├── examples/                       # Examples or tutorials
│   ├── example1.py
│   └── ...
└── CHANGELOG.md                    # Documenting changes and updates
"""

pers  = 0
import pandas as pd

data = pd.read_csv("GAARBAGE/2weekstart.csv")
print(list(data['Thursday']).count("Andy"))

column_name = 'Thursday' 
andy_count = list(data[column_name]).count("Andy")
print(f"Count of 'Andy' in {column_name}: {andy_count}")


for column in data.columns:
    count = data[column].apply(lambda x: x.count("EHQ") if isinstance(x, str) else 0).sum()
    print(f"Column '{column}': Count of 'EHQ' = {count}")

first_column = data.iloc[:, 0].tolist()

data = data.applymap(lambda x: x if x in ["OFF",'Andy','Dispatch', 'EHQ'] else "MAIN")



data.insert(0, "New_Column", first_column)


data.to_csv("GAARBAGE/modified_2weekstart.csv", index=False)




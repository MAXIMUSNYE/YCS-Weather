#from pepoleinit2 import dframe
import pandas

import pandas as pd
import pandas as pd

# Load the spreadsheet data


# Load the spreadsheet data
file_path = 'GAARBAGE/2wwker.csv'
data = pd.read_csv(file_path)

# Melt the dataframe to make it easier to count
melted_data = data.melt(id_vars=["Name"], var_name="Day", value_name="Location")

# Count occurrences
location_counts = melted_data.groupby(["Name", "Location"]).size().unstack(fill_value=0)

# Print out the result
print(location_counts)

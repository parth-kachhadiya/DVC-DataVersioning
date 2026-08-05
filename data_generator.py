import pandas as pd
import os

data = {
    'name' : ['Alice', 'Bob', 'Charlie'],
    'age' : [29, 32, 51],
    'city' : ['LA', 'Chicago', 'San Fransisco']
}

DIR_LOCATION = "csv_storage"

df = pd.DataFrame(data)

os.makedirs(DIR_LOCATION, exist_ok=True)

file_path = os.path.join(DIR_LOCATION, "sample_data.csv")

df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")
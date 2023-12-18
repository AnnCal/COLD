from whatsapp_api_client_python import API
import pandas as pd
import os
from pathlib import Path

directory_path = Path('path/to/directory')

# List all files in the directory
dat_files = list(directory_path.glob('*.dat'))
#files = os.listdir(directory_path)
#print(files)

# Print the list of files
for file in dat_files:
     if file.is_file():
        with open(file, 'r') as file:
            #data = file.read()
            data = pd.read_csv(file, delimiter='\t')
            pressure = data['P5']
            for i in pressure:
                if i > 800:
                    greenAPI = API.GreenAPI("IDinstance", "ApiTokenInstance")
                    response = greenAPI.sending.sendMessage("wid@c.us", "!! warning message ")
                    print(response.data)
            else:
                pass

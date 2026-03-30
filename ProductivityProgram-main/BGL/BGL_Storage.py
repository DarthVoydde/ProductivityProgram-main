import os
import json

# Gets the folder where this script is stored
folder_path = os.path.dirname(os.path.abspath(__file__))

# Stores the path for the glucose_log
json_path = os.path.join(folder_path, "glucose_log.json")

# If the glucose_log file doesn't exist
if not os.path.exists(json_path):
    with open(json_path, "w") as f:
        json.dump({}, f)


import json
from datafed.CommandLib import API

# Initialize the DataFed API
df_api = API()

# Define the metadata parameters
parameters = {
    "Title and Description": "Seoul Bike Sharing Demand",
    "Data Type and Format": "Numerical and CSV",
}
# Specify the record ID
record_id = "d/500183866"

# Call the dataUpdate function with the record ID, new title, and metadata
du_resp = df_api.dataUpdate(
    record_id,
    metadata=json.dumps(parameters)  # Use the corrected metadata parameters
)

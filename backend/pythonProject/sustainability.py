import numpy as np
from sentinelhub import SHConfig, SentinelHubRequest, DataCollection, MimeType, CRS, BBox, bbox_to_dimensions
import matplotlib.pyplot as plt

# Configure your Sentinel Hub account
CLIENT_ID = "90b037f9-9396-4d29-9ebc-38bc9f76f747"   # Replace with your Client ID
CLIENT_SECRET = "GUwEX5xKIdEe2NX5qcktX04FMOejeUrX" # Replace with your Client Secret

config = SHConfig()
if CLIENT_ID and CLIENT_SECRET:
    config.sh_client_id = CLIENT_ID
    config.sh_client_secret = CLIENT_SECRET

# Define your area of interest (AOI)
resolution = 10.0  # Sentinel-2 resolution in meters


bbox = BBox([3.367310,47.315620,3.690033,47.403041], crs=CRS.WGS84)  # Replace with your bounding box coordinates
time_interval = ('2020-01-01', '2020-12-31')  # Replace with your desired time interval
size = bbox_to_dimensions(bbox, resolution=resolution)


# Define the Evalscript


# Fetch CNES Land Cover Labels
def fetch_cnes_land_cover_labels(bbox, time_interval, config):
    request = SentinelHubRequest(
        evalscript=CNES_LABEL_EVALSCRIPT,
        input_data=[
            SentinelHubRequest.input_data(
                data_collection=DataCollection.define_byoc("9baa2732-6597-49d2-ae3b-68ba0a5386b2"),
                time_interval=time_interval,
            )
        ],
        responses=[SentinelHubRequest.output_response("default", MimeType.TIFF)],
        bbox=bbox,
        size=size,
        config=config,
    )
    data = request.get_data()
    return data[0]  # Assuming you're interested in the first response


# Fetch the data
land_cover_data = fetch_cnes_land_cover_labels(bbox, time_interval, config)

# Calculate the percentages of occurrence for each label
(unique, counts) = np.unique(land_cover_data, return_counts=True)
percentages = dict(zip(unique, counts * 100 / counts.sum()))

# Define the CNES Label Map (full version, not simplified)


# Print the percentages
for label, percentage in percentages.items():
    label_name = CNES_LABEL_MAP.get(label, "Unknown")
    print(f"{label_name}: {percentage:.2f}%")

import requests
import logging

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def satellite_data(dataset, bbox):
    """
    Fetches satellite images from the Remote Sensing API.

    Parameters:
    - dataset: The name or ID of the satellite dataset to fetch.
    - bbox: The bounding box specifying the area of interest in "minLon,minLat,maxLon,maxLat" format.

    Returns:
    The API response containing satellite images.
    """
    # Example API URL (replace with the actual API endpoint)
    api_url = f"https://api.remote-sensing.cropwise.com/scenes"

    # Assuming the API requires an API key for authentication (replace 'YourApiKeyHere' with the actual API key)
    headers = {"Authorization": "Bearer YourApiKeyHere"}

    # Parameters for the API request
    params = {
        "dataset": dataset,
        "bbox": bbox
    }

    try:
        # Make the request to the Remote Sensing API
        response = requests.get(api_url, headers=headers, params=params)

        # Check for successful response
        if response.status_code == 200:
            return response.json()  # Return the JSON content of the response
        else:
            # Log error details if the response indicates failure
            logging.error(
                f"Failed to fetch satellite data. Status Code: {response.status_code}, Response: {response.text}")
            return {"error": "Failed to fetch satellite data", "status_code": response.status_code}
    except requests.RequestException as e:
        # Log any errors that occur during the request making process
        logging.exception("Error making request to the Remote Sensing API")
        return {"error": "Error making request to the Remote Sensing API", "exception": str(e)}

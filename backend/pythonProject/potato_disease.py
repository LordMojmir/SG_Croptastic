import http.client
import os
import json  # Added import for JSON parsing


def get_potato_disease_risk(longitude, latitude, relative_humidity, start_date, end_date, model_id='EarlyBlight'):
    AUTH_FORECAST_API = "f48f7d2e-97e6-413a-bc95-cd13e425f478"
    forecast_API = AUTH_FORECAST_API

    conn = http.client.HTTPSConnection("services.cehub.syngenta-ais.com")
    headers = {
        'accept': '/',
        'ApiKey': forecast_API
    }

    # Construct the API endpoint with query parameters
    endpoint = f"/api/DiseaseRisk/PotatoRisk?latitude={latitude}&longitude={longitude}&startDate={start_date}&endDate={end_date}&modelId={model_id}&relativeHumidity={relative_humidity}"

    # Send the request
    conn.request("GET", endpoint, '', headers)
    res = conn.getresponse()
    data = res.read()
    all_data = data.decode("utf-8")

    # Return the decoded data
    result_data = json.loads(all_data)
    result_dict = {}

    for entry in result_data:
        date = entry['date']
        risk_value = entry['value']
        result_dict[date] = risk_value

    #    result_data = json.loads(result_dict)

    return result_dict


# Example usage
if __name__ == '__main__':
    # Define your parameters here
    longitude = 7
    latitude = 47
    relative_humidity = 60  # Example humidity level
    start_date = '2024-03-21'
    end_date = '2024-03-24'

    result = get_potato_disease_risk(longitude, latitude, relative_humidity, start_date, end_date)
    print(result)


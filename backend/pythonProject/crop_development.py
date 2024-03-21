import http.client
import json
from dotenv import load_dotenv
import os
import pandas as pd
from datetime import datetime
import matplotlib
matplotlib.use('Agg')  # Use the Anti-Grain Geometry non-interactive backend suited for scripts
import matplotlib.pyplot as plt
import plotly.express as px

def get_crop_prediction(long, lat, depth_val, density_val, row_spacing_val, field_water_capacity_val, crop =  "CORN", crop_variety = {"relative_maturity":"RM114"}):
  load_dotenv()

  # Get the authentication token from the environment
  auth_token = os.getenv('AUTH_TOKEN_BEARER')
  planted_day = "2023-10-28"

  conn = http.client.HTTPSConnection("api.insights.cropwise.com")
  payload = json.dumps({
    "request_version": "v1.0",
    "fields": [
      {
        "models": [
          {
            "name": "DSSAT",
            "version": "v2.0"
          }
        ],
        "location": {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [
              long,
              lat
            ]
          }
        },
        "crop": crop,
        "crop_variety": crop_variety,
        "planting": {
          "date": planted_day +"T00:00:00Z",
          "depth": {
            "value": depth_val,
            "unit": "cm"
          },
          "density": {
            "value": density_val,
            "unit": "plants/m2"
          },
          "row_spacing": {
            "value": row_spacing_val,
            "unit": "cm"
          },
          "field_water_capacity": {
            "value": field_water_capacity_val,
            "unit": "percentage"
          }
        },
        "water_supply": {
          "is_irrigated": False
        },
        "time_period": {
          "historical": {
            "start_date": "2004-11-24T00:00:00Z",
            "end_date": "2022-05-09T00:00:00Z"
          },
          "forecast": {
            "start_date": "2023-11-07T00:00:00Z",
            "end_date": "2023-12-02T00:00:00Z"
          }
        }
      }
    ]
  })
  headers = {
    'Content-Type': 'application/json',
    'Authorization': auth_token
  }
  conn.request("POST", "/v2.0/predictions", payload, headers)
  res = conn.getresponse()
  data = res.read()
  # print(data.decode("utf-8"))
  data = json.loads(data.decode("utf-8"))

  growth_stage_dates = {"V0": planted_day+"T00:00:00Z"}

  # Assuming 'data' contains your JSON data
  for result in data['results']:
      for prediction in result['predictions']:
          for feature in prediction['features']:
              if feature['type'] == 'growth_stage:start_date':
                  growth_stage_dates[prediction['features'][0]['value']] = feature['value']

  # Now 'growth_stage_dates' contains the extracted dates
  return growth_stage_dates

def create_custom_dataframe(data):
    planting_date = datetime.strptime(data['V0'], '%Y-%m-%dT%H:%M:%SZ')
    custom_data = {}
    for key, value in data.items():
      if key.startswith("V"):
        delta = datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ') - planting_date
        custom_data[key.replace("V", "")] = delta.days

    df = pd.DataFrame(list(custom_data.items()), columns=['x', 'y'])
    return df


def get_and_create_custom_dataframe(long, lat, depth_val, density_val, row_spacing_val, field_water_capacity_val,
                                    crop="CORN", crop_variety={"relative_maturity": "RM114"}):
  result = get_crop_prediction(long, lat, depth_val, density_val, row_spacing_val, field_water_capacity_val, crop,
                               crop_variety)
  custom_df = create_custom_dataframe(result)
  return custom_df.values.tolist()

def scatter_crop_development(data):
  x = [int(point[0]) for point in data]
  y = [point[1] for point in data]

  # Plotting the data with axes flipped
  plt.figure(figsize=(10, 5))
  plt.scatter(y, x)  # Note the change here for the flipped axes
  plt.plot(y, x, linestyle='-', marker='o')  # Connect the points with a line with axes flipped
  plt.title('Scatter Plot of Crop Development')
  plt.xlabel('Days from Planting Date')
  plt.ylabel('Stage')
  plt.grid(True)
  # plt.show()
  plt.savefig('scatter_plot.png')


if __name__ == '__main__':
  custom_df = get_and_create_custom_dataframe(-58.737, -29.025, 7, 5, 76, 90, "MAIZE", {"name": "SYN897"})
  # print(custom_df.to_string(index=False, header=False))

  # array_without_header = custom_df.values.tolist()
  # print(array_without_header)
  # scatter_crop_development(custom_df)
  # # return growth_stage_dates
  # result = get_crop_prediction(-58.737, -29.025, 7, 5, 76, 90, "MAIZE", {"name":"SYN897"})
  # print(result)
  # custom_df = create_custom_dataframe(result)
  # print(custom_df)
import json

from flask import Flask, request, jsonify
from sentinelhub import BBox, CRS

from crop_development import get_and_create_custom_dataframe
from satellite_images import satellite_data
from sustainability import get_biodiversity

app = Flask(__name__)


@app.route('/fetch_satellite_images', methods=['GET'])
def fetch_satellite_images():
    """
    Flask route that handles requests to fetch satellite images.
    """
    # Extract 'dataset' and 'bbox' from the query parameters
    dataset = request.args.get('dataset')
    bbox = request.args.get('bbox')

    # Input validation (simplified for demonstration)
    if not dataset or not bbox:
        return jsonify({"error": "Missing 'dataset' or 'bbox' query parameter"}), 400

    # Call the satellite_data function
    data = satellite_data(dataset, bbox)

    # Return the fetched data
    return jsonify(data)


@app.route('/get_land_cover_percentages', methods=['GET'])
def get_land_cover_percentages():
    """
    Flask route that takes a 'bbox' parameter and returns land cover label percentages.
    """
    # Extract 'bbox' from the query parameters and convert it to a tuple of tuples
    #bbox = request.args.get('bbox')
    bbox = BBox([3.367310, 47.315620, 3.690033, 47.403041], crs=CRS.WGS84)

    # Call the get_land_cover_label_percentages function
    percentages = get_biodiversity(bbox)

    # Return the land cover label percentages
    return jsonify(percentages)


@app.route('/get_crop_development', methods=['GET'])
def get_crop_development():
    """
    Flask route to get crop development data.
    """
    try:
        # Extract parameters from the request query string
        long = float(request.args.get('long'))
        lat = float(request.args.get('lat'))
        depth_val = int(request.args.get('depth_val'))
        density_val = int(request.args.get('density_val'))
        row_spacing_val = int(request.args.get('row_spacing_val'))
        field_water_capacity_val = int(request.args.get('field_water_capacity_val'))
        crop = request.args.get('crop', default="CORN")
        crop_variety = request.args.get('crop_variety', default='{"relative_maturity": "RM114"}')

        print(long, lat, depth_val, density_val, row_spacing_val, field_water_capacity_val)

        # Call the function to get and create custom dataframe
        data = get_and_create_custom_dataframe(long, lat, depth_val, density_val, row_spacing_val, field_water_capacity_val)
        print(data)
        # Return the data as JSON
        return jsonify({"crop_development_data": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

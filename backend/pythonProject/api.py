from flask import Flask, request, jsonify
from sentinelhub import BBox, CRS
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

if __name__ == '__main__':
    app.run(debug=True)

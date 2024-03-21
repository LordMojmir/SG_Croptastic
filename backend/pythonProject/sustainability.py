import numpy as np
from sentinelhub import SHConfig, SentinelHubRequest, DataCollection, MimeType, CRS, BBox, bbox_to_dimensions


def fetch_cnes_land_cover_labels(bbox):
    resolution = 10.0
    time_interval = ('2020-01-01', '2020-12-31')
    CLIENT_ID = "90b037f9-9396-4d29-9ebc-38bc9f76f747"
    CLIENT_SECRET = "GUwEX5xKIdEe2NX5qcktX04FMOejeUrX"
    bbox = BBox([3.367310, 47.315620, 3.690033, 47.403041], crs=CRS.WGS84)
    size = bbox_to_dimensions(bbox, resolution=resolution)
    config = SHConfig()
    if CLIENT_ID and CLIENT_SECRET:
        config.sh_client_id = CLIENT_ID
        config.sh_client_secret = CLIENT_SECRET

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
    return data[0]


def get_biodiversity(bbox: BBox):
    land_cover_data = fetch_cnes_land_cover_labels(bbox)
    (unique, counts) = np.unique(land_cover_data, return_counts=True)
    percentages = {CNES_LABEL_MAP[key]: value for key, value in zip(unique, counts * 100 / counts.sum())}
    return percentages


CNES_LABEL_MAP = {
        1: "Dense built-up area",
        2: "Diffuse built-up area",
        3: "Industrial and commercial areas",
        4: "Roads",
        5: "Oilseeds (Rapeseed)",
        6: "Straw cereals (Wheat, Triticale, Barley)",
        7: "Protein crops (Beans / Peas)",
        8: "Soy",
        9: "Sunflower",
        10: "Corn",
        11: "Rice",
        12: "Tubers/roots",
        13: "Grasslands",
        14: "Orchards and fruit growing",
        15: "Vineyards",
        16: "Hardwood forest",
        17: "Softwood forest",
        18: "Natural grasslands and pastures",
        19: "Woody moorlands",
        20: "Natural mineral surfaces",
        21: "Beaches and dunes",
        22: "Glaciers and eternal snows",
        23: "Water"
    }

CNES_LABEL_EVALSCRIPT = """
    //VERSION=3
    function setup() {
        return {
            input: [{"bands": ["OCS"], "units": "DN"}],
            output: {bands: 1, sampleType: "UINT8"}
        };
    }
    function evaluatePixel(sample) {
        return [sample.OCS];
    }
    """




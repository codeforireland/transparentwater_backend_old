"""
The API functions
"""
import json

import requests


def get_json_from_url(url):
    """
    This function requests JSON data from a URL and returns a python
    representation of that data

    :param url the URL to fetch data from:
    :return: the JSON data as python objects
    """
    req = requests.get(url=url)
    if req.status_code != 200:
        return None

    output_json = req.json()
    return output_json


def fetch_irish_water():
    """
    Fetches data from the Irish water service notices API

    :return: the data with only the relevant fields, represented as python objects
    """
    url = "https://www.water.ie/site-files/cms-templates/utils/proxy/index.xml?" \
          "https://services2.arcgis.com/OqejhVam51LdtxGa/ArcGIS/rest/services/" \
          "WaterAdvisoryCR021/FeatureServer/0/query?returnGeometry=true&where=" \
          "STATUS!%3D%27Closed%27&outFields=*&orderByFields=STARTDATE%20DESC" \
          "&outSR=4326&returnIdsOnly=false&f=pgeojson"
    data = get_json_from_url(url)

    # parse the result
    final_structure = []
    for feature in data["features"]:
        lat = feature["geometry"]["coordinates"][1]
        lng = feature["geometry"]["coordinates"][0]
        properties = feature["properties"]
        struct = properties
        struct["LAT"] = lat
        struct["LONG"] = lng
        # remove unnecessary keys
        del struct["LASTEDITOR"]
        del struct["CREATEDBY"]
        del struct["LASTUPDATE"]
        del struct["CREATEDATE"]
        del struct["PROJECTNUMBER"]
        del struct["PROJECT"]
        del struct["PRIORITY"]
        del struct["APPROVALSTATUS"]
        struct["NOTICETYPE"] = []
        for key in ["BOILWATERNOTICE", "TRAFFICDISRUPTIONS", "POLLUTION",
                    "WATEROUTAGE", "DONOTDRINK"]:
            value = struct[key]
            del struct[key]
            if value is not None:
                struct["NOTICETYPE"].append(key)
        final_structure.append(struct)
        outfile = open("sample-out.json", "w")
        outfile.write(json.dumps(final_structure))
        outfile.close()
    return final_structure

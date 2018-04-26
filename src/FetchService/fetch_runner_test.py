"""
This module provides tests for the FetchRunner class and
fetch functions
"""
import json

import requests_mock

from .apis import fetch_irish_water, get_json_from_url


def test_get_json_from_url():
    data = {
        "firstKey": 1,
        "users": [
            "alice",
            "bob"
        ]
    }
    with requests_mock.mock() as m:  # pylint: disable-msg=invalid-name
        m.register_uri("GET", "http://test.com", text=json.dumps(data),
                       status_code=200)
        text = get_json_from_url("http://test.com")
    assert text == data

    with requests_mock.mock() as m:  # pylint: disable-msg=invalid-name
        m.register_uri("GET", "http://secondtest.com", text=json.dumps(data),
                       status_code=400)
        text = get_json_from_url("http://secondTest.com")
    assert text is None


def test_fetch_irish_water():
    url = "https://www.water.ie/site-files/cms-templates/utils/proxy/index.xml?" \
          "https://services2.arcgis.com/OqejhVam51LdtxGa/ArcGIS/rest/services/" \
          "WaterAdvisoryCR021/FeatureServer/0/query?returnGeometry=true&where=" \
          "STATUS!%3D%27Closed%27&outFields=*&orderByFields=STARTDATE%20DESC" \
          "&outSR=4326&returnIdsOnly=false&f=pgeojson"  # pylint: disable=duplicate-code
    import os
    test_dir = os.path.dirname(os.path.realpath(__file__))
    with open(test_dir + "/sample-in.json", "r") as f:  # pylint: disable-msg=invalid-name
        json_data = f.read()

    with requests_mock.mock() as m:  # pylint: disable-msg=invalid-name
        m.register_uri("GET", url, text=json_data,
                       status_code=200)
        got = fetch_irish_water()

    # just checking formatting. No need to check everything for now
    expected = [{
        "OBJECTID": 1,
        "WORKTYPE": None,
        "TITLE": "Essential Maintenance Works - Dublin",
        "CONTACTDETAILS": None,
        "AFFECTEDPREMISES": None,
        "TRAFFICIMPLICATIONS": None,
        "DESCRIPTION": "Maintenance works",
        "STATUS": "Open",
        "GLOBALID": "d34db33f",
        "STARTDATE": 1527980400000,
        "ENDDATE": 1525388400000,
        "LOCATION": "Dublin",
        "COUNTY": "Dublin",
        "REFERENCENUM": "ABC1234",
        "LONG": -1.23,
        "LAT": 44.44,
        "NOTICETYPE": ["BOILWATERNOTICE", "TRAFFICDISRUPTIONS", "WATEROUTAGE"]
    }]
    assert got == expected

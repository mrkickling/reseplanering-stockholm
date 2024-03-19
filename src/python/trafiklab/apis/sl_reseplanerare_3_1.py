"""
Implementation of SL Reseplanerare 3.1 in Python
https://www.trafiklab.se/api/trafiklab-apis/sl/route-planner-31/
"""

import requests
import os


base_url = "https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/"


def create_url(path, api_key, parameters: dict):
    url = f"{base_url}/{path}?key={api_key}"
    for k, v in iter(parameters):
        url += f"&{k}={v}"
    return url


def trip(api_key, origin, destination, parameters):
    parameters = {}
    parameters['originExtId'] = origin
    parameters['destExtId'] = destination

    return create_url(path='trip.json', api_key=api_key, parameters=parameters)
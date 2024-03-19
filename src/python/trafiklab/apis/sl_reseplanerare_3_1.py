"""
Implementation of SL Reseplanerare 3.1 in Python
https://www.trafiklab.se/api/trafiklab-apis/sl/route-planner-31/
"""

import logging

from trafiklab.apis.common import make_request

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
base_url = "https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1"


def create_url(path, api_key, parameters: dict):
    """Returns the url in correct format, given path api_key and parameters"""
    url = f"{base_url}/{path}?key={api_key}"
    for k, v in parameters.items():
        url += f"&{k}={v}"
    return url


def trip(api_key, origin, destination):
    """Make a query to the 'trip' api of SL Reseplanerare 3.1"""
    logger.info(f"Making trip to {destination}")

    parameters = {}
    parameters['originExtId'] = origin
    parameters['destExtId'] = destination

    url = create_url(path='trip.json', api_key=api_key, parameters=parameters)
    res = make_request(url, 'GET')
    return res.json().get('Trip')[0].get('LegList').get('Leg')[0]

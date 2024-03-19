
from trafiklab.apis.common import make_request

base_url = "https://journeyplanner.integration.sl.se/v1"


def create_url(path, api_key, parameters: dict):
    """Returns the url in correct format, given path api_key and parameters"""
    url = f"{base_url}/{path}?key={api_key}"
    for k, v in parameters.items():
        url += f"&{k}={v}"
    return url


def search(api_key, search_string):
    """Search for the ID of a station / bus stop"""
    params = {
        "searchstring": search_string,
        "limit": 1
    }

    res = make_request(
        create_url('typeahead.json', api_key, params),
        "GET"
    )
    return res.json().get("ResponseData")

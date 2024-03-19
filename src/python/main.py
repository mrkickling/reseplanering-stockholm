"""For testing"""

import logging
import os
from trafiklab.apis import sl_reseplanerare_3_1, sl_platsuppslag

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
api_key = os.getenv("SL_RESEPLANERARE_API_KEY")

site_one = sl_platsuppslag.search(api_key, 'Hökarängen')
site_two = sl_platsuppslag.search(api_key, 'Skanstull')

if not site_one or not site_two:
    print("Error fetching data")

site_id1 = site_one[0]['SiteId']
site_id2 = site_two[0]['SiteId']

trip = sl_reseplanerare_3_1.trip(api_key, site_id1, site_id2)
print(
    trip.get('name'),
    trip.get('Origin').get('name'),
    trip.get('Origin').get('time'),
    "--->",
    trip.get('Destination').get('name'),
    trip.get('Destination').get('time')
)
breakpoint()
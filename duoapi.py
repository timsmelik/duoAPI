#!usr/bin/env python3

import json
import requests

API_URL = 'https://api.duo.nl/v0/datasets/03.-leerlingen-vo-per-vestiging-en-bestuur-%28vavo-apart%29-2015-2016'
API_URL_ALL_DATASETS = 'https://api.duo.nl/v0/search'

class DuoAPI:
    def unpack_response(self, r):
        if (r.status_code != 200):
            return False
        
        return r.json()['results']

    def get_results(self, url, filter_key=False, filter_val=False, filter_exact=False):
        response = requests.get(url)
        unpacked_response = self.unpack_response(response)

        if filter_key and filter_val:
            return self.filter_on(unpacked_response, filter_key, filter_val, filter_exact=filter_exact)
        else:
            return unpacked_response

    def filter_on(self, l, filter_key, filter_val, filter_exact=True):
        if filter_exact:
            return [x for x in l if x[filter_key] == filter_val]
        else:
            return [x for x in l if filter_val.lower() in x[filter_key].lower()]


d = DuoAPI()

filter_key = "INSTELLINGSNAAM VESTIGING"
filter_val = input()
filter_val = filter_val.strip()

results = d.get_results(API_URL, filter_key=filter_key, filter_val=filter_val, filter_exact=False)

print(json.dumps(results, indent=2, sort_keys=True))

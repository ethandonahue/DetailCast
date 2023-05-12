import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.geoapify.com/v1/geocode/autocomplete?text=Mosco&apiKey=53a7ab2226e84cd48b9bd599eca20ae3"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"

resp = requests.get(url, headers=headers)

print(resp.status_code)
import requests
input = 'https://www.metaweather.com/api/location/search?query=london'
def get_data(url_endpoint):
    response = requests.get(url_endpoint)
    data = response.json()
    return data
print(get_data(input))

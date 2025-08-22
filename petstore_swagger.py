import requests

def get_endpoints(swagger_url):
    response = requests.get(swagger_url)
    swagger_json = response.json()
    paths = swagger_json.get("paths", {})
    return list(paths.keys())

# Example usage
swagger_url = "https://petstore.swagger.io/v2/swagger.json"
endpoints = get_endpoints(swagger_url)
print("Endpoints found:")
for ep in endpoints:
    print(ep)

import requests
from datetime import datetime

USERNAME = "piyushh"
TOKEN = "fds7687ds6f87dsv687vdf96dsfds"
GRAPH_ID = "pus"

pixella_endpoint = "https://pixe.la/v1/users"

user_params = {
 "token": TOKEN,
 "username": USERNAME,
 "agreeTermsOfService": "yes",
 "notMinor":"yes",
}
#
# response = requests.post(url=pixella_endpoint, json=user_params)
# print(response.text)

graph_endpoint =f"{pixella_endpoint}/{USERNAME}/graphs"

graph_config = {
 "id":GRAPH_ID,
 "name":"Cycling Graph",
 "unit": "Km",
 "type": "float",
 "color": "ajisai"
}

headers = {
 "X-USER-TOKEN": TOKEN

}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
pixel_endpoint = f"{pixella_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
pixel_config = {
 "date": today.strftime("%Y%m%d"),
 "quantity": input("How many km do you Runn?"),
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

updaye_endpoint = f"{pixella_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_config = {
 "quantity" : "2"
}

# response = requests.put(url=updaye_endpoint, json=update_config, headers=headers)
# print(response.text)

# response = requests.delete(url=updaye_endpoint, headers=headers)
# print(response.text)
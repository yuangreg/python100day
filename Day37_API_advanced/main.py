import requests, datetime

USER_NAME = "yuangreg"
TOKEN = "asde8954jk90sd7u54"
GRAPH_ID = "mygraph"

####################### Step 1. Create your user account ######################

pixela_endpoint = "https://pixe.la/v1/users"
user_para = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_para)
# print(response.text)


####################### Step 2. Create a graph definition ######################
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_para = {
    "id": GRAPH_ID,
    "name": "My Cycling Graph",
    "unit": "Meters",
    "type": "int",
    "color": "momiji",
}

header_para = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_para, headers=header_para)
# print(response.text)

####################### Step 3. Get the graph! ######################
# https://pixe.la/v1/users/yuangreg/graphs/mygraph

####################### Step 4. Post value to the graph ######################
post_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.datetime.now()
yesterday = datetime.datetime(year=2023, month=4, day=20)

newdata_para = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "5000",
}

# response = requests.post(url=post_endpoint, json=newdata_para, headers=header_para)
# print(response.text)


####################### Step 5. Update the graph ######################
update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_data = {
    "quantity": "100"
}

# response = requests.put(url=update_endpoint, json=new_data, headers=header_para)
# print(response.text)

###################### Step 6. Delete data from graph ######################
delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"

response = requests.delete(url=update_endpoint, headers=header_para)
print(response.text)
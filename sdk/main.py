import typer
import requests
import json
import os
import platform
import globus_sdk

app = typer.Typer()
TOKEN = ''
# TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJzdWIiOiI2MTRhY2M5ZC01N2U2LTQzNWYtOTAzNS0xY2I1ZjI2ZmQ3MjAiLCJuYW1lIjoic2RrQ2xpZW50Q3JlZGVudGlhbHMiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiI2MTRhY2M5ZC01N2U2LTQzNWYtOTAzNS0xY2I1ZjI2ZmQ3MjBAY2xpZW50cy5hdXRoLmdsb2J1cy5vcmciLCJpZGVudGl0eV9wcm92aWRlciI6IjNhNzQ4NzdiLWUyYTMtNDRiMS04OTU4LWVkZTEwMzFiMTgyNyIsImlkZW50aXR5X3Byb3ZpZGVyX2Rpc3BsYXlfbmFtZSI6Ikdsb2J1cyBBdXRoIiwiZW1haWwiOm51bGwsImxhc3RfYXV0aGVudGljYXRpb24iOm51bGwsImlkZW50aXR5X3NldCI6W3sic3ViIjoiNjE0YWNjOWQtNTdlNi00MzVmLTkwMzUtMWNiNWYyNmZkNzIwIiwibmFtZSI6InNka0NsaWVudENyZWRlbnRpYWxzIiwidXNlcm5hbWUiOiI2MTRhY2M5ZC01N2U2LTQzNWYtOTAzNS0xY2I1ZjI2ZmQ3MjBAY2xpZW50cy5hdXRoLmdsb2J1cy5vcmciLCJpZGVudGl0eV9wcm92aWRlciI6IjNhNzQ4NzdiLWUyYTMtNDRiMS04OTU4LWVkZTEwMzFiMTgyNyIsImlkZW50aXR5X3Byb3ZpZGVyX2Rpc3BsYXlfbmFtZSI6Ikdsb2J1cyBBdXRoIiwiZW1haWwiOm51bGwsImxhc3RfYXV0aGVudGljYXRpb24iOm51bGx9XSwiaXNzIjoiaHR0cHM6Ly9hdXRoLmdsb2J1cy5vcmciLCJhdWQiOiI2MTRhY2M5ZC01N2U2LTQzNWYtOTAzNS0xY2I1ZjI2ZmQ3MjAiLCJleHAiOjE2MjcwODc0NDAsImlhdCI6MTYyNjkxNDY0MCwiYXRfaGFzaCI6InNiUnA1TDlsV2RiZ2FZQ1liOFpOYm9KMk5fNldZMjRPNW1hVHBEQmw2NjAifQ.Bf6cOmkuojoOMYA_d9C-9jfIBHzqIN_-QoXY1gNnZIFGy8CU5U744lF6eI78MEVP_LnGIQjFVhaJI2-mTG3gg9AIhO6zbMgtFDOjQmXI-DPudaP49bpsId2dIiomxReP9sXQ1Y6UJezP_e_rWFpHgAO87-Q7UlZrBDkza-9WH0jbCk4Z8DQwdqUT1nbX7Gmad3VwF78e34jEd4iK-KEIbz3YlknQZ2kNMOL6GeNw49c_mKH5klnSZm649AizY4Vv3WtRyKE1EtOKX7Lco0tW3Mzw9z17GsfJIktx0Nsi5odShgaSp54kg_JT8sZs2vHy64hZ-CZYRs-MuLPJRcLC5w'
headers = {
    'Authorization': 'Bearer' + TOKEN,
    'Content-Type': 'application/json',
    'Cookie': 'csrftoken=7YtuX6V3HIEg3LJv84RyoUjMl7c8MvzdS5HdejDtWDLQPtlyOa3QvyJsndr88YJ8'
}


@app.command()
def send(v: str):
    with open(v) as graph_query:
        query = graph_query.read()
    url = 'http://localhost/graphql/'
    r = requests.post(url, json={'query': query})
    print(r.status_code)
    print(r.text)


@app.command()
def keywords(v="keywords.txt"):
    with open("querys/" + v) as graph_query:
        query = graph_query.read()
    url = 'http://localhost/graphql/'
    r = requests.get(url, json={'query': query})
    if (r.status_code == 200):
        print("This is your response:")
        print(r.text)
    else:
        print("Something is Wrong!!")
        print(r.text)


@app.command()
def keyword():
    with open("querys/keywordsId.txt") as graph_query:
        query = graph_query.read()
    url = 'http://localhost/graphql/'
    r = requests.get(url, json={'query': query})
    if (r.status_code == 200):
        print("This is your response:")
        print(r.text)
    else:
        print("Something is Wrong!!")
        print(r.text)

''' User'''

@app.command()
def me():
    with open("querys/me.txt") as graph_query:
        query = graph_query.read()
    url = 'http://localhost/graphql/'
    r = requests.get(url, json={'query': query}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
        print(r.text)
    else:
        print("Something is Wrong!!")
        print(r.text)


@app.command()
def users(id: str):
    variables = {"id":id}
    with open("querys/users.txt") as graph_query:
        query = graph_query.read()
    url = 'http://localhost/graphql/'
    r = requests.get(url, json={'query': query, 'variables': variables}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
        print(r.text)
    else:
        print("Something is Wrong!!")
        print(r.text)

@app.command()
def user(id: str):
    variables = {"id":id}
    with open("querys/user.txt") as graph_query:
        query = graph_query.read()
    url = 'http://localhost/graphql/'
    r = requests.get(url, json={'query': query, 'variables': variables}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
        print(r.text)
    else:
        print("Something is Wrong!!")
        print(r.text)

""" Study """

@app.command()
def studies():
    with open("querys/studies.txt") as graph_query:
        query = graph_query.read()
    url = 'http://localhost/graphql/'
    r = requests.post(url, json={'query': query}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
        print(r.text)
    else:
        print("Something is Wrong!!")
        print(r.text)

@app.command()
def study(v: str):
    with open("variables/" + v) as variables:
        variables = json.load(variables)
    with open("querys/study.txt") as graph_query:
        query = graph_query.read()
    url = 'http://localhost/graphql/'
    r = requests.post(url, json={'query': query}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
        print(r.text)
    else:
        print("Something is Wrong!!")
        print(r.text)

@app.command()
def createStudy(v: str):
    with open("variables/" + v) as variables:
        variables = json.load(variables)

    with open("querys/createStudy.txt") as graph_query:
        query = graph_query.read()
    url = 'http://localhost/graphql/'
    r = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
        print(r.text)
    else:
        print("Something is Wrong!!")
        print(r.text)

'''Samples'''

@app.command()
def samples():
    with open("querys/samples.txt") as graph_query:
        query = graph_query.read()
    url = 'http://localhost/graphql/'
    r = requests.post(url, json={'query': query}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
        print(r.text)
    else:
        print("Something is Wrong!!")
        print(r.text)

@app.command()
def sample(id: str):
    variables = {"id":id}
    with open("querys/sample.txt") as graph_query:
        query = graph_query.read()
    url = 'http://localhost/graphql/'
    r = requests.get(url, json={'query': query, 'variables': variables}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
        print(r.text)
    else:
        print("Something is Wrong!!")
        print(r.text)


''' Investigations'''
@app.command()
def investigations():
    with open("querys/investigations.txt") as graph_query:
        query = graph_query.read()
    url = 'http://localhost/graphql/'
    r = requests.post(url, json={'query': query}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
        print(r.text)
    else:
        print("Something is Wrong!!")
        print(r.text)

@app.command()
def investigation(id: str):
    variables = {"id":id}
    with open("querys/investigation.txt") as graph_query:
        query = graph_query.read()
    url = 'http://localhost/graphql/'
    r = requests.get(url, json={'query': query, 'variables': variables}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
        print(r.text)
    else:
        print("Something is Wrong!!")
        print(r.text)
@app.command()
def createInvestigation(v: str):
    with open("variables/" + v) as variables:
        variables = json.load(variables)

    with open("querys/createInvestigation.txt") as graph_query:
        query = graph_query.read()
    url = 'http://localhost/graphql/'
    r = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
        print(r.text)
    else:
        print("Something is Wrong!!")
        print(r.text)

''' Manage Files'''

@app.command()
def createvariables():
    print("Name of File")
    file = input()
    path = 'variables/' + file
    os.system('nano ' + path)

@app.command()
def updatesquerys():
    print("Name of File")
    file = input()
    path = 'querys/' + file
    os.system('nano ' + path)

@app.command()
def auth(id: str):

    CLIENT_ID = "896bbeb8-55fe-49d4-88d8-6307d87091a4"

    client = globus_sdk.NativeAppAuthClient(CLIENT_ID)
    client.oauth2_start_flow()

    authorize_url = client.oauth2_get_authorize_url()
    print("Please go to this URL and login: {0}".format(authorize_url))

    auth_code = input("Please enter the code you get after login here: ").strip()
    token_response = client.oauth2_exchange_code_for_tokens(auth_code)

    globus_auth_data = token_response.by_resource_server["auth.globus.org"]
    globus_transfer_data = token_response.by_resource_server["transfer.api.globus.org"]

    # most specifically, you want these tokens as strings
    AUTH_TOKEN = globus_auth_data["access_token"]
    TRANSFER_TOKEN = globus_transfer_data["access_token"]
    TOKEN = AUTH_TOKEN


if __name__ == "__main__":
    app()

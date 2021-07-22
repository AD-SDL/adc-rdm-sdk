import typer
import requests
import json
import os
import platform
import globus_sdk
from dotenv import load_dotenv
load_dotenv('.env')
print(os.getenv("TOKEN"))

app = typer.Typer()

authtoken=''
if (os.getenv("TOKEN")):
    authtoken = os.getenv("TOKEN")
token = authtoken
auth = "JWT " + token
headers = {
        'Authorization': auth,
        'Content-Type': 'application/json'
    }

@app.command()
def authtoken():
    print("Insert token here:")
    authtoken= input()
    token = authtoken
    auth = "JWT " + token
    makeheader(auth)
    print(auth)

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

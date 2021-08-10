import globus_sdk
import json
import os
import platform
import requests
import sys
import typer
from querys import query as graphql
from variables import variable
from dotenv import load_dotenv

load_dotenv('.env')

app = typer.Typer()
url = "http://localhost/graphql/"
# url = "https://rdm-stage.discoverycloud.anl.gov/"
if (os.getenv("URL")):
    url = os.getenv("URL")

authtoken = ''
if (os.getenv("TOKEN")):
    authtoken = os.getenv("TOKEN")
token = authtoken
auth = "JWT " + token
headers = {
    'Authorization': auth,
    'Content-Type': 'application/json'
}


def checkHeaders():
    auth=''
    if (os.environ.get("TOKEN")):
        authtoken = os.environ.get("TOKEN")
        auth = "JWT " + authtoken
    else:
        print("token missed", os.environ.get("TOKEN"))
    headers = {
        'Authorization': auth,
        'Content-Type': 'application/json'
    }
    return headers


@app.command()
def authtoken(token=None):
    if token:
        authtoken = token
    else:
        print("Insert token here:")
        authtoken = input()
    os.environ['TOKEN'] = str(authtoken)
    load_dotenv('.env')
    return os.getenv("TOKEN")


def showToken():
    return os.getenv("TOKEN")


@app.command()
def send(v: str):
    with open(v) as graph_query:
        query = graph_query.read()
    r = requests.post(url, json={'query': query})
    data = json.loads(r.text)
    return data["data"]


@app.command()
def keywords():
    r = requests.get(url, json={'query': graphql.keywords})
    if (r.status_code == 200):
        print("This is your response:")
    else:
        print("Something is Wrong!!")
    data = json.loads(r.text)
    return data["data"]


@app.command()
def keyword():
    url = 'http://localhost/graphql/'
    r = requests.get(url, json={'query': graphql.keywords})
    if (r.status_code == 200):
        print("This is your response:")
    else:
        print("Something is Wrong!!")
    data = json.loads(r.text)
    return data["data"]


''' User'''


@app.command()
def me():
    headers = checkHeaders()
    r = requests.get(url, json={'query': graphql.me}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
    else:
        print("Something is Wrong!!")

    data = json.loads(r.text)
    return (json.dumps(data["data"], indent=4, sort_keys=True))


@app.command()
def users():
    headers = checkHeaders()
    r = requests.get(url, json={'query': graphql.users}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
    else:
        print("Something is Wrong!!")
    data = json.loads(r.text)
    return (json.dumps(data["data"], indent=4, sort_keys=True))


@app.command()
def user(u=None):
    headers = checkHeaders()
    if sys.argv[1]:
        u = sys.argv[1]

    variables = {
        "id": u
    }
    r = requests.get(url, json={'query': graphql.user, 'variables': variables}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
    else:
        print("Something is Wrong!!")
    data = json.loads(r.text)
    return (json.dumps(data["data"], indent=4, sort_keys=True))


""" Study """


@app.command()
def studies():
    headers = checkHeaders()
    r = requests.post(url, json={'query': graphql.studies}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
    else:
        print("Something is Wrong!!")
    data = json.loads(r.text)
    return (json.dumps(data["data"], indent=4, sort_keys=True))


@app.command()
def study(u=None):
    headers = checkHeaders()
    if u:
        variables = {
            "id": u
        }
    else:
        if sys.argv[1]:
            variables = {
                "id": sys.argv[1]
            }
        else:
            return "Argument missed"


    r = requests.post(url, json={'query': graphql.study, 'variables': variables}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
    else:
        print("Something is Wrong!!")
    data = json.loads(r.text)
    return (json.dumps(data["data"], indent=4, sort_keys=True))


@app.command()
def createStudy(v=None):
    if not v:
        msg = "Use a pre-charged variable file"
        variables = variable.createStudy
    else:
        msg = "Use your param variable file"
        variables = v
        try:
            if sys.argv[1] and  v == None :
                print (v)
                variables = sys.argv[1]
        except:
            pass
    headers = checkHeaders()
    r = requests.post(url, json={'query': graphql.createStudy, 'variables': variables}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
    else:
        print("Something is Wrong!!")
    data = json.loads(r.text)
    return (json.dumps(data["data"], indent=4, sort_keys=True))


'''Samples'''


@app.command()
def samples():
    headers = checkHeaders()
    r = requests.post(url, json={'query': graphql.samples}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
    else:
        print("Something is Wrong!!")
    data = json.loads(r.text)
    return (json.dumps(data["data"], indent=4, sort_keys=True))


@app.command()
def sample(u=None):
    headers = checkHeaders()
    if u:
        variables = {
            "id": u
        }
    else:
        if sys.argv[1]:
            variables = {
                "id": sys.argv[1]
            }
        else:
            return "Argument missed"
    r = requests.get(url, json={'query': graphql.sample, 'variables': variables}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
    else:
        print("Something is Wrong!!")
    data = json.loads(r.text)
    return (json.dumps(data["data"], indent=4, sort_keys=True))


''' Investigations'''


@app.command()
def investigations():
    r = requests.post(url, json={'query': graphql.investigations}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
    else:
        print("Something is Wrong!!")
    data = json.loads(r.text)
    return (json.dumps(data["data"], indent=4, sort_keys=True))


@app.command()
def investigation(u=None):
    headers = checkHeaders()
    if u:
        variables = {
            "id": u
        }
    else:
        if sys.argv[1]:
            variables = {
                "id": sys.argv[1]
            }
        else:
            return "Argument missed"
    r = requests.get(url, json={'query': graphql.investigation, 'variables': variables}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
    else:
        print("Something is Wrong!!")
    data = json.loads(r.text)
    return (json.dumps(data["data"], indent=4, sort_keys=True))


@app.command()
def createInvestigation(v=None):
    if not v:
        msg = "Use a pre-charged variable file"
        variables = variable.createStudy
    else:
        msg = "Use your param variable file"
        variables = v
        try:
            if sys.argv[1] and v == None:
                print(v)
                variables = sys.argv[1]
        except:
            pass
    headers = checkHeaders()
    r = requests.post(url, json={'query': graphql.createInvestigation, 'variables': variables}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
        data = json.loads(r.text)
        return (json.dumps(data["data"], indent=4, sort_keys=True))
    else:
        print("Something is Wrong!!")
        data = json.loads(r.text)
        return data


@app.command()
def createsample(o=None, op=None, m=None):
    operation ="""{"query":"mutation ($name: String!, $parentId: ID, $keywords: [String!], $file: Upload!) {createSample(name: $name, parentId: $parentId, keywords: $keywords, file: $file) {sample { id name keywords url}}}",     "variables": { "name": "test sample", "keywords": ["test", "python"], "file": null}}"""
    map ="""{ "0": ["variables.file"]}"""
    f = "sample.json"
    if o:
        operation = op
        map = m
        f = str(o)
    else:
        print("enter file")
        file = open("testfile.json", "w")
        file.write("")

        file.close()
    f = input()
    files = [
        ('0', (f,
               open('' + f, 'rb'), 'application/json'))
    ]
    payload = {
        'operations': operation,
        'map': map}

    headers = {
        'Authorization': "JWT " + token

    }
    r = requests.request("POST", url, headers=headers, data=payload, files=files)
    if (r.status_code == 200):
        print("This is your response:")
    else:
        print("Something is Wrong!!")
    data = json.loads(r.text)
    return (json.dumps(data, indent=4, sort_keys=True))

@app.command()
def createsampleWithFile(file=None):
    operation ="""{"query":"mutation ($name: String!, $parentId: ID, $keywords: [String!], $file: Upload!) {createSample(name: $name, parentId: $parentId, keywords: $keywords, file: $file) {sample { id name keywords url}}}",     "variables": { "name": "test sample", "keywords": ["test", "python"], "file": null}}"""
    map ="""{ "0": ["variables.file"]}"""
    files = [
        ('0', ("sample,json",
               open('' + str(file), 'rb'), 'application/json'))
    ]
    payload = {
        'operations': operation,
        'map': map}

    headers = {
        'Authorization': "JWT " + token

    }
    r = requests.request("POST", url, headers=headers, data=payload, files=files)
    if (r.status_code == 200):
        print("This is your response:")
    else:
        print("Something is Wrong!!")
    data = json.loads(r.text)
    return (json.dumps(data, indent=4, sort_keys=True))

def cSampleWithStr(file_content=None,nFile= None):
    operation ="""{"query":"mutation ($name: String!, $parentId: ID, $keywords: [String!], $file: Upload!) {createSample(name: $name, parentId: $parentId, keywords: $keywords, file: $file) {sample { id name keywords url}}}",     "variables": { "name": "test sample", "keywords": ["test", "python"], "file": null}}"""
    map ="""{ "0": ["variables.file"]}"""
    file_name="sample_json"
    file = open(file_name, "w+")
    file.write(str(file_content))
    file.close()
    if nFile:
        name=nFile
    else:
        name="sample_query.json"

    files = [
        ('0', (name,
               open('' + str(file), 'w+'), 'application/json'))
    ]
    payload = {
        'operations': operation,
        'map': map}

    headers = {
        'Authorization': "JWT " + token

    }
    r = requests.request("POST", url, headers=headers, data=payload, files=files)
    if (r.status_code == 200):
        print("This is your response:")
    else:
        print("Something is Wrong!!")
    data = json.loads(r.text)
    return data


@app.command()
def customvarq(v: str, q: str):
    with open("variables/" + v) as variables:
        variables = json.load(variables)
    with open("querys/" + q) as graph_query:
        query = graph_query.read()
    r = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)
    if (r.status_code == 200):
        print("This is your response:")
    else:
        print("Something is Wrong!!")
    data = json.loads(r.text)
    return (json.dumps(data["data"], indent=4, sort_keys=True))


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

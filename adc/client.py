from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.websockets import WebsocketsTransport
from .queries import (
    TOKENS,
    STUDIES,
    STUDY,
    ME,
    INVESTIGATION,
    CREATE_TOKEN,
    DELETE_TOKEN,
    CREATE_STUDY,
    CREATE_SAMPLE,
    CREATE_INVESTIGATION,
    SET_PERMISSIONS,
    REMOVE_PERMISSIONS,
    STUDY_SUBSCRIPTION,
)
import json
import requests


class ADCClient:
    def __init__(self, token):
        self.token = token
        self.http_url = "http://localhost/graphql/"
        self.ws_url = "ws://localhost/graphql/"
        self.headers = {"authorization": f"JWT {token}"}
        self.client = Client(
            transport=AIOHTTPTransport(url=self.http_url, headers=self.headers)
        )
        self.ws_client = Client(
            transport=WebsocketsTransport(url=self.ws_url, headers=self.headers)
        )

    def get_tokens(self):
        return self.client.execute(TOKENS)

    def get_studies(self):
        return self.client.execute(STUDIES)

    def get_study(self, study_id):
        variables = {"id": study_id}
        return self.client.execute(STUDY, variable_values=variables)

    def get_current_user(self):
        return self.client.execute(ME)

    def get_investigation(self, investigation_id):
        variables = {"id": investigation_id}
        return self.client.execute(INVESTIGATION, variable_values=variables)

    def create_token(self, name):
        variables = {"name": name}
        return self.client.execute(CREATE_TOKEN, variable_values=variables)

    def delete_token(self, token_id):
        variables = {"tokenId": token_id}
        return self.client.execute(DELETE_TOKEN, variable_values=variables)

    def create_study(self, name, description, keywords=[]):
        variables = {
            "description": description,
            "keywords": keywords,
            "name": name,
        }
        return self.client.execute(CREATE_STUDY, variable_values=variables)

    def create_sample(
        self, file, study_id, name, keywords=[], parent_id=None, source=None
    ):
        variables = {
            "file": None,
            "studyId": study_id,
            "name": name,
            "keywords": keywords,
        }
        if parent_id:
            variables["parentId"] = parent_id
        if source:
            variables["source"] = source
        operations = json.dumps(
            {"query": CREATE_SAMPLE, "variables": variables}
        )
        map = json.dumps({"0": ["variables.file"]})
        response = requests.post(
            self.http_url,
            data={"operations": operations, "map": map},
            files={"0": file},
            headers=self.headers,
        )
        return json.loads(response.content)

    def create_investigation(
        self, study_id, name, description, keywords=[], investigation_type=None
    ):
        variables = {
            "studyId": study_id,
            "name": name,
            "description": description,
            "keywords": keywords,
        }
        if investigation_type:
            variables["investigationType"] = investigation_type
        return self.client.execute(
            CREATE_INVESTIGATION, variable_values=variables
        )

    def set_permissions(self, study_id, user_id, permission_level):
        variables = {
            "studyId": study_id,
            "userId": user_id,
            "permission": permission_level,
        }
        return self.client.execute(SET_PERMISSIONS, variable_values=variables)

    def remove_permissions(self, study_id, user_id):
        variables = {"studyId": study_id, "userId": user_id}
        return self.client.execute(
            REMOVE_PERMISSIONS, variable_values=variables
        )

    def subscribe_to_study(self, study_id, callback):
        variables = {"studyId": study_id}
        for result in self.ws_client.subscribe(
            STUDY_SUBSCRIPTION, variable_values=variables
        ):
            callback(result)

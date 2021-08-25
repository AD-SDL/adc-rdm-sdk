from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.websockets import WebsocketsTransport
from adc import queries, exceptions
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

    def _execute(self, query_cls, variables=None):
        raw_response = self.client.execute(query_cls.query, variable_values=variables)
        response = raw_response[query_cls.path] if query_cls.path else raw_response
        self._check_for_errors(response)
        return response

    def get_tokens(self):
        return self._execute(queries.TOKENS)

    def get_studies(self):
        return self._execute(queries.STUDIES)

    def get_study(self, study_id):
        variables = {"id": study_id}
        return self._execute(queries.STUDY, variables)

    def get_current_user(self):
        return self._execute(queries.CURRENT_USER)

    def get_investigation(self, investigation_id):
        variables = {"id": investigation_id}
        return self._execute(queries.INVESTIGATION, variables)

    def create_token(self, name):
        variables = {"name": name}
        return self._execute(queries.CREATE_TOKEN, variables)

    def delete_token(self, token_id):
        variables = {"tokenId": token_id}
        return self._execute(queries.DELETE_TOKEN, variables)

    def create_study(self, name, description, keywords=[]):
        variables = {
            "description": description,
            "keywords": keywords,
            "name": name,
        }
        return self._execute(queries.CREATE_STUDY, variables)

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
            {"query": queries.CREATE_SAMPLE.raw_query, "variables": variables}
        )
        map = json.dumps({"0": ["variables.file"]})
        raw_response = requests.post(
            self.http_url,
            data={"operations": operations, "map": map},
            files={"0": file},
            headers=self.headers,
        )
        response = json.loads(raw_response.content)['data'][queries.CREATE_SAMPLE.path]
        self._check_for_errors(response)
        return response

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
        return self._execute(queries.CREATE_INVESTIGATION, variables)

    def set_permissions(self, study_id, user_id, permission_level):
        variables = {
            "studyId": study_id,
            "userId": user_id,
            "permission": permission_level,
        }
        return self._execute(queries.SET_PERMISSIONS, variables)

    def remove_permissions(self, study_id, user_id):
        variables = {"studyId": study_id, "userId": user_id}
        return self._execute(queries.REMOVE_PERMISSIONS, variables)

    def subscribe_to_study(self, study_id, callback):
        variables = {"studyId": study_id}
        for result in self.ws_client.subscribe(
            queries.STUDY_SUBSCRIPTION.query, variable_values=variables
        ):
            callback(result)

    @staticmethod
    def _check_for_errors(response):
        if "error" in response and response["error"]:
            raise exceptions.ADCError(response["error"])
        if "errors" in response:
            raise exceptions.ADCError(response["errors"][0]["message"])

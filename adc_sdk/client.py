from gql import Client
from gql.transport.exceptions import TransportQueryError
from datetime import datetime
from typing import BinaryIO
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.websockets import WebsocketsTransport
from adc_sdk import queries, exceptions
from typing import Iterator


class ADCClient:
    """
    Client class to use in order to interact with Argonne Discovery Cloud API.
    """

    def __init__(self, token: str):
        """
        Create an ADCClient instance to interact with the API.
        Arguments:
            token: API Access Token
        """
        self.token = token
        self.http_url = "https://rdm-stage.discoverycloud.anl.gov/graphql/"
        self.ws_url = "wss://rdm-stage.discoverycloud.anl.gov/graphql/"
        self.headers = {"authorization": f"JWT {token}"}
        self.client = Client(
            transport=AIOHTTPTransport(url=self.http_url, headers=self.headers)
        )
        self.ws_client = Client(
            transport=WebsocketsTransport(url=self.ws_url, headers=self.headers)
        )

    def _execute(self, query_cls, variables=None, file_upload=False):
        """
        Run query and return response's relevant content.
        """
        try:
            response = self.client.execute(query_cls.query, variable_values=variables, upload_files=file_upload)
        except TransportQueryError as e:
            raise exceptions.ADCError(e.errors[0]['message'])
        return response[query_cls.path] if query_cls.path else response

    def get_tokens(self) -> dict:
        """
        Retrieve the current user's tokens.
        """
        return self._execute(queries.TOKENS)

    def get_studies(self) -> dict:
        """
        Retrieve studies the current user has permission over.
        """
        return self._execute(queries.STUDIES)

    def get_study(self, study_id: str) -> dict:
        """
        Retrieve a specific study.
        Arguments:
            study_id: Study ID
        """
        variables = {"id": study_id}
        return self._execute(queries.STUDY, variables)

    def get_sample(self, sample_id: str) -> dict:
        """
        Retrieve a specific sample.
        Arguments:
            sample_id: Sample ID
        """
        variables = {"id": sample_id}
        return self._execute(queries.SAMPLE, variables)

    def get_datafile(self, datafile_id: str) -> dict:
        """
        Retrieve a specific datafile.
        Arguments:
            datafile_id: Datafile ID
        """
        variables = {"id": datafile_id}
        return self._execute(queries.DATAFILE, variables)

    def get_job(self, job_id: str) -> dict:
        """
        Retrieve a specific job.
        Arguments:
            job_id: Job ID
        """
        variables = {"id": job_id}
        return self._execute(queries.JOB, variables)

    def get_current_user(self) -> dict:
        """
        Retrieve the currently authenticated user.
        """
        return self._execute(queries.CURRENT_USER)

    def get_investigation(self, investigation_id: str) -> dict:
        """
        Retrieve a specific investigation.
        Arguments:
            investigation_id: Investigation ID
        """
        variables = {"id": investigation_id}
        return self._execute(queries.INVESTIGATION, variables)

    def create_token(self, name: str) -> dict:
        """
        Create a new access token for the currently logged user.
        Arguments:
            name: Desired token name
        """
        variables = {"name": name}
        return self._execute(queries.CREATE_TOKEN, variables)

    def delete_token(self, token_id: str) -> dict:
        """
        Delete a specific access token for the current user.
        Arguments:
            token_id: ID of the token that will be deleted
        """
        variables = {"tokenId": token_id}
        return self._execute(queries.DELETE_TOKEN, variables)

    def create_study(self, name: str, description: str, keywords: list = None) -> dict:
        """
        Create a new study.
        Arguments:
            name: study name
            description: study description
            keywords: study keywords
        """
        variables = {
            "description": description,
            "keywords": keywords if keywords else [],
            "name": name,
        }
        return self._execute(queries.CREATE_STUDY, variables)

    def create_sample(
        self, file: BinaryIO, study_id: str, name: str, keywords: list = None, parent_id: str = None, source: str = None
    ) -> dict:
        """
        Create a new sample.
        Arguments:
            file: sample file, opened as binary (i.e. with 'rb')
            study_id: study id
            name: sample name
            keywords: sample keywords
            parent_id: id of parent sample
            source: custom additional string value
        """
        variables = {
            "file": file,
            "studyId": study_id,
            "name": name,
            "keywords": keywords if keywords else [],
        }
        if parent_id: variables["parentId"] = parent_id
        if source: variables["source"] = source
        return self._execute(queries.CREATE_SAMPLE, variables, file_upload=True)

    def create_datafile(
        self, name: str, job_id: str, file: BinaryIO, description: str = None, source: str = None
    ) -> dict:
        """
        Create a new datafile.
        Arguments:
            file: actual file, opened as binary (i.e. with 'rb')
            job_id: job id
            name: sample name
            description: datafile description
            source: custom additional string value
        """
        variables = {
            "file": file,
            "jobId": job_id,
            "name": name,
        }
        if description: variables["description"] = description
        if source: variables["source"] = source
        return self._execute(queries.CREATE_DATAFILE, variables, file_upload=True)

    def create_investigation(
        self, study_id: str, name: str, description: str, keywords: list = None, investigation_type: str = None
    ) -> dict:
        """
        Create a new investigation.
        Arguments:
            study_id: study id
            name: investigation name
            description: investigation description
            keywords: investigation keywords
            investigation_type: available values are ['experiment', 'simulation', 'observation', 'measurement']
        """
        variables = {
            "studyId": study_id,
            "name": name,
            "description": description,
            "keywords": keywords if keywords else [],
        }
        if investigation_type: variables["investigationType"] = investigation_type
        return self._execute(queries.CREATE_INVESTIGATION, variables)

    def create_job(self, investigation_id: str, sample_id: str, start_datetime: datetime, end_datetime: datetime = None, status: str = None, source: str = None) -> dict:
        """
        Create a new job.
        Arguments:
            investigation_id: investigation id
            sample_id: id of sample to be used as job input
            start_datetime: job start datetime
            end_datetime: job end datetime
            status: available values are ['completed', 'cancelled', 'running']
            source: custom additional string value
        """
        variables = {
            "investigationId": investigation_id,
            "sampleId": sample_id,
            "startDatetime": start_datetime.isoformat(),
        }
        if end_datetime: variables["endDatetime"] = end_datetime.isoformat()
        if status: variables["status"] = status
        if source: variables["source"] = source
        return self._execute(queries.CREATE_JOB, variables)

    def update_job(self, job_id: str, status: str, end_datetime: datetime = None, source: str = None) -> dict:
        """
        Update an already existing job.
        Arguments:
            job_id: job id
            end_datetime: job end datetime
            status: available values are ['completed', 'cancelled', 'running']
            source: custom additional string value
        """
        variables = {
            "jobId": job_id,
            "status": status,
        }
        if end_datetime: variables["endDatetime"] = end_datetime.isoformat()
        if source: variables["source"] = source
        return self._execute(queries.UPDATE_JOB, variables)

    def set_permissions(self, study_id: str, user_id: str, permission_level: str) -> dict:
        """
        Set user permissions over a study.
        Arguments:
            study_id: study id
            user_id: id of the user we want to add / modify permissions over a study
            permission_level: available values are ['read', 'write', 'access']
        """
        variables = {
            "studyId": study_id,
            "userId": user_id,
            "permission": permission_level,
        }
        return self._execute(queries.SET_PERMISSIONS, variables)

    def remove_permissions(self, study_id: str, user_id: str) -> dict:
        """
        Remove user permissions over a study.
        Arguments:
            study_id: study id
            user_id: id of the user we want remove from a study
        """
        variables = {"studyId": study_id, "userId": user_id}
        return self._execute(queries.REMOVE_PERMISSIONS, variables)

    def subscribe_to_study(self, study_id: str) -> Iterator[dict]:
        """
        Subscribe to a study to get notifications when a new sample is added or an investigation is created.
        Arguments:
            study_id: study id
        """
        variables = {"studyId": study_id}
        for result in self.ws_client.subscribe(
            queries.STUDY_SUBSCRIPTION.query, variable_values=variables
        ):
            yield result

    def subscribe_to_investigation(self, investigation_id: str) -> Iterator[dict]:
        """
        Subscribe to an investigation to get notifications when a new job is created.
        Arguments:
            investigation_id: investigation id
        """
        variables = {"investigationId": investigation_id}
        for result in self.ws_client.subscribe(
                queries.INVESTIGATION_SUBSCRIPTION.query, variable_values=variables
        ):
            yield result

    def subscribe_to_job(self, job_id: str) -> Iterator[dict]:
        """
        Subscribe to a job to get notifications when a new datafile is created.
        Arguments:
            job_id: job id
        """
        variables = {"jobId": job_id}
        for result in self.ws_client.subscribe(
                queries.JOB_SUBSCRIPTION.query, variable_values=variables
        ):
            yield result

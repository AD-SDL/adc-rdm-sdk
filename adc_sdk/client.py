from gql.transport.exceptions import TransportQueryError
from datetime import datetime, date
from typing import BinaryIO, List
from adc_sdk import queries, exceptions
from adc_sdk.base import ADCBaseClient
from typing import Iterator

from adc_sdk.models import User, Sample, Study, StudySubscriptionEvent, CreateSampleResponse


class ADCClient(ADCBaseClient):
    """
    Client class to use in order to interact with Argonne Discovery Cloud API.
    """

    def get_tokens(self) -> dict:
        """
        Retrieve the current user's tokens.
        Example:
            ```
            from adc_sdk.client import ADCClient
            adc = ADCClient(<api_token>)
            adc.get_tokens()
            ```
        """
        return self._execute(queries.TOKENS)

    def get_studies(self) -> dict:
        """
        Retrieve studies the current user has permission over.
        Example:
            ```
            from adc_sdk.client import ADCClient
            adc = ADCClient(<api_token>)
            adc.get_studies()
            ```
        """
        return self._execute(queries.STUDIES)

    def get_study(self, study_id: str) -> Study:
        """
        Retrieve a specific study.
        Example:
            ```
            from adc_sdk.client import ADCClient
            adc = ADCClient(<api_token>)
            adc.get_study(<study_id>)
            ```
        Arguments:
            study_id: Study ID
        """
        variables = {"id": study_id}
        response = self._execute(queries.STUDY, variables)
        return Study.parse_response(response['study'])

    def get_sample(self, sample_id: str) -> Sample:
        """
        Retrieve a specific sample.
        Example:
            ```
            from adc_sdk.client import ADCClient
            adc = ADCClient(<api_token>)
            adc.get_sample(<sample_id>)
            ```
        Arguments:
            sample_id: Sample ID
        """
        variables = {"id": sample_id}
        response = self._execute(queries.SAMPLE, variables)
        return Sample.parse_obj(response['sample'])

    def get_datafile(self, datafile_id: str) -> dict:
        """
        Retrieve a specific datafile.
        Example:
            ```
            from adc_sdk.client import ADCClient
            adc = ADCClient(<api_token>)
            adc.get_datafile(<datafile_id>)
            ```
        Arguments:
            datafile_id: Datafile ID
        """
        variables = {"id": datafile_id}
        return self._execute(queries.DATAFILE, variables)

    def get_job(self, job_id: str) -> dict:
        """
        Retrieve a specific job.
        Example:
            ```
            from adc_sdk.client import ADCClient
            adc = ADCClient(<api_token>)
            adc.get_job(<job_id>)
            ```
        Arguments:
            job_id: Job ID
        """
        variables = {"id": job_id}
        return self._execute(queries.JOB, variables)

    def get_current_user(self) -> User:
        """
        Retrieve the currently authenticated user.
        Example:
            ```
            from adc_sdk.client import ADCClient
            adc = ADCClient(<api_token>)
            adc.current_user()
            ```
        """
        response = self._execute(queries.CURRENT_USER)
        return User.parse_obj(response['me'])

    def get_investigation(self, investigation_id: str) -> dict:
        """
        Retrieve a specific investigation.
        Example:
            ```
            from adc_sdk.client import ADCClient
            adc = ADCClient(<api_token>)
            adc.get_investigation(<investigation_id>)
            ```
        Arguments:
            investigation_id: Investigation ID
        """
        variables = {"id": investigation_id}
        return self._execute(queries.INVESTIGATION, variables)

    def create_token(self, name: str) -> dict:
        """
        Create a new access token for the currently logged user.
        Example:
            ```
            from adc_sdk.client import ADCClient
            adc = ADCClient(<api_token>)
            adc.create_token('<token_name>')
            ```
        Arguments:
            name: Desired token name
        """
        variables = {"name": name}
        return self._execute(queries.CREATE_TOKEN, variables)

    def delete_token(self, token_id: str) -> dict:
        """
        Delete a specific access token for the current user.
        Example:
            ```
            from adc_sdk.client import ADCClient
            adc = ADCClient(<api_token>)
            adc.delete_token('<token_id>')
            ```
        Arguments:
            token_id: ID of the token that will be deleted
        """
        variables = {"tokenId": token_id}
        return self._execute(queries.DELETE_TOKEN, variables)

    def create_study(
        self,
        name: str,
        description: str = None,
        keywords: List[str] = None,
        start_date: date = None,
        end_date: date = None,
    ) -> dict:
        """
        Create a new study.
        Example:
            ```
            from adc_sdk.client import ADCClient
            adc = ADCClient(<api_token>)
            adc.create_study(
                <study_name>,
                description=<study_description>,
                keywords=[<keywords>],
                start_date=<start_date>,
                end_date=<end_date>
            )
            ```
        Arguments:
            name: study name
            description: study description
            keywords: study keywords
            start_date: Date when the study began
            end_date: Date when the study ended
        """
        if start_date:
            start_date = start_date.isoformat()
        if end_date:
            end_date = end_date.isoformat()
        variables = {
            "name": name,
            "description": description,
            "keywords": keywords,
            "startDate": start_date,
            "endDate": end_date,
        }
        return self._execute(queries.CREATE_STUDY, variables)

    def create_sample(
        self,
        study_id: str,
        name: str,
        file: BinaryIO = None,
        keywords: list = None,
        parent_id: str = None,
        source: str = None,
    ) -> CreateSampleResponse:
        """
        Create a new sample.
        Example:
            ```
            from adc_sdk.client import ADCClient
            adc = ADCClient(<api_token>)
            adc.create_sample(
                <study_id>,
                <sample_name>,
                file=<binary_file>,
                keywords=[<keywords>],
                parent_id=<parent_sample_id>,
                source=<custom_subscription_message>
            )
            ```
        Arguments:
            file: sample file, opened as binary (i.e. with 'rb')
            study_id: study id
            name: sample name
            keywords: sample keywords
            parent_id: id of parent sample
            source: custom additional string value
        """
        variables = {
            "studyId": study_id,
            "name": name,
            "file": file,
            "keywords": keywords,
            "parentId": parent_id,
            "source": source,
        }
        response = self._execute(queries.CREATE_SAMPLE, variables, file_upload=True)
        return CreateSampleResponse.parse_obj(response)

    def create_datafile(
        self,
        name: str,
        job_id: str,
        file: BinaryIO,
        description: str = None,
        source: str = None,
    ) -> dict:
        """
        Create a new datafile.
        Example:
            ```
            from adc_sdk.client import ADCClient
            adc = ADCClient(<api_token>)
            adc.create_datafile(
                <datafile_name>,
                <job_id>,
                <binary_file>,
                description=<datafile_description>,
                source=<custom_subscription_message>
            )
            ```
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
            "description": description,
            "source": source,
        }
        return self._execute(queries.CREATE_DATAFILE, variables, file_upload=True)

    def create_investigation(
        self,
        study_id: str,
        name: str,
        description: str = None,
        investigation_type: str = None,
        keywords: list = None,
        start_date: date = None,
        end_date: date = None,
        source: str = None,
    ) -> dict:
        """
        Create a new investigation.
        Example:
            ```
            from adc_sdk.client import ADCClient
            adc = ADCClient(<api_token>)
            adc.create_investigation(
                <study_id>,
                <investigation_name>,
                description=<investigation_description>,
                investigation_type=<investigation_type>,
                keywords=[<keywords>],
                start_date=<start_date>,
                end_date=<end_date>,
                source=<custom_subscription_message>
            )
            ```
        Arguments:
            study_id: study id
            name: investigation name
            description: investigation description
            keywords: investigation keywords
            investigation_type: investigation type
            start_date: Date when the investigation began
            end_date: Date when the investigation ended
            source: custom additional string value
        """
        if start_date:
            start_date = start_date.isoformat()
        if end_date:
            end_date = end_date.isoformat()
        variables = {
            "name": name,
            "studyId": study_id,
            "description": description,
            "investigationType": investigation_type,
            "keywords": keywords,
            "startDate": start_date,
            "endDate": end_date,
            "source": source,
        }
        return self._execute(queries.CREATE_INVESTIGATION, variables)

    def create_job(
        self,
        investigation_id: str,
        sample_id: str = None,
        start_datetime: datetime = None,
        end_datetime: datetime = None,
        status: str = None,
        source: str = None,
    ) -> dict:
        """
        Create a new job.
        Example:
            ```
            from adc_sdk.client import ADCClient
            adc = ADCClient(<api_token>)
            adc.create_job(
                <investigation_id>,
                sample_id=<sample_id>,
                start_datetime=<start_datetime>,
                end_datetime=<end_datetime>,
                status=<job_status>,
                source=<custom_subscription_message>
            )
            ```
        Arguments:
            investigation_id: investigation id
            sample_id: id of sample to be used as job input
            start_datetime: job start datetime
            end_datetime: job end datetime
            status: available values are ['completed', 'cancelled', 'running', 'created']
            source: custom additional string value
        """
        if start_datetime:
            start_datetime = start_datetime.isoformat()
        if end_datetime:
            end_datetime = end_datetime.isoformat()
        variables = {
            "investigationId": investigation_id,
            "sampleId": sample_id,
            "status": status,
            "startDatetime": start_datetime,
            "endDatetime": end_datetime,
            "source": source,
        }
        return self._execute(queries.CREATE_JOB, variables)

    def update_job(
        self,
        job_id: str,
        status: str = None,
        start_datetime: datetime = None,
        end_datetime: datetime = None,
        source: str = None,
    ) -> dict:
        """
        Update an already existing job.
        Example:
            ```
            from adc_sdk.client import ADCClient
            adc = ADCClient(<api_token>)
            adc.update_job(
                <job_id>,
                status=<job_status>,
                start_datetime=<start_datetime>,
                end_datetime=<end_datetime>,
                source=<custom_subscription_message>
            )
            ```
        Arguments:
            job_id: job id
            start_datetime: job start datetime
            end_datetime: job end datetime
            status: available values are ['completed', 'cancelled', 'running', 'created']
            source: custom additional string value
        """
        if start_datetime:
            start_datetime = start_datetime.isoformat()
        if end_datetime:
            end_datetime = end_datetime.isoformat()
        variables = {
            "jobId": job_id,
            "status": status,
            "startDatetime": start_datetime,
            "endDatetime": end_datetime,
            "source": source,
        }
        return self._execute(queries.UPDATE_JOB, variables)

    def set_permissions(
        self, study_id: str, user_id: str, permission_level: str
    ) -> dict:
        """
        Set user permissions over a study.
        Example:
            ```
            from adc_sdk.client import ADCClient
            adc = ADCClient(<api_token>)
            adc.set_permissions(<study_id>, <user_id>, <permission_level>)
            ```
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
        Example:
            ```
            from adc_sdk.client import ADCClient
            adc = ADCClient(<api_token>)
            adc.remove_permissions(<study_id>, <user_id>)
            ```
        Arguments:
            study_id: study id
            user_id: id of the user we want remove from a study
        """
        variables = {"studyId": study_id, "userId": user_id}
        return self._execute(queries.REMOVE_PERMISSIONS, variables)

    def subscribe_to_study(self, study_id: str) -> Iterator[StudySubscriptionEvent]:
        """
        Subscribe to a study to get notifications when a new sample is added or an investigation is created.
        Example:
            ```
            from adc_sdk.client import ADCClient
            adc = ADCClient(<api_token>)
            for notification in adc.subscribe_to_study(<study_id>):
                print(notification)
            ```
        Arguments:
            study_id: study id
        """
        variables = {"studyId": study_id}
        try:
            for result in self.ws_client.subscribe(
                queries.STUDY_SUBSCRIPTION.query, variable_values=variables
            ):
                yield StudySubscriptionEvent.parse_event(result['study'])
        except TransportQueryError as e:
            raise exceptions.ADCError(e.errors[0]["message"])

    def subscribe_to_investigation(self, investigation_id: str) -> Iterator[dict]:
        """
        Subscribe to an investigation to get notifications when a new job is created.
        Example:
            ```
            from adc_sdk.client import ADCClient
            adc = ADCClient(<api_token>)
            for notification in adc.subscribe_to_investigation(<study_id>):
                print(notification)
            ```
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
        Example:
            ```
            from adc_sdk.client import ADCClient
            adc = ADCClient(<api_token>)
            for notification in adc.subscribe_to_job(<study_id>):
                print(notification)
            ```
        Arguments:
            job_id: job id
        """
        variables = {"jobId": job_id}
        for result in self.ws_client.subscribe(
            queries.JOB_SUBSCRIPTION.query, variable_values=variables
        ):
            yield result

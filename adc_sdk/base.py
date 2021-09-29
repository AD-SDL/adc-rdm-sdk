from gql import Client
from gql.transport.exceptions import TransportQueryError
from aiohttp.client_exceptions import ClientConnectorError
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.websockets import WebsocketsTransport
from adc_sdk.exceptions import ADCError


class ADCBaseClient:
    def __init__(self, token: str):
        """
        Create an ADCBaseClient instance to interact with the API.
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
            response = self.client.execute(
                query_cls.query, variable_values=variables, upload_files=file_upload
            )
        except TransportQueryError as e:
            raise ADCError(e.errors[0]["message"])
        except ClientConnectorError:
            raise ADCError("Unable to connect to ADC servers.")
        return response[query_cls.path] if query_cls.path else response

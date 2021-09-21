"""Data models for the return types produced by the SDK"""
from datetime import datetime
from typing import Optional, List

import requests
from pydantic import BaseModel, Field, EmailStr, HttpUrl


def _remove_edgenode_syntax(data: dict) -> List[dict]:
    """Remove the edge-node syntax"""
    return [x['node'] for x in data['edges']]


class User(BaseModel):
    """Argonne Discovery Cloud user information"""

    id: str = Field(..., help='Unique identifier of the user')
    email: EmailStr = Field(..., help='Email address of the user')
    name: str = Field(..., help='Name of the user')
    globus_username: Optional[str] = Field(None, help='Globus username', alias='globusUsername')
    organization: Optional[str] = Field(None, help='Name of the organization to which this user belonds')
    created: Optional[datetime] = Field(None, help='Date when this user was created')
    updated: Optional[datetime] = Field(None, help='Latest time when user information was modified')


class Sample(BaseModel):
    """Single sample from a larger study"""

    id: str = Field(..., help='Unique identifier of the sample')
    name: str = Field(..., help='User-provided name of the sample. Need not be unique')
    keywords: List[str] = Field(default_factory=list, help='List of keywords that categorize a sample')
    url: HttpUrl = Field(..., help='File associated with this sample')
    created: datetime = Field(..., help='Date at which this sample was created')
    user: Optional[User] = Field(None, help='User who created this sample')

    def get_file(self) -> str:
        """Access the file associated with this sample

        Returns:
            The file content as a string
        """

        return requests.get(self.url).text


class Permission(BaseModel):
    """Permissions record"""

    user: User = Field(..., help='User information')
    level: str = Field(..., help='Level of access')  # TODO (wardlt): Enum for the level of access


# TODO (wardlt): Not sure what the investigation data model looks like yet
class Investigation(BaseModel):
    """A collection of studies"""
    class Config:
        extra = 'ignore'


class Study(BaseModel):
    """Single study from a larger investigation"""

    name: str = Field(..., help='User-provided name of the study')
    description: str = Field(..., help='Longer-form description of the study')
    keywords: List[str] = Field(default_factory=list, help='List of keywords that categorize a study')
    start_date: Optional[datetime] = Field(None, help='Date when the study began')
    created: datetime = Field(..., help='Date when this study record was created')
    updated: datetime = Field(..., help=' Latest date when this study record was created')
    permissions: List[Permission] = Field(default_factory=list, help='List of user permissions to access this study')
    investigations: List[dict] = Field(default_factory=list, help='List of investigations this study is part of')
    samples: List[Sample] = Field(default_factory=list, help='List of samples associated with this study')

    # TODO (wardlt): I'm presuming "edge/node" syntax is not meaningful to most users, so will strip it out
    @classmethod
    def parse_response(cls, response: dict) -> 'Study':
        """Construct record using the response from the ADC

        Removes

        Args:
            response: Response from the GraphQL service
        Returns:
            Representation of that response content
        """

        # We are going to change the values of keys, so we need will
        response = response.copy()

        # Convert samples, investigations and permissions to their respective data models
        for tag, dtype in [('samples', Sample), ('investigations', Investigation), ('permissions', Permission)]:
            response[tag] = [dtype.parse_obj(x) for x in _remove_edgenode_syntax(response[tag])]

        return cls.parse_obj(response)

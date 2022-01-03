"""Data models for the return types produced by the SDK"""
# TODO (wardlt): Perhaps break base formats into separate files from subscription and modification events?
from datetime import datetime
from typing import Optional, List

import requests
from pydantic import BaseModel, Field, EmailStr, HttpUrl, validator
from .references import StudyReference, InvestigationReference


def _remove_relay_syntax(data: dict) -> List[dict]:
    """Remove the "edge" and "node" syntax from API response introduced by relay"""
    return [x['node'] for x in data['edges']]


def parse_string_dates(cls, value):
    return datetime.strptime(
        value,
        "%Y-%m-%d"
    )


class User(BaseModel):
    """Argonne Discovery Cloud user information"""

    id: str = Field(..., help='Unique identifier of the user')
    email: EmailStr = Field(..., help='Email address of the user')
    name: str = Field(..., help='Name of the user')
    globus_username: Optional[str] = Field(None, help='Globus username', alias='globusUsername')
    organization: Optional[str] = Field(None, help='Name of the organization to which this user belonds')
    created: Optional[datetime] = Field(None, help='Date when this user was created')
    updated: Optional[datetime] = Field(None, help='Latest time when user information was modified')


class File(BaseModel):
    """Single file attachment for Samples"""

    id: str = Field(..., help='Unique identifier of the attachment record')
    name: str = Field(..., help='Name of the attachment')
    url: HttpUrl = Field(..., help='URL of the hosted attachment file')
    description: str = Field(None, help='Longer-form description of the attachment')

    def get_file(self, **kwargs) -> str:
        """Access the file associated with this attachment

        Keyword arguments are passed to requests.get

        Returns:
            The file content as a string
        """

        return requests.get(self.url, **kwargs).text


class ParentSample(BaseModel):
    """ Parent sample node """
    id: str = Field(..., help='Unique identifier of the parent sample')


class SampleSource(BaseModel):
    """Sample source information: type, company name, product url and product number"""

    type: str = Field(..., help='Sample type')
    company_name: str = Field(None, help='Name of the sample provider')
    product_url: str = Field(None, help='URL of the original sample (from the provider)')
    product_number: str = Field(None, help='Sample SKU')


class SampleLocation(BaseModel):
    """ Sample physical location"""
    building: str = Field(None, help='Building name')
    room: str = Field(None, help='Room')
    storage_unit: str = Field(None, help='Storage unit')
    sub_unit: str = Field(None, help='Sub unit')


class Sample(BaseModel):
    """Single sample from a larger study"""

    id: str = Field(..., help='Unique identifier of the sample')
    name: str = Field(..., help='User-provided name of the sample. Need not be unique')
    description: str = Field(..., help='User-provided description of the sample. Need not be unique')
    formula: str = Field(..., help='Formula of the sample')
    keywords: List[str] = Field(default_factory=list, help='List of keywords that categorize a sample')
    files: List[File] = Field(default_factory=list, help='List of files attached to the sample')
    created: datetime = Field(..., help='Date at which this sample was created')
    updated: datetime = Field(..., help='Date at which this sample record was last updated')
    user: Optional[User] = Field(None, help='User who created this sample')
    parent: ParentSample = Field(None, help='Parent sample node')
    source: SampleSource = Field(None, help='Sample source information')
    preparation_steps: List[str] = Field(default_factory=list, help='List of preparation steps for the sample')
    location: SampleLocation = Field(None, help='Sample location information')


class Permission(BaseModel):
    """Permissions record"""

    user: User = Field(..., help='User information')
    level: str = Field(..., help='Level of access')  # TODO (wardlt): Enum for the level of access


# TODO (wardlt): Not sure what the investigation data model looks like yet
class Investigation(BaseModel):
    """Single instanced investigations that arE part of a study"""

    id: str = Field(..., help='Unique identifier')
    name: str = Field(..., help='User-provided name')
    description: str = Field(None, help='Longer-form description')
    investigation_type: str = Field(..., alias='investigationType', help='Type of investigation')
    keywords: List[str] = Field(default_factory=list, help='List of keywords/tags')
    start_date: Optional[datetime] = Field(None, alias="startDate", help='Date when the investigation began')
    end_date: Optional[datetime] = Field(None, alias="startDate", help='Date when the investigation ended')
    created: datetime = Field(None, help='Date when this investigation record was created')
    updated: datetime = Field(None, help=' Latest date when this investigation record was created')
    user: User = Field(None, help='User who created this investigation')
    study: StudyReference = Field(None, help='Study the investigation belongs to')

    @validator("start_date", pre=True)
    def parse_start_date(cls, value):
        return parse_string_dates(cls, value)

    @validator("end_date", pre=True)
    def parse_end_date(cls, value):
        return parse_string_dates(cls, value)


class Study(BaseModel):
    """Larger entity containing multiple investigations"""

    id: str = Field(..., help='Unique identifier of the study')
    name: str = Field(..., help='User-provided name of the study')
    description: str = Field(None, help='Longer-form description of the study')
    keywords: List[str] = Field(default_factory=list, help='List of keywords that categorize a study')
    start_date: Optional[datetime] = Field(None, alias="startDate", help='Date when the study began')
    end_date: Optional[datetime] = Field(None, alias="endDate", help='Date when the study ended')
    created: datetime = Field(..., help='Date when this study record was created')
    updated: datetime = Field(..., help=' Latest date when this study record was created')
    permissions: List[Permission] = Field(default_factory=list, help='List of user permissions to access this study')
    investigations: List[dict] = Field(default_factory=list, help='List of investigations this study is part of')
    samples: List[Sample] = Field(default_factory=list, help='List of samples associated with this study')

    @classmethod
    def parse_response(cls, response: dict) -> 'Study':
        """Construct record using the response from the ADC

        Removes the "edge" and "node" syntax, which is not needed by SDK users.

        Args:
            response: Response from the ADC service
        Returns:
            Representation of that response content
        """

        # We are going to change the values of keys, so we need will
        response = response.copy()

        # Convert samples, investigations and permissions to their respective data models
        for tag, dtype in [('samples', Sample), ('investigations', InvestigationReference), ('permissions', Permission)]:
            response[tag] = [dtype.parse_obj(x) for x in _remove_relay_syntax(response[tag])]

        return cls.parse_obj(response)

    @validator("start_date", pre=True)
    def parse_start_date(cls, value):
        return parse_string_dates(cls, value)

    @validator("end_date", pre=True)
    def parse_end_date(cls, value):
        return parse_string_dates(cls, value)


class CreateSampleResponse(BaseModel):
    """Response for creating a sample"""

    success: bool = Field(..., help='Whether the creation was successful')
    sample: Optional[Sample] = Field(None, help='Metadata for the new sample')


class StudySubscriptionEvent(BaseModel):
    """Information provided when subscribing to a Study.

    Contains study information, the sample that was added, and the associated investigation.
    """

    study: Study = Field(..., help='Study from which the event originated')
    investigation: Optional[Investigation] = Field(None, help='Associated investigation')
    sample: Sample = Field(..., help='Sample that triggered this event.')
    source: Optional[str] = Field(..., help='Source of event. Format TBD')

    @classmethod
    def parse_event(cls, event: dict) -> 'StudySubscriptionEvent':
        """Parse the event record from ADC

        Removes the "edge" and "node" syntax, which is not needed by SDK users.

        Args:
            event: Raw event details from the ADC service
        Returns:
            Representation of the event details
        """

        # We are going to change some of the details
        event = event.copy()

        # Parse the study
        event['study'] = Study.parse_response(event['study'])

        return cls.parse_obj(event)

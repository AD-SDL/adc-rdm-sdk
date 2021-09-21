"""Data models for the return types produced by the SDK"""
from datetime import datetime
from typing import Optional, List

import requests
from pydantic import BaseModel, Field, EmailStr, HttpUrl


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
    user: User = Field(..., help='User who created this sample')

    def get_file(self) -> str:
        """Access the file associated with this sample

        Returns:
            The file content as a string
        """

        return requests.get(self.url).text

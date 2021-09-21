"""Data models for the return types produced by the SDK"""
from datetime import datetime

from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    """Single sample from a larger study"""

    id: str = Field(..., help='Unique identifier of the user')
    email: EmailStr = Field(..., help='Email address of the user')
    name: str = Field(..., help='Name of the user')
    globus_username: str = Field(..., help='Globus username', alias='globusUsername')
    organization: str = Field(..., help='Name of the organization to which this user belonds')
    created: datetime = Field(..., help='Date when this user was created')
    updated: datetime = Field(..., help='Latest time when user information was modified')

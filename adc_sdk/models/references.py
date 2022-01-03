from pydantic import BaseModel, Field
from datetime import datetime


class StudyReference(BaseModel):
    """Referenced Study"""

    id: str = Field(..., help='Unique identifier of the study')
    name: str = Field(..., help='User-provided name of the study')
    created: datetime = Field(..., help='Date when this study record was created')


class InvestigationReference(BaseModel):
    """Referenced Investigation"""

    id: str = Field(..., help='Unique identifier')
    name: str = Field(..., help='User-provided name')
    created: datetime = Field(..., help='Date when this investigation record was created')
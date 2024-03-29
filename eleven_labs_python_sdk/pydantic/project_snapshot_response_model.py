# coding: utf-8

"""
    ElevenLabs API Documentation

    This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://elevenlabs.io. Our API is experimental so all endpoints are subject to change.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel


class ProjectSnapshotResponseModel(BaseModel):
    project_snapshot_id: str = Field(alias='project_snapshot_id')

    project_id: str = Field(alias='project_id')

    created_at_unix: int = Field(alias='created_at_unix')

    name: str = Field(alias='name')
    class Config:
        arbitrary_types_allowed = True

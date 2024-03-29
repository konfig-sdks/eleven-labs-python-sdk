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

from eleven_labs_python_sdk.pydantic.dubbing_metadata_response_target_languages import DubbingMetadataResponseTargetLanguages

class DubbingMetadataResponse(BaseModel):
    dubbing_id: str = Field(alias='dubbing_id')

    name: str = Field(alias='name')

    status: str = Field(alias='status')

    error: str = Field(alias='error')

    target_languages: DubbingMetadataResponseTargetLanguages = Field(alias='target_languages')
    class Config:
        arbitrary_types_allowed = True

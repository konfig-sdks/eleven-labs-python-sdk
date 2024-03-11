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

from eleven_labs_python_sdk.type.chapter_response_model import ChapterResponseModel

class RequiredGetChaptersResponseModel(TypedDict):
    chapters: typing.List[ChapterResponseModel]

class OptionalGetChaptersResponseModel(TypedDict, total=False):
    pass

class GetChaptersResponseModel(RequiredGetChaptersResponseModel, OptionalGetChaptersResponseModel):
    pass

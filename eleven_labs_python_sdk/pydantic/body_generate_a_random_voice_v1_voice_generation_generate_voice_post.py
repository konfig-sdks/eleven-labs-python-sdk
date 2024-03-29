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


class BodyGenerateARandomVoiceV1VoiceGenerationGenerateVoicePost(BaseModel):
    # Category code corresponding to the gender of the generated voice. Possible values: female, male.
    gender: Literal["female", "male"] = Field(alias='gender')

    # Category code corresponding to the accent of the generated voice. Possible values: american, british, african, australian, indian.
    accent: str = Field(alias='accent')

    # Category code corresponding to the age of the generated voice. Possible values: young, middle_aged, old.
    age: Literal["young", "middle_aged", "old"] = Field(alias='age')

    # The strength of the accent of the generated voice. Has to be between 0.3 and 2.0.
    accent_strength: typing.Union[int, float] = Field(alias='accent_strength')

    # Text to generate, text length has to be between 100 and 1000.
    text: str = Field(alias='text')
    class Config:
        arbitrary_types_allowed = True

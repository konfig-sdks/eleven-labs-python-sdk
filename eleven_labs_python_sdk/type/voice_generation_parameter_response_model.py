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

from eleven_labs_python_sdk.type.voice_generation_parameter_option_response_model import VoiceGenerationParameterOptionResponseModel

class RequiredVoiceGenerationParameterResponseModel(TypedDict):
    genders: typing.List[VoiceGenerationParameterOptionResponseModel]

    accents: typing.List[VoiceGenerationParameterOptionResponseModel]

    ages: typing.List[VoiceGenerationParameterOptionResponseModel]

    minimum_characters: int

    maximum_characters: int

    minimum_accent_strength: typing.Union[int, float]

    maximum_accent_strength: typing.Union[int, float]

class OptionalVoiceGenerationParameterResponseModel(TypedDict, total=False):
    pass

class VoiceGenerationParameterResponseModel(RequiredVoiceGenerationParameterResponseModel, OptionalVoiceGenerationParameterResponseModel):
    pass
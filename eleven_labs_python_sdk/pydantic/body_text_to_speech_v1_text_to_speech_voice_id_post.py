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

from eleven_labs_python_sdk.pydantic.pronunciation_dictionary_version_locator_db_model import PronunciationDictionaryVersionLocatorDBModel
from eleven_labs_python_sdk.pydantic.voice_settings_response_model import VoiceSettingsResponseModel

class BodyTextToSpeechV1TextToSpeechVoiceIdPost(BaseModel):
    # The text that will get converted into speech.
    text: str = Field(alias='text')

    # Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.
    model_id_: typing.Optional[str] = Field(None, alias='model_id')

    # Voice settings overriding stored setttings for the given voice. They are applied only on the given request.
    voice_settings: typing.Optional[VoiceSettingsResponseModel] = Field(None, alias='voice_settings')

    # A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request
    pronunciation_dictionary_locators: typing.Optional[typing.List[PronunciationDictionaryVersionLocatorDBModel]] = Field(None, alias='pronunciation_dictionary_locators')
    class Config:
        arbitrary_types_allowed = True

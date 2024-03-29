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

from eleven_labs_python_sdk.pydantic.feedback_response_model import FeedbackResponseModel

class SpeechHistoryItemResponseModel(BaseModel):
    history_item_id: str = Field(alias='history_item_id')

    request_id: str = Field(alias='request_id')

    voice_id: str = Field(alias='voice_id')

    model_id_: str = Field(alias='model_id')

    voice_name: str = Field(alias='voice_name')

    voice_category: Literal["premade", "cloned", "generated", "professional"] = Field(alias='voice_category')

    text: str = Field(alias='text')

    date_unix: int = Field(alias='date_unix')

    character_count_change_from: int = Field(alias='character_count_change_from')

    character_count_change_to: int = Field(alias='character_count_change_to')

    content_type: str = Field(alias='content_type')

    state: Literal["created", "deleted", "processing"] = Field(alias='state')

    settings: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='settings')

    feedback: FeedbackResponseModel = Field(alias='feedback')

    share_link_id: str = Field(alias='share_link_id')

    source: Literal["TTS", "STS"] = Field(alias='source')
    class Config:
        arbitrary_types_allowed = True

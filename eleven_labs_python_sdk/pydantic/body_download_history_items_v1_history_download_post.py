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

from eleven_labs_python_sdk.pydantic.body_download_history_items_v1_history_download_post_history_item_ids import BodyDownloadHistoryItemsV1HistoryDownloadPostHistoryItemIds

class BodyDownloadHistoryItemsV1HistoryDownloadPost(BaseModel):
    history_item_ids: BodyDownloadHistoryItemsV1HistoryDownloadPostHistoryItemIds = Field(alias='history_item_ids')
    class Config:
        arbitrary_types_allowed = True

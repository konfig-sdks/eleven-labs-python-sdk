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


class RequiredBodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromFilePost(TypedDict):
    # The name of the pronunciation dictionary, used for identification only.
    name: str

class OptionalBodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromFilePost(TypedDict, total=False):
    # A description of the pronunciation dictionary, used for identification only.
    description: str

    # A lexicon .pls file which we will use to initialize the project with.
    file: typing.IO

class BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromFilePost(RequiredBodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromFilePost, OptionalBodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromFilePost):
    pass

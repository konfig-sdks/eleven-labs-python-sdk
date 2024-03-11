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


class RequiredBodyCreatesAudioNativeEnabledProjectV1AudioNativePost(TypedDict):
    # Project name.
    name: str

    # Either txt or HTML input file containing the article content. HTML should be formatted as follows '&lt;html&gt;&lt;body&gt;&lt;div&gt;&lt;p&gt;Your content&lt;/p&gt;&lt;h5&gt;More of your content&lt;/h5&gt;&lt;p&gt;Some more of your content&lt;/p&gt;&lt;/div&gt;&lt;/body&gt;&lt;/html&gt;'
    file: typing.IO

class OptionalBodyCreatesAudioNativeEnabledProjectV1AudioNativePost(TypedDict, total=False):
    # Title used in the player and inserted at the top of the uploaded article. If not provided, the default title set in the Player settings is used.
    title: str

    # Image URL used in the player. If not provided, default image set in the Player settings is used.
    image: str

    # Author used in the player and inserted at the start of the uploaded article. If not provided, the default author set in the Player settings is used.
    author: str

    # Whether to use small player or not. If not provided, default value set in the Player settings is used.
    small: bool

    # Text color used in the player. If not provided, default text color set in the Player settings is used.
    text_color: str

    # Background color used in the player. If not provided, default background color set in the Player settings is used.
    background_color: str

    # Specifies for how many minutes to persist the session across page reloads. If not provided, default sessionization set in the Player settings is used.
    sessionization: int

    # Voice ID used to voice the content. If not provided, default voice ID set in the Player settings is used.
    voice_id: str

    # TTS Model ID used in the player. If not provided, default model ID set in the Player settings is used.
    model_id: str

    # Whether to auto convert the project to audio or not.
    auto_convert: bool

class BodyCreatesAudioNativeEnabledProjectV1AudioNativePost(RequiredBodyCreatesAudioNativeEnabledProjectV1AudioNativePost, OptionalBodyCreatesAudioNativeEnabledProjectV1AudioNativePost):
    pass

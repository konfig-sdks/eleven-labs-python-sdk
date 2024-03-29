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


class RequiredBodyDubAVideoOrAnAudioFileV1DubbingPost(TypedDict):
    # Target language.
    target_lang: str

class OptionalBodyDubAVideoOrAnAudioFileV1DubbingPost(TypedDict, total=False):
    # automatic or manual.
    mode: str

    # One or more audio files to clone the voice from
    file: typing.IO

    # CSV file containing transcription/translation metadata
    csv_file: typing.IO

    # For use only with csv input
    foreground_audio_file: typing.IO

    # For use only with csv input
    background_audio_file: typing.IO

    # Name of the dubbing project.
    name: str

    # URL of the source video/audio file.
    source_url: str

    # Source language.
    source_lang: str

    # Number of speakers to use for the dubbing.
    num_speakers: int

    # Whether to apply watermark to the output video.
    watermark: bool

    # Start time of the source video/audio file.
    start_time: int

    # End time of the source video/audio file.
    end_time: int

    # Whether to use the highest resolution available.
    highest_resolution: bool

    # Whether to prepare dub for edits in dubbing studio.
    dubbing_studio: bool

class BodyDubAVideoOrAnAudioFileV1DubbingPost(RequiredBodyDubAVideoOrAnAudioFileV1DubbingPost, OptionalBodyDubAVideoOrAnAudioFileV1DubbingPost):
    pass

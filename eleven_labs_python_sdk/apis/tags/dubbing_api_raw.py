# coding: utf-8

"""
    ElevenLabs API Documentation

    This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://elevenlabs.io. Our API is experimental so all endpoints are subject to change.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from eleven_labs_python_sdk.paths.v1_dubbing_dubbing_id.delete import DeleteProjectRaw
from eleven_labs_python_sdk.paths.v1_dubbing.post import FileInLanguageRaw
from eleven_labs_python_sdk.paths.v1_dubbing_dubbing_id_audio_language_code.get import GetFileRaw
from eleven_labs_python_sdk.paths.v1_dubbing_dubbing_id.get import GetProjectMetadataRaw


class DubbingApiRaw(
    DeleteProjectRaw,
    FileInLanguageRaw,
    GetFileRaw,
    GetProjectMetadataRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass

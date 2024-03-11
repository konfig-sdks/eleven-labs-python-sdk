# coding: utf-8

"""
    ElevenLabs API Documentation

    This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://elevenlabs.io. Our API is experimental so all endpoints are subject to change.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from eleven_labs_python_sdk.paths.v1_audio_native.post import CreateProjectWithEmbeddableHtml
from eleven_labs_python_sdk.apis.tags.audio_native_api_raw import AudioNativeApiRaw


class AudioNativeApi(
    CreateProjectWithEmbeddableHtml,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AudioNativeApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AudioNativeApiRaw(api_client)

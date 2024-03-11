# coding: utf-8

"""
    ElevenLabs API Documentation

    This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://elevenlabs.io. Our API is experimental so all endpoints are subject to change.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from eleven_labs_python_sdk.paths.v1_voices_add_public_user_id_voice_id.post import AddToCollectionRaw
from eleven_labs_python_sdk.paths.v1_voices_add.post import AddVoiceToCollectionRaw
from eleven_labs_python_sdk.paths.v1_voices_voice_id.delete import DeleteByIdRaw
from eleven_labs_python_sdk.paths.v1_voices_voice_id_settings_edit.post import EditSettingsPostRaw
from eleven_labs_python_sdk.paths.v1_voices_settings_default.get import GetDefaultVoiceSettingsRaw
from eleven_labs_python_sdk.paths.v1_voices_voice_id_settings.get import GetSettingsRaw
from eleven_labs_python_sdk.paths.v1_shared_voices.get import GetSharedVoicesRaw
from eleven_labs_python_sdk.paths.v1_voices_voice_id.get import GetVoiceMetadataRaw
from eleven_labs_python_sdk.paths.v1_voices.get import ListAllVoicesRaw
from eleven_labs_python_sdk.paths.v1_voices_voice_id_edit.post import UpdateVoiceByIdRaw


class VoicesApiRaw(
    AddToCollectionRaw,
    AddVoiceToCollectionRaw,
    DeleteByIdRaw,
    EditSettingsPostRaw,
    GetDefaultVoiceSettingsRaw,
    GetSettingsRaw,
    GetSharedVoicesRaw,
    GetVoiceMetadataRaw,
    ListAllVoicesRaw,
    UpdateVoiceByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass

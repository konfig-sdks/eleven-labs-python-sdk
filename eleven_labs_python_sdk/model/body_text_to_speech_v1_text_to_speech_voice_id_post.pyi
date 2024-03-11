# coding: utf-8

"""
    ElevenLabs API Documentation

    This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://elevenlabs.io. Our API is experimental so all endpoints are subject to change.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from eleven_labs_python_sdk import schemas  # noqa: F401


class BodyTextToSpeechV1TextToSpeechVoiceIdPost(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "text",
        }
        
        class properties:
            text = schemas.StrSchema
            model_id = schemas.StrSchema
        
            @staticmethod
            def voice_settings() -> typing.Type['VoiceSettingsResponseModel']:
                return VoiceSettingsResponseModel
            
            
            class pronunciation_dictionary_locators(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PronunciationDictionaryVersionLocatorDBModel']:
                        return PronunciationDictionaryVersionLocatorDBModel
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PronunciationDictionaryVersionLocatorDBModel'], typing.List['PronunciationDictionaryVersionLocatorDBModel']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'pronunciation_dictionary_locators':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PronunciationDictionaryVersionLocatorDBModel':
                    return super().__getitem__(i)
            __annotations__ = {
                "text": text,
                "model_id": model_id,
                "voice_settings": voice_settings,
                "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
            }
    
    text: MetaOapg.properties.text
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model_id"]) -> MetaOapg.properties.model_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voice_settings"]) -> 'VoiceSettingsResponseModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pronunciation_dictionary_locators"]) -> MetaOapg.properties.pronunciation_dictionary_locators: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["text", "model_id", "voice_settings", "pronunciation_dictionary_locators", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model_id"]) -> typing.Union[MetaOapg.properties.model_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voice_settings"]) -> typing.Union['VoiceSettingsResponseModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pronunciation_dictionary_locators"]) -> typing.Union[MetaOapg.properties.pronunciation_dictionary_locators, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["text", "model_id", "voice_settings", "pronunciation_dictionary_locators", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        text: typing.Union[MetaOapg.properties.text, str, ],
        model_id: typing.Union[MetaOapg.properties.model_id, str, schemas.Unset] = schemas.unset,
        voice_settings: typing.Union['VoiceSettingsResponseModel', schemas.Unset] = schemas.unset,
        pronunciation_dictionary_locators: typing.Union[MetaOapg.properties.pronunciation_dictionary_locators, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BodyTextToSpeechV1TextToSpeechVoiceIdPost':
        return super().__new__(
            cls,
            *args,
            text=text,
            model_id=model_id,
            voice_settings=voice_settings,
            pronunciation_dictionary_locators=pronunciation_dictionary_locators,
            _configuration=_configuration,
            **kwargs,
        )

from eleven_labs_python_sdk.model.pronunciation_dictionary_version_locator_db_model import PronunciationDictionaryVersionLocatorDBModel
from eleven_labs_python_sdk.model.voice_settings_response_model import VoiceSettingsResponseModel

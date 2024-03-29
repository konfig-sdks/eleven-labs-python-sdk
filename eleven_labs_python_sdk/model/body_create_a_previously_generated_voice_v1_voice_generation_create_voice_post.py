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


class BodyCreateAPreviouslyGeneratedVoiceV1VoiceGenerationCreateVoicePost(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "generated_voice_id",
            "voice_name",
            "voice_description",
        }
        
        class properties:
            voice_name = schemas.StrSchema
            voice_description = schemas.StrSchema
            generated_voice_id = schemas.StrSchema
        
            @staticmethod
            def labels() -> typing.Type['BodyCreateAPreviouslyGeneratedVoiceV1VoiceGenerationCreateVoicePostLabels']:
                return BodyCreateAPreviouslyGeneratedVoiceV1VoiceGenerationCreateVoicePostLabels
            __annotations__ = {
                "voice_name": voice_name,
                "voice_description": voice_description,
                "generated_voice_id": generated_voice_id,
                "labels": labels,
            }
    
    generated_voice_id: MetaOapg.properties.generated_voice_id
    voice_name: MetaOapg.properties.voice_name
    voice_description: MetaOapg.properties.voice_description
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voice_name"]) -> MetaOapg.properties.voice_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voice_description"]) -> MetaOapg.properties.voice_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["generated_voice_id"]) -> MetaOapg.properties.generated_voice_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["labels"]) -> 'BodyCreateAPreviouslyGeneratedVoiceV1VoiceGenerationCreateVoicePostLabels': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["voice_name", "voice_description", "generated_voice_id", "labels", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voice_name"]) -> MetaOapg.properties.voice_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voice_description"]) -> MetaOapg.properties.voice_description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["generated_voice_id"]) -> MetaOapg.properties.generated_voice_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["labels"]) -> typing.Union['BodyCreateAPreviouslyGeneratedVoiceV1VoiceGenerationCreateVoicePostLabels', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["voice_name", "voice_description", "generated_voice_id", "labels", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        generated_voice_id: typing.Union[MetaOapg.properties.generated_voice_id, str, ],
        voice_name: typing.Union[MetaOapg.properties.voice_name, str, ],
        voice_description: typing.Union[MetaOapg.properties.voice_description, str, ],
        labels: typing.Union['BodyCreateAPreviouslyGeneratedVoiceV1VoiceGenerationCreateVoicePostLabels', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BodyCreateAPreviouslyGeneratedVoiceV1VoiceGenerationCreateVoicePost':
        return super().__new__(
            cls,
            *args,
            generated_voice_id=generated_voice_id,
            voice_name=voice_name,
            voice_description=voice_description,
            labels=labels,
            _configuration=_configuration,
            **kwargs,
        )

from eleven_labs_python_sdk.model.body_create_a_previously_generated_voice_v1_voice_generation_create_voice_post_labels import BodyCreateAPreviouslyGeneratedVoiceV1VoiceGenerationCreateVoicePostLabels

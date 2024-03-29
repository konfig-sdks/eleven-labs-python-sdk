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


class VoiceSettingsResponseModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "similarity_boost",
            "stability",
        }
        
        class properties:
            stability = schemas.NumberSchema
            similarity_boost = schemas.NumberSchema
            style = schemas.NumberSchema
            use_speaker_boost = schemas.BoolSchema
            __annotations__ = {
                "stability": stability,
                "similarity_boost": similarity_boost,
                "style": style,
                "use_speaker_boost": use_speaker_boost,
            }
    
    similarity_boost: MetaOapg.properties.similarity_boost
    stability: MetaOapg.properties.stability
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stability"]) -> MetaOapg.properties.stability: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["similarity_boost"]) -> MetaOapg.properties.similarity_boost: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["style"]) -> MetaOapg.properties.style: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["use_speaker_boost"]) -> MetaOapg.properties.use_speaker_boost: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["stability", "similarity_boost", "style", "use_speaker_boost", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stability"]) -> MetaOapg.properties.stability: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["similarity_boost"]) -> MetaOapg.properties.similarity_boost: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["style"]) -> typing.Union[MetaOapg.properties.style, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["use_speaker_boost"]) -> typing.Union[MetaOapg.properties.use_speaker_boost, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["stability", "similarity_boost", "style", "use_speaker_boost", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        similarity_boost: typing.Union[MetaOapg.properties.similarity_boost, decimal.Decimal, int, float, ],
        stability: typing.Union[MetaOapg.properties.stability, decimal.Decimal, int, float, ],
        style: typing.Union[MetaOapg.properties.style, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        use_speaker_boost: typing.Union[MetaOapg.properties.use_speaker_boost, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VoiceSettingsResponseModel':
        return super().__new__(
            cls,
            *args,
            similarity_boost=similarity_boost,
            stability=stability,
            style=style,
            use_speaker_boost=use_speaker_boost,
            _configuration=_configuration,
            **kwargs,
        )

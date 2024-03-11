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


class BodyGenerateARandomVoiceV1VoiceGenerationGenerateVoicePost(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "gender",
            "accent_strength",
            "text",
            "accent",
            "age",
        }
        
        class properties:
            
            
            class gender(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def FEMALE(cls):
                    return cls("female")
                
                @schemas.classproperty
                def MALE(cls):
                    return cls("male")
            accent = schemas.StrSchema
            
            
            class age(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def YOUNG(cls):
                    return cls("young")
                
                @schemas.classproperty
                def MIDDLE_AGED(cls):
                    return cls("middle_aged")
                
                @schemas.classproperty
                def OLD(cls):
                    return cls("old")
            accent_strength = schemas.NumberSchema
            text = schemas.StrSchema
            __annotations__ = {
                "gender": gender,
                "accent": accent,
                "age": age,
                "accent_strength": accent_strength,
                "text": text,
            }
    
    gender: MetaOapg.properties.gender
    accent_strength: MetaOapg.properties.accent_strength
    text: MetaOapg.properties.text
    accent: MetaOapg.properties.accent
    age: MetaOapg.properties.age
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gender"]) -> MetaOapg.properties.gender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accent"]) -> MetaOapg.properties.accent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["age"]) -> MetaOapg.properties.age: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accent_strength"]) -> MetaOapg.properties.accent_strength: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["gender", "accent", "age", "accent_strength", "text", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gender"]) -> MetaOapg.properties.gender: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accent"]) -> MetaOapg.properties.accent: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["age"]) -> MetaOapg.properties.age: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accent_strength"]) -> MetaOapg.properties.accent_strength: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["gender", "accent", "age", "accent_strength", "text", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        gender: typing.Union[MetaOapg.properties.gender, str, ],
        accent_strength: typing.Union[MetaOapg.properties.accent_strength, decimal.Decimal, int, float, ],
        text: typing.Union[MetaOapg.properties.text, str, ],
        accent: typing.Union[MetaOapg.properties.accent, str, ],
        age: typing.Union[MetaOapg.properties.age, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BodyGenerateARandomVoiceV1VoiceGenerationGenerateVoicePost':
        return super().__new__(
            cls,
            *args,
            gender=gender,
            accent_strength=accent_strength,
            text=text,
            accent=accent,
            age=age,
            _configuration=_configuration,
            **kwargs,
        )
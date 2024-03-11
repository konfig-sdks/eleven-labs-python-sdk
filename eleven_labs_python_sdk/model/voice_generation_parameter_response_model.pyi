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


class VoiceGenerationParameterResponseModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "accents",
            "minimum_characters",
            "ages",
            "genders",
            "minimum_accent_strength",
            "maximum_accent_strength",
            "maximum_characters",
        }
        
        class properties:
            
            
            class genders(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['VoiceGenerationParameterOptionResponseModel']:
                        return VoiceGenerationParameterOptionResponseModel
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['VoiceGenerationParameterOptionResponseModel'], typing.List['VoiceGenerationParameterOptionResponseModel']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'genders':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'VoiceGenerationParameterOptionResponseModel':
                    return super().__getitem__(i)
            
            
            class accents(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['VoiceGenerationParameterOptionResponseModel']:
                        return VoiceGenerationParameterOptionResponseModel
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['VoiceGenerationParameterOptionResponseModel'], typing.List['VoiceGenerationParameterOptionResponseModel']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'accents':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'VoiceGenerationParameterOptionResponseModel':
                    return super().__getitem__(i)
            
            
            class ages(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['VoiceGenerationParameterOptionResponseModel']:
                        return VoiceGenerationParameterOptionResponseModel
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['VoiceGenerationParameterOptionResponseModel'], typing.List['VoiceGenerationParameterOptionResponseModel']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ages':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'VoiceGenerationParameterOptionResponseModel':
                    return super().__getitem__(i)
            minimum_characters = schemas.IntSchema
            maximum_characters = schemas.IntSchema
            minimum_accent_strength = schemas.NumberSchema
            maximum_accent_strength = schemas.NumberSchema
            __annotations__ = {
                "genders": genders,
                "accents": accents,
                "ages": ages,
                "minimum_characters": minimum_characters,
                "maximum_characters": maximum_characters,
                "minimum_accent_strength": minimum_accent_strength,
                "maximum_accent_strength": maximum_accent_strength,
            }
    
    accents: MetaOapg.properties.accents
    minimum_characters: MetaOapg.properties.minimum_characters
    ages: MetaOapg.properties.ages
    genders: MetaOapg.properties.genders
    minimum_accent_strength: MetaOapg.properties.minimum_accent_strength
    maximum_accent_strength: MetaOapg.properties.maximum_accent_strength
    maximum_characters: MetaOapg.properties.maximum_characters
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["genders"]) -> MetaOapg.properties.genders: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accents"]) -> MetaOapg.properties.accents: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ages"]) -> MetaOapg.properties.ages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minimum_characters"]) -> MetaOapg.properties.minimum_characters: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maximum_characters"]) -> MetaOapg.properties.maximum_characters: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minimum_accent_strength"]) -> MetaOapg.properties.minimum_accent_strength: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maximum_accent_strength"]) -> MetaOapg.properties.maximum_accent_strength: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["genders", "accents", "ages", "minimum_characters", "maximum_characters", "minimum_accent_strength", "maximum_accent_strength", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["genders"]) -> MetaOapg.properties.genders: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accents"]) -> MetaOapg.properties.accents: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ages"]) -> MetaOapg.properties.ages: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minimum_characters"]) -> MetaOapg.properties.minimum_characters: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maximum_characters"]) -> MetaOapg.properties.maximum_characters: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minimum_accent_strength"]) -> MetaOapg.properties.minimum_accent_strength: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maximum_accent_strength"]) -> MetaOapg.properties.maximum_accent_strength: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["genders", "accents", "ages", "minimum_characters", "maximum_characters", "minimum_accent_strength", "maximum_accent_strength", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        accents: typing.Union[MetaOapg.properties.accents, list, tuple, ],
        minimum_characters: typing.Union[MetaOapg.properties.minimum_characters, decimal.Decimal, int, ],
        ages: typing.Union[MetaOapg.properties.ages, list, tuple, ],
        genders: typing.Union[MetaOapg.properties.genders, list, tuple, ],
        minimum_accent_strength: typing.Union[MetaOapg.properties.minimum_accent_strength, decimal.Decimal, int, float, ],
        maximum_accent_strength: typing.Union[MetaOapg.properties.maximum_accent_strength, decimal.Decimal, int, float, ],
        maximum_characters: typing.Union[MetaOapg.properties.maximum_characters, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VoiceGenerationParameterResponseModel':
        return super().__new__(
            cls,
            *args,
            accents=accents,
            minimum_characters=minimum_characters,
            ages=ages,
            genders=genders,
            minimum_accent_strength=minimum_accent_strength,
            maximum_accent_strength=maximum_accent_strength,
            maximum_characters=maximum_characters,
            _configuration=_configuration,
            **kwargs,
        )

from eleven_labs_python_sdk.model.voice_generation_parameter_option_response_model import VoiceGenerationParameterOptionResponseModel

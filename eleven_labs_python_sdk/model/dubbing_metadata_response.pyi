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


class DubbingMetadataResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "target_languages",
            "name",
            "error",
            "dubbing_id",
            "status",
        }
        
        class properties:
            dubbing_id = schemas.StrSchema
            name = schemas.StrSchema
            status = schemas.StrSchema
            error = schemas.StrSchema
        
            @staticmethod
            def target_languages() -> typing.Type['DubbingMetadataResponseTargetLanguages']:
                return DubbingMetadataResponseTargetLanguages
            __annotations__ = {
                "dubbing_id": dubbing_id,
                "name": name,
                "status": status,
                "error": error,
                "target_languages": target_languages,
            }
    
    target_languages: 'DubbingMetadataResponseTargetLanguages'
    name: MetaOapg.properties.name
    error: MetaOapg.properties.error
    dubbing_id: MetaOapg.properties.dubbing_id
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dubbing_id"]) -> MetaOapg.properties.dubbing_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target_languages"]) -> 'DubbingMetadataResponseTargetLanguages': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["dubbing_id", "name", "status", "error", "target_languages", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dubbing_id"]) -> MetaOapg.properties.dubbing_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target_languages"]) -> 'DubbingMetadataResponseTargetLanguages': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["dubbing_id", "name", "status", "error", "target_languages", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        target_languages: 'DubbingMetadataResponseTargetLanguages',
        name: typing.Union[MetaOapg.properties.name, str, ],
        error: typing.Union[MetaOapg.properties.error, str, ],
        dubbing_id: typing.Union[MetaOapg.properties.dubbing_id, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DubbingMetadataResponse':
        return super().__new__(
            cls,
            *args,
            target_languages=target_languages,
            name=name,
            error=error,
            dubbing_id=dubbing_id,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from eleven_labs_python_sdk.model.dubbing_metadata_response_target_languages import DubbingMetadataResponseTargetLanguages

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


class AddPronunciationDictionaryResponseModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "creation_time_unix",
            "name",
            "id",
            "version_id",
            "created_by",
        }
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            created_by = schemas.StrSchema
            creation_time_unix = schemas.IntSchema
            version_id = schemas.StrSchema
            description = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "created_by": created_by,
                "creation_time_unix": creation_time_unix,
                "version_id": version_id,
                "description": description,
            }
    
    creation_time_unix: MetaOapg.properties.creation_time_unix
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    version_id: MetaOapg.properties.version_id
    created_by: MetaOapg.properties.created_by
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_by"]) -> MetaOapg.properties.created_by: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creation_time_unix"]) -> MetaOapg.properties.creation_time_unix: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version_id"]) -> MetaOapg.properties.version_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "created_by", "creation_time_unix", "version_id", "description", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_by"]) -> MetaOapg.properties.created_by: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creation_time_unix"]) -> MetaOapg.properties.creation_time_unix: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version_id"]) -> MetaOapg.properties.version_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "created_by", "creation_time_unix", "version_id", "description", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        creation_time_unix: typing.Union[MetaOapg.properties.creation_time_unix, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        version_id: typing.Union[MetaOapg.properties.version_id, str, ],
        created_by: typing.Union[MetaOapg.properties.created_by, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AddPronunciationDictionaryResponseModel':
        return super().__new__(
            cls,
            *args,
            creation_time_unix=creation_time_unix,
            name=name,
            id=id,
            version_id=version_id,
            created_by=created_by,
            description=description,
            _configuration=_configuration,
            **kwargs,
        )
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


class ChapterSnapshotResponseModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "project_id",
            "name",
            "created_at_unix",
            "chapter_id",
            "chapter_snapshot_id",
        }
        
        class properties:
            chapter_snapshot_id = schemas.StrSchema
            project_id = schemas.StrSchema
            chapter_id = schemas.StrSchema
            created_at_unix = schemas.IntSchema
            name = schemas.StrSchema
            __annotations__ = {
                "chapter_snapshot_id": chapter_snapshot_id,
                "project_id": project_id,
                "chapter_id": chapter_id,
                "created_at_unix": created_at_unix,
                "name": name,
            }
    
    project_id: MetaOapg.properties.project_id
    name: MetaOapg.properties.name
    created_at_unix: MetaOapg.properties.created_at_unix
    chapter_id: MetaOapg.properties.chapter_id
    chapter_snapshot_id: MetaOapg.properties.chapter_snapshot_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chapter_snapshot_id"]) -> MetaOapg.properties.chapter_snapshot_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project_id"]) -> MetaOapg.properties.project_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chapter_id"]) -> MetaOapg.properties.chapter_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at_unix"]) -> MetaOapg.properties.created_at_unix: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["chapter_snapshot_id", "project_id", "chapter_id", "created_at_unix", "name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chapter_snapshot_id"]) -> MetaOapg.properties.chapter_snapshot_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project_id"]) -> MetaOapg.properties.project_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chapter_id"]) -> MetaOapg.properties.chapter_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at_unix"]) -> MetaOapg.properties.created_at_unix: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["chapter_snapshot_id", "project_id", "chapter_id", "created_at_unix", "name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        project_id: typing.Union[MetaOapg.properties.project_id, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        created_at_unix: typing.Union[MetaOapg.properties.created_at_unix, decimal.Decimal, int, ],
        chapter_id: typing.Union[MetaOapg.properties.chapter_id, str, ],
        chapter_snapshot_id: typing.Union[MetaOapg.properties.chapter_snapshot_id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ChapterSnapshotResponseModel':
        return super().__new__(
            cls,
            *args,
            project_id=project_id,
            name=name,
            created_at_unix=created_at_unix,
            chapter_id=chapter_id,
            chapter_snapshot_id=chapter_snapshot_id,
            _configuration=_configuration,
            **kwargs,
        )

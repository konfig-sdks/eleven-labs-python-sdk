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


class GetChaptersResponseModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "chapters",
        }
        
        class properties:
            
            
            class chapters(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ChapterResponseModel']:
                        return ChapterResponseModel
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ChapterResponseModel'], typing.List['ChapterResponseModel']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'chapters':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ChapterResponseModel':
                    return super().__getitem__(i)
            __annotations__ = {
                "chapters": chapters,
            }
    
    chapters: MetaOapg.properties.chapters
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chapters"]) -> MetaOapg.properties.chapters: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["chapters", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chapters"]) -> MetaOapg.properties.chapters: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["chapters", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        chapters: typing.Union[MetaOapg.properties.chapters, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GetChaptersResponseModel':
        return super().__new__(
            cls,
            *args,
            chapters=chapters,
            _configuration=_configuration,
            **kwargs,
        )

from eleven_labs_python_sdk.model.chapter_response_model import ChapterResponseModel
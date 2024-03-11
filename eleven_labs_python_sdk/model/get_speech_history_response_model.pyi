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


class GetSpeechHistoryResponseModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "last_history_item_id",
            "has_more",
            "history",
        }
        
        class properties:
            
            
            class history(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SpeechHistoryItemResponseModel']:
                        return SpeechHistoryItemResponseModel
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['SpeechHistoryItemResponseModel'], typing.List['SpeechHistoryItemResponseModel']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'history':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SpeechHistoryItemResponseModel':
                    return super().__getitem__(i)
            last_history_item_id = schemas.StrSchema
            has_more = schemas.BoolSchema
            __annotations__ = {
                "history": history,
                "last_history_item_id": last_history_item_id,
                "has_more": has_more,
            }
    
    last_history_item_id: MetaOapg.properties.last_history_item_id
    has_more: MetaOapg.properties.has_more
    history: MetaOapg.properties.history
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["history"]) -> MetaOapg.properties.history: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_history_item_id"]) -> MetaOapg.properties.last_history_item_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_more"]) -> MetaOapg.properties.has_more: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["history", "last_history_item_id", "has_more", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["history"]) -> MetaOapg.properties.history: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_history_item_id"]) -> MetaOapg.properties.last_history_item_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_more"]) -> MetaOapg.properties.has_more: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["history", "last_history_item_id", "has_more", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        last_history_item_id: typing.Union[MetaOapg.properties.last_history_item_id, str, ],
        has_more: typing.Union[MetaOapg.properties.has_more, bool, ],
        history: typing.Union[MetaOapg.properties.history, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GetSpeechHistoryResponseModel':
        return super().__new__(
            cls,
            *args,
            last_history_item_id=last_history_item_id,
            has_more=has_more,
            history=history,
            _configuration=_configuration,
            **kwargs,
        )

from eleven_labs_python_sdk.model.speech_history_item_response_model import SpeechHistoryItemResponseModel
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


class VerificationAttemptResponseModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "date_unix",
            "levenshtein_distance",
            "similarity",
            "accepted",
            "text",
        }
        
        class properties:
            text = schemas.StrSchema
            date_unix = schemas.IntSchema
            accepted = schemas.BoolSchema
            similarity = schemas.NumberSchema
            levenshtein_distance = schemas.NumberSchema
        
            @staticmethod
            def recording() -> typing.Type['RecordingResponseModel']:
                return RecordingResponseModel
            __annotations__ = {
                "text": text,
                "date_unix": date_unix,
                "accepted": accepted,
                "similarity": similarity,
                "levenshtein_distance": levenshtein_distance,
                "recording": recording,
            }
    
    date_unix: MetaOapg.properties.date_unix
    levenshtein_distance: MetaOapg.properties.levenshtein_distance
    similarity: MetaOapg.properties.similarity
    accepted: MetaOapg.properties.accepted
    text: MetaOapg.properties.text
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_unix"]) -> MetaOapg.properties.date_unix: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accepted"]) -> MetaOapg.properties.accepted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["similarity"]) -> MetaOapg.properties.similarity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["levenshtein_distance"]) -> MetaOapg.properties.levenshtein_distance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recording"]) -> 'RecordingResponseModel': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["text", "date_unix", "accepted", "similarity", "levenshtein_distance", "recording", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_unix"]) -> MetaOapg.properties.date_unix: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accepted"]) -> MetaOapg.properties.accepted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["similarity"]) -> MetaOapg.properties.similarity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["levenshtein_distance"]) -> MetaOapg.properties.levenshtein_distance: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recording"]) -> typing.Union['RecordingResponseModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["text", "date_unix", "accepted", "similarity", "levenshtein_distance", "recording", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        date_unix: typing.Union[MetaOapg.properties.date_unix, decimal.Decimal, int, ],
        levenshtein_distance: typing.Union[MetaOapg.properties.levenshtein_distance, decimal.Decimal, int, float, ],
        similarity: typing.Union[MetaOapg.properties.similarity, decimal.Decimal, int, float, ],
        accepted: typing.Union[MetaOapg.properties.accepted, bool, ],
        text: typing.Union[MetaOapg.properties.text, str, ],
        recording: typing.Union['RecordingResponseModel', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VerificationAttemptResponseModel':
        return super().__new__(
            cls,
            *args,
            date_unix=date_unix,
            levenshtein_distance=levenshtein_distance,
            similarity=similarity,
            accepted=accepted,
            text=text,
            recording=recording,
            _configuration=_configuration,
            **kwargs,
        )

from eleven_labs_python_sdk.model.recording_response_model import RecordingResponseModel
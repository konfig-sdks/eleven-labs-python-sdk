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


class BodyCreatesAudioNativeEnabledProjectV1AudioNativePost(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "file",
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            file = schemas.BinarySchema
            title = schemas.StrSchema
            image = schemas.StrSchema
            author = schemas.StrSchema
            small = schemas.BoolSchema
            text_color = schemas.StrSchema
            background_color = schemas.StrSchema
            sessionization = schemas.IntSchema
            voice_id = schemas.StrSchema
            model_id = schemas.StrSchema
            auto_convert = schemas.BoolSchema
            __annotations__ = {
                "name": name,
                "file": file,
                "title": title,
                "image": image,
                "author": author,
                "small": small,
                "text_color": text_color,
                "background_color": background_color,
                "sessionization": sessionization,
                "voice_id": voice_id,
                "model_id": model_id,
                "auto_convert": auto_convert,
            }
    
    file: MetaOapg.properties.file
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file"]) -> MetaOapg.properties.file: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["author"]) -> MetaOapg.properties.author: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["small"]) -> MetaOapg.properties.small: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["text_color"]) -> MetaOapg.properties.text_color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["background_color"]) -> MetaOapg.properties.background_color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sessionization"]) -> MetaOapg.properties.sessionization: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voice_id"]) -> MetaOapg.properties.voice_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model_id"]) -> MetaOapg.properties.model_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_convert"]) -> MetaOapg.properties.auto_convert: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "file", "title", "image", "author", "small", "text_color", "background_color", "sessionization", "voice_id", "model_id", "auto_convert", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file"]) -> MetaOapg.properties.file: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image"]) -> typing.Union[MetaOapg.properties.image, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["author"]) -> typing.Union[MetaOapg.properties.author, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["small"]) -> typing.Union[MetaOapg.properties.small, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["text_color"]) -> typing.Union[MetaOapg.properties.text_color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["background_color"]) -> typing.Union[MetaOapg.properties.background_color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sessionization"]) -> typing.Union[MetaOapg.properties.sessionization, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voice_id"]) -> typing.Union[MetaOapg.properties.voice_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model_id"]) -> typing.Union[MetaOapg.properties.model_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_convert"]) -> typing.Union[MetaOapg.properties.auto_convert, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "file", "title", "image", "author", "small", "text_color", "background_color", "sessionization", "voice_id", "model_id", "auto_convert", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        file: typing.Union[MetaOapg.properties.file, bytes, io.FileIO, io.BufferedReader, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        image: typing.Union[MetaOapg.properties.image, str, schemas.Unset] = schemas.unset,
        author: typing.Union[MetaOapg.properties.author, str, schemas.Unset] = schemas.unset,
        small: typing.Union[MetaOapg.properties.small, bool, schemas.Unset] = schemas.unset,
        text_color: typing.Union[MetaOapg.properties.text_color, str, schemas.Unset] = schemas.unset,
        background_color: typing.Union[MetaOapg.properties.background_color, str, schemas.Unset] = schemas.unset,
        sessionization: typing.Union[MetaOapg.properties.sessionization, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        voice_id: typing.Union[MetaOapg.properties.voice_id, str, schemas.Unset] = schemas.unset,
        model_id: typing.Union[MetaOapg.properties.model_id, str, schemas.Unset] = schemas.unset,
        auto_convert: typing.Union[MetaOapg.properties.auto_convert, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BodyCreatesAudioNativeEnabledProjectV1AudioNativePost':
        return super().__new__(
            cls,
            *args,
            file=file,
            name=name,
            title=title,
            image=image,
            author=author,
            small=small,
            text_color=text_color,
            background_color=background_color,
            sessionization=sessionization,
            voice_id=voice_id,
            model_id=model_id,
            auto_convert=auto_convert,
            _configuration=_configuration,
            **kwargs,
        )
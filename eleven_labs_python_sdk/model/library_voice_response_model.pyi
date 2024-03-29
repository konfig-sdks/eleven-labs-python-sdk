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


class LibraryVoiceResponseModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "featured",
            "gender",
            "usage_character_count_1y",
            "twitter_username",
            "description",
            "language",
            "public_owner_id",
            "date_unix",
            "rate",
            "cloned_by_count",
            "free_users_allowed",
            "instagram_username",
            "live_moderation_enabled",
            "youtube_username",
            "voice_id",
            "tiktok_username",
            "accent",
            "use_case",
            "preview_url",
            "name",
            "descriptive",
            "usage_character_count_7d",
            "category",
            "notice_period",
            "age",
        }
        
        class properties:
            description = schemas.StrSchema
            public_owner_id = schemas.StrSchema
            voice_id = schemas.StrSchema
            date_unix = schemas.IntSchema
            name = schemas.StrSchema
            accent = schemas.StrSchema
            gender = schemas.StrSchema
            age = schemas.StrSchema
            descriptive = schemas.StrSchema
            use_case = schemas.StrSchema
            category = schemas.StrSchema
            language = schemas.StrSchema
            preview_url = schemas.StrSchema
            usage_character_count_1y = schemas.IntSchema
            usage_character_count_7d = schemas.IntSchema
            cloned_by_count = schemas.IntSchema
            rate = schemas.NumberSchema
            free_users_allowed = schemas.BoolSchema
            live_moderation_enabled = schemas.BoolSchema
            notice_period = schemas.IntSchema
            instagram_username = schemas.StrSchema
            twitter_username = schemas.StrSchema
            youtube_username = schemas.StrSchema
            tiktok_username = schemas.StrSchema
            featured = schemas.BoolSchema
            __annotations__ = {
                "description": description,
                "public_owner_id": public_owner_id,
                "voice_id": voice_id,
                "date_unix": date_unix,
                "name": name,
                "accent": accent,
                "gender": gender,
                "age": age,
                "descriptive": descriptive,
                "use_case": use_case,
                "category": category,
                "language": language,
                "preview_url": preview_url,
                "usage_character_count_1y": usage_character_count_1y,
                "usage_character_count_7d": usage_character_count_7d,
                "cloned_by_count": cloned_by_count,
                "rate": rate,
                "free_users_allowed": free_users_allowed,
                "live_moderation_enabled": live_moderation_enabled,
                "notice_period": notice_period,
                "instagram_username": instagram_username,
                "twitter_username": twitter_username,
                "youtube_username": youtube_username,
                "tiktok_username": tiktok_username,
                "featured": featured,
            }
    
    featured: MetaOapg.properties.featured
    gender: MetaOapg.properties.gender
    usage_character_count_1y: MetaOapg.properties.usage_character_count_1y
    twitter_username: MetaOapg.properties.twitter_username
    description: MetaOapg.properties.description
    language: MetaOapg.properties.language
    public_owner_id: MetaOapg.properties.public_owner_id
    date_unix: MetaOapg.properties.date_unix
    rate: MetaOapg.properties.rate
    cloned_by_count: MetaOapg.properties.cloned_by_count
    free_users_allowed: MetaOapg.properties.free_users_allowed
    instagram_username: MetaOapg.properties.instagram_username
    live_moderation_enabled: MetaOapg.properties.live_moderation_enabled
    youtube_username: MetaOapg.properties.youtube_username
    voice_id: MetaOapg.properties.voice_id
    tiktok_username: MetaOapg.properties.tiktok_username
    accent: MetaOapg.properties.accent
    use_case: MetaOapg.properties.use_case
    preview_url: MetaOapg.properties.preview_url
    name: MetaOapg.properties.name
    descriptive: MetaOapg.properties.descriptive
    usage_character_count_7d: MetaOapg.properties.usage_character_count_7d
    category: MetaOapg.properties.category
    notice_period: MetaOapg.properties.notice_period
    age: MetaOapg.properties.age
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["public_owner_id"]) -> MetaOapg.properties.public_owner_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voice_id"]) -> MetaOapg.properties.voice_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_unix"]) -> MetaOapg.properties.date_unix: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accent"]) -> MetaOapg.properties.accent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gender"]) -> MetaOapg.properties.gender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["age"]) -> MetaOapg.properties.age: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["descriptive"]) -> MetaOapg.properties.descriptive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["use_case"]) -> MetaOapg.properties.use_case: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["language"]) -> MetaOapg.properties.language: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preview_url"]) -> MetaOapg.properties.preview_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usage_character_count_1y"]) -> MetaOapg.properties.usage_character_count_1y: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usage_character_count_7d"]) -> MetaOapg.properties.usage_character_count_7d: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cloned_by_count"]) -> MetaOapg.properties.cloned_by_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rate"]) -> MetaOapg.properties.rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["free_users_allowed"]) -> MetaOapg.properties.free_users_allowed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["live_moderation_enabled"]) -> MetaOapg.properties.live_moderation_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notice_period"]) -> MetaOapg.properties.notice_period: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["instagram_username"]) -> MetaOapg.properties.instagram_username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["twitter_username"]) -> MetaOapg.properties.twitter_username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["youtube_username"]) -> MetaOapg.properties.youtube_username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tiktok_username"]) -> MetaOapg.properties.tiktok_username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["featured"]) -> MetaOapg.properties.featured: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "public_owner_id", "voice_id", "date_unix", "name", "accent", "gender", "age", "descriptive", "use_case", "category", "language", "preview_url", "usage_character_count_1y", "usage_character_count_7d", "cloned_by_count", "rate", "free_users_allowed", "live_moderation_enabled", "notice_period", "instagram_username", "twitter_username", "youtube_username", "tiktok_username", "featured", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["public_owner_id"]) -> MetaOapg.properties.public_owner_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voice_id"]) -> MetaOapg.properties.voice_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_unix"]) -> MetaOapg.properties.date_unix: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accent"]) -> MetaOapg.properties.accent: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gender"]) -> MetaOapg.properties.gender: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["age"]) -> MetaOapg.properties.age: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["descriptive"]) -> MetaOapg.properties.descriptive: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["use_case"]) -> MetaOapg.properties.use_case: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["language"]) -> MetaOapg.properties.language: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preview_url"]) -> MetaOapg.properties.preview_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usage_character_count_1y"]) -> MetaOapg.properties.usage_character_count_1y: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usage_character_count_7d"]) -> MetaOapg.properties.usage_character_count_7d: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cloned_by_count"]) -> MetaOapg.properties.cloned_by_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rate"]) -> MetaOapg.properties.rate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["free_users_allowed"]) -> MetaOapg.properties.free_users_allowed: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["live_moderation_enabled"]) -> MetaOapg.properties.live_moderation_enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notice_period"]) -> MetaOapg.properties.notice_period: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["instagram_username"]) -> MetaOapg.properties.instagram_username: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["twitter_username"]) -> MetaOapg.properties.twitter_username: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["youtube_username"]) -> MetaOapg.properties.youtube_username: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tiktok_username"]) -> MetaOapg.properties.tiktok_username: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["featured"]) -> MetaOapg.properties.featured: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "public_owner_id", "voice_id", "date_unix", "name", "accent", "gender", "age", "descriptive", "use_case", "category", "language", "preview_url", "usage_character_count_1y", "usage_character_count_7d", "cloned_by_count", "rate", "free_users_allowed", "live_moderation_enabled", "notice_period", "instagram_username", "twitter_username", "youtube_username", "tiktok_username", "featured", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        featured: typing.Union[MetaOapg.properties.featured, bool, ],
        gender: typing.Union[MetaOapg.properties.gender, str, ],
        usage_character_count_1y: typing.Union[MetaOapg.properties.usage_character_count_1y, decimal.Decimal, int, ],
        twitter_username: typing.Union[MetaOapg.properties.twitter_username, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        language: typing.Union[MetaOapg.properties.language, str, ],
        public_owner_id: typing.Union[MetaOapg.properties.public_owner_id, str, ],
        date_unix: typing.Union[MetaOapg.properties.date_unix, decimal.Decimal, int, ],
        rate: typing.Union[MetaOapg.properties.rate, decimal.Decimal, int, float, ],
        cloned_by_count: typing.Union[MetaOapg.properties.cloned_by_count, decimal.Decimal, int, ],
        free_users_allowed: typing.Union[MetaOapg.properties.free_users_allowed, bool, ],
        instagram_username: typing.Union[MetaOapg.properties.instagram_username, str, ],
        live_moderation_enabled: typing.Union[MetaOapg.properties.live_moderation_enabled, bool, ],
        youtube_username: typing.Union[MetaOapg.properties.youtube_username, str, ],
        voice_id: typing.Union[MetaOapg.properties.voice_id, str, ],
        tiktok_username: typing.Union[MetaOapg.properties.tiktok_username, str, ],
        accent: typing.Union[MetaOapg.properties.accent, str, ],
        use_case: typing.Union[MetaOapg.properties.use_case, str, ],
        preview_url: typing.Union[MetaOapg.properties.preview_url, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        descriptive: typing.Union[MetaOapg.properties.descriptive, str, ],
        usage_character_count_7d: typing.Union[MetaOapg.properties.usage_character_count_7d, decimal.Decimal, int, ],
        category: typing.Union[MetaOapg.properties.category, str, ],
        notice_period: typing.Union[MetaOapg.properties.notice_period, decimal.Decimal, int, ],
        age: typing.Union[MetaOapg.properties.age, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LibraryVoiceResponseModel':
        return super().__new__(
            cls,
            *args,
            featured=featured,
            gender=gender,
            usage_character_count_1y=usage_character_count_1y,
            twitter_username=twitter_username,
            description=description,
            language=language,
            public_owner_id=public_owner_id,
            date_unix=date_unix,
            rate=rate,
            cloned_by_count=cloned_by_count,
            free_users_allowed=free_users_allowed,
            instagram_username=instagram_username,
            live_moderation_enabled=live_moderation_enabled,
            youtube_username=youtube_username,
            voice_id=voice_id,
            tiktok_username=tiktok_username,
            accent=accent,
            use_case=use_case,
            preview_url=preview_url,
            name=name,
            descriptive=descriptive,
            usage_character_count_7d=usage_character_count_7d,
            category=category,
            notice_period=notice_period,
            age=age,
            _configuration=_configuration,
            **kwargs,
        )

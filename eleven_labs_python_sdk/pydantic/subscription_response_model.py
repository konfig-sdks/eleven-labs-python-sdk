# coding: utf-8

"""
    ElevenLabs API Documentation

    This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://elevenlabs.io. Our API is experimental so all endpoints are subject to change.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel


class SubscriptionResponseModel(BaseModel):
    tier: str = Field(alias='tier')

    character_count: int = Field(alias='character_count')

    character_limit: int = Field(alias='character_limit')

    can_extend_character_limit: bool = Field(alias='can_extend_character_limit')

    allowed_to_extend_character_limit: bool = Field(alias='allowed_to_extend_character_limit')

    next_character_count_reset_unix: int = Field(alias='next_character_count_reset_unix')

    voice_limit: int = Field(alias='voice_limit')

    max_voice_add_edits: int = Field(alias='max_voice_add_edits')

    voice_add_edit_counter: int = Field(alias='voice_add_edit_counter')

    professional_voice_limit: int = Field(alias='professional_voice_limit')

    can_extend_voice_limit: bool = Field(alias='can_extend_voice_limit')

    can_use_instant_voice_cloning: bool = Field(alias='can_use_instant_voice_cloning')

    can_use_professional_voice_cloning: bool = Field(alias='can_use_professional_voice_cloning')

    currency: Literal["usd", "eur"] = Field(alias='currency')

    status: Literal["trialing", "active", "incomplete", "incomplete_expired", "past_due", "canceled", "unpaid", "free"] = Field(alias='status')

    billing_period: Literal["monthly_period", "annual_period"] = Field(alias='billing_period')
    class Config:
        arbitrary_types_allowed = True

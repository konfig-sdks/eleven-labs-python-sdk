# coding: utf-8

"""
    ElevenLabs API Documentation

    This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://elevenlabs.io. Our API is experimental so all endpoints are subject to change.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import eleven_labs_python_sdk
from eleven_labs_python_sdk.paths.v1_voices_voice_id_samples_sample_id_audio import get
from eleven_labs_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1VoicesVoiceIdSamplesSampleIdAudio(ApiTestMixin, unittest.TestCase):
    """
    V1VoicesVoiceIdSamplesSampleIdAudio unit test stubs
        Get Audio From Sample
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()

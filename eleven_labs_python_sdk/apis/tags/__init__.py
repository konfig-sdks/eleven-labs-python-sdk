# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from eleven_labs_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    PROJECTS = "projects"
    VOICES = "voices"
    ADMIN = "admin"
    SPEECHHISTORY = "speech-history"
    DUBBING = "dubbing"
    VOICEGENERATION = "voice-generation"
    TEXTTOSPEECH = "text-to-speech"
    SPEECHTOSPEECH = "speech-to-speech"
    SAMPLES = "samples"
    USER = "user"
    PRONUNCIATION_DICTIONARY = "Pronunciation Dictionary"
    MODELS = "models"
    WORKSPACE = "workspace"
    AUDIONATIVE = "audio-native"
    REDIRECT = "redirect"

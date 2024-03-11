import typing_extensions

from eleven_labs_python_sdk.apis.tags import TagValues
from eleven_labs_python_sdk.apis.tags.projects_api import ProjectsApi
from eleven_labs_python_sdk.apis.tags.voices_api import VoicesApi
from eleven_labs_python_sdk.apis.tags.speech_history_api import SpeechHistoryApi
from eleven_labs_python_sdk.apis.tags.dubbing_api import DubbingApi
from eleven_labs_python_sdk.apis.tags.voice_generation_api import VoiceGenerationApi
from eleven_labs_python_sdk.apis.tags.text_to_speech_api import TextToSpeechApi
from eleven_labs_python_sdk.apis.tags.speech_to_speech_api import SpeechToSpeechApi
from eleven_labs_python_sdk.apis.tags.samples_api import SamplesApi
from eleven_labs_python_sdk.apis.tags.user_api import UserApi
from eleven_labs_python_sdk.apis.tags.pronunciation_dictionary_api import PronunciationDictionaryApi
from eleven_labs_python_sdk.apis.tags.models_api import ModelsApi
from eleven_labs_python_sdk.apis.tags.workspace_api import WorkspaceApi
from eleven_labs_python_sdk.apis.tags.audio_native_api import AudioNativeApi
from eleven_labs_python_sdk.apis.tags.redirect_api import RedirectApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PROJECTS: ProjectsApi,
        TagValues.VOICES: VoicesApi,
        TagValues.SPEECHHISTORY: SpeechHistoryApi,
        TagValues.DUBBING: DubbingApi,
        TagValues.VOICEGENERATION: VoiceGenerationApi,
        TagValues.TEXTTOSPEECH: TextToSpeechApi,
        TagValues.SPEECHTOSPEECH: SpeechToSpeechApi,
        TagValues.SAMPLES: SamplesApi,
        TagValues.USER: UserApi,
        TagValues.PRONUNCIATION_DICTIONARY: PronunciationDictionaryApi,
        TagValues.MODELS: ModelsApi,
        TagValues.WORKSPACE: WorkspaceApi,
        TagValues.AUDIONATIVE: AudioNativeApi,
        TagValues.REDIRECT: RedirectApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PROJECTS: ProjectsApi,
        TagValues.VOICES: VoicesApi,
        TagValues.SPEECHHISTORY: SpeechHistoryApi,
        TagValues.DUBBING: DubbingApi,
        TagValues.VOICEGENERATION: VoiceGenerationApi,
        TagValues.TEXTTOSPEECH: TextToSpeechApi,
        TagValues.SPEECHTOSPEECH: SpeechToSpeechApi,
        TagValues.SAMPLES: SamplesApi,
        TagValues.USER: UserApi,
        TagValues.PRONUNCIATION_DICTIONARY: PronunciationDictionaryApi,
        TagValues.MODELS: ModelsApi,
        TagValues.WORKSPACE: WorkspaceApi,
        TagValues.AUDIONATIVE: AudioNativeApi,
        TagValues.REDIRECT: RedirectApi,
    }
)

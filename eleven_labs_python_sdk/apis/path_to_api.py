import typing_extensions

from eleven_labs_python_sdk.paths import PathValues
from eleven_labs_python_sdk.apis.paths.v1_history import V1History
from eleven_labs_python_sdk.apis.paths.v1_history_history_item_id import V1HistoryHistoryItemId
from eleven_labs_python_sdk.apis.paths.v1_history_history_item_id_audio import V1HistoryHistoryItemIdAudio
from eleven_labs_python_sdk.apis.paths.v1_history_download import V1HistoryDownload
from eleven_labs_python_sdk.apis.paths.v1_voices_voice_id_samples_sample_id import V1VoicesVoiceIdSamplesSampleId
from eleven_labs_python_sdk.apis.paths.v1_voices_voice_id_samples_sample_id_audio import V1VoicesVoiceIdSamplesSampleIdAudio
from eleven_labs_python_sdk.apis.paths.v1_text_to_speech_voice_id import V1TextToSpeechVoiceId
from eleven_labs_python_sdk.apis.paths.v1_text_to_speech_voice_id_stream import V1TextToSpeechVoiceIdStream
from eleven_labs_python_sdk.apis.paths.v1_speech_to_speech_voice_id import V1SpeechToSpeechVoiceId
from eleven_labs_python_sdk.apis.paths.v1_speech_to_speech_voice_id_stream import V1SpeechToSpeechVoiceIdStream
from eleven_labs_python_sdk.apis.paths.v1_voice_generation_generate_voice_parameters import V1VoiceGenerationGenerateVoiceParameters
from eleven_labs_python_sdk.apis.paths.v1_voice_generation_generate_voice import V1VoiceGenerationGenerateVoice
from eleven_labs_python_sdk.apis.paths.v1_voice_generation_create_voice import V1VoiceGenerationCreateVoice
from eleven_labs_python_sdk.apis.paths.v1_user_subscription import V1UserSubscription
from eleven_labs_python_sdk.apis.paths.v1_user import V1User
from eleven_labs_python_sdk.apis.paths.v1_voices import V1Voices
from eleven_labs_python_sdk.apis.paths.v1_voices_settings_default import V1VoicesSettingsDefault
from eleven_labs_python_sdk.apis.paths.v1_voices_voice_id_settings import V1VoicesVoiceIdSettings
from eleven_labs_python_sdk.apis.paths.v1_voices_voice_id import V1VoicesVoiceId
from eleven_labs_python_sdk.apis.paths.v1_voices_voice_id_settings_edit import V1VoicesVoiceIdSettingsEdit
from eleven_labs_python_sdk.apis.paths.v1_voices_add import V1VoicesAdd
from eleven_labs_python_sdk.apis.paths.v1_voices_voice_id_edit import V1VoicesVoiceIdEdit
from eleven_labs_python_sdk.apis.paths.v1_voices_add_public_user_id_voice_id import V1VoicesAddPublicUserIdVoiceId
from eleven_labs_python_sdk.apis.paths.v1_projects import V1Projects
from eleven_labs_python_sdk.apis.paths.v1_projects_add import V1ProjectsAdd
from eleven_labs_python_sdk.apis.paths.v1_projects_project_id import V1ProjectsProjectId
from eleven_labs_python_sdk.apis.paths.v1_projects_project_id_convert import V1ProjectsProjectIdConvert
from eleven_labs_python_sdk.apis.paths.v1_projects_project_id_snapshots import V1ProjectsProjectIdSnapshots
from eleven_labs_python_sdk.apis.paths.v1_projects_project_id_snapshots_project_snapshot_id_stream import V1ProjectsProjectIdSnapshotsProjectSnapshotIdStream
from eleven_labs_python_sdk.apis.paths.v1_projects_project_id_chapters import V1ProjectsProjectIdChapters
from eleven_labs_python_sdk.apis.paths.v1_projects_project_id_chapters_chapter_id import V1ProjectsProjectIdChaptersChapterId
from eleven_labs_python_sdk.apis.paths.v1_projects_project_id_chapters_chapter_id_convert import V1ProjectsProjectIdChaptersChapterIdConvert
from eleven_labs_python_sdk.apis.paths.v1_projects_project_id_chapters_chapter_id_snapshots import V1ProjectsProjectIdChaptersChapterIdSnapshots
from eleven_labs_python_sdk.apis.paths.v1_projects_project_id_chapters_chapter_id_snapshots_chapter_snapshot_id_stream import V1ProjectsProjectIdChaptersChapterIdSnapshotsChapterSnapshotIdStream
from eleven_labs_python_sdk.apis.paths.v1_projects_project_id_update_pronunciation_dictionaries import V1ProjectsProjectIdUpdatePronunciationDictionaries
from eleven_labs_python_sdk.apis.paths.v1_dubbing import V1Dubbing
from eleven_labs_python_sdk.apis.paths.v1_dubbing_dubbing_id import V1DubbingDubbingId
from eleven_labs_python_sdk.apis.paths.v1_dubbing_dubbing_id_audio_language_code import V1DubbingDubbingIdAudioLanguageCode
from eleven_labs_python_sdk.apis.paths.admin_admin_url_prefix_sso_provider import AdminAdminUrlPrefixSsoProvider
from eleven_labs_python_sdk.apis.paths.v1_models import V1Models
from eleven_labs_python_sdk.apis.paths.v1_audio_native import V1AudioNative
from eleven_labs_python_sdk.apis.paths.v1_shared_voices import V1SharedVoices
from eleven_labs_python_sdk.apis.paths.v1_pronunciation_dictionaries_add_from_file import V1PronunciationDictionariesAddFromFile
from eleven_labs_python_sdk.apis.paths.admin_n8enylacgd_vanity_link_vanity_link_id_update import AdminN8enylacgdVanityLinkVanityLinkIdUpdate
from eleven_labs_python_sdk.apis.paths.admin_n8enylacgd_vanity_link_vanity_link_id_delete import AdminN8enylacgdVanityLinkVanityLinkIdDelete
from eleven_labs_python_sdk.apis.paths.admin_n8enylacgd_vanity_links import AdminN8enylacgdVanityLinks
from eleven_labs_python_sdk.apis.paths.admin_n8enylacgd_vanity_link_slug import AdminN8enylacgdVanityLinkSlug
from eleven_labs_python_sdk.apis.paths.admin_n8enylacgd_coupon_promocode_archive import AdminN8enylacgdCouponPromocodeArchive
from eleven_labs_python_sdk.apis.paths.admin_n8enylacgd_coupons import AdminN8enylacgdCoupons
from eleven_labs_python_sdk.apis.paths.docs import Docs
from eleven_labs_python_sdk.apis.paths.v1_pronunciation_dictionaries_pronunciation_dictionary_id import V1PronunciationDictionariesPronunciationDictionaryId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_HISTORY: V1History,
        PathValues.V1_HISTORY_HISTORY_ITEM_ID: V1HistoryHistoryItemId,
        PathValues.V1_HISTORY_HISTORY_ITEM_ID_AUDIO: V1HistoryHistoryItemIdAudio,
        PathValues.V1_HISTORY_DOWNLOAD: V1HistoryDownload,
        PathValues.V1_VOICES_VOICE_ID_SAMPLES_SAMPLE_ID: V1VoicesVoiceIdSamplesSampleId,
        PathValues.V1_VOICES_VOICE_ID_SAMPLES_SAMPLE_ID_AUDIO: V1VoicesVoiceIdSamplesSampleIdAudio,
        PathValues.V1_TEXTTOSPEECH_VOICE_ID: V1TextToSpeechVoiceId,
        PathValues.V1_TEXTTOSPEECH_VOICE_ID_STREAM: V1TextToSpeechVoiceIdStream,
        PathValues.V1_SPEECHTOSPEECH_VOICE_ID: V1SpeechToSpeechVoiceId,
        PathValues.V1_SPEECHTOSPEECH_VOICE_ID_STREAM: V1SpeechToSpeechVoiceIdStream,
        PathValues.V1_VOICEGENERATION_GENERATEVOICE_PARAMETERS: V1VoiceGenerationGenerateVoiceParameters,
        PathValues.V1_VOICEGENERATION_GENERATEVOICE: V1VoiceGenerationGenerateVoice,
        PathValues.V1_VOICEGENERATION_CREATEVOICE: V1VoiceGenerationCreateVoice,
        PathValues.V1_USER_SUBSCRIPTION: V1UserSubscription,
        PathValues.V1_USER: V1User,
        PathValues.V1_VOICES: V1Voices,
        PathValues.V1_VOICES_SETTINGS_DEFAULT: V1VoicesSettingsDefault,
        PathValues.V1_VOICES_VOICE_ID_SETTINGS: V1VoicesVoiceIdSettings,
        PathValues.V1_VOICES_VOICE_ID: V1VoicesVoiceId,
        PathValues.V1_VOICES_VOICE_ID_SETTINGS_EDIT: V1VoicesVoiceIdSettingsEdit,
        PathValues.V1_VOICES_ADD: V1VoicesAdd,
        PathValues.V1_VOICES_VOICE_ID_EDIT: V1VoicesVoiceIdEdit,
        PathValues.V1_VOICES_ADD_PUBLIC_USER_ID_VOICE_ID: V1VoicesAddPublicUserIdVoiceId,
        PathValues.V1_PROJECTS: V1Projects,
        PathValues.V1_PROJECTS_ADD: V1ProjectsAdd,
        PathValues.V1_PROJECTS_PROJECT_ID: V1ProjectsProjectId,
        PathValues.V1_PROJECTS_PROJECT_ID_CONVERT: V1ProjectsProjectIdConvert,
        PathValues.V1_PROJECTS_PROJECT_ID_SNAPSHOTS: V1ProjectsProjectIdSnapshots,
        PathValues.V1_PROJECTS_PROJECT_ID_SNAPSHOTS_PROJECT_SNAPSHOT_ID_STREAM: V1ProjectsProjectIdSnapshotsProjectSnapshotIdStream,
        PathValues.V1_PROJECTS_PROJECT_ID_CHAPTERS: V1ProjectsProjectIdChapters,
        PathValues.V1_PROJECTS_PROJECT_ID_CHAPTERS_CHAPTER_ID: V1ProjectsProjectIdChaptersChapterId,
        PathValues.V1_PROJECTS_PROJECT_ID_CHAPTERS_CHAPTER_ID_CONVERT: V1ProjectsProjectIdChaptersChapterIdConvert,
        PathValues.V1_PROJECTS_PROJECT_ID_CHAPTERS_CHAPTER_ID_SNAPSHOTS: V1ProjectsProjectIdChaptersChapterIdSnapshots,
        PathValues.V1_PROJECTS_PROJECT_ID_CHAPTERS_CHAPTER_ID_SNAPSHOTS_CHAPTER_SNAPSHOT_ID_STREAM: V1ProjectsProjectIdChaptersChapterIdSnapshotsChapterSnapshotIdStream,
        PathValues.V1_PROJECTS_PROJECT_ID_UPDATEPRONUNCIATIONDICTIONARIES: V1ProjectsProjectIdUpdatePronunciationDictionaries,
        PathValues.V1_DUBBING: V1Dubbing,
        PathValues.V1_DUBBING_DUBBING_ID: V1DubbingDubbingId,
        PathValues.V1_DUBBING_DUBBING_ID_AUDIO_LANGUAGE_CODE: V1DubbingDubbingIdAudioLanguageCode,
        PathValues.ADMIN_ADMIN_URL_PREFIX_SSOPROVIDER: AdminAdminUrlPrefixSsoProvider,
        PathValues.V1_MODELS: V1Models,
        PathValues.V1_AUDIONATIVE: V1AudioNative,
        PathValues.V1_SHAREDVOICES: V1SharedVoices,
        PathValues.V1_PRONUNCIATIONDICTIONARIES_ADDFROMFILE: V1PronunciationDictionariesAddFromFile,
        PathValues.ADMIN_N8ENYLACGD_VANITYLINK_VANITY_LINK_ID_UPDATE: AdminN8enylacgdVanityLinkVanityLinkIdUpdate,
        PathValues.ADMIN_N8ENYLACGD_VANITYLINK_VANITY_LINK_ID_DELETE: AdminN8enylacgdVanityLinkVanityLinkIdDelete,
        PathValues.ADMIN_N8ENYLACGD_VANITYLINKS: AdminN8enylacgdVanityLinks,
        PathValues.ADMIN_N8ENYLACGD_VANITYLINK_SLUG: AdminN8enylacgdVanityLinkSlug,
        PathValues.ADMIN_N8ENYLACGD_COUPON_PROMOCODE_ARCHIVE: AdminN8enylacgdCouponPromocodeArchive,
        PathValues.ADMIN_N8ENYLACGD_COUPONS: AdminN8enylacgdCoupons,
        PathValues.DOCS: Docs,
        PathValues.V1_PRONUNCIATIONDICTIONARIES_PRONUNCIATION_DICTIONARY_ID: V1PronunciationDictionariesPronunciationDictionaryId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_HISTORY: V1History,
        PathValues.V1_HISTORY_HISTORY_ITEM_ID: V1HistoryHistoryItemId,
        PathValues.V1_HISTORY_HISTORY_ITEM_ID_AUDIO: V1HistoryHistoryItemIdAudio,
        PathValues.V1_HISTORY_DOWNLOAD: V1HistoryDownload,
        PathValues.V1_VOICES_VOICE_ID_SAMPLES_SAMPLE_ID: V1VoicesVoiceIdSamplesSampleId,
        PathValues.V1_VOICES_VOICE_ID_SAMPLES_SAMPLE_ID_AUDIO: V1VoicesVoiceIdSamplesSampleIdAudio,
        PathValues.V1_TEXTTOSPEECH_VOICE_ID: V1TextToSpeechVoiceId,
        PathValues.V1_TEXTTOSPEECH_VOICE_ID_STREAM: V1TextToSpeechVoiceIdStream,
        PathValues.V1_SPEECHTOSPEECH_VOICE_ID: V1SpeechToSpeechVoiceId,
        PathValues.V1_SPEECHTOSPEECH_VOICE_ID_STREAM: V1SpeechToSpeechVoiceIdStream,
        PathValues.V1_VOICEGENERATION_GENERATEVOICE_PARAMETERS: V1VoiceGenerationGenerateVoiceParameters,
        PathValues.V1_VOICEGENERATION_GENERATEVOICE: V1VoiceGenerationGenerateVoice,
        PathValues.V1_VOICEGENERATION_CREATEVOICE: V1VoiceGenerationCreateVoice,
        PathValues.V1_USER_SUBSCRIPTION: V1UserSubscription,
        PathValues.V1_USER: V1User,
        PathValues.V1_VOICES: V1Voices,
        PathValues.V1_VOICES_SETTINGS_DEFAULT: V1VoicesSettingsDefault,
        PathValues.V1_VOICES_VOICE_ID_SETTINGS: V1VoicesVoiceIdSettings,
        PathValues.V1_VOICES_VOICE_ID: V1VoicesVoiceId,
        PathValues.V1_VOICES_VOICE_ID_SETTINGS_EDIT: V1VoicesVoiceIdSettingsEdit,
        PathValues.V1_VOICES_ADD: V1VoicesAdd,
        PathValues.V1_VOICES_VOICE_ID_EDIT: V1VoicesVoiceIdEdit,
        PathValues.V1_VOICES_ADD_PUBLIC_USER_ID_VOICE_ID: V1VoicesAddPublicUserIdVoiceId,
        PathValues.V1_PROJECTS: V1Projects,
        PathValues.V1_PROJECTS_ADD: V1ProjectsAdd,
        PathValues.V1_PROJECTS_PROJECT_ID: V1ProjectsProjectId,
        PathValues.V1_PROJECTS_PROJECT_ID_CONVERT: V1ProjectsProjectIdConvert,
        PathValues.V1_PROJECTS_PROJECT_ID_SNAPSHOTS: V1ProjectsProjectIdSnapshots,
        PathValues.V1_PROJECTS_PROJECT_ID_SNAPSHOTS_PROJECT_SNAPSHOT_ID_STREAM: V1ProjectsProjectIdSnapshotsProjectSnapshotIdStream,
        PathValues.V1_PROJECTS_PROJECT_ID_CHAPTERS: V1ProjectsProjectIdChapters,
        PathValues.V1_PROJECTS_PROJECT_ID_CHAPTERS_CHAPTER_ID: V1ProjectsProjectIdChaptersChapterId,
        PathValues.V1_PROJECTS_PROJECT_ID_CHAPTERS_CHAPTER_ID_CONVERT: V1ProjectsProjectIdChaptersChapterIdConvert,
        PathValues.V1_PROJECTS_PROJECT_ID_CHAPTERS_CHAPTER_ID_SNAPSHOTS: V1ProjectsProjectIdChaptersChapterIdSnapshots,
        PathValues.V1_PROJECTS_PROJECT_ID_CHAPTERS_CHAPTER_ID_SNAPSHOTS_CHAPTER_SNAPSHOT_ID_STREAM: V1ProjectsProjectIdChaptersChapterIdSnapshotsChapterSnapshotIdStream,
        PathValues.V1_PROJECTS_PROJECT_ID_UPDATEPRONUNCIATIONDICTIONARIES: V1ProjectsProjectIdUpdatePronunciationDictionaries,
        PathValues.V1_DUBBING: V1Dubbing,
        PathValues.V1_DUBBING_DUBBING_ID: V1DubbingDubbingId,
        PathValues.V1_DUBBING_DUBBING_ID_AUDIO_LANGUAGE_CODE: V1DubbingDubbingIdAudioLanguageCode,
        PathValues.ADMIN_ADMIN_URL_PREFIX_SSOPROVIDER: AdminAdminUrlPrefixSsoProvider,
        PathValues.V1_MODELS: V1Models,
        PathValues.V1_AUDIONATIVE: V1AudioNative,
        PathValues.V1_SHAREDVOICES: V1SharedVoices,
        PathValues.V1_PRONUNCIATIONDICTIONARIES_ADDFROMFILE: V1PronunciationDictionariesAddFromFile,
        PathValues.ADMIN_N8ENYLACGD_VANITYLINK_VANITY_LINK_ID_UPDATE: AdminN8enylacgdVanityLinkVanityLinkIdUpdate,
        PathValues.ADMIN_N8ENYLACGD_VANITYLINK_VANITY_LINK_ID_DELETE: AdminN8enylacgdVanityLinkVanityLinkIdDelete,
        PathValues.ADMIN_N8ENYLACGD_VANITYLINKS: AdminN8enylacgdVanityLinks,
        PathValues.ADMIN_N8ENYLACGD_VANITYLINK_SLUG: AdminN8enylacgdVanityLinkSlug,
        PathValues.ADMIN_N8ENYLACGD_COUPON_PROMOCODE_ARCHIVE: AdminN8enylacgdCouponPromocodeArchive,
        PathValues.ADMIN_N8ENYLACGD_COUPONS: AdminN8enylacgdCoupons,
        PathValues.DOCS: Docs,
        PathValues.V1_PRONUNCIATIONDICTIONARIES_PRONUNCIATION_DICTIONARY_ID: V1PronunciationDictionariesPronunciationDictionaryId,
    }
)

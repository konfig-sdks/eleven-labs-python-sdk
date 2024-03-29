# coding: utf-8

"""
    ElevenLabs API Documentation

    This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://elevenlabs.io. Our API is experimental so all endpoints are subject to change.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from eleven_labs_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from eleven_labs_python_sdk.api_response import AsyncGeneratorResponse
from eleven_labs_python_sdk import api_client, exceptions
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

from eleven_labs_python_sdk.model.body_creates_audio_native_enabled_project_v1_audio_native_post import BodyCreatesAudioNativeEnabledProjectV1AudioNativePost as BodyCreatesAudioNativeEnabledProjectV1AudioNativePostSchema
from eleven_labs_python_sdk.model.http_validation_error import HTTPValidationError as HTTPValidationErrorSchema
from eleven_labs_python_sdk.model.audio_native_create_project_response_model import AudioNativeCreateProjectResponseModel as AudioNativeCreateProjectResponseModelSchema

from eleven_labs_python_sdk.type.audio_native_create_project_response_model import AudioNativeCreateProjectResponseModel
from eleven_labs_python_sdk.type.body_creates_audio_native_enabled_project_v1_audio_native_post import BodyCreatesAudioNativeEnabledProjectV1AudioNativePost
from eleven_labs_python_sdk.type.http_validation_error import HTTPValidationError

from ...api_client import Dictionary
from eleven_labs_python_sdk.pydantic.audio_native_create_project_response_model import AudioNativeCreateProjectResponseModel as AudioNativeCreateProjectResponseModelPydantic
from eleven_labs_python_sdk.pydantic.body_creates_audio_native_enabled_project_v1_audio_native_post import BodyCreatesAudioNativeEnabledProjectV1AudioNativePost as BodyCreatesAudioNativeEnabledProjectV1AudioNativePostPydantic
from eleven_labs_python_sdk.pydantic.http_validation_error import HTTPValidationError as HTTPValidationErrorPydantic

# Header params
XiApiKeySchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'xi-api-key': typing.Union[XiApiKeySchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_xi_api_key = api_client.HeaderParameter(
    name="xi-api-key",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XiApiKeySchema,
)
# body param
SchemaForRequestBodyMultipartFormData = BodyCreatesAudioNativeEnabledProjectV1AudioNativePostSchema


request_body_body_creates_audio_native_enabled_project_v1_audio_native_post = api_client.RequestBody(
    content={
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = AudioNativeCreateProjectResponseModelSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AudioNativeCreateProjectResponseModel


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AudioNativeCreateProjectResponseModel


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = HTTPValidationErrorSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: HTTPValidationError


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: HTTPValidationError


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_project_with_embeddable_html_mapped_args(
        self,
        name: str,
        file: typing.IO,
        xi_api_key: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        author: typing.Optional[str] = None,
        small: typing.Optional[bool] = None,
        text_color: typing.Optional[str] = None,
        background_color: typing.Optional[str] = None,
        sessionization: typing.Optional[int] = None,
        voice_id: typing.Optional[str] = None,
        model_id: typing.Optional[str] = None,
        auto_convert: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        if title is not None:
            _body["title"] = title
        if name is not None:
            _body["name"] = name
        if image is not None:
            _body["image"] = image
        if author is not None:
            _body["author"] = author
        if small is not None:
            _body["small"] = small
        if text_color is not None:
            _body["text_color"] = text_color
        if background_color is not None:
            _body["background_color"] = background_color
        if sessionization is not None:
            _body["sessionization"] = sessionization
        if voice_id is not None:
            _body["voice_id"] = voice_id
        if model_id is not None:
            _body["model_id"] = model_id
        if file is not None:
            _body["file"] = file
        if auto_convert is not None:
            _body["auto_convert"] = auto_convert
        args.body = _body
        if xi_api_key is not None:
            _header_params["xi-api-key"] = xi_api_key
        args.header = _header_params
        return args

    async def _acreate_project_with_embeddable_html_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Creates Audionative Enabled Project.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_xi_api_key,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/audio-native',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_body_creates_audio_native_enabled_project_v1_audio_native_post.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_project_with_embeddable_html_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Creates Audionative Enabled Project.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_xi_api_key,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/audio-native',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_body_creates_audio_native_enabled_project_v1_audio_native_post.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateProjectWithEmbeddableHtmlRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_project_with_embeddable_html(
        self,
        name: str,
        file: typing.IO,
        xi_api_key: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        author: typing.Optional[str] = None,
        small: typing.Optional[bool] = None,
        text_color: typing.Optional[str] = None,
        background_color: typing.Optional[str] = None,
        sessionization: typing.Optional[int] = None,
        voice_id: typing.Optional[str] = None,
        model_id: typing.Optional[str] = None,
        auto_convert: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_project_with_embeddable_html_mapped_args(
            name=name,
            file=file,
            xi_api_key=xi_api_key,
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
        )
        return await self._acreate_project_with_embeddable_html_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def create_project_with_embeddable_html(
        self,
        name: str,
        file: typing.IO,
        xi_api_key: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        author: typing.Optional[str] = None,
        small: typing.Optional[bool] = None,
        text_color: typing.Optional[str] = None,
        background_color: typing.Optional[str] = None,
        sessionization: typing.Optional[int] = None,
        voice_id: typing.Optional[str] = None,
        model_id: typing.Optional[str] = None,
        auto_convert: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_project_with_embeddable_html_mapped_args(
            name=name,
            file=file,
            xi_api_key=xi_api_key,
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
        )
        return self._create_project_with_embeddable_html_oapg(
            body=args.body,
            header_params=args.header,
        )

class CreateProjectWithEmbeddableHtml(BaseApi):

    async def acreate_project_with_embeddable_html(
        self,
        name: str,
        file: typing.IO,
        xi_api_key: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        author: typing.Optional[str] = None,
        small: typing.Optional[bool] = None,
        text_color: typing.Optional[str] = None,
        background_color: typing.Optional[str] = None,
        sessionization: typing.Optional[int] = None,
        voice_id: typing.Optional[str] = None,
        model_id: typing.Optional[str] = None,
        auto_convert: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> AudioNativeCreateProjectResponseModelPydantic:
        raw_response = await self.raw.acreate_project_with_embeddable_html(
            name=name,
            file=file,
            xi_api_key=xi_api_key,
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
            **kwargs,
        )
        if validate:
            return AudioNativeCreateProjectResponseModelPydantic(**raw_response.body)
        return api_client.construct_model_instance(AudioNativeCreateProjectResponseModelPydantic, raw_response.body)
    
    
    def create_project_with_embeddable_html(
        self,
        name: str,
        file: typing.IO,
        xi_api_key: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        author: typing.Optional[str] = None,
        small: typing.Optional[bool] = None,
        text_color: typing.Optional[str] = None,
        background_color: typing.Optional[str] = None,
        sessionization: typing.Optional[int] = None,
        voice_id: typing.Optional[str] = None,
        model_id: typing.Optional[str] = None,
        auto_convert: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> AudioNativeCreateProjectResponseModelPydantic:
        raw_response = self.raw.create_project_with_embeddable_html(
            name=name,
            file=file,
            xi_api_key=xi_api_key,
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
        )
        if validate:
            return AudioNativeCreateProjectResponseModelPydantic(**raw_response.body)
        return api_client.construct_model_instance(AudioNativeCreateProjectResponseModelPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        file: typing.IO,
        xi_api_key: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        author: typing.Optional[str] = None,
        small: typing.Optional[bool] = None,
        text_color: typing.Optional[str] = None,
        background_color: typing.Optional[str] = None,
        sessionization: typing.Optional[int] = None,
        voice_id: typing.Optional[str] = None,
        model_id: typing.Optional[str] = None,
        auto_convert: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_project_with_embeddable_html_mapped_args(
            name=name,
            file=file,
            xi_api_key=xi_api_key,
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
        )
        return await self._acreate_project_with_embeddable_html_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        file: typing.IO,
        xi_api_key: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        image: typing.Optional[str] = None,
        author: typing.Optional[str] = None,
        small: typing.Optional[bool] = None,
        text_color: typing.Optional[str] = None,
        background_color: typing.Optional[str] = None,
        sessionization: typing.Optional[int] = None,
        voice_id: typing.Optional[str] = None,
        model_id: typing.Optional[str] = None,
        auto_convert: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_project_with_embeddable_html_mapped_args(
            name=name,
            file=file,
            xi_api_key=xi_api_key,
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
        )
        return self._create_project_with_embeddable_html_oapg(
            body=args.body,
            header_params=args.header,
        )


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

from eleven_labs_python_sdk.model.body_speech_to_speech_streaming_v1_speech_to_speech_voice_id_stream_post import BodySpeechToSpeechStreamingV1SpeechToSpeechVoiceIdStreamPost as BodySpeechToSpeechStreamingV1SpeechToSpeechVoiceIdStreamPostSchema
from eleven_labs_python_sdk.model.http_validation_error import HTTPValidationError as HTTPValidationErrorSchema

from eleven_labs_python_sdk.type.http_validation_error import HTTPValidationError
from eleven_labs_python_sdk.type.body_speech_to_speech_streaming_v1_speech_to_speech_voice_id_stream_post import BodySpeechToSpeechStreamingV1SpeechToSpeechVoiceIdStreamPost

from ...api_client import Dictionary
from eleven_labs_python_sdk.pydantic.body_speech_to_speech_streaming_v1_speech_to_speech_voice_id_stream_post import BodySpeechToSpeechStreamingV1SpeechToSpeechVoiceIdStreamPost as BodySpeechToSpeechStreamingV1SpeechToSpeechVoiceIdStreamPostPydantic
from eleven_labs_python_sdk.pydantic.http_validation_error import HTTPValidationError as HTTPValidationErrorPydantic

from . import path

# Query params
OptimizeStreamingLatencySchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'optimize_streaming_latency': typing.Union[OptimizeStreamingLatencySchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_optimize_streaming_latency = api_client.QueryParameter(
    name="optimize_streaming_latency",
    style=api_client.ParameterStyle.FORM,
    schema=OptimizeStreamingLatencySchema,
    explode=True,
)
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
# Path params
VoiceIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'voice_id': typing.Union[VoiceIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_voice_id = api_client.PathParameter(
    name="voice_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=VoiceIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyMultipartFormData = BodySpeechToSpeechStreamingV1SpeechToSpeechVoiceIdStreamPostSchema


request_body_body_speech_to_speech_streaming_v1_speech_to_speech_voice_id_stream_post = api_client.RequestBody(
    content={
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
    },
    required=True,
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
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
_status_code_to_response = {
    '200': _response_for_200,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_with_voice_0_mapped_args(
        self,
        voice_id: str,
        audio: typing.IO,
        optimize_streaming_latency: typing.Optional[int] = None,
        xi_api_key: typing.Optional[str] = None,
        model_id: typing.Optional[str] = None,
        voice_settings: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        _path_params = {}
        _body = {}
        if audio is not None:
            _body["audio"] = audio
        if model_id is not None:
            _body["model_id"] = model_id
        if voice_settings is not None:
            _body["voice_settings"] = voice_settings
        args.body = _body
        if optimize_streaming_latency is not None:
            _query_params["optimize_streaming_latency"] = optimize_streaming_latency
        if xi_api_key is not None:
            _header_params["xi-api-key"] = xi_api_key
        if voice_id is not None:
            _path_params["voice_id"] = voice_id
        args.query = _query_params
        args.header = _header_params
        args.path = _path_params
        return args

    async def _acreate_with_voice_0_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
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
        Speech To Speech Streaming
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_voice_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_optimize_streaming_latency,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
            path_template='/v1/speech-to-speech/{voice_id}/stream',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_body_speech_to_speech_streaming_v1_speech_to_speech_voice_id_stream_post.serialize(body, content_type)
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
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _create_with_voice_0_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
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
        Speech To Speech Streaming
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_voice_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_optimize_streaming_latency,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
            path_template='/v1/speech-to-speech/{voice_id}/stream',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_body_speech_to_speech_streaming_v1_speech_to_speech_voice_id_stream_post.serialize(body, content_type)
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
            prefix_separator_iterator=prefix_separator_iterator,
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


class CreateWithVoice0Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_with_voice_0(
        self,
        voice_id: str,
        audio: typing.IO,
        optimize_streaming_latency: typing.Optional[int] = None,
        xi_api_key: typing.Optional[str] = None,
        model_id: typing.Optional[str] = None,
        voice_settings: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_with_voice_0_mapped_args(
            voice_id=voice_id,
            audio=audio,
            optimize_streaming_latency=optimize_streaming_latency,
            xi_api_key=xi_api_key,
            model_id=model_id,
            voice_settings=voice_settings,
        )
        return await self._acreate_with_voice_0_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def create_with_voice_0(
        self,
        voice_id: str,
        audio: typing.IO,
        optimize_streaming_latency: typing.Optional[int] = None,
        xi_api_key: typing.Optional[str] = None,
        model_id: typing.Optional[str] = None,
        voice_settings: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_with_voice_0_mapped_args(
            voice_id=voice_id,
            audio=audio,
            optimize_streaming_latency=optimize_streaming_latency,
            xi_api_key=xi_api_key,
            model_id=model_id,
            voice_settings=voice_settings,
        )
        return self._create_with_voice_0_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )

class CreateWithVoice0(BaseApi):

    async def acreate_with_voice_0(
        self,
        voice_id: str,
        audio: typing.IO,
        optimize_streaming_latency: typing.Optional[int] = None,
        xi_api_key: typing.Optional[str] = None,
        model_id: typing.Optional[str] = None,
        voice_settings: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.acreate_with_voice_0(
            voice_id=voice_id,
            audio=audio,
            optimize_streaming_latency=optimize_streaming_latency,
            xi_api_key=xi_api_key,
            model_id=model_id,
            voice_settings=voice_settings,
            **kwargs,
        )
    
    
    def create_with_voice_0(
        self,
        voice_id: str,
        audio: typing.IO,
        optimize_streaming_latency: typing.Optional[int] = None,
        xi_api_key: typing.Optional[str] = None,
        model_id: typing.Optional[str] = None,
        voice_settings: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.create_with_voice_0(
            voice_id=voice_id,
            audio=audio,
            optimize_streaming_latency=optimize_streaming_latency,
            xi_api_key=xi_api_key,
            model_id=model_id,
            voice_settings=voice_settings,
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        voice_id: str,
        audio: typing.IO,
        optimize_streaming_latency: typing.Optional[int] = None,
        xi_api_key: typing.Optional[str] = None,
        model_id: typing.Optional[str] = None,
        voice_settings: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_with_voice_0_mapped_args(
            voice_id=voice_id,
            audio=audio,
            optimize_streaming_latency=optimize_streaming_latency,
            xi_api_key=xi_api_key,
            model_id=model_id,
            voice_settings=voice_settings,
        )
        return await self._acreate_with_voice_0_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        voice_id: str,
        audio: typing.IO,
        optimize_streaming_latency: typing.Optional[int] = None,
        xi_api_key: typing.Optional[str] = None,
        model_id: typing.Optional[str] = None,
        voice_settings: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_with_voice_0_mapped_args(
            voice_id=voice_id,
            audio=audio,
            optimize_streaming_latency=optimize_streaming_latency,
            xi_api_key=xi_api_key,
            model_id=model_id,
            voice_settings=voice_settings,
        )
        return self._create_with_voice_0_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )


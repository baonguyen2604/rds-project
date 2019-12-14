# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: volume.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='volume.proto',
  package='volume_pb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cvolume.proto\x12\tvolume_pb\"*\n\x15\x41llocateVolumeRequest\x12\x11\n\tvolume_id\x18\x01 \x01(\r\"\x18\n\x16\x41llocateVolumeResponse\"\"\n\x0fUploadFileChunk\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\"Y\n\x12UploadFileResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x32\n\rresponse_code\x18\x02 \x01(\x0e\x32\x1b.volume_pb.UploadStatusCode*8\n\x10UploadStatusCode\x12\x0b\n\x07unknown\x10\x00\x12\x0b\n\x07success\x10\x01\x12\n\n\x06\x66\x61iled\x10\x02\x32\xb2\x01\n\nVolumeNode\x12W\n\x0e\x41llocateVolume\x12 .volume_pb.AllocateVolumeRequest\x1a!.volume_pb.AllocateVolumeResponse\"\x00\x12K\n\nUploadFile\x12\x1a.volume_pb.UploadFileChunk\x1a\x1d.volume_pb.UploadFileResponse\"\x00(\x01\x62\x06proto3')
)

_UPLOADSTATUSCODE = _descriptor.EnumDescriptor(
  name='UploadStatusCode',
  full_name='volume_pb.UploadStatusCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='unknown', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='success', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='failed', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=224,
  serialized_end=280,
)
_sym_db.RegisterEnumDescriptor(_UPLOADSTATUSCODE)

UploadStatusCode = enum_type_wrapper.EnumTypeWrapper(_UPLOADSTATUSCODE)
unknown = 0
success = 1
failed = 2



_ALLOCATEVOLUMEREQUEST = _descriptor.Descriptor(
  name='AllocateVolumeRequest',
  full_name='volume_pb.AllocateVolumeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='volume_id', full_name='volume_pb.AllocateVolumeRequest.volume_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=69,
)


_ALLOCATEVOLUMERESPONSE = _descriptor.Descriptor(
  name='AllocateVolumeResponse',
  full_name='volume_pb.AllocateVolumeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=95,
)


_UPLOADFILECHUNK = _descriptor.Descriptor(
  name='UploadFileChunk',
  full_name='volume_pb.UploadFileChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='volume_pb.UploadFileChunk.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=131,
)


_UPLOADFILERESPONSE = _descriptor.Descriptor(
  name='UploadFileResponse',
  full_name='volume_pb.UploadFileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='volume_pb.UploadFileResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response_code', full_name='volume_pb.UploadFileResponse.response_code', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=222,
)

_UPLOADFILERESPONSE.fields_by_name['response_code'].enum_type = _UPLOADSTATUSCODE
DESCRIPTOR.message_types_by_name['AllocateVolumeRequest'] = _ALLOCATEVOLUMEREQUEST
DESCRIPTOR.message_types_by_name['AllocateVolumeResponse'] = _ALLOCATEVOLUMERESPONSE
DESCRIPTOR.message_types_by_name['UploadFileChunk'] = _UPLOADFILECHUNK
DESCRIPTOR.message_types_by_name['UploadFileResponse'] = _UPLOADFILERESPONSE
DESCRIPTOR.enum_types_by_name['UploadStatusCode'] = _UPLOADSTATUSCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AllocateVolumeRequest = _reflection.GeneratedProtocolMessageType('AllocateVolumeRequest', (_message.Message,), {
  'DESCRIPTOR' : _ALLOCATEVOLUMEREQUEST,
  '__module__' : 'volume_pb2'
  # @@protoc_insertion_point(class_scope:volume_pb.AllocateVolumeRequest)
  })
_sym_db.RegisterMessage(AllocateVolumeRequest)

AllocateVolumeResponse = _reflection.GeneratedProtocolMessageType('AllocateVolumeResponse', (_message.Message,), {
  'DESCRIPTOR' : _ALLOCATEVOLUMERESPONSE,
  '__module__' : 'volume_pb2'
  # @@protoc_insertion_point(class_scope:volume_pb.AllocateVolumeResponse)
  })
_sym_db.RegisterMessage(AllocateVolumeResponse)

UploadFileChunk = _reflection.GeneratedProtocolMessageType('UploadFileChunk', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADFILECHUNK,
  '__module__' : 'volume_pb2'
  # @@protoc_insertion_point(class_scope:volume_pb.UploadFileChunk)
  })
_sym_db.RegisterMessage(UploadFileChunk)

UploadFileResponse = _reflection.GeneratedProtocolMessageType('UploadFileResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADFILERESPONSE,
  '__module__' : 'volume_pb2'
  # @@protoc_insertion_point(class_scope:volume_pb.UploadFileResponse)
  })
_sym_db.RegisterMessage(UploadFileResponse)



_VOLUMENODE = _descriptor.ServiceDescriptor(
  name='VolumeNode',
  full_name='volume_pb.VolumeNode',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=283,
  serialized_end=461,
  methods=[
  _descriptor.MethodDescriptor(
    name='AllocateVolume',
    full_name='volume_pb.VolumeNode.AllocateVolume',
    index=0,
    containing_service=None,
    input_type=_ALLOCATEVOLUMEREQUEST,
    output_type=_ALLOCATEVOLUMERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UploadFile',
    full_name='volume_pb.VolumeNode.UploadFile',
    index=1,
    containing_service=None,
    input_type=_UPLOADFILECHUNK,
    output_type=_UPLOADFILERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_VOLUMENODE)

DESCRIPTOR.services_by_name['VolumeNode'] = _VOLUMENODE

# @@protoc_insertion_point(module_scope)
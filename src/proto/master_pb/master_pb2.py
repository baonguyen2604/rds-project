# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: master.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='master.proto',
  package='master_pb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cmaster.proto\x12\tmaster_pb\"$\n\x14KeepConnectedRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"1\n\x0eVolumeLocation\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x12\n\npublic_url\x18\x02 \x01(\t\")\n\x13LookupVolumeRequest\x12\x12\n\nvolume_ids\x18\x01 \x03(\t\"\xc3\x01\n\x14LookupVolumeResponse\x12M\n\x13volume_id_locations\x18\x01 \x03(\x0b\x32\x30.master_pb.LookupVolumeResponse.VolumeIdLocation\x1a\\\n\x10VolumeIdLocation\x12\x11\n\tvolume_id\x18\x01 \x01(\t\x12&\n\tlocations\x18\x02 \x03(\x0b\x32\x13.master_pb.Location\x12\r\n\x05\x65rror\x18\x03 \x01(\t\"+\n\x08Location\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x12\n\npublic_url\x18\x02 \x01(\t\"3\n\rUploadRequest\x12\x11\n\tfile_path\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\"_\n\x0eUploadResponse\x12\x11\n\tvolume_id\x18\x01 \x01(\r\":\n\x12UploadResponseCode\x12\x0b\n\x07unknown\x10\x00\x12\x0b\n\x07success\x10\x01\x12\n\n\x06\x66\x61iled\x10\x02\"\x13\n\x11VolumeListRequest\"\x14\n\x12VolumeListResponse\"\'\n\x10\x41\x64\x64VolumeRequest\x12\x13\n\x0bvolume_grpc\x18\x01 \x01(\t\"\xa4\x01\n\x11\x41\x64\x64VolumeResponse\x12\x11\n\tvolume_id\x18\x01 \x01(\r\x12I\n\rresponse_code\x18\x02 \x01(\x0e\x32\x32.master_pb.AddVolumeResponse.AddVolumeResponseCode\"1\n\x15\x41\x64\x64VolumeResponseCode\x12\x0b\n\x07unknown\x10\x00\x12\x0b\n\x07success\x10\x01\x32\xb7\x02\n\nMasterNode\x12Q\n\x0cLookupVolume\x12\x1e.master_pb.LookupVolumeRequest\x1a\x1f.master_pb.LookupVolumeResponse\"\x00\x12?\n\x06Upload\x12\x18.master_pb.UploadRequest\x1a\x19.master_pb.UploadResponse\"\x00\x12K\n\nVolumeList\x12\x1c.master_pb.VolumeListRequest\x1a\x1d.master_pb.VolumeListResponse\"\x00\x12H\n\tAddVolume\x12\x1b.master_pb.AddVolumeRequest\x1a\x1c.master_pb.AddVolumeResponse\"\x00\x62\x06proto3')
)



_UPLOADRESPONSE_UPLOADRESPONSECODE = _descriptor.EnumDescriptor(
  name='UploadResponseCode',
  full_name='master_pb.UploadResponse.UploadResponseCode',
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
  serialized_start=492,
  serialized_end=550,
)
_sym_db.RegisterEnumDescriptor(_UPLOADRESPONSE_UPLOADRESPONSECODE)

_ADDVOLUMERESPONSE_ADDVOLUMERESPONSECODE = _descriptor.EnumDescriptor(
  name='AddVolumeResponseCode',
  full_name='master_pb.AddVolumeResponse.AddVolumeResponseCode',
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
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=752,
  serialized_end=801,
)
_sym_db.RegisterEnumDescriptor(_ADDVOLUMERESPONSE_ADDVOLUMERESPONSECODE)


_KEEPCONNECTEDREQUEST = _descriptor.Descriptor(
  name='KeepConnectedRequest',
  full_name='master_pb.KeepConnectedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='master_pb.KeepConnectedRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_end=63,
)


_VOLUMELOCATION = _descriptor.Descriptor(
  name='VolumeLocation',
  full_name='master_pb.VolumeLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='master_pb.VolumeLocation.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='public_url', full_name='master_pb.VolumeLocation.public_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=65,
  serialized_end=114,
)


_LOOKUPVOLUMEREQUEST = _descriptor.Descriptor(
  name='LookupVolumeRequest',
  full_name='master_pb.LookupVolumeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='volume_ids', full_name='master_pb.LookupVolumeRequest.volume_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=116,
  serialized_end=157,
)


_LOOKUPVOLUMERESPONSE_VOLUMEIDLOCATION = _descriptor.Descriptor(
  name='VolumeIdLocation',
  full_name='master_pb.LookupVolumeResponse.VolumeIdLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='volume_id', full_name='master_pb.LookupVolumeResponse.VolumeIdLocation.volume_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locations', full_name='master_pb.LookupVolumeResponse.VolumeIdLocation.locations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='master_pb.LookupVolumeResponse.VolumeIdLocation.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=263,
  serialized_end=355,
)

_LOOKUPVOLUMERESPONSE = _descriptor.Descriptor(
  name='LookupVolumeResponse',
  full_name='master_pb.LookupVolumeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='volume_id_locations', full_name='master_pb.LookupVolumeResponse.volume_id_locations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LOOKUPVOLUMERESPONSE_VOLUMEIDLOCATION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=160,
  serialized_end=355,
)


_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='master_pb.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='master_pb.Location.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='public_url', full_name='master_pb.Location.public_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=357,
  serialized_end=400,
)


_UPLOADREQUEST = _descriptor.Descriptor(
  name='UploadRequest',
  full_name='master_pb.UploadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_path', full_name='master_pb.UploadRequest.file_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='master_pb.UploadRequest.content', index=1,
      number=2, type=12, cpp_type=9, label=1,
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
  serialized_start=402,
  serialized_end=453,
)


_UPLOADRESPONSE = _descriptor.Descriptor(
  name='UploadResponse',
  full_name='master_pb.UploadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='volume_id', full_name='master_pb.UploadResponse.volume_id', index=0,
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
    _UPLOADRESPONSE_UPLOADRESPONSECODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=455,
  serialized_end=550,
)


_VOLUMELISTREQUEST = _descriptor.Descriptor(
  name='VolumeListRequest',
  full_name='master_pb.VolumeListRequest',
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
  serialized_start=552,
  serialized_end=571,
)


_VOLUMELISTRESPONSE = _descriptor.Descriptor(
  name='VolumeListResponse',
  full_name='master_pb.VolumeListResponse',
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
  serialized_start=573,
  serialized_end=593,
)


_ADDVOLUMEREQUEST = _descriptor.Descriptor(
  name='AddVolumeRequest',
  full_name='master_pb.AddVolumeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='volume_grpc', full_name='master_pb.AddVolumeRequest.volume_grpc', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=595,
  serialized_end=634,
)


_ADDVOLUMERESPONSE = _descriptor.Descriptor(
  name='AddVolumeResponse',
  full_name='master_pb.AddVolumeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='volume_id', full_name='master_pb.AddVolumeResponse.volume_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response_code', full_name='master_pb.AddVolumeResponse.response_code', index=1,
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
    _ADDVOLUMERESPONSE_ADDVOLUMERESPONSECODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=637,
  serialized_end=801,
)

_LOOKUPVOLUMERESPONSE_VOLUMEIDLOCATION.fields_by_name['locations'].message_type = _LOCATION
_LOOKUPVOLUMERESPONSE_VOLUMEIDLOCATION.containing_type = _LOOKUPVOLUMERESPONSE
_LOOKUPVOLUMERESPONSE.fields_by_name['volume_id_locations'].message_type = _LOOKUPVOLUMERESPONSE_VOLUMEIDLOCATION
_UPLOADRESPONSE_UPLOADRESPONSECODE.containing_type = _UPLOADRESPONSE
_ADDVOLUMERESPONSE.fields_by_name['response_code'].enum_type = _ADDVOLUMERESPONSE_ADDVOLUMERESPONSECODE
_ADDVOLUMERESPONSE_ADDVOLUMERESPONSECODE.containing_type = _ADDVOLUMERESPONSE
DESCRIPTOR.message_types_by_name['KeepConnectedRequest'] = _KEEPCONNECTEDREQUEST
DESCRIPTOR.message_types_by_name['VolumeLocation'] = _VOLUMELOCATION
DESCRIPTOR.message_types_by_name['LookupVolumeRequest'] = _LOOKUPVOLUMEREQUEST
DESCRIPTOR.message_types_by_name['LookupVolumeResponse'] = _LOOKUPVOLUMERESPONSE
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['UploadRequest'] = _UPLOADREQUEST
DESCRIPTOR.message_types_by_name['UploadResponse'] = _UPLOADRESPONSE
DESCRIPTOR.message_types_by_name['VolumeListRequest'] = _VOLUMELISTREQUEST
DESCRIPTOR.message_types_by_name['VolumeListResponse'] = _VOLUMELISTRESPONSE
DESCRIPTOR.message_types_by_name['AddVolumeRequest'] = _ADDVOLUMEREQUEST
DESCRIPTOR.message_types_by_name['AddVolumeResponse'] = _ADDVOLUMERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeepConnectedRequest = _reflection.GeneratedProtocolMessageType('KeepConnectedRequest', (_message.Message,), {
  'DESCRIPTOR' : _KEEPCONNECTEDREQUEST,
  '__module__' : 'master_pb2'
  # @@protoc_insertion_point(class_scope:master_pb.KeepConnectedRequest)
  })
_sym_db.RegisterMessage(KeepConnectedRequest)

VolumeLocation = _reflection.GeneratedProtocolMessageType('VolumeLocation', (_message.Message,), {
  'DESCRIPTOR' : _VOLUMELOCATION,
  '__module__' : 'master_pb2'
  # @@protoc_insertion_point(class_scope:master_pb.VolumeLocation)
  })
_sym_db.RegisterMessage(VolumeLocation)

LookupVolumeRequest = _reflection.GeneratedProtocolMessageType('LookupVolumeRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOOKUPVOLUMEREQUEST,
  '__module__' : 'master_pb2'
  # @@protoc_insertion_point(class_scope:master_pb.LookupVolumeRequest)
  })
_sym_db.RegisterMessage(LookupVolumeRequest)

LookupVolumeResponse = _reflection.GeneratedProtocolMessageType('LookupVolumeResponse', (_message.Message,), {

  'VolumeIdLocation' : _reflection.GeneratedProtocolMessageType('VolumeIdLocation', (_message.Message,), {
    'DESCRIPTOR' : _LOOKUPVOLUMERESPONSE_VOLUMEIDLOCATION,
    '__module__' : 'master_pb2'
    # @@protoc_insertion_point(class_scope:master_pb.LookupVolumeResponse.VolumeIdLocation)
    })
  ,
  'DESCRIPTOR' : _LOOKUPVOLUMERESPONSE,
  '__module__' : 'master_pb2'
  # @@protoc_insertion_point(class_scope:master_pb.LookupVolumeResponse)
  })
_sym_db.RegisterMessage(LookupVolumeResponse)
_sym_db.RegisterMessage(LookupVolumeResponse.VolumeIdLocation)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'master_pb2'
  # @@protoc_insertion_point(class_scope:master_pb.Location)
  })
_sym_db.RegisterMessage(Location)

UploadRequest = _reflection.GeneratedProtocolMessageType('UploadRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADREQUEST,
  '__module__' : 'master_pb2'
  # @@protoc_insertion_point(class_scope:master_pb.UploadRequest)
  })
_sym_db.RegisterMessage(UploadRequest)

UploadResponse = _reflection.GeneratedProtocolMessageType('UploadResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADRESPONSE,
  '__module__' : 'master_pb2'
  # @@protoc_insertion_point(class_scope:master_pb.UploadResponse)
  })
_sym_db.RegisterMessage(UploadResponse)

VolumeListRequest = _reflection.GeneratedProtocolMessageType('VolumeListRequest', (_message.Message,), {
  'DESCRIPTOR' : _VOLUMELISTREQUEST,
  '__module__' : 'master_pb2'
  # @@protoc_insertion_point(class_scope:master_pb.VolumeListRequest)
  })
_sym_db.RegisterMessage(VolumeListRequest)

VolumeListResponse = _reflection.GeneratedProtocolMessageType('VolumeListResponse', (_message.Message,), {
  'DESCRIPTOR' : _VOLUMELISTRESPONSE,
  '__module__' : 'master_pb2'
  # @@protoc_insertion_point(class_scope:master_pb.VolumeListResponse)
  })
_sym_db.RegisterMessage(VolumeListResponse)

AddVolumeRequest = _reflection.GeneratedProtocolMessageType('AddVolumeRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDVOLUMEREQUEST,
  '__module__' : 'master_pb2'
  # @@protoc_insertion_point(class_scope:master_pb.AddVolumeRequest)
  })
_sym_db.RegisterMessage(AddVolumeRequest)

AddVolumeResponse = _reflection.GeneratedProtocolMessageType('AddVolumeResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDVOLUMERESPONSE,
  '__module__' : 'master_pb2'
  # @@protoc_insertion_point(class_scope:master_pb.AddVolumeResponse)
  })
_sym_db.RegisterMessage(AddVolumeResponse)



_MASTERNODE = _descriptor.ServiceDescriptor(
  name='MasterNode',
  full_name='master_pb.MasterNode',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=804,
  serialized_end=1115,
  methods=[
  _descriptor.MethodDescriptor(
    name='LookupVolume',
    full_name='master_pb.MasterNode.LookupVolume',
    index=0,
    containing_service=None,
    input_type=_LOOKUPVOLUMEREQUEST,
    output_type=_LOOKUPVOLUMERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Upload',
    full_name='master_pb.MasterNode.Upload',
    index=1,
    containing_service=None,
    input_type=_UPLOADREQUEST,
    output_type=_UPLOADRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='VolumeList',
    full_name='master_pb.MasterNode.VolumeList',
    index=2,
    containing_service=None,
    input_type=_VOLUMELISTREQUEST,
    output_type=_VOLUMELISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddVolume',
    full_name='master_pb.MasterNode.AddVolume',
    index=3,
    containing_service=None,
    input_type=_ADDVOLUMEREQUEST,
    output_type=_ADDVOLUMERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MASTERNODE)

DESCRIPTOR.services_by_name['MasterNode'] = _MASTERNODE

# @@protoc_insertion_point(module_scope)

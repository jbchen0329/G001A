# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: G001A.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='G001A.proto',
  package='rpc_package',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bG001A.proto\x12\x0brpc_package\"2\n\tInspt_Req\x12\n\n\x02\x66n\x18\x01 \x01(\t\x12\x0b\n\x03pic\x18\x02 \x01(\x0c\x12\x0c\n\x04pred\x18\x03 \x01(\x08\"\x16\n\x07\x41\x63k_Res\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\x08\"&\n\x03Req\x12\x1f\n\x04sign\x18\x01 \x03(\x0e\x32\x11.rpc_package.Sign\"4\n\x06\x43oordn\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01w\x18\x03 \x01(\x02\x12\t\n\x01h\x18\x04 \x01(\x02\"?\n\tThreshold\x12\x11\n\tthreshold\x18\x01 \x01(\x02\x12\x1f\n\x04sign\x18\x02 \x03(\x0e\x32\x11.rpc_package.Sign\"b\n\x0bSystem_Info\x12\x10\n\x08\x63pu_info\x18\x01 \x01(\x02\x12\x10\n\x08gpu_info\x18\x02 \x01(\x02\x12\x10\n\x08mem_info\x18\x03 \x01(\x02\x12\x11\n\ttmpt_info\x18\x04 \x01(\x02\x12\n\n\x02hd\x18\x05 \x01(\x02*`\n\x04Sign\x12\n\n\x06\x64\x65viat\x10\x00\x12\x07\n\x03\x62rk\x10\x01\x12\t\n\x05metar\x10\x02\x12\x07\n\x03\x63pu\x10\x03\x12\x07\n\x03mem\x10\x04\x12\x08\n\x04tmpt\x10\x05\x12\x0b\n\x07restart\x10\x06\x12\x0f\n\x0bsystem_info\x10\x07\x32\xb1\x03\n\tAlgorithm\x12<\n\nDeviatPred\x12\x16.rpc_package.Inspt_Req\x1a\x14.rpc_package.Ack_Res\"\x00\x12\x37\n\x0c\x43oordnGetter\x12\x10.rpc_package.Req\x1a\x13.rpc_package.Coordn\"\x00\x12;\n\x0c\x43oordnSetter\x12\x13.rpc_package.Coordn\x1a\x14.rpc_package.Ack_Res\"\x00\x12\x39\n\x07\x42rkPred\x12\x16.rpc_package.Inspt_Req\x1a\x14.rpc_package.Ack_Res\"\x00\x12\x39\n\x0bThresGetter\x12\x10.rpc_package.Req\x1a\x16.rpc_package.Threshold\"\x00\x12=\n\x0bThresSetter\x12\x16.rpc_package.Threshold\x1a\x14.rpc_package.Ack_Res\"\x00\x12;\n\tMetarPred\x12\x16.rpc_package.Inspt_Req\x1a\x14.rpc_package.Ack_Res\"\x00\x32{\n\x06System\x12<\n\x0cSystemGetter\x12\x10.rpc_package.Req\x1a\x18.rpc_package.System_Info\"\x00\x12\x33\n\x07Restart\x12\x10.rpc_package.Req\x1a\x14.rpc_package.Ack_Res\"\x00\x62\x06proto3'
)

_SIGN = _descriptor.EnumDescriptor(
  name='Sign',
  full_name='rpc_package.Sign',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='deviat', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='brk', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='metar', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='cpu', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='mem', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='tmpt', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='restart', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='system_info', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=363,
  serialized_end=459,
)
_sym_db.RegisterEnumDescriptor(_SIGN)

Sign = enum_type_wrapper.EnumTypeWrapper(_SIGN)
deviat = 0
brk = 1
metar = 2
cpu = 3
mem = 4
tmpt = 5
restart = 6
system_info = 7



_INSPT_REQ = _descriptor.Descriptor(
  name='Inspt_Req',
  full_name='rpc_package.Inspt_Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fn', full_name='rpc_package.Inspt_Req.fn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pic', full_name='rpc_package.Inspt_Req.pic', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pred', full_name='rpc_package.Inspt_Req.pred', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=28,
  serialized_end=78,
)


_ACK_RES = _descriptor.Descriptor(
  name='Ack_Res',
  full_name='rpc_package.Ack_Res',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack', full_name='rpc_package.Ack_Res.ack', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=80,
  serialized_end=102,
)


_REQ = _descriptor.Descriptor(
  name='Req',
  full_name='rpc_package.Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sign', full_name='rpc_package.Req.sign', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=104,
  serialized_end=142,
)


_COORDN = _descriptor.Descriptor(
  name='Coordn',
  full_name='rpc_package.Coordn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='rpc_package.Coordn.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='rpc_package.Coordn.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='w', full_name='rpc_package.Coordn.w', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='h', full_name='rpc_package.Coordn.h', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=144,
  serialized_end=196,
)


_THRESHOLD = _descriptor.Descriptor(
  name='Threshold',
  full_name='rpc_package.Threshold',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='threshold', full_name='rpc_package.Threshold.threshold', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sign', full_name='rpc_package.Threshold.sign', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=198,
  serialized_end=261,
)


_SYSTEM_INFO = _descriptor.Descriptor(
  name='System_Info',
  full_name='rpc_package.System_Info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cpu_info', full_name='rpc_package.System_Info.cpu_info', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gpu_info', full_name='rpc_package.System_Info.gpu_info', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mem_info', full_name='rpc_package.System_Info.mem_info', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tmpt_info', full_name='rpc_package.System_Info.tmpt_info', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hd', full_name='rpc_package.System_Info.hd', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_end=361,
)

_REQ.fields_by_name['sign'].enum_type = _SIGN
_THRESHOLD.fields_by_name['sign'].enum_type = _SIGN
DESCRIPTOR.message_types_by_name['Inspt_Req'] = _INSPT_REQ
DESCRIPTOR.message_types_by_name['Ack_Res'] = _ACK_RES
DESCRIPTOR.message_types_by_name['Req'] = _REQ
DESCRIPTOR.message_types_by_name['Coordn'] = _COORDN
DESCRIPTOR.message_types_by_name['Threshold'] = _THRESHOLD
DESCRIPTOR.message_types_by_name['System_Info'] = _SYSTEM_INFO
DESCRIPTOR.enum_types_by_name['Sign'] = _SIGN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Inspt_Req = _reflection.GeneratedProtocolMessageType('Inspt_Req', (_message.Message,), {
  'DESCRIPTOR' : _INSPT_REQ,
  '__module__' : 'G001A_pb2'
  # @@protoc_insertion_point(class_scope:rpc_package.Inspt_Req)
  })
_sym_db.RegisterMessage(Inspt_Req)

Ack_Res = _reflection.GeneratedProtocolMessageType('Ack_Res', (_message.Message,), {
  'DESCRIPTOR' : _ACK_RES,
  '__module__' : 'G001A_pb2'
  # @@protoc_insertion_point(class_scope:rpc_package.Ack_Res)
  })
_sym_db.RegisterMessage(Ack_Res)

Req = _reflection.GeneratedProtocolMessageType('Req', (_message.Message,), {
  'DESCRIPTOR' : _REQ,
  '__module__' : 'G001A_pb2'
  # @@protoc_insertion_point(class_scope:rpc_package.Req)
  })
_sym_db.RegisterMessage(Req)

Coordn = _reflection.GeneratedProtocolMessageType('Coordn', (_message.Message,), {
  'DESCRIPTOR' : _COORDN,
  '__module__' : 'G001A_pb2'
  # @@protoc_insertion_point(class_scope:rpc_package.Coordn)
  })
_sym_db.RegisterMessage(Coordn)

Threshold = _reflection.GeneratedProtocolMessageType('Threshold', (_message.Message,), {
  'DESCRIPTOR' : _THRESHOLD,
  '__module__' : 'G001A_pb2'
  # @@protoc_insertion_point(class_scope:rpc_package.Threshold)
  })
_sym_db.RegisterMessage(Threshold)

System_Info = _reflection.GeneratedProtocolMessageType('System_Info', (_message.Message,), {
  'DESCRIPTOR' : _SYSTEM_INFO,
  '__module__' : 'G001A_pb2'
  # @@protoc_insertion_point(class_scope:rpc_package.System_Info)
  })
_sym_db.RegisterMessage(System_Info)



_ALGORITHM = _descriptor.ServiceDescriptor(
  name='Algorithm',
  full_name='rpc_package.Algorithm',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=462,
  serialized_end=895,
  methods=[
  _descriptor.MethodDescriptor(
    name='DeviatPred',
    full_name='rpc_package.Algorithm.DeviatPred',
    index=0,
    containing_service=None,
    input_type=_INSPT_REQ,
    output_type=_ACK_RES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CoordnGetter',
    full_name='rpc_package.Algorithm.CoordnGetter',
    index=1,
    containing_service=None,
    input_type=_REQ,
    output_type=_COORDN,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CoordnSetter',
    full_name='rpc_package.Algorithm.CoordnSetter',
    index=2,
    containing_service=None,
    input_type=_COORDN,
    output_type=_ACK_RES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BrkPred',
    full_name='rpc_package.Algorithm.BrkPred',
    index=3,
    containing_service=None,
    input_type=_INSPT_REQ,
    output_type=_ACK_RES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ThresGetter',
    full_name='rpc_package.Algorithm.ThresGetter',
    index=4,
    containing_service=None,
    input_type=_REQ,
    output_type=_THRESHOLD,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ThresSetter',
    full_name='rpc_package.Algorithm.ThresSetter',
    index=5,
    containing_service=None,
    input_type=_THRESHOLD,
    output_type=_ACK_RES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MetarPred',
    full_name='rpc_package.Algorithm.MetarPred',
    index=6,
    containing_service=None,
    input_type=_INSPT_REQ,
    output_type=_ACK_RES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ALGORITHM)

DESCRIPTOR.services_by_name['Algorithm'] = _ALGORITHM


_SYSTEM = _descriptor.ServiceDescriptor(
  name='System',
  full_name='rpc_package.System',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=897,
  serialized_end=1020,
  methods=[
  _descriptor.MethodDescriptor(
    name='SystemGetter',
    full_name='rpc_package.System.SystemGetter',
    index=0,
    containing_service=None,
    input_type=_REQ,
    output_type=_SYSTEM_INFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Restart',
    full_name='rpc_package.System.Restart',
    index=1,
    containing_service=None,
    input_type=_REQ,
    output_type=_ACK_RES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SYSTEM)

DESCRIPTOR.services_by_name['System'] = _SYSTEM

# @@protoc_insertion_point(module_scope)
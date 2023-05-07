from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eLocalizationLanguageFile.proto\x12\x12sp.protobuf.locale\"/\n\x11LanguageFileEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"J\n\x10LanguageFileData\x12\x36\n\x07\x65ntries\x18\x01 \x03(\x0b\x32%.sp.protobuf.locale.LanguageFileEntryb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'LocalizationLanguageFile_pb2', _globals)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_LANGUAGEFILEENTRY"]._serialized_start = 54
    _globals["_LANGUAGEFILEENTRY"]._serialized_end = 101
    _globals["_LANGUAGEFILEDATA"]._serialized_start = 103
    _globals["_LANGUAGEFILEDATA"]._serialized_end = 177
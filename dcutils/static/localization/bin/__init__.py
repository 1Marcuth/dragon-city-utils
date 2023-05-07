from pydantic import validate_arguments
from typing import Optional, Union
from pyfilter import FromDictList
import httpx

from ..json_ import Localization
from . import loca_pb2

class LocalizationBin(Localization):
    def __init__(
        self,
        language: Optional[str] = None,
        loc: Optional[Union[list[dict], dict]] = None
    ) -> None:
        if loc is None:
            self.__bytes = self.fetch(language)
            loc = self.parse_to_list(self.__bytes)

        else:
            self.__bytes = bytes(loc)
            loc = self.parse_to_list(loc)

        super().__init__(loc=loc)

    @classmethod
    @validate_arguments
    def parse_to_list(cls, data: bytes) -> list[dict]:
        language_file = loca_pb2.LanguageFileData()
        language_file.ParseFromString(data)
        localization_first_field = language_file.DESCRIPTOR.fields[0]
        repeated_composite_container_entries = getattr(language_file, localization_first_field.name)
        localization_list = [ { entry.key: entry.value } for entry in repeated_composite_container_entries ]
        
        return localization_list

    @classmethod
    @validate_arguments
    def parse_to_dict(cls, data: bytes) -> list[dict]:
        localization_list = LocalizationBin.parse_to_list(data)
        localization_dict = FromDictList(localization_list).merge_dicts()
        return localization_dict

    @classmethod
    @validate_arguments
    def load_file(cls, file_path: str):
        with open(file_path, "rb") as file:
            loc = cls.parse_to_list(file.read())
            return Localization(loc=loc)

    @classmethod
    @validate_arguments
    def load(cls, loc: bytes):
        loc_obj = LocalizationBin(loc=loc)
        return loc_obj

    @classmethod
    @validate_arguments
    def fetch(cls, language: str) -> bytes:
        endpoint_url = f"https://sp-translations.socialpointgames.com/deploy/dc/android/prod/dc_android_{language}_prod_wetd46pWuR8J5CmS.pb.bin"

        response = httpx.get(endpoint_url)
        data = response.content

        return data

    @validate_arguments
    def save_file(
        self,
        file_path: str
    ) -> None:
        with open(file_path, "wb") as file:
            file.write(self.__bytes)

__all__ = [ "LocalizationBin" ]
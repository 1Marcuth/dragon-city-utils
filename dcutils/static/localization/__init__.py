from typing import Optional, Union, Any, Self
from pydantic import validate_call
from pyfilter import DictListFilter
import httpx
import json

from ..._utils.file import (
    write_json_file,
    read_json_file,
    write_compressed_json_file,
    read_compressed_json_file
)

LocalizationDict = dict[str, str]
LocalizationList = list[LocalizationDict]

class Localization:
    __list: list
    __dict: dict

    @validate_call
    def __init__(
        self,
        language: Optional[str] = None,
        loc: Optional[
            Union[list[dict], dict]
        ] = None
    ) -> None:
        if language:
            self.__list: LocalizationList = self.fetch(language)
            self.__dict: LocalizationDict = DictListFilter(self.__list).merge_dicts()

        elif loc:
            self.__load(loc)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({json.dumps(self.dict, indent=4)[:300]}" + "...})"

    def __str__(self) -> str:
        return self.__repr__()

    # >> Desativados temporariamente por conta de erros
    # @validate_call
    # def __getitem__(self, key: str) -> str:
    #     result = self.get_value_from_key(key)

    #     if result is None:
    #         raise KeyError(key)

    #     return result

    # @validate_call
    # def __getattr__(self, name: str) -> str:
    #     result = self.get_value_from_key(name)

    #     if result is None:
    #         raise AttributeError(name)

    #     return result
    # >>

    @classmethod
    @validate_call
    def load_file(cls, file_path: str, encoding: str = "utf-8") -> Self:
        loc = read_json_file(file_path, encoding = encoding)
        return cls(loc = loc)

    @classmethod
    @validate_call
    def load(cls, loc: Union[list, dict]) -> Self:
        loc_obj = cls()
        object_type = type(loc)

        if object_type == list:
            loc_obj._Localization__list = loc
            loc_obj._Localization__dict = DictListFilter(loc).merge_dicts()

        elif object_type == dict:
            loc_obj._Localization__dict = loc
            loc_obj._Localization__list = []

            for key, value in loc.items():
                dict_ = { key: value }
                loc_obj._Localization__localization.append(dict_)

        else:
            raise ValueError(f"'{object_type}' is an invalid type to load a localization!")

        return loc_obj

    @validate_call
    def save_file(
        self,
        file_path: str,
        from_: str = "dict"
    ) -> None:
        if from_ == "dict":
            data = self.__dict

        elif from_ == "list":
            data = self.__list

        else:
            ValueError()

        write_json_file(file_path, data)

    @validate_call
    def save_compressed_file(
        self,
        file_path: str,
        encoding: str = "utf-8",
        indent: Optional[int] = None
    ) -> None:
        write_compressed_json_file(file_path, self.dict, indent, encoding)

    @classmethod
    @validate_call
    def load_compressed_file(
        cls,
        file_path: str,
        encoding: str = "utf-8"
    ) -> Self:
        loc = read_compressed_json_file(file_path, encoding)
        return cls(loc = loc)

    @classmethod
    def fetch(cls, language: str) -> list[dict[str, str]]:
        endpoint_url = f"https://sp-translations.socialpointgames.com/deploy/dc/android/prod/dc_android_{language}_prod_wetd46pWuR8J5CmS.json"

        response = httpx.get(endpoint_url)
        data = response.json()
        return data

    @validate_call
    def __load(self, loc: Union[list, dict]):
        type_ = type(loc)

        if type_ == list:
            self.__load_list(loc)

        elif type_ == dict:
            self.__load_dict(loc)

        else:
            raise ValueError(f"{type_} is an invalid type to load a localization")

    @validate_call
    def __load_list(self, loc: list[dict]):
        self.__list = loc
        self.__dict = DictListFilter(loc).merge_dicts()

    @validate_call
    def __load_dict(self, loc: dict):
        self.__dict = loc
        self.__list = []

        for key, value in loc.items():
            dict_ = { key: value }
            self.__list.append(dict_)

    @validate_call
    def get_value_from_key(self, key: str) -> Optional[str]:
        if key in self.__dict.keys():
            return self.__dict[key]

    @validate_call
    def get_key_from_value(self, value: str) -> Optional[str]:
        for dict_key, dict_value in self.__dict.items():
            if dict_value == value:
                return dict_key

    @validate_call
    def get_dragon_name(self, id: int) -> Optional[str]:
        key = f"tid_unit_{id}_name"
        return self.get_value_from_key(key)

    @validate_call
    def get_dragon_description(self, id: int) -> Optional[str]:
        key = f"tid_unit_{id}_description"
        return self.get_value_from_key(key)

    @validate_call
    def get_attack_name(self, id: int) -> Optional[str]:
        key = f"tid_attack_name_{id}"
        return self.get_value_from_key(key)

    @validate_call
    def get_skill_name(self, id: int) -> Optional[str]:
        key = f"tid_skill_name_{id}"
        return self.get_value_from_key(key)

    @validate_call
    def get_skill_description(self, id: int) -> Optional[str]:
        key = f"tid_skill_description_{id}"
        return self.get_value_from_key(key)

    @validate_call
    def search_keys(self, query: str) -> list[str]:
        query = (query
            .lower()
            .strip())

        results = []

        for key in self.__dict.keys():
            parsed_key = (key
                .lower()
                .strip())

            if query in parsed_key:
                results.append(key)

        return results

    @validate_call
    def search_values(self, query: str) -> list[str] | list:
        query = (query
            .lower()
            .strip())

        results = []

        for value in self.__dict.values():
            parsed_value = (value
                .lower()
                .strip())

            if query in parsed_value:
                results.append(value)

        return results

    @validate_call
    def compare(
        self,
        old_localization: Any
    ) -> dict[str, list]:
        if isinstance(old_localization, list):
            old_localization = DictListFilter(old_localization).merge_dicts()

        elif not isinstance(old_localization, dict):
            old_localization = old_localization.dict

        new_fields = []
        edited_fields = []
        deleted_fields = []

        old_localization_keys = old_localization.keys()

        for key in self.__dict.keys():
            if key not in old_localization_keys:
                new_fields.append({
                    "key": key,
                    "value": self.__dict[key]
                })

        for key in old_localization_keys:
            if key not in self.__dict:
                deleted_fields.append({
                    "key": key,
                    "value": old_localization[key]
                })

            elif old_localization[key] != self.__dict[key]:
                edited_fields.append({
                    "key": key,
                    "values": {
                        "new": old_localization[key],
                        "old": self.__dict[key]
                    }
                })

        return dict(
            new_fields = new_fields,
            edited_fields = edited_fields,
            deleted_fields = deleted_fields
        )

    @property
    def list(self) -> LocalizationList:
        return self.__list or []

    @property
    def dict(self) -> LocalizationDict:
        return self.__dict or {}

__all__ = [ "Localization" ]
from pydantic import validate_arguments
from typing import Optional, Union, Any
from pyfilter import FromDictList
import httpx
import json

class Localization:
    __localization_list: list
    __localization_dict: dict

    @validate_arguments
    def __init__(
        self,
        language: Optional[str] = None,
        loc: Optional[
            Union[list[dict], dict]
        ] = None
    ) -> None:
        if language:
            self.__localization_list = self.fetch(language)
            self.__localization_dict = FromDictList(self.__localization_list).merge_dicts()

        elif loc:
            self.__load(loc)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({json.dumps(self.dict, indent=4)})"

    def __str__(self) -> str:
        return self.__repr__()

    @validate_arguments
    def __getitem__(self, key: str) -> str:
        result = self.get_value_from_key(key)

        if result is None:
            raise KeyError(key)

        return result

    @validate_arguments
    def __getattr__(self, name: str) -> str:
        result = self.get_value_from_key(name)

        if result is None:
            raise AttributeError(name)

        return result

    @classmethod
    @validate_arguments
    def load_file(cls, file_path: str):
        with open(file_path, "r", encoding="utf-8") as file:
            loc = json.load(file)
            return Localization(loc=loc)

    @classmethod
    @validate_arguments
    def load(cls, loc: Union[list, dict]):
        loc_obj = Localization()
        type_ = type(loc)

        if type_ == list:
            loc_obj._Localization__localization_list = loc
            loc_obj._Localization__localization_dict = FromDictList(loc).merge_dicts()

        elif type_ == dict:
            loc_obj._Localization__localization_dict = loc
            loc_obj._Localization__localization_list = []

            for key, value in loc.items():
                dict_ = { key: value }
                loc_obj._Localization__localization.append(dict_)

        else:
            raise ValueError(f"{type_} is an invalid type to load a localization")

        return loc_obj

    @validate_arguments
    def save_file(
        self,
        file_path: str,
        from_: str = "dict"
    ) -> None:
        if from_ == "dict":
            data = self.__localization_dict

        elif from_ == "list":
            data = self.__localization_list

        else:
            ValueError()

        with open(file_path, "w+", encoding="utf-8") as file:
            json.dump(data, file)

    @classmethod
    def fetch(cls, language: str) -> list[dict[str, str]]:
        endpoint_url = f"https://sp-translations.socialpointgames.com/deploy/dc/android/prod/dc_android_{language}_prod_wetd46pWuR8J5CmS.json"

        response = httpx.get(endpoint_url)
        data = response.json()
        return data

    @validate_arguments
    def __load(self, loc: Union[list, dict]):
        type_ = type(loc)

        if type_ == list:
            self.__load_list(list(loc))

        elif type_ == dict:
            self.__load_dict(dict(loc))

        else:
            raise ValueError(f"{type_} is an invalid type to load a localization")

    @validate_arguments
    def __load_list(self, loc: list[dict]):
        self.__localization_list = loc
        self.__localization_dict = FromDictList(loc).merge_dicts()

    @validate_arguments
    def __load_dict(self, loc: dict):
        self.__localization_dict = loc
        self.__localization_list = []

        for key, value in loc.items():
            dict_ = { key: value }
            self.__localization_list.append(dict_)

    @validate_arguments
    def get_value_from_key(self, key: str) -> Optional[str]:
        if key in self.__localization_dict.keys():
            return self.__localization_dict[key]

    @validate_arguments
    def get_key_from_value(self, value: str) -> Optional[str]:
        for dict_key, dict_value in self.__localization_dict.items():
            if dict_value == value:
                return dict_key

    @validate_arguments
    def get_dragon_name(self, id: int) -> Optional[str]:
        key = f"tid_unit_{id}_name"
        return self.get_value_from_key(key)

    @validate_arguments
    def get_dragon_description(self, id: int) -> Optional[str]:
        key = f"tid_unit_{id}_description"
        return self.get_value_from_key(key)

    @validate_arguments
    def get_attack_name(self, id: int) -> Optional[str]:
        key = f"tid_attack_name_{id}"
        return self.get_value_from_key(key)

    @validate_arguments
    def get_skill_name(self, id: int) -> Optional[str]:
        key = f"tid_skill_name_{id}"
        return self.get_value_from_key(key)

    @validate_arguments
    def get_skill_description(self, id: int) -> Optional[str]:
        key = f"tid_skill_description_{id}"
        return self.get_value_from_key(key)

    @validate_arguments
    def search_keys(self, query: str) -> list[str]:
        query = (query
            .lower()
            .strip())

        results = []

        for key in self.__localization_dict.keys():
            parsed_key = (key
                .lower()
                .strip())

            if query in parsed_key:
                results.append(key)

        return results

    @validate_arguments
    def search_values(self, query: str) -> list[str] | list:
        query = (query
            .lower()
            .strip())

        results = []

        for value in self.__localization_dict.values():
            parsed_value = (value
                .lower()
                .strip())

            if query in parsed_value:
                results.append(value)

        return results

    @validate_arguments
    def compare(
        self,
        old_localization: Any
    ) -> dict[str, list]:
        if isinstance(old_localization, list):
            old_localization = FromDictList(old_localization).merge_dicts()

        elif not isinstance(old_localization, dict):
            old_localization = old_localization.dict

        new_fields = []
        edited_fields = []

        old_localization_keys = dict(old_localization).keys()

        for key in self.__localization_dict.keys():
            if key not in old_localization_keys:
                new_fields.append({
                    "key": key,
                    "value": self.__localization_dict[key]
                })

        for key in old_localization_keys:
            if old_localization[key] != self.__localization_dict[key]:
                edited_fields.append({
                    "key": key,
                    "old_value": old_localization[key],
                    "new_value": self.__localization_dict[key]
                })

        return dict(
            new_fields = new_fields,
            edited_fields = edited_fields
        )

    @property
    def list(self) -> list[dict[str, str]]:
        return self.__localization_list

    @property
    def dict(self) -> dict[str, str]:
        return self.__localization_dict

__all__ = [ "Localization" ]
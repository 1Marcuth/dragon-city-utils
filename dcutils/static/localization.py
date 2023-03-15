from pydantic import validate_arguments
from pyfilter import FromDictList
import httpx

class Localization:
    @validate_arguments
    def __init__(
        self,
        language: str | None = None,
        loc: list[dict] | dict | None = None
    ) -> None:
        if language:
            self.__endpoint_url = f"https://sp-translations.socialpointgames.com/deploy/dc/android/prod/dc_android_{language}_prod_wetd46pWuR8J5CmS.json"
            self.__localization = self.__fetch()
            self.__localization_dict = FromDictList(self.__localization).concatenate_child_dicts_into_a_new_dict()

        elif loc:
            self.__load(loc)

        else:
            raise ValueError()

    def __fetch(self) -> list[dict]:
        response = httpx.get(self.__endpoint_url)
        data = response.json()
        return data

    @validate_arguments
    def __load(self, loc: list | dict):
        type_ = type(loc)

        if type_ == list:
            self.__load_list(list(loc))

        elif type_ == dict:
            self.__load_dict(dict(loc))

        else:
            raise ValueError(f"{type_} is an invalid type to load a localization")

    @validate_arguments
    def __load_list(self, loc: list[dict]):
        self.__localization = loc
        self.__localization_dict = FromDictList(loc).concatenate_child_dicts_into_a_new_dict()

    @validate_arguments
    def __load_dict(self, loc: dict):
        self.__localization_dict = loc
        self.__localization = []

        for key, value in loc.items():
            dict_ = { key: value }
            self.__localization.append(dict_)

    @validate_arguments
    def get_value_from_key(self, key: str) -> str | None:
        if key in self.__localization_dict.keys():
            return self.__localization_dict[key]

    @validate_arguments
    def get_key_from_value(self, value: str) -> str | None:
        for dict_key, dict_value in self.__localization_dict.items():
            if dict_value == value:
                return dict_key

    @validate_arguments
    def get_dragon_name(self, id: int) -> str | None:
        key = f"tid_unit_{id}_name"
        return self.get_value_from_key(key)

    @validate_arguments
    def get_dragon_description(self, id: int) -> str | None:
        key = f"tid_unit_{id}_description"
        return self.get_value_from_key(key)

    @validate_arguments
    def get_attack_name(self, id: int) -> str | None:
        key = f"tid_attack_name_{id}"
        return self.get_value_from_key(key)

    @validate_arguments
    def get_skill_name(self, id: int) -> str | None:
        key = f"tid_skill_name_{id}"
        return self.get_value_from_key(key)

    @validate_arguments
    def get_skill_description(self, id: int) -> str | None:
        key = f"tid_skill_description_{id}"
        return self.get_value_from_key(key)

    @validate_arguments
    def search_keys(self, query: str) -> list[str] | list:
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
    def compare(self, old_localization: dict | list) -> dict[str, list]:
        if type(old_localization) == list:
            old_localization = FromDictList(list(old_localization)).concatenate_child_dicts_into_a_new_dict()

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

    def get_list(self):
        return self.__localization

    def get_dict(self):
        return self.__localization_dict

__all__ = [ "Localization" ]
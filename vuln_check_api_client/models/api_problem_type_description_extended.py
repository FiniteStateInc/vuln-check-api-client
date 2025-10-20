from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProblemTypeDescriptionExtended")


@_attrs_define
class ApiProblemTypeDescriptionExtended:
    """
    Attributes:
        lang (Union[Unset, str]):
        name (Union[Unset, str]):
        url (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    lang: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lang = self.lang

        name = self.name

        url = self.url

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lang is not UNSET:
            field_dict["lang"] = lang
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lang = d.pop("lang", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        value = d.pop("value", UNSET)

        api_problem_type_description_extended = cls(
            lang=lang,
            name=name,
            url=url,
            value=value,
        )

        api_problem_type_description_extended.additional_properties = d
        return api_problem_type_description_extended

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

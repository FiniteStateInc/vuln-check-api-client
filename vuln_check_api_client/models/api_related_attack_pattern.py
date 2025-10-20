from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiRelatedAttackPattern")


@_attrs_define
class ApiRelatedAttackPattern:
    """
    Attributes:
        capec_id (Union[Unset, str]):
        capec_name (Union[Unset, str]):
        capec_url (Union[Unset, str]):
        lang (Union[Unset, str]):
    """

    capec_id: Union[Unset, str] = UNSET
    capec_name: Union[Unset, str] = UNSET
    capec_url: Union[Unset, str] = UNSET
    lang: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        capec_id = self.capec_id

        capec_name = self.capec_name

        capec_url = self.capec_url

        lang = self.lang

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if capec_id is not UNSET:
            field_dict["capec_id"] = capec_id
        if capec_name is not UNSET:
            field_dict["capec_name"] = capec_name
        if capec_url is not UNSET:
            field_dict["capec_url"] = capec_url
        if lang is not UNSET:
            field_dict["lang"] = lang

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        capec_id = d.pop("capec_id", UNSET)

        capec_name = d.pop("capec_name", UNSET)

        capec_url = d.pop("capec_url", UNSET)

        lang = d.pop("lang", UNSET)

        api_related_attack_pattern = cls(
            capec_id=capec_id,
            capec_name=capec_name,
            capec_url=capec_url,
            lang=lang,
        )

        api_related_attack_pattern.additional_properties = d
        return api_related_attack_pattern

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

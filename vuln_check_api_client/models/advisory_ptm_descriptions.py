from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryPTMDescriptions")


@_attrs_define
class AdvisoryPTMDescriptions:
    """
    Attributes:
        cwe_id (Union[Unset, str]):
        description (Union[Unset, str]):
        lang (Union[Unset, str]):
        type_ (Union[Unset, str]):
    """

    cwe_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    lang: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cwe_id = self.cwe_id

        description = self.description

        lang = self.lang

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cwe_id is not UNSET:
            field_dict["cweId"] = cwe_id
        if description is not UNSET:
            field_dict["description"] = description
        if lang is not UNSET:
            field_dict["lang"] = lang
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cwe_id = d.pop("cweId", UNSET)

        description = d.pop("description", UNSET)

        lang = d.pop("lang", UNSET)

        type_ = d.pop("type", UNSET)

        advisory_ptm_descriptions = cls(
            cwe_id=cwe_id,
            description=description,
            lang=lang,
            type_=type_,
        )

        advisory_ptm_descriptions.additional_properties = d
        return advisory_ptm_descriptions

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

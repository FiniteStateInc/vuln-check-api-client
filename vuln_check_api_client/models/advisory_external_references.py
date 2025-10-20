from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryExternalReferences")


@_attrs_define
class AdvisoryExternalReferences:
    """
    Attributes:
        description (Union[Unset, str]):
        external_id (Union[Unset, str]):
        source_name (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    description: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    source_name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        external_id = self.external_id

        source_name = self.source_name

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if source_name is not UNSET:
            field_dict["source_name"] = source_name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        external_id = d.pop("external_id", UNSET)

        source_name = d.pop("source_name", UNSET)

        url = d.pop("url", UNSET)

        advisory_external_references = cls(
            description=description,
            external_id=external_id,
            source_name=source_name,
            url=url,
        )

        advisory_external_references.additional_properties = d
        return advisory_external_references

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

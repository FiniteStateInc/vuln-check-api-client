from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryMProviderMetadata")


@_attrs_define
class AdvisoryMProviderMetadata:
    """
    Attributes:
        date_updated (Union[Unset, str]): FIXME: flip to time
        org_id (Union[Unset, str]):
        short_name (Union[Unset, str]):
    """

    date_updated: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_updated = self.date_updated

        org_id = self.org_id

        short_name = self.short_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_updated is not UNSET:
            field_dict["dateUpdated"] = date_updated
        if org_id is not UNSET:
            field_dict["orgId"] = org_id
        if short_name is not UNSET:
            field_dict["shortName"] = short_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date_updated = d.pop("dateUpdated", UNSET)

        org_id = d.pop("orgId", UNSET)

        short_name = d.pop("shortName", UNSET)

        advisory_m_provider_metadata = cls(
            date_updated=date_updated,
            org_id=org_id,
            short_name=short_name,
        )

        advisory_m_provider_metadata.additional_properties = d
        return advisory_m_provider_metadata

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

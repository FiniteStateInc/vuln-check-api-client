from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryVendorNameForThreatActor")


@_attrs_define
class AdvisoryVendorNameForThreatActor:
    """
    Attributes:
        threat_actor_name (Union[Unset, str]):
        url (Union[Unset, str]):
        vendor_name (Union[Unset, str]):
    """

    threat_actor_name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    vendor_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        threat_actor_name = self.threat_actor_name

        url = self.url

        vendor_name = self.vendor_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if threat_actor_name is not UNSET:
            field_dict["threat_actor_name"] = threat_actor_name
        if url is not UNSET:
            field_dict["url"] = url
        if vendor_name is not UNSET:
            field_dict["vendor_name"] = vendor_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        threat_actor_name = d.pop("threat_actor_name", UNSET)

        url = d.pop("url", UNSET)

        vendor_name = d.pop("vendor_name", UNSET)

        advisory_vendor_name_for_threat_actor = cls(
            threat_actor_name=threat_actor_name,
            url=url,
            vendor_name=vendor_name,
        )

        advisory_vendor_name_for_threat_actor.additional_properties = d
        return advisory_vendor_name_for_threat_actor

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

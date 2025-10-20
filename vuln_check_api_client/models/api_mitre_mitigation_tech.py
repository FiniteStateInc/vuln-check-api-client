from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiMitreMitigationTech")


@_attrs_define
class ApiMitreMitigationTech:
    """
    Attributes:
        description (Union[Unset, str]):
        id (Union[Unset, str]):
        mitigation_url (Union[Unset, str]):
    """

    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    mitigation_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        id = self.id

        mitigation_url = self.mitigation_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if mitigation_url is not UNSET:
            field_dict["mitigation_url"] = mitigation_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        mitigation_url = d.pop("mitigation_url", UNSET)

        api_mitre_mitigation_tech = cls(
            description=description,
            id=id,
            mitigation_url=mitigation_url,
        )

        api_mitre_mitigation_tech.additional_properties = d
        return api_mitre_mitigation_tech

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

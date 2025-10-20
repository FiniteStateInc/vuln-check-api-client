from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCweAcceptanceLevel")


@_attrs_define
class AdvisoryCweAcceptanceLevel:
    """
    Attributes:
        description (Union[Unset, str]):
        last_modified (Union[Unset, str]):
    """

    description: Union[Unset, str] = UNSET
    last_modified: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        last_modified = self.last_modified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        last_modified = d.pop("lastModified", UNSET)

        advisory_cwe_acceptance_level = cls(
            description=description,
            last_modified=last_modified,
        )

        advisory_cwe_acceptance_level.additional_properties = d
        return advisory_cwe_acceptance_level

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

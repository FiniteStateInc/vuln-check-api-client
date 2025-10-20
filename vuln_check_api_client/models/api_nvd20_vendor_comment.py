from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiNVD20VendorComment")


@_attrs_define
class ApiNVD20VendorComment:
    """
    Attributes:
        comment (Union[Unset, str]):
        last_modified (Union[Unset, str]):
        organization (Union[Unset, str]):
    """

    comment: Union[Unset, str] = UNSET
    last_modified: Union[Unset, str] = UNSET
    organization: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        last_modified = self.last_modified

        organization = self.organization

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if organization is not UNSET:
            field_dict["organization"] = organization

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment = d.pop("comment", UNSET)

        last_modified = d.pop("lastModified", UNSET)

        organization = d.pop("organization", UNSET)

        api_nvd20_vendor_comment = cls(
            comment=comment,
            last_modified=last_modified,
            organization=organization,
        )

        api_nvd20_vendor_comment.additional_properties = d
        return api_nvd20_vendor_comment

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

from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiCPEName")


@_attrs_define
class ApiCPEName:
    """
    Attributes:
        cpe_22_uri (Union[Unset, str]):
        cpe_23_uri (Union[Unset, str]):
        last_modified_date (Union[Unset, str]):
    """

    cpe_22_uri: Union[Unset, str] = UNSET
    cpe_23_uri: Union[Unset, str] = UNSET
    last_modified_date: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpe_22_uri = self.cpe_22_uri

        cpe_23_uri = self.cpe_23_uri

        last_modified_date = self.last_modified_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpe_22_uri is not UNSET:
            field_dict["cpe22Uri"] = cpe_22_uri
        if cpe_23_uri is not UNSET:
            field_dict["cpe23Uri"] = cpe_23_uri
        if last_modified_date is not UNSET:
            field_dict["lastModifiedDate"] = last_modified_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cpe_22_uri = d.pop("cpe22Uri", UNSET)

        cpe_23_uri = d.pop("cpe23Uri", UNSET)

        last_modified_date = d.pop("lastModifiedDate", UNSET)

        api_cpe_name = cls(
            cpe_22_uri=cpe_22_uri,
            cpe_23_uri=cpe_23_uri,
            last_modified_date=last_modified_date,
        )

        api_cpe_name.additional_properties = d
        return api_cpe_name

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

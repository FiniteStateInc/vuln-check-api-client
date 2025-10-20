from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiNVD20CPEName")


@_attrs_define
class ApiNVD20CPEName:
    """
    Attributes:
        cpe_name (Union[Unset, str]):
        cpe_name_id (Union[Unset, str]):
    """

    cpe_name: Union[Unset, str] = UNSET
    cpe_name_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpe_name = self.cpe_name

        cpe_name_id = self.cpe_name_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpe_name is not UNSET:
            field_dict["cpeName"] = cpe_name
        if cpe_name_id is not UNSET:
            field_dict["cpeNameId"] = cpe_name_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cpe_name = d.pop("cpeName", UNSET)

        cpe_name_id = d.pop("cpeNameId", UNSET)

        api_nvd20cpe_name = cls(
            cpe_name=cpe_name,
            cpe_name_id=cpe_name_id,
        )

        api_nvd20cpe_name.additional_properties = d
        return api_nvd20cpe_name

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

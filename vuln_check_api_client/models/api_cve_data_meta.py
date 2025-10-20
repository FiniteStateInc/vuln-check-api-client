from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiCVEDataMeta")


@_attrs_define
class ApiCVEDataMeta:
    """
    Attributes:
        assigner (Union[Unset, str]):
        id (Union[Unset, str]):
    """

    assigner: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigner = self.assigner

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assigner is not UNSET:
            field_dict["ASSIGNER"] = assigner
        if id is not UNSET:
            field_dict["ID"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assigner = d.pop("ASSIGNER", UNSET)

        id = d.pop("ID", UNSET)

        api_cve_data_meta = cls(
            assigner=assigner,
            id=id,
        )

        api_cve_data_meta.additional_properties = d
        return api_cve_data_meta

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

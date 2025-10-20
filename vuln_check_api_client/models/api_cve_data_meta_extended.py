from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiCVEDataMetaExtended")


@_attrs_define
class ApiCVEDataMetaExtended:
    """
    Attributes:
        alias (Union[Unset, str]):
        assigner (Union[Unset, str]):
        id (Union[Unset, str]):
        status (Union[Unset, str]):
    """

    alias: Union[Unset, str] = UNSET
    assigner: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alias = self.alias

        assigner = self.assigner

        id = self.id

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alias is not UNSET:
            field_dict["ALIAS"] = alias
        if assigner is not UNSET:
            field_dict["ASSIGNER"] = assigner
        if id is not UNSET:
            field_dict["ID"] = id
        if status is not UNSET:
            field_dict["STATUS"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alias = d.pop("ALIAS", UNSET)

        assigner = d.pop("ASSIGNER", UNSET)

        id = d.pop("ID", UNSET)

        status = d.pop("STATUS", UNSET)

        api_cve_data_meta_extended = cls(
            alias=alias,
            assigner=assigner,
            id=id,
            status=status,
        )

        api_cve_data_meta_extended.additional_properties = d
        return api_cve_data_meta_extended

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

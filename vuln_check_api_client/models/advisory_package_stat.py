from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryPackageStat")


@_attrs_define
class AdvisoryPackageStat:
    """
    Attributes:
        cpe (Union[Unset, str]):
        fix_state (Union[Unset, str]):
        package_name (Union[Unset, str]):
        product_name (Union[Unset, str]):
    """

    cpe: Union[Unset, str] = UNSET
    fix_state: Union[Unset, str] = UNSET
    package_name: Union[Unset, str] = UNSET
    product_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpe = self.cpe

        fix_state = self.fix_state

        package_name = self.package_name

        product_name = self.product_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpe is not UNSET:
            field_dict["cpe"] = cpe
        if fix_state is not UNSET:
            field_dict["fix_state"] = fix_state
        if package_name is not UNSET:
            field_dict["package_name"] = package_name
        if product_name is not UNSET:
            field_dict["product_name"] = product_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cpe = d.pop("cpe", UNSET)

        fix_state = d.pop("fix_state", UNSET)

        package_name = d.pop("package_name", UNSET)

        product_name = d.pop("product_name", UNSET)

        advisory_package_stat = cls(
            cpe=cpe,
            fix_state=fix_state,
            package_name=package_name,
            product_name=product_name,
        )

        advisory_package_stat.additional_properties = d
        return advisory_package_stat

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

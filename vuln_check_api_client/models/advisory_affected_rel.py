from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryAffectedRel")


@_attrs_define
class AdvisoryAffectedRel:
    """
    Attributes:
        advisory (Union[Unset, str]):
        cpe (Union[Unset, str]):
        package (Union[Unset, str]):
        product_name (Union[Unset, str]):
        release_date (Union[Unset, str]):
    """

    advisory: Union[Unset, str] = UNSET
    cpe: Union[Unset, str] = UNSET
    package: Union[Unset, str] = UNSET
    product_name: Union[Unset, str] = UNSET
    release_date: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advisory = self.advisory

        cpe = self.cpe

        package = self.package

        product_name = self.product_name

        release_date = self.release_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advisory is not UNSET:
            field_dict["advisory"] = advisory
        if cpe is not UNSET:
            field_dict["cpe"] = cpe
        if package is not UNSET:
            field_dict["package"] = package
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if release_date is not UNSET:
            field_dict["release_date"] = release_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        advisory = d.pop("advisory", UNSET)

        cpe = d.pop("cpe", UNSET)

        package = d.pop("package", UNSET)

        product_name = d.pop("product_name", UNSET)

        release_date = d.pop("release_date", UNSET)

        advisory_affected_rel = cls(
            advisory=advisory,
            cpe=cpe,
            package=package,
            product_name=product_name,
            release_date=release_date,
        )

        advisory_affected_rel.additional_properties = d
        return advisory_affected_rel

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

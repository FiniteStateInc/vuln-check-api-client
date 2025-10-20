from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryAffectedProduct")


@_attrs_define
class AdvisoryAffectedProduct:
    """
    Attributes:
        affected_releases (Union[Unset, str]):
        fixed_releases (Union[Unset, str]):
        lexmark_models (Union[Unset, str]):
    """

    affected_releases: Union[Unset, str] = UNSET
    fixed_releases: Union[Unset, str] = UNSET
    lexmark_models: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_releases = self.affected_releases

        fixed_releases = self.fixed_releases

        lexmark_models = self.lexmark_models

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_releases is not UNSET:
            field_dict["affectedReleases"] = affected_releases
        if fixed_releases is not UNSET:
            field_dict["fixedReleases"] = fixed_releases
        if lexmark_models is not UNSET:
            field_dict["lexmarkModels"] = lexmark_models

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_releases = d.pop("affectedReleases", UNSET)

        fixed_releases = d.pop("fixedReleases", UNSET)

        lexmark_models = d.pop("lexmarkModels", UNSET)

        advisory_affected_product = cls(
            affected_releases=affected_releases,
            fixed_releases=fixed_releases,
            lexmark_models=lexmark_models,
        )

        advisory_affected_product.additional_properties = d
        return advisory_affected_product

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

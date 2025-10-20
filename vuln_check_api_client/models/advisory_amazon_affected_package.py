from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryAmazonAffectedPackage")


@_attrs_define
class AdvisoryAmazonAffectedPackage:
    """
    Attributes:
        advisory (Union[Unset, str]):
        package (Union[Unset, str]):
        platform (Union[Unset, str]):
        release_date (Union[Unset, str]):
        status (Union[Unset, str]):
    """

    advisory: Union[Unset, str] = UNSET
    package: Union[Unset, str] = UNSET
    platform: Union[Unset, str] = UNSET
    release_date: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advisory = self.advisory

        package = self.package

        platform = self.platform

        release_date = self.release_date

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advisory is not UNSET:
            field_dict["advisory"] = advisory
        if package is not UNSET:
            field_dict["package"] = package
        if platform is not UNSET:
            field_dict["platform"] = platform
        if release_date is not UNSET:
            field_dict["releaseDate"] = release_date
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        advisory = d.pop("advisory", UNSET)

        package = d.pop("package", UNSET)

        platform = d.pop("platform", UNSET)

        release_date = d.pop("releaseDate", UNSET)

        status = d.pop("status", UNSET)

        advisory_amazon_affected_package = cls(
            advisory=advisory,
            package=package,
            platform=platform,
            release_date=release_date,
            status=status,
        )

        advisory_amazon_affected_package.additional_properties = d
        return advisory_amazon_affected_package

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

from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiOSSPackageResearchAttributes")


@_attrs_define
class ApiOSSPackageResearchAttributes:
    """
    Attributes:
        abandoned (Union[Unset, bool]):
        eol (Union[Unset, bool]):
        is_malicious (Union[Unset, bool]):
        malicious_source (Union[Unset, str]):
        repo_hijackable (Union[Unset, bool]):
        squatted_package (Union[Unset, str]):
    """

    abandoned: Union[Unset, bool] = UNSET
    eol: Union[Unset, bool] = UNSET
    is_malicious: Union[Unset, bool] = UNSET
    malicious_source: Union[Unset, str] = UNSET
    repo_hijackable: Union[Unset, bool] = UNSET
    squatted_package: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        abandoned = self.abandoned

        eol = self.eol

        is_malicious = self.is_malicious

        malicious_source = self.malicious_source

        repo_hijackable = self.repo_hijackable

        squatted_package = self.squatted_package

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if abandoned is not UNSET:
            field_dict["abandoned"] = abandoned
        if eol is not UNSET:
            field_dict["eol"] = eol
        if is_malicious is not UNSET:
            field_dict["is_malicious"] = is_malicious
        if malicious_source is not UNSET:
            field_dict["malicious_source"] = malicious_source
        if repo_hijackable is not UNSET:
            field_dict["repo_hijackable"] = repo_hijackable
        if squatted_package is not UNSET:
            field_dict["squatted_package"] = squatted_package

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        abandoned = d.pop("abandoned", UNSET)

        eol = d.pop("eol", UNSET)

        is_malicious = d.pop("is_malicious", UNSET)

        malicious_source = d.pop("malicious_source", UNSET)

        repo_hijackable = d.pop("repo_hijackable", UNSET)

        squatted_package = d.pop("squatted_package", UNSET)

        api_oss_package_research_attributes = cls(
            abandoned=abandoned,
            eol=eol,
            is_malicious=is_malicious,
            malicious_source=malicious_source,
            repo_hijackable=repo_hijackable,
            squatted_package=squatted_package,
        )

        api_oss_package_research_attributes.additional_properties = d
        return api_oss_package_research_attributes

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

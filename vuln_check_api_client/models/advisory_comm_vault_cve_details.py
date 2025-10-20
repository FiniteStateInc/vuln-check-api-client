from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCommVaultCVEDetails")


@_attrs_define
class AdvisoryCommVaultCVEDetails:
    """
    Attributes:
        cve_id (Union[Unset, str]):
        cvss (Union[Unset, str]):
        description (Union[Unset, str]):
        external_links (Union[Unset, list[str]]):
    """

    cve_id: Union[Unset, str] = UNSET
    cvss: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    external_links: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve_id = self.cve_id

        cvss = self.cvss

        description = self.description

        external_links: Union[Unset, list[str]] = UNSET
        if not isinstance(self.external_links, Unset):
            external_links = self.external_links

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve_id is not UNSET:
            field_dict["cve_id"] = cve_id
        if cvss is not UNSET:
            field_dict["cvss"] = cvss
        if description is not UNSET:
            field_dict["description"] = description
        if external_links is not UNSET:
            field_dict["external_links"] = external_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve_id = d.pop("cve_id", UNSET)

        cvss = d.pop("cvss", UNSET)

        description = d.pop("description", UNSET)

        external_links = cast(list[str], d.pop("external_links", UNSET))

        advisory_comm_vault_cve_details = cls(
            cve_id=cve_id,
            cvss=cvss,
            description=description,
            external_links=external_links,
        )

        advisory_comm_vault_cve_details.additional_properties = d
        return advisory_comm_vault_cve_details

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

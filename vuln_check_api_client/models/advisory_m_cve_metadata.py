from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryMCveMetadata")


@_attrs_define
class AdvisoryMCveMetadata:
    """
    Attributes:
        assigner_org_id (Union[Unset, str]):
        assigner_short_name (Union[Unset, str]):
        cve_id (Union[Unset, str]):
        date_published (Union[Unset, str]):
        date_reserved (Union[Unset, str]):
        date_updated (Union[Unset, str]):
        state (Union[Unset, str]):
    """

    assigner_org_id: Union[Unset, str] = UNSET
    assigner_short_name: Union[Unset, str] = UNSET
    cve_id: Union[Unset, str] = UNSET
    date_published: Union[Unset, str] = UNSET
    date_reserved: Union[Unset, str] = UNSET
    date_updated: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigner_org_id = self.assigner_org_id

        assigner_short_name = self.assigner_short_name

        cve_id = self.cve_id

        date_published = self.date_published

        date_reserved = self.date_reserved

        date_updated = self.date_updated

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assigner_org_id is not UNSET:
            field_dict["assignerOrgId"] = assigner_org_id
        if assigner_short_name is not UNSET:
            field_dict["assignerShortName"] = assigner_short_name
        if cve_id is not UNSET:
            field_dict["cveId"] = cve_id
        if date_published is not UNSET:
            field_dict["datePublished"] = date_published
        if date_reserved is not UNSET:
            field_dict["dateReserved"] = date_reserved
        if date_updated is not UNSET:
            field_dict["dateUpdated"] = date_updated
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assigner_org_id = d.pop("assignerOrgId", UNSET)

        assigner_short_name = d.pop("assignerShortName", UNSET)

        cve_id = d.pop("cveId", UNSET)

        date_published = d.pop("datePublished", UNSET)

        date_reserved = d.pop("dateReserved", UNSET)

        date_updated = d.pop("dateUpdated", UNSET)

        state = d.pop("state", UNSET)

        advisory_m_cve_metadata = cls(
            assigner_org_id=assigner_org_id,
            assigner_short_name=assigner_short_name,
            cve_id=cve_id,
            date_published=date_published,
            date_reserved=date_reserved,
            date_updated=date_updated,
            state=state,
        )

        advisory_m_cve_metadata.additional_properties = d
        return advisory_m_cve_metadata

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

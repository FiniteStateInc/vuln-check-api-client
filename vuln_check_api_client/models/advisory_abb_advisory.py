from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryABBAdvisory")


@_attrs_define
class AdvisoryABBAdvisory:
    """
    Attributes:
        abb_vulnerability_id (Union[Unset, list[str]]):
        csaf (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        document_id (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    abb_vulnerability_id: Union[Unset, list[str]] = UNSET
    csaf: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    document_id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        abb_vulnerability_id: Union[Unset, list[str]] = UNSET
        if not isinstance(self.abb_vulnerability_id, Unset):
            abb_vulnerability_id = self.abb_vulnerability_id

        csaf = self.csaf

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        document_id = self.document_id

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if abb_vulnerability_id is not UNSET:
            field_dict["abb_vulnerability_id"] = abb_vulnerability_id
        if csaf is not UNSET:
            field_dict["csaf"] = csaf
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        abb_vulnerability_id = cast(list[str], d.pop("abb_vulnerability_id", UNSET))

        csaf = d.pop("csaf", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        document_id = d.pop("document_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        advisory_abb_advisory = cls(
            abb_vulnerability_id=abb_vulnerability_id,
            csaf=csaf,
            cve=cve,
            date_added=date_added,
            document_id=document_id,
            updated_at=updated_at,
            url=url,
        )

        advisory_abb_advisory.additional_properties = d
        return advisory_abb_advisory

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

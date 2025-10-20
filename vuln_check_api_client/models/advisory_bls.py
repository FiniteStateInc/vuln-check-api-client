from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryBLS")


@_attrs_define
class AdvisoryBLS:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        cvss (Union[Unset, str]):
        date_added (Union[Unset, str]):
        prodcut (Union[Unset, str]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
        vendor (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    cvss: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    prodcut: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvss = self.cvss

        date_added = self.date_added

        prodcut = self.prodcut

        summary = self.summary

        title = self.title

        url = self.url

        vendor = self.vendor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss is not UNSET:
            field_dict["cvss"] = cvss
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if prodcut is not UNSET:
            field_dict["prodcut"] = prodcut
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url
        if vendor is not UNSET:
            field_dict["vendor"] = vendor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        cvss = d.pop("cvss", UNSET)

        date_added = d.pop("date_added", UNSET)

        prodcut = d.pop("prodcut", UNSET)

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        vendor = d.pop("vendor", UNSET)

        advisory_bls = cls(
            cve=cve,
            cvss=cvss,
            date_added=date_added,
            prodcut=prodcut,
            summary=summary,
            title=title,
            url=url,
            vendor=vendor,
        )

        advisory_bls.additional_properties = d
        return advisory_bls

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

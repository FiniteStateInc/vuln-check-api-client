from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCertIRSecurityAlert")


@_attrs_define
class AdvisoryCertIRSecurityAlert:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        summary_fa (Union[Unset, str]):
        title_fa (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    summary_fa: Union[Unset, str] = UNSET
    title_fa: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        summary_fa = self.summary_fa

        title_fa = self.title_fa

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if references is not UNSET:
            field_dict["references"] = references
        if summary_fa is not UNSET:
            field_dict["summary_fa"] = summary_fa
        if title_fa is not UNSET:
            field_dict["title_fa"] = title_fa
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        summary_fa = d.pop("summary_fa", UNSET)

        title_fa = d.pop("title_fa", UNSET)

        url = d.pop("url", UNSET)

        advisory_cert_ir_security_alert = cls(
            cve=cve,
            date_added=date_added,
            references=references,
            summary_fa=summary_fa,
            title_fa=title_fa,
            url=url,
        )

        advisory_cert_ir_security_alert.additional_properties = d
        return advisory_cert_ir_security_alert

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

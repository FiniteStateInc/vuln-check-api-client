from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCertSE")


@_attrs_define
class AdvisoryCertSE:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        summary_sv (Union[Unset, str]):
        title_sv (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    summary_sv: Union[Unset, str] = UNSET
    title_sv: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        summary_sv = self.summary_sv

        title_sv = self.title_sv

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if summary_sv is not UNSET:
            field_dict["summary_sv"] = summary_sv
        if title_sv is not UNSET:
            field_dict["title_sv"] = title_sv
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        summary_sv = d.pop("summary_sv", UNSET)

        title_sv = d.pop("title_sv", UNSET)

        url = d.pop("url", UNSET)

        advisory_cert_se = cls(
            cve=cve,
            date_added=date_added,
            summary_sv=summary_sv,
            title_sv=title_sv,
            url=url,
        )

        advisory_cert_se.additional_properties = d
        return advisory_cert_se

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

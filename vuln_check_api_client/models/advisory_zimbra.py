from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryZimbra")


@_attrs_define
class AdvisoryZimbra:
    """
    Attributes:
        bugs (Union[Unset, list[int]]):
        cve (Union[Unset, list[str]]):
        cvss (Union[Unset, str]):
        date_added (Union[Unset, str]):
        fix (Union[Unset, str]):
        rating (Union[Unset, str]):
        reporter (Union[Unset, str]):
        summary (Union[Unset, str]):
    """

    bugs: Union[Unset, list[int]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvss: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    fix: Union[Unset, str] = UNSET
    rating: Union[Unset, str] = UNSET
    reporter: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bugs: Union[Unset, list[int]] = UNSET
        if not isinstance(self.bugs, Unset):
            bugs = self.bugs

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvss = self.cvss

        date_added = self.date_added

        fix = self.fix

        rating = self.rating

        reporter = self.reporter

        summary = self.summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bugs is not UNSET:
            field_dict["bugs"] = bugs
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss is not UNSET:
            field_dict["cvss"] = cvss
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if fix is not UNSET:
            field_dict["fix"] = fix
        if rating is not UNSET:
            field_dict["rating"] = rating
        if reporter is not UNSET:
            field_dict["reporter"] = reporter
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bugs = cast(list[int], d.pop("bugs", UNSET))

        cve = cast(list[str], d.pop("cve", UNSET))

        cvss = d.pop("cvss", UNSET)

        date_added = d.pop("date_added", UNSET)

        fix = d.pop("fix", UNSET)

        rating = d.pop("rating", UNSET)

        reporter = d.pop("reporter", UNSET)

        summary = d.pop("summary", UNSET)

        advisory_zimbra = cls(
            bugs=bugs,
            cve=cve,
            cvss=cvss,
            date_added=date_added,
            fix=fix,
            rating=rating,
            reporter=reporter,
            summary=summary,
        )

        advisory_zimbra.additional_properties = d
        return advisory_zimbra

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

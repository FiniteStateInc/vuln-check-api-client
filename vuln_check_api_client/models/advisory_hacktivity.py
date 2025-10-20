from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryHacktivity")


@_attrs_define
class AdvisoryHacktivity:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        float64 (Union[Unset, float]):
        rank (Union[Unset, int]):
        reports_submitted (Union[Unset, int]):
        summary (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    float64: Union[Unset, float] = UNSET
    rank: Union[Unset, int] = UNSET
    reports_submitted: Union[Unset, int] = UNSET
    summary: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        float64 = self.float64

        rank = self.rank

        reports_submitted = self.reports_submitted

        summary = self.summary

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if float64 is not UNSET:
            field_dict["float64"] = float64
        if rank is not UNSET:
            field_dict["rank"] = rank
        if reports_submitted is not UNSET:
            field_dict["reports_submitted"] = reports_submitted
        if summary is not UNSET:
            field_dict["summary"] = summary
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        float64 = d.pop("float64", UNSET)

        rank = d.pop("rank", UNSET)

        reports_submitted = d.pop("reports_submitted", UNSET)

        summary = d.pop("summary", UNSET)

        url = d.pop("url", UNSET)

        advisory_hacktivity = cls(
            cve=cve,
            date_added=date_added,
            float64=float64,
            rank=rank,
            reports_submitted=reports_submitted,
            summary=summary,
            url=url,
        )

        advisory_hacktivity.additional_properties = d
        return advisory_hacktivity

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

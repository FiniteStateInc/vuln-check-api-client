from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_osv_obj import AdvisoryOSVObj


T = TypeVar("T", bound="AdvisoryOSV")


@_attrs_define
class AdvisoryOSV:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        date_updated (Union[Unset, str]):
        osv (Union[Unset, AdvisoryOSVObj]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    date_updated: Union[Unset, str] = UNSET
    osv: Union[Unset, "AdvisoryOSVObj"] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        date_updated = self.date_updated

        osv: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.osv, Unset):
            osv = self.osv.to_dict()

        summary = self.summary

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_updated is not UNSET:
            field_dict["date_updated"] = date_updated
        if osv is not UNSET:
            field_dict["osv"] = osv
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_osv_obj import AdvisoryOSVObj

        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        date_updated = d.pop("date_updated", UNSET)

        _osv = d.pop("osv", UNSET)
        osv: Union[Unset, AdvisoryOSVObj]
        if isinstance(_osv, Unset):
            osv = UNSET
        else:
            osv = AdvisoryOSVObj.from_dict(_osv)

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_osv = cls(
            cve=cve,
            date_added=date_added,
            date_updated=date_updated,
            osv=osv,
            summary=summary,
            title=title,
            url=url,
        )

        advisory_osv.additional_properties = d
        return advisory_osv

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

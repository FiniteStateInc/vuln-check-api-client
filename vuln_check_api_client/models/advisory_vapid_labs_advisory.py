from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryVapidLabsAdvisory")


@_attrs_define
class AdvisoryVapidLabsAdvisory:
    """
    Attributes:
        author (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        exploit (Union[Unset, str]):
        link (Union[Unset, str]):
        title (Union[Unset, str]):
        vapid_id (Union[Unset, str]):
        vendor (Union[Unset, str]):
        vulnerability (Union[Unset, str]):
    """

    author: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    exploit: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    vapid_id: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    vulnerability: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author = self.author

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        description = self.description

        exploit = self.exploit

        link = self.link

        title = self.title

        vapid_id = self.vapid_id

        vendor = self.vendor

        vulnerability = self.vulnerability

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if exploit is not UNSET:
            field_dict["exploit"] = exploit
        if link is not UNSET:
            field_dict["link"] = link
        if title is not UNSET:
            field_dict["title"] = title
        if vapid_id is not UNSET:
            field_dict["vapidId"] = vapid_id
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if vulnerability is not UNSET:
            field_dict["vulnerability"] = vulnerability

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        author = d.pop("author", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        exploit = d.pop("exploit", UNSET)

        link = d.pop("link", UNSET)

        title = d.pop("title", UNSET)

        vapid_id = d.pop("vapidId", UNSET)

        vendor = d.pop("vendor", UNSET)

        vulnerability = d.pop("vulnerability", UNSET)

        advisory_vapid_labs_advisory = cls(
            author=author,
            cve=cve,
            date_added=date_added,
            description=description,
            exploit=exploit,
            link=link,
            title=title,
            vapid_id=vapid_id,
            vendor=vendor,
            vulnerability=vulnerability,
        )

        advisory_vapid_labs_advisory.additional_properties = d
        return advisory_vapid_labs_advisory

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

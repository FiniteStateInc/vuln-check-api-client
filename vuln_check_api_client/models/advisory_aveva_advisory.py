from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryAVEVAAdvisory")


@_attrs_define
class AdvisoryAVEVAAdvisory:
    """
    Attributes:
        aveva_vulnerability_id (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cwe (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        published_by (Union[Unset, str]):
        rating (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    aveva_vulnerability_id: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cwe: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    published_by: Union[Unset, str] = UNSET
    rating: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aveva_vulnerability_id = self.aveva_vulnerability_id

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cwe: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cwe, Unset):
            cwe = self.cwe

        date_added = self.date_added

        published_by = self.published_by

        rating = self.rating

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aveva_vulnerability_id is not UNSET:
            field_dict["aveva_vulnerability_id"] = aveva_vulnerability_id
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cwe is not UNSET:
            field_dict["cwe"] = cwe
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if published_by is not UNSET:
            field_dict["published_by"] = published_by
        if rating is not UNSET:
            field_dict["rating"] = rating
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aveva_vulnerability_id = d.pop("aveva_vulnerability_id", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cwe = cast(list[str], d.pop("cwe", UNSET))

        date_added = d.pop("date_added", UNSET)

        published_by = d.pop("published_by", UNSET)

        rating = d.pop("rating", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_aveva_advisory = cls(
            aveva_vulnerability_id=aveva_vulnerability_id,
            cve=cve,
            cwe=cwe,
            date_added=date_added,
            published_by=published_by,
            rating=rating,
            title=title,
            url=url,
        )

        advisory_aveva_advisory.additional_properties = d
        return advisory_aveva_advisory

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

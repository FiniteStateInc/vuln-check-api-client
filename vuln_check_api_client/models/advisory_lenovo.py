from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryLenovo")


@_attrs_define
class AdvisoryLenovo:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        industry_identifiers (Union[Unset, list[str]]):
        last_updated (Union[Unset, str]):
        lenovo_id (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    industry_identifiers: Union[Unset, list[str]] = UNSET
    last_updated: Union[Unset, str] = UNSET
    lenovo_id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        industry_identifiers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.industry_identifiers, Unset):
            industry_identifiers = self.industry_identifiers

        last_updated = self.last_updated

        lenovo_id = self.lenovo_id

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if industry_identifiers is not UNSET:
            field_dict["industry_identifiers"] = industry_identifiers
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if lenovo_id is not UNSET:
            field_dict["lenovo_id"] = lenovo_id
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        industry_identifiers = cast(list[str], d.pop("industry_identifiers", UNSET))

        last_updated = d.pop("last_updated", UNSET)

        lenovo_id = d.pop("lenovo_id", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_lenovo = cls(
            cve=cve,
            date_added=date_added,
            industry_identifiers=industry_identifiers,
            last_updated=last_updated,
            lenovo_id=lenovo_id,
            title=title,
            url=url,
        )

        advisory_lenovo.additional_properties = d
        return advisory_lenovo

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

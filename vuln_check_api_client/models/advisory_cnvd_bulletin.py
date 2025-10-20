from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCNVDBulletin")


@_attrs_define
class AdvisoryCNVDBulletin:
    """
    Attributes:
        cnta (Union[Unset, str]):
        cnvd (Union[Unset, list[str]]):
        cve (Union[Unset, list[str]]):
        date (Union[Unset, str]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        id (Union[Unset, str]):
        reference_urls (Union[Unset, list[str]]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cnta: Union[Unset, str] = UNSET
    cnvd: Union[Unset, list[str]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    reference_urls: Union[Unset, list[str]] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cnta = self.cnta

        cnvd: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cnvd, Unset):
            cnvd = self.cnvd

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date = self.date

        date_added = self.date_added

        description = self.description

        id = self.id

        reference_urls: Union[Unset, list[str]] = UNSET
        if not isinstance(self.reference_urls, Unset):
            reference_urls = self.reference_urls

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cnta is not UNSET:
            field_dict["cnta"] = cnta
        if cnvd is not UNSET:
            field_dict["cnvd"] = cnvd
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date is not UNSET:
            field_dict["date"] = date
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if reference_urls is not UNSET:
            field_dict["reference_urls"] = reference_urls
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cnta = d.pop("cnta", UNSET)

        cnvd = cast(list[str], d.pop("cnvd", UNSET))

        cve = cast(list[str], d.pop("cve", UNSET))

        date = d.pop("date", UNSET)

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        reference_urls = cast(list[str], d.pop("reference_urls", UNSET))

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_cnvd_bulletin = cls(
            cnta=cnta,
            cnvd=cnvd,
            cve=cve,
            date=date,
            date_added=date_added,
            description=description,
            id=id,
            reference_urls=reference_urls,
            title=title,
            url=url,
        )

        advisory_cnvd_bulletin.additional_properties = d
        return advisory_cnvd_bulletin

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

from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryKRCertAdvisory")


@_attrs_define
class AdvisoryKRCertAdvisory:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        description_ko (Union[Unset, str]):
        link (Union[Unset, str]):
        overview_ko (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        title_ko (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description_ko: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    overview_ko: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    title_ko: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        description_ko = self.description_ko

        link = self.link

        overview_ko = self.overview_ko

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        title_ko = self.title_ko

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description_ko is not UNSET:
            field_dict["description_ko"] = description_ko
        if link is not UNSET:
            field_dict["link"] = link
        if overview_ko is not UNSET:
            field_dict["overview_ko"] = overview_ko
        if references is not UNSET:
            field_dict["references"] = references
        if title_ko is not UNSET:
            field_dict["title_ko"] = title_ko

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        description_ko = d.pop("description_ko", UNSET)

        link = d.pop("link", UNSET)

        overview_ko = d.pop("overview_ko", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        title_ko = d.pop("title_ko", UNSET)

        advisory_kr_cert_advisory = cls(
            cve=cve,
            date_added=date_added,
            description_ko=description_ko,
            link=link,
            overview_ko=overview_ko,
            references=references,
            title_ko=title_ko,
        )

        advisory_kr_cert_advisory.additional_properties = d
        return advisory_kr_cert_advisory

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

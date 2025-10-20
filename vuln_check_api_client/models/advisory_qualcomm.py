from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryQualcomm")


@_attrs_define
class AdvisoryQualcomm:
    """
    Attributes:
        chipsets (Union[Unset, list[str]]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        score (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    chipsets: Union[Unset, list[str]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    score: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chipsets: Union[Unset, list[str]] = UNSET
        if not isinstance(self.chipsets, Unset):
            chipsets = self.chipsets

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        description = self.description

        score = self.score

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chipsets is not UNSET:
            field_dict["chipsets"] = chipsets
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if score is not UNSET:
            field_dict["score"] = score
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chipsets = cast(list[str], d.pop("chipsets", UNSET))

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        score = d.pop("score", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_qualcomm = cls(
            chipsets=chipsets,
            cve=cve,
            date_added=date_added,
            description=description,
            score=score,
            title=title,
            url=url,
        )

        advisory_qualcomm.additional_properties = d
        return advisory_qualcomm

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

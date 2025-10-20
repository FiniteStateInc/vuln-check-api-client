from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryNEC")


@_attrs_define
class AdvisoryNEC:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        nvd_id (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    nvd_id: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        nvd_id = self.nvd_id

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if nvd_id is not UNSET:
            field_dict["nvd_id"] = nvd_id
        if references is not UNSET:
            field_dict["references"] = references
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

        nvd_id = d.pop("nvd_id", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_nec = cls(
            cve=cve,
            date_added=date_added,
            nvd_id=nvd_id,
            references=references,
            title=title,
            url=url,
        )

        advisory_nec.additional_properties = d
        return advisory_nec

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

from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryK8S")


@_attrs_define
class AdvisoryK8S:
    """
    Attributes:
        content (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        issue_id (Union[Unset, int]):
        summary (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    content: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    issue_id: Union[Unset, int] = UNSET
    summary: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        issue_id = self.issue_id

        summary = self.summary

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if issue_id is not UNSET:
            field_dict["issue_id"] = issue_id
        if summary is not UNSET:
            field_dict["summary"] = summary
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        issue_id = d.pop("issue_id", UNSET)

        summary = d.pop("summary", UNSET)

        url = d.pop("url", UNSET)

        advisory_k8s = cls(
            content=content,
            cve=cve,
            date_added=date_added,
            issue_id=issue_id,
            summary=summary,
            url=url,
        )

        advisory_k8s.additional_properties = d
        return advisory_k8s

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

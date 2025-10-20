from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryEmergingThreatsSnort")


@_attrs_define
class AdvisoryEmergingThreatsSnort:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        rev (Union[Unset, str]):
        rule_disabled (Union[Unset, bool]):
        rule_name (Union[Unset, str]):
        sid (Union[Unset, int]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    rev: Union[Unset, str] = UNSET
    rule_disabled: Union[Unset, bool] = UNSET
    rule_name: Union[Unset, str] = UNSET
    sid: Union[Unset, int] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        rev = self.rev

        rule_disabled = self.rule_disabled

        rule_name = self.rule_name

        sid = self.sid

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if references is not UNSET:
            field_dict["references"] = references
        if rev is not UNSET:
            field_dict["rev"] = rev
        if rule_disabled is not UNSET:
            field_dict["rule_disabled"] = rule_disabled
        if rule_name is not UNSET:
            field_dict["rule_name"] = rule_name
        if sid is not UNSET:
            field_dict["sid"] = sid
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        rev = d.pop("rev", UNSET)

        rule_disabled = d.pop("rule_disabled", UNSET)

        rule_name = d.pop("rule_name", UNSET)

        sid = d.pop("sid", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        advisory_emerging_threats_snort = cls(
            cve=cve,
            date_added=date_added,
            references=references,
            rev=rev,
            rule_disabled=rule_disabled,
            rule_name=rule_name,
            sid=sid,
            updated_at=updated_at,
            url=url,
        )

        advisory_emerging_threats_snort.additional_properties = d
        return advisory_emerging_threats_snort

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

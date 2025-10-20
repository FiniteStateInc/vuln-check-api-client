from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryMozillaComponent")


@_attrs_define
class AdvisoryMozillaComponent:
    """
    Attributes:
        bugzilla (Union[Unset, list[str]]):
        cve (Union[Unset, list[str]]):
        description (Union[Unset, str]):
        impact (Union[Unset, str]):
        reporter (Union[Unset, str]):
        title (Union[Unset, str]):
    """

    bugzilla: Union[Unset, list[str]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    description: Union[Unset, str] = UNSET
    impact: Union[Unset, str] = UNSET
    reporter: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bugzilla: Union[Unset, list[str]] = UNSET
        if not isinstance(self.bugzilla, Unset):
            bugzilla = self.bugzilla

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        description = self.description

        impact = self.impact

        reporter = self.reporter

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bugzilla is not UNSET:
            field_dict["bugzilla"] = bugzilla
        if cve is not UNSET:
            field_dict["cve"] = cve
        if description is not UNSET:
            field_dict["description"] = description
        if impact is not UNSET:
            field_dict["impact"] = impact
        if reporter is not UNSET:
            field_dict["reporter"] = reporter
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bugzilla = cast(list[str], d.pop("bugzilla", UNSET))

        cve = cast(list[str], d.pop("cve", UNSET))

        description = d.pop("description", UNSET)

        impact = d.pop("impact", UNSET)

        reporter = d.pop("reporter", UNSET)

        title = d.pop("title", UNSET)

        advisory_mozilla_component = cls(
            bugzilla=bugzilla,
            cve=cve,
            description=description,
            impact=impact,
            reporter=reporter,
            title=title,
        )

        advisory_mozilla_component.additional_properties = d
        return advisory_mozilla_component

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

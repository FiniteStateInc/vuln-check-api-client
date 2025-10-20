from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryNZAdvisory")


@_attrs_define
class AdvisoryNZAdvisory:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        happening (Union[Unset, str]):
        link (Union[Unset, str]):
        look_for (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        title (Union[Unset, str]):
        what_to_do (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    happening: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    look_for: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    title: Union[Unset, str] = UNSET
    what_to_do: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        description = self.description

        happening = self.happening

        link = self.link

        look_for = self.look_for

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        title = self.title

        what_to_do = self.what_to_do

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if happening is not UNSET:
            field_dict["happening"] = happening
        if link is not UNSET:
            field_dict["link"] = link
        if look_for is not UNSET:
            field_dict["lookFor"] = look_for
        if references is not UNSET:
            field_dict["references"] = references
        if title is not UNSET:
            field_dict["title"] = title
        if what_to_do is not UNSET:
            field_dict["whatToDo"] = what_to_do

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        happening = d.pop("happening", UNSET)

        link = d.pop("link", UNSET)

        look_for = d.pop("lookFor", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        title = d.pop("title", UNSET)

        what_to_do = d.pop("whatToDo", UNSET)

        advisory_nz_advisory = cls(
            cve=cve,
            date_added=date_added,
            description=description,
            happening=happening,
            link=link,
            look_for=look_for,
            references=references,
            title=title,
            what_to_do=what_to_do,
        )

        advisory_nz_advisory.additional_properties = d
        return advisory_nz_advisory

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

from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryIncibeAdvisory")


@_attrs_define
class AdvisoryIncibeAdvisory:
    """
    Attributes:
        affected (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        detail (Union[Unset, str]):
        link (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        solution (Union[Unset, str]):
        title (Union[Unset, str]):
    """

    affected: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    detail: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    solution: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected = self.affected

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        description = self.description

        detail = self.detail

        link = self.link

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        solution = self.solution

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected is not UNSET:
            field_dict["affected"] = affected
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if detail is not UNSET:
            field_dict["detail"] = detail
        if link is not UNSET:
            field_dict["link"] = link
        if references is not UNSET:
            field_dict["references"] = references
        if solution is not UNSET:
            field_dict["solution"] = solution
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected = d.pop("affected", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        detail = d.pop("detail", UNSET)

        link = d.pop("link", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        solution = d.pop("solution", UNSET)

        title = d.pop("title", UNSET)

        advisory_incibe_advisory = cls(
            affected=affected,
            cve=cve,
            date_added=date_added,
            description=description,
            detail=detail,
            link=link,
            references=references,
            solution=solution,
            title=title,
        )

        advisory_incibe_advisory.additional_properties = d
        return advisory_incibe_advisory

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

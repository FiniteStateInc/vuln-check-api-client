from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryWRT")


@_attrs_define
class AdvisoryWRT:
    """
    Attributes:
        advisory (Union[Unset, str]):
        affected_versions (Union[Unset, str]):
        credits_ (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        mitigations (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        requirements (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    advisory: Union[Unset, str] = UNSET
    affected_versions: Union[Unset, str] = UNSET
    credits_: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    mitigations: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    requirements: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advisory = self.advisory

        affected_versions = self.affected_versions

        credits_ = self.credits_

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        description = self.description

        mitigations = self.mitigations

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        requirements = self.requirements

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advisory is not UNSET:
            field_dict["advisory"] = advisory
        if affected_versions is not UNSET:
            field_dict["affectedVersions"] = affected_versions
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if mitigations is not UNSET:
            field_dict["mitigations"] = mitigations
        if references is not UNSET:
            field_dict["references"] = references
        if requirements is not UNSET:
            field_dict["requirements"] = requirements
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        advisory = d.pop("advisory", UNSET)

        affected_versions = d.pop("affectedVersions", UNSET)

        credits_ = d.pop("credits", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        mitigations = d.pop("mitigations", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        requirements = d.pop("requirements", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_wrt = cls(
            advisory=advisory,
            affected_versions=affected_versions,
            credits_=credits_,
            cve=cve,
            date_added=date_added,
            description=description,
            mitigations=mitigations,
            references=references,
            requirements=requirements,
            title=title,
            url=url,
        )

        advisory_wrt.additional_properties = d
        return advisory_wrt

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

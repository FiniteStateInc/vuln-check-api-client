from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryASRG")


@_attrs_define
class AdvisoryASRG:
    """
    Attributes:
        affected_products (Union[Unset, str]):
        capec (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cvss (Union[Unset, str]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        problem_type (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    affected_products: Union[Unset, str] = UNSET
    capec: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvss: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    problem_type: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_products = self.affected_products

        capec = self.capec

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvss = self.cvss

        date_added = self.date_added

        description = self.description

        problem_type = self.problem_type

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_products is not UNSET:
            field_dict["affected_products"] = affected_products
        if capec is not UNSET:
            field_dict["capec"] = capec
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss is not UNSET:
            field_dict["cvss"] = cvss
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if problem_type is not UNSET:
            field_dict["problem_type"] = problem_type
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
        affected_products = d.pop("affected_products", UNSET)

        capec = d.pop("capec", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cvss = d.pop("cvss", UNSET)

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        problem_type = d.pop("problem_type", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_asrg = cls(
            affected_products=affected_products,
            capec=capec,
            cve=cve,
            cvss=cvss,
            date_added=date_added,
            description=description,
            problem_type=problem_type,
            references=references,
            title=title,
            url=url,
        )

        advisory_asrg.additional_properties = d
        return advisory_asrg

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

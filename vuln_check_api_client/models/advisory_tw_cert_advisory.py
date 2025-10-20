from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryTWCertAdvisory")


@_attrs_define
class AdvisoryTWCertAdvisory:
    """
    Attributes:
        affected_cn (Union[Unset, str]):
        affected_en (Union[Unset, str]):
        credit_cn (Union[Unset, str]):
        credit_en (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        description_cn (Union[Unset, str]):
        description_en (Union[Unset, str]):
        link (Union[Unset, str]):
        solution_cn (Union[Unset, str]):
        solution_en (Union[Unset, str]):
        title_cn (Union[Unset, str]):
        title_en (Union[Unset, str]):
        tvnid (Union[Unset, str]):
    """

    affected_cn: Union[Unset, str] = UNSET
    affected_en: Union[Unset, str] = UNSET
    credit_cn: Union[Unset, str] = UNSET
    credit_en: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description_cn: Union[Unset, str] = UNSET
    description_en: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    solution_cn: Union[Unset, str] = UNSET
    solution_en: Union[Unset, str] = UNSET
    title_cn: Union[Unset, str] = UNSET
    title_en: Union[Unset, str] = UNSET
    tvnid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_cn = self.affected_cn

        affected_en = self.affected_en

        credit_cn = self.credit_cn

        credit_en = self.credit_en

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        description_cn = self.description_cn

        description_en = self.description_en

        link = self.link

        solution_cn = self.solution_cn

        solution_en = self.solution_en

        title_cn = self.title_cn

        title_en = self.title_en

        tvnid = self.tvnid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_cn is not UNSET:
            field_dict["affected_cn"] = affected_cn
        if affected_en is not UNSET:
            field_dict["affected_en"] = affected_en
        if credit_cn is not UNSET:
            field_dict["credit_cn"] = credit_cn
        if credit_en is not UNSET:
            field_dict["credit_en"] = credit_en
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description_cn is not UNSET:
            field_dict["description_cn"] = description_cn
        if description_en is not UNSET:
            field_dict["description_en"] = description_en
        if link is not UNSET:
            field_dict["link"] = link
        if solution_cn is not UNSET:
            field_dict["solution_cn"] = solution_cn
        if solution_en is not UNSET:
            field_dict["solution_en"] = solution_en
        if title_cn is not UNSET:
            field_dict["title_cn"] = title_cn
        if title_en is not UNSET:
            field_dict["title_en"] = title_en
        if tvnid is not UNSET:
            field_dict["tvnid"] = tvnid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_cn = d.pop("affected_cn", UNSET)

        affected_en = d.pop("affected_en", UNSET)

        credit_cn = d.pop("credit_cn", UNSET)

        credit_en = d.pop("credit_en", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        description_cn = d.pop("description_cn", UNSET)

        description_en = d.pop("description_en", UNSET)

        link = d.pop("link", UNSET)

        solution_cn = d.pop("solution_cn", UNSET)

        solution_en = d.pop("solution_en", UNSET)

        title_cn = d.pop("title_cn", UNSET)

        title_en = d.pop("title_en", UNSET)

        tvnid = d.pop("tvnid", UNSET)

        advisory_tw_cert_advisory = cls(
            affected_cn=affected_cn,
            affected_en=affected_en,
            credit_cn=credit_cn,
            credit_en=credit_en,
            cve=cve,
            date_added=date_added,
            description_cn=description_cn,
            description_en=description_en,
            link=link,
            solution_cn=solution_cn,
            solution_en=solution_en,
            title_cn=title_cn,
            title_en=title_en,
            tvnid=tvnid,
        )

        advisory_tw_cert_advisory.additional_properties = d
        return advisory_tw_cert_advisory

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

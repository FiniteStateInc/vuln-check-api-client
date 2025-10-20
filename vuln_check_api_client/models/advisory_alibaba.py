from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryAlibaba")


@_attrs_define
class AdvisoryAlibaba:
    """
    Attributes:
        cnnvd (Union[Unset, list[str]]):
        cnvd (Union[Unset, list[str]]):
        cve (Union[Unset, list[str]]):
        cvss_score (Union[Unset, str]):
        cvss_vector (Union[Unset, str]):
        cwe (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        id (Union[Unset, str]):
        mitigation_cn (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        summary_cn (Union[Unset, str]):
        title_cn (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cnnvd: Union[Unset, list[str]] = UNSET
    cnvd: Union[Unset, list[str]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvss_score: Union[Unset, str] = UNSET
    cvss_vector: Union[Unset, str] = UNSET
    cwe: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    mitigation_cn: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    summary_cn: Union[Unset, str] = UNSET
    title_cn: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cnnvd: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cnnvd, Unset):
            cnnvd = self.cnnvd

        cnvd: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cnvd, Unset):
            cnvd = self.cnvd

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvss_score = self.cvss_score

        cvss_vector = self.cvss_vector

        cwe: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cwe, Unset):
            cwe = self.cwe

        date_added = self.date_added

        id = self.id

        mitigation_cn = self.mitigation_cn

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        summary_cn = self.summary_cn

        title_cn = self.title_cn

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cnnvd is not UNSET:
            field_dict["cnnvd"] = cnnvd
        if cnvd is not UNSET:
            field_dict["cnvd"] = cnvd
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss_score is not UNSET:
            field_dict["cvss_score"] = cvss_score
        if cvss_vector is not UNSET:
            field_dict["cvss_vector"] = cvss_vector
        if cwe is not UNSET:
            field_dict["cwe"] = cwe
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if id is not UNSET:
            field_dict["id"] = id
        if mitigation_cn is not UNSET:
            field_dict["mitigation_cn"] = mitigation_cn
        if references is not UNSET:
            field_dict["references"] = references
        if summary_cn is not UNSET:
            field_dict["summary_cn"] = summary_cn
        if title_cn is not UNSET:
            field_dict["title_cn"] = title_cn
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cnnvd = cast(list[str], d.pop("cnnvd", UNSET))

        cnvd = cast(list[str], d.pop("cnvd", UNSET))

        cve = cast(list[str], d.pop("cve", UNSET))

        cvss_score = d.pop("cvss_score", UNSET)

        cvss_vector = d.pop("cvss_vector", UNSET)

        cwe = cast(list[str], d.pop("cwe", UNSET))

        date_added = d.pop("date_added", UNSET)

        id = d.pop("id", UNSET)

        mitigation_cn = d.pop("mitigation_cn", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        summary_cn = d.pop("summary_cn", UNSET)

        title_cn = d.pop("title_cn", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        advisory_alibaba = cls(
            cnnvd=cnnvd,
            cnvd=cnvd,
            cve=cve,
            cvss_score=cvss_score,
            cvss_vector=cvss_vector,
            cwe=cwe,
            date_added=date_added,
            id=id,
            mitigation_cn=mitigation_cn,
            references=references,
            summary_cn=summary_cn,
            title_cn=title_cn,
            updated_at=updated_at,
            url=url,
        )

        advisory_alibaba.additional_properties = d
        return advisory_alibaba

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

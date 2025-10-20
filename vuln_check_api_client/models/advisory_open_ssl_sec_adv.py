from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_open_ssl_vulnerability import AdvisoryOpenSSLVulnerability


T = TypeVar("T", bound="AdvisoryOpenSSLSecAdv")


@_attrs_define
class AdvisoryOpenSSLSecAdv:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        date_updated (Union[Unset, str]):
        description (Union[Unset, str]):
        filename (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
        vulnerabilities (Union[Unset, list['AdvisoryOpenSSLVulnerability']]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    date_updated: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    vulnerabilities: Union[Unset, list["AdvisoryOpenSSLVulnerability"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        date_updated = self.date_updated

        description = self.description

        filename = self.filename

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        title = self.title

        url = self.url

        vulnerabilities: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vulnerabilities, Unset):
            vulnerabilities = []
            for vulnerabilities_item_data in self.vulnerabilities:
                vulnerabilities_item = vulnerabilities_item_data.to_dict()
                vulnerabilities.append(vulnerabilities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_updated is not UNSET:
            field_dict["date_updated"] = date_updated
        if description is not UNSET:
            field_dict["description"] = description
        if filename is not UNSET:
            field_dict["filename"] = filename
        if references is not UNSET:
            field_dict["references"] = references
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url
        if vulnerabilities is not UNSET:
            field_dict["vulnerabilities"] = vulnerabilities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_open_ssl_vulnerability import AdvisoryOpenSSLVulnerability

        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        date_updated = d.pop("date_updated", UNSET)

        description = d.pop("description", UNSET)

        filename = d.pop("filename", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        vulnerabilities = []
        _vulnerabilities = d.pop("vulnerabilities", UNSET)
        for vulnerabilities_item_data in _vulnerabilities or []:
            vulnerabilities_item = AdvisoryOpenSSLVulnerability.from_dict(vulnerabilities_item_data)

            vulnerabilities.append(vulnerabilities_item)

        advisory_open_ssl_sec_adv = cls(
            cve=cve,
            date_added=date_added,
            date_updated=date_updated,
            description=description,
            filename=filename,
            references=references,
            title=title,
            url=url,
            vulnerabilities=vulnerabilities,
        )

        advisory_open_ssl_sec_adv.additional_properties = d
        return advisory_open_ssl_sec_adv

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

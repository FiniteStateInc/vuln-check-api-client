from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_cvss import AdvisoryCVSS
    from ..models.advisory_jvn_reference import AdvisoryJVNReference
    from ..models.advisory_jvncpe import AdvisoryJVNCPE


T = TypeVar("T", bound="AdvisoryJVNAdvisoryItem")


@_attrs_define
class AdvisoryJVNAdvisoryItem:
    """
    Attributes:
        cpe (Union[Unset, list['AdvisoryJVNCPE']]):
        cve (Union[Unset, list[str]]):
        cvss (Union[Unset, list['AdvisoryCVSS']]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        description_en (Union[Unset, str]):
        identifier (Union[Unset, str]):
        issued (Union[Unset, str]):
        modified (Union[Unset, str]):
        references (Union[Unset, list['AdvisoryJVNReference']]):
        title (Union[Unset, str]):
        title_en (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
        url_en (Union[Unset, str]):
    """

    cpe: Union[Unset, list["AdvisoryJVNCPE"]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvss: Union[Unset, list["AdvisoryCVSS"]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    description_en: Union[Unset, str] = UNSET
    identifier: Union[Unset, str] = UNSET
    issued: Union[Unset, str] = UNSET
    modified: Union[Unset, str] = UNSET
    references: Union[Unset, list["AdvisoryJVNReference"]] = UNSET
    title: Union[Unset, str] = UNSET
    title_en: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    url_en: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpe: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cpe, Unset):
            cpe = []
            for cpe_item_data in self.cpe:
                cpe_item = cpe_item_data.to_dict()
                cpe.append(cpe_item)

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvss: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cvss, Unset):
            cvss = []
            for cvss_item_data in self.cvss:
                cvss_item = cvss_item_data.to_dict()
                cvss.append(cvss_item)

        date_added = self.date_added

        description = self.description

        description_en = self.description_en

        identifier = self.identifier

        issued = self.issued

        modified = self.modified

        references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        title = self.title

        title_en = self.title_en

        updated_at = self.updated_at

        url = self.url

        url_en = self.url_en

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpe is not UNSET:
            field_dict["cpe"] = cpe
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss is not UNSET:
            field_dict["cvss"] = cvss
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if description_en is not UNSET:
            field_dict["description_en"] = description_en
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if issued is not UNSET:
            field_dict["issued"] = issued
        if modified is not UNSET:
            field_dict["modified"] = modified
        if references is not UNSET:
            field_dict["references"] = references
        if title is not UNSET:
            field_dict["title"] = title
        if title_en is not UNSET:
            field_dict["title_en"] = title_en
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url
        if url_en is not UNSET:
            field_dict["url_en"] = url_en

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_cvss import AdvisoryCVSS
        from ..models.advisory_jvn_reference import AdvisoryJVNReference
        from ..models.advisory_jvncpe import AdvisoryJVNCPE

        d = dict(src_dict)
        cpe = []
        _cpe = d.pop("cpe", UNSET)
        for cpe_item_data in _cpe or []:
            cpe_item = AdvisoryJVNCPE.from_dict(cpe_item_data)

            cpe.append(cpe_item)

        cve = cast(list[str], d.pop("cve", UNSET))

        cvss = []
        _cvss = d.pop("cvss", UNSET)
        for cvss_item_data in _cvss or []:
            cvss_item = AdvisoryCVSS.from_dict(cvss_item_data)

            cvss.append(cvss_item)

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        description_en = d.pop("description_en", UNSET)

        identifier = d.pop("identifier", UNSET)

        issued = d.pop("issued", UNSET)

        modified = d.pop("modified", UNSET)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = AdvisoryJVNReference.from_dict(references_item_data)

            references.append(references_item)

        title = d.pop("title", UNSET)

        title_en = d.pop("title_en", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        url_en = d.pop("url_en", UNSET)

        advisory_jvn_advisory_item = cls(
            cpe=cpe,
            cve=cve,
            cvss=cvss,
            date_added=date_added,
            description=description,
            description_en=description_en,
            identifier=identifier,
            issued=issued,
            modified=modified,
            references=references,
            title=title,
            title_en=title_en,
            updated_at=updated_at,
            url=url,
            url_en=url_en,
        )

        advisory_jvn_advisory_item.additional_properties = d
        return advisory_jvn_advisory_item

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

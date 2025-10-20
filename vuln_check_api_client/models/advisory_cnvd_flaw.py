from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCNVDFlaw")


@_attrs_define
class AdvisoryCNVDFlaw:
    """
    Attributes:
        affected_products_cn (Union[Unset, str]):
        bugtraq_id (Union[Unset, str]):
        cnvd (Union[Unset, str]):
        collection_time (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        harm_level (Union[Unset, str]):
        id (Union[Unset, str]):
        public_date (Union[Unset, str]):
        reference_urls (Union[Unset, list[str]]):
        submission_time (Union[Unset, str]):
        title_cn (Union[Unset, str]):
        update_time (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
        validation_info_cn (Union[Unset, str]):
        validation_info_en (Union[Unset, str]):
        vendor_patch_cn (Union[Unset, str]):
        vuln_attachments (Union[Unset, list[str]]):
        vuln_description_cn (Union[Unset, str]):
        vuln_solution_cn (Union[Unset, str]):
        vuln_type_cn (Union[Unset, str]):
    """

    affected_products_cn: Union[Unset, str] = UNSET
    bugtraq_id: Union[Unset, str] = UNSET
    cnvd: Union[Unset, str] = UNSET
    collection_time: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    harm_level: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    public_date: Union[Unset, str] = UNSET
    reference_urls: Union[Unset, list[str]] = UNSET
    submission_time: Union[Unset, str] = UNSET
    title_cn: Union[Unset, str] = UNSET
    update_time: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    validation_info_cn: Union[Unset, str] = UNSET
    validation_info_en: Union[Unset, str] = UNSET
    vendor_patch_cn: Union[Unset, str] = UNSET
    vuln_attachments: Union[Unset, list[str]] = UNSET
    vuln_description_cn: Union[Unset, str] = UNSET
    vuln_solution_cn: Union[Unset, str] = UNSET
    vuln_type_cn: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_products_cn = self.affected_products_cn

        bugtraq_id = self.bugtraq_id

        cnvd = self.cnvd

        collection_time = self.collection_time

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        harm_level = self.harm_level

        id = self.id

        public_date = self.public_date

        reference_urls: Union[Unset, list[str]] = UNSET
        if not isinstance(self.reference_urls, Unset):
            reference_urls = self.reference_urls

        submission_time = self.submission_time

        title_cn = self.title_cn

        update_time = self.update_time

        updated_at = self.updated_at

        url = self.url

        validation_info_cn = self.validation_info_cn

        validation_info_en = self.validation_info_en

        vendor_patch_cn = self.vendor_patch_cn

        vuln_attachments: Union[Unset, list[str]] = UNSET
        if not isinstance(self.vuln_attachments, Unset):
            vuln_attachments = self.vuln_attachments

        vuln_description_cn = self.vuln_description_cn

        vuln_solution_cn = self.vuln_solution_cn

        vuln_type_cn = self.vuln_type_cn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_products_cn is not UNSET:
            field_dict["affected_products_cn"] = affected_products_cn
        if bugtraq_id is not UNSET:
            field_dict["bugtraq_id"] = bugtraq_id
        if cnvd is not UNSET:
            field_dict["cnvd"] = cnvd
        if collection_time is not UNSET:
            field_dict["collection_time"] = collection_time
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if harm_level is not UNSET:
            field_dict["harm_level"] = harm_level
        if id is not UNSET:
            field_dict["id"] = id
        if public_date is not UNSET:
            field_dict["public_date"] = public_date
        if reference_urls is not UNSET:
            field_dict["reference_urls"] = reference_urls
        if submission_time is not UNSET:
            field_dict["submission_time"] = submission_time
        if title_cn is not UNSET:
            field_dict["title_cn"] = title_cn
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url
        if validation_info_cn is not UNSET:
            field_dict["validation_info_cn"] = validation_info_cn
        if validation_info_en is not UNSET:
            field_dict["validation_info_en"] = validation_info_en
        if vendor_patch_cn is not UNSET:
            field_dict["vendor_patch_cn"] = vendor_patch_cn
        if vuln_attachments is not UNSET:
            field_dict["vuln_attachments"] = vuln_attachments
        if vuln_description_cn is not UNSET:
            field_dict["vuln_description_cn"] = vuln_description_cn
        if vuln_solution_cn is not UNSET:
            field_dict["vuln_solution_cn"] = vuln_solution_cn
        if vuln_type_cn is not UNSET:
            field_dict["vuln_type_cn"] = vuln_type_cn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_products_cn = d.pop("affected_products_cn", UNSET)

        bugtraq_id = d.pop("bugtraq_id", UNSET)

        cnvd = d.pop("cnvd", UNSET)

        collection_time = d.pop("collection_time", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        harm_level = d.pop("harm_level", UNSET)

        id = d.pop("id", UNSET)

        public_date = d.pop("public_date", UNSET)

        reference_urls = cast(list[str], d.pop("reference_urls", UNSET))

        submission_time = d.pop("submission_time", UNSET)

        title_cn = d.pop("title_cn", UNSET)

        update_time = d.pop("update_time", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        validation_info_cn = d.pop("validation_info_cn", UNSET)

        validation_info_en = d.pop("validation_info_en", UNSET)

        vendor_patch_cn = d.pop("vendor_patch_cn", UNSET)

        vuln_attachments = cast(list[str], d.pop("vuln_attachments", UNSET))

        vuln_description_cn = d.pop("vuln_description_cn", UNSET)

        vuln_solution_cn = d.pop("vuln_solution_cn", UNSET)

        vuln_type_cn = d.pop("vuln_type_cn", UNSET)

        advisory_cnvd_flaw = cls(
            affected_products_cn=affected_products_cn,
            bugtraq_id=bugtraq_id,
            cnvd=cnvd,
            collection_time=collection_time,
            cve=cve,
            date_added=date_added,
            harm_level=harm_level,
            id=id,
            public_date=public_date,
            reference_urls=reference_urls,
            submission_time=submission_time,
            title_cn=title_cn,
            update_time=update_time,
            updated_at=updated_at,
            url=url,
            validation_info_cn=validation_info_cn,
            validation_info_en=validation_info_en,
            vendor_patch_cn=vendor_patch_cn,
            vuln_attachments=vuln_attachments,
            vuln_description_cn=vuln_description_cn,
            vuln_solution_cn=vuln_solution_cn,
            vuln_type_cn=vuln_type_cn,
        )

        advisory_cnvd_flaw.additional_properties = d
        return advisory_cnvd_flaw

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

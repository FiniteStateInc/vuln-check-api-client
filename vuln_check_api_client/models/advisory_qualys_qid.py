from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_cvsss_v23 import AdvisoryCvsssV23
    from ..models.advisory_patch import AdvisoryPatch
    from ..models.advisory_vendor_ref import AdvisoryVendorRef


T = TypeVar("T", bound="AdvisoryQualysQID")


@_attrs_define
class AdvisoryQualysQID:
    """
    Attributes:
        consequence (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cvss_v2 (Union[Unset, list['AdvisoryCvsssV23']]):
        cvss_v3 (Union[Unset, list['AdvisoryCvsssV23']]):
        date_added (Union[Unset, str]):
        date_insert (Union[Unset, str]):
        description (Union[Unset, str]):
        patches (Union[Unset, list['AdvisoryPatch']]):
        published (Union[Unset, str]):
        qid (Union[Unset, str]):
        severity (Union[Unset, str]):
        solution (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
        vendor_refs (Union[Unset, list['AdvisoryVendorRef']]):
    """

    consequence: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvss_v2: Union[Unset, list["AdvisoryCvsssV23"]] = UNSET
    cvss_v3: Union[Unset, list["AdvisoryCvsssV23"]] = UNSET
    date_added: Union[Unset, str] = UNSET
    date_insert: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    patches: Union[Unset, list["AdvisoryPatch"]] = UNSET
    published: Union[Unset, str] = UNSET
    qid: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    solution: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    vendor_refs: Union[Unset, list["AdvisoryVendorRef"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        consequence = self.consequence

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvss_v2: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cvss_v2, Unset):
            cvss_v2 = []
            for cvss_v2_item_data in self.cvss_v2:
                cvss_v2_item = cvss_v2_item_data.to_dict()
                cvss_v2.append(cvss_v2_item)

        cvss_v3: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cvss_v3, Unset):
            cvss_v3 = []
            for cvss_v3_item_data in self.cvss_v3:
                cvss_v3_item = cvss_v3_item_data.to_dict()
                cvss_v3.append(cvss_v3_item)

        date_added = self.date_added

        date_insert = self.date_insert

        description = self.description

        patches: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.patches, Unset):
            patches = []
            for patches_item_data in self.patches:
                patches_item = patches_item_data.to_dict()
                patches.append(patches_item)

        published = self.published

        qid = self.qid

        severity = self.severity

        solution = self.solution

        title = self.title

        url = self.url

        vendor_refs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vendor_refs, Unset):
            vendor_refs = []
            for vendor_refs_item_data in self.vendor_refs:
                vendor_refs_item = vendor_refs_item_data.to_dict()
                vendor_refs.append(vendor_refs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if consequence is not UNSET:
            field_dict["consequence"] = consequence
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss_v2 is not UNSET:
            field_dict["cvss_v2"] = cvss_v2
        if cvss_v3 is not UNSET:
            field_dict["cvss_v3"] = cvss_v3
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_insert is not UNSET:
            field_dict["date_insert"] = date_insert
        if description is not UNSET:
            field_dict["description"] = description
        if patches is not UNSET:
            field_dict["patches"] = patches
        if published is not UNSET:
            field_dict["published"] = published
        if qid is not UNSET:
            field_dict["qid"] = qid
        if severity is not UNSET:
            field_dict["severity"] = severity
        if solution is not UNSET:
            field_dict["solution"] = solution
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url
        if vendor_refs is not UNSET:
            field_dict["vendor_refs"] = vendor_refs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_cvsss_v23 import AdvisoryCvsssV23
        from ..models.advisory_patch import AdvisoryPatch
        from ..models.advisory_vendor_ref import AdvisoryVendorRef

        d = dict(src_dict)
        consequence = d.pop("consequence", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cvss_v2 = []
        _cvss_v2 = d.pop("cvss_v2", UNSET)
        for cvss_v2_item_data in _cvss_v2 or []:
            cvss_v2_item = AdvisoryCvsssV23.from_dict(cvss_v2_item_data)

            cvss_v2.append(cvss_v2_item)

        cvss_v3 = []
        _cvss_v3 = d.pop("cvss_v3", UNSET)
        for cvss_v3_item_data in _cvss_v3 or []:
            cvss_v3_item = AdvisoryCvsssV23.from_dict(cvss_v3_item_data)

            cvss_v3.append(cvss_v3_item)

        date_added = d.pop("date_added", UNSET)

        date_insert = d.pop("date_insert", UNSET)

        description = d.pop("description", UNSET)

        patches = []
        _patches = d.pop("patches", UNSET)
        for patches_item_data in _patches or []:
            patches_item = AdvisoryPatch.from_dict(patches_item_data)

            patches.append(patches_item)

        published = d.pop("published", UNSET)

        qid = d.pop("qid", UNSET)

        severity = d.pop("severity", UNSET)

        solution = d.pop("solution", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        vendor_refs = []
        _vendor_refs = d.pop("vendor_refs", UNSET)
        for vendor_refs_item_data in _vendor_refs or []:
            vendor_refs_item = AdvisoryVendorRef.from_dict(vendor_refs_item_data)

            vendor_refs.append(vendor_refs_item)

        advisory_qualys_qid = cls(
            consequence=consequence,
            cve=cve,
            cvss_v2=cvss_v2,
            cvss_v3=cvss_v3,
            date_added=date_added,
            date_insert=date_insert,
            description=description,
            patches=patches,
            published=published,
            qid=qid,
            severity=severity,
            solution=solution,
            title=title,
            url=url,
            vendor_refs=vendor_refs,
        )

        advisory_qualys_qid.additional_properties = d
        return advisory_qualys_qid

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

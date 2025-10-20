from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_cve_detail import AdvisoryCVEDetail
    from ..models.advisory_hardware_update import AdvisoryHardwareUpdate
    from ..models.advisory_nvidia_revision import AdvisoryNvidiaRevision
    from ..models.advisory_software_update import AdvisorySoftwareUpdate


T = TypeVar("T", bound="AdvisorySecurityBulletin")


@_attrs_define
class AdvisorySecurityBulletin:
    """
    Attributes:
        acknowledgement (Union[Unset, str]):
        bulletin_id (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cvedetails (Union[Unset, list['AdvisoryCVEDetail']]):
        date_added (Union[Unset, str]):
        hardware_updates (Union[Unset, list['AdvisoryHardwareUpdate']]):
        last_updated (Union[Unset, str]):
        link (Union[Unset, str]):
        revisions (Union[Unset, list['AdvisoryNvidiaRevision']]):
        severity (Union[Unset, str]):
        software_updates (Union[Unset, list['AdvisorySoftwareUpdate']]):
        title (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    acknowledgement: Union[Unset, str] = UNSET
    bulletin_id: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvedetails: Union[Unset, list["AdvisoryCVEDetail"]] = UNSET
    date_added: Union[Unset, str] = UNSET
    hardware_updates: Union[Unset, list["AdvisoryHardwareUpdate"]] = UNSET
    last_updated: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    revisions: Union[Unset, list["AdvisoryNvidiaRevision"]] = UNSET
    severity: Union[Unset, str] = UNSET
    software_updates: Union[Unset, list["AdvisorySoftwareUpdate"]] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acknowledgement = self.acknowledgement

        bulletin_id = self.bulletin_id

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvedetails: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cvedetails, Unset):
            cvedetails = []
            for cvedetails_item_data in self.cvedetails:
                cvedetails_item = cvedetails_item_data.to_dict()
                cvedetails.append(cvedetails_item)

        date_added = self.date_added

        hardware_updates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.hardware_updates, Unset):
            hardware_updates = []
            for hardware_updates_item_data in self.hardware_updates:
                hardware_updates_item = hardware_updates_item_data.to_dict()
                hardware_updates.append(hardware_updates_item)

        last_updated = self.last_updated

        link = self.link

        revisions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.revisions, Unset):
            revisions = []
            for revisions_item_data in self.revisions:
                revisions_item = revisions_item_data.to_dict()
                revisions.append(revisions_item)

        severity = self.severity

        software_updates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.software_updates, Unset):
            software_updates = []
            for software_updates_item_data in self.software_updates:
                software_updates_item = software_updates_item_data.to_dict()
                software_updates.append(software_updates_item)

        title = self.title

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acknowledgement is not UNSET:
            field_dict["acknowledgement"] = acknowledgement
        if bulletin_id is not UNSET:
            field_dict["bulletinId"] = bulletin_id
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvedetails is not UNSET:
            field_dict["cvedetails"] = cvedetails
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if hardware_updates is not UNSET:
            field_dict["hardwareUpdates"] = hardware_updates
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if link is not UNSET:
            field_dict["link"] = link
        if revisions is not UNSET:
            field_dict["revisions"] = revisions
        if severity is not UNSET:
            field_dict["severity"] = severity
        if software_updates is not UNSET:
            field_dict["softwareUpdates"] = software_updates
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_cve_detail import AdvisoryCVEDetail
        from ..models.advisory_hardware_update import AdvisoryHardwareUpdate
        from ..models.advisory_nvidia_revision import AdvisoryNvidiaRevision
        from ..models.advisory_software_update import AdvisorySoftwareUpdate

        d = dict(src_dict)
        acknowledgement = d.pop("acknowledgement", UNSET)

        bulletin_id = d.pop("bulletinId", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cvedetails = []
        _cvedetails = d.pop("cvedetails", UNSET)
        for cvedetails_item_data in _cvedetails or []:
            cvedetails_item = AdvisoryCVEDetail.from_dict(cvedetails_item_data)

            cvedetails.append(cvedetails_item)

        date_added = d.pop("date_added", UNSET)

        hardware_updates = []
        _hardware_updates = d.pop("hardwareUpdates", UNSET)
        for hardware_updates_item_data in _hardware_updates or []:
            hardware_updates_item = AdvisoryHardwareUpdate.from_dict(hardware_updates_item_data)

            hardware_updates.append(hardware_updates_item)

        last_updated = d.pop("lastUpdated", UNSET)

        link = d.pop("link", UNSET)

        revisions = []
        _revisions = d.pop("revisions", UNSET)
        for revisions_item_data in _revisions or []:
            revisions_item = AdvisoryNvidiaRevision.from_dict(revisions_item_data)

            revisions.append(revisions_item)

        severity = d.pop("severity", UNSET)

        software_updates = []
        _software_updates = d.pop("softwareUpdates", UNSET)
        for software_updates_item_data in _software_updates or []:
            software_updates_item = AdvisorySoftwareUpdate.from_dict(software_updates_item_data)

            software_updates.append(software_updates_item)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        advisory_security_bulletin = cls(
            acknowledgement=acknowledgement,
            bulletin_id=bulletin_id,
            cve=cve,
            cvedetails=cvedetails,
            date_added=date_added,
            hardware_updates=hardware_updates,
            last_updated=last_updated,
            link=link,
            revisions=revisions,
            severity=severity,
            software_updates=software_updates,
            title=title,
            updated_at=updated_at,
        )

        advisory_security_bulletin.additional_properties = d
        return advisory_security_bulletin

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

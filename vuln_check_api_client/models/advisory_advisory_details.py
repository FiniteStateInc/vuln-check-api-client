from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_bugzilla import AdvisoryBugzilla
    from ..models.advisory_issued import AdvisoryIssued
    from ..models.advisory_oval_cve import AdvisoryOvalCVE
    from ..models.advisory_updated import AdvisoryUpdated


T = TypeVar("T", bound="AdvisoryAdvisoryDetails")


@_attrs_define
class AdvisoryAdvisoryDetails:
    """
    Attributes:
        bugzilla (Union[Unset, AdvisoryBugzilla]):
        cve (Union[Unset, AdvisoryOvalCVE]):
        issued (Union[Unset, AdvisoryIssued]):
        severity (Union[Unset, str]):
        updated (Union[Unset, AdvisoryUpdated]):
    """

    bugzilla: Union[Unset, "AdvisoryBugzilla"] = UNSET
    cve: Union[Unset, "AdvisoryOvalCVE"] = UNSET
    issued: Union[Unset, "AdvisoryIssued"] = UNSET
    severity: Union[Unset, str] = UNSET
    updated: Union[Unset, "AdvisoryUpdated"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bugzilla: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bugzilla, Unset):
            bugzilla = self.bugzilla.to_dict()

        cve: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve.to_dict()

        issued: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.issued, Unset):
            issued = self.issued.to_dict()

        severity = self.severity

        updated: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bugzilla is not UNSET:
            field_dict["bugzilla"] = bugzilla
        if cve is not UNSET:
            field_dict["cve"] = cve
        if issued is not UNSET:
            field_dict["issued"] = issued
        if severity is not UNSET:
            field_dict["severity"] = severity
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_bugzilla import AdvisoryBugzilla
        from ..models.advisory_issued import AdvisoryIssued
        from ..models.advisory_oval_cve import AdvisoryOvalCVE
        from ..models.advisory_updated import AdvisoryUpdated

        d = dict(src_dict)
        _bugzilla = d.pop("bugzilla", UNSET)
        bugzilla: Union[Unset, AdvisoryBugzilla]
        if isinstance(_bugzilla, Unset):
            bugzilla = UNSET
        else:
            bugzilla = AdvisoryBugzilla.from_dict(_bugzilla)

        _cve = d.pop("cve", UNSET)
        cve: Union[Unset, AdvisoryOvalCVE]
        if isinstance(_cve, Unset):
            cve = UNSET
        else:
            cve = AdvisoryOvalCVE.from_dict(_cve)

        _issued = d.pop("issued", UNSET)
        issued: Union[Unset, AdvisoryIssued]
        if isinstance(_issued, Unset):
            issued = UNSET
        else:
            issued = AdvisoryIssued.from_dict(_issued)

        severity = d.pop("severity", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, AdvisoryUpdated]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = AdvisoryUpdated.from_dict(_updated)

        advisory_advisory_details = cls(
            bugzilla=bugzilla,
            cve=cve,
            issued=issued,
            severity=severity,
            updated=updated,
        )

        advisory_advisory_details.additional_properties = d
        return advisory_advisory_details

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

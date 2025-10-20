from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_triage_notes import AdvisoryTriageNotes


T = TypeVar("T", bound="AdvisoryOverrideAnnotation")


@_attrs_define
class AdvisoryOverrideAnnotation:
    """
    Attributes:
        cve_id (Union[Unset, str]):
        reason (Union[Unset, str]):
        snapshot (Union[Unset, str]):
        triage_notes (Union[Unset, AdvisoryTriageNotes]):
    """

    cve_id: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    snapshot: Union[Unset, str] = UNSET
    triage_notes: Union[Unset, "AdvisoryTriageNotes"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve_id = self.cve_id

        reason = self.reason

        snapshot = self.snapshot

        triage_notes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.triage_notes, Unset):
            triage_notes = self.triage_notes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve_id is not UNSET:
            field_dict["cve_id"] = cve_id
        if reason is not UNSET:
            field_dict["reason"] = reason
        if snapshot is not UNSET:
            field_dict["snapshot"] = snapshot
        if triage_notes is not UNSET:
            field_dict["triage_notes"] = triage_notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_triage_notes import AdvisoryTriageNotes

        d = dict(src_dict)
        cve_id = d.pop("cve_id", UNSET)

        reason = d.pop("reason", UNSET)

        snapshot = d.pop("snapshot", UNSET)

        _triage_notes = d.pop("triage_notes", UNSET)
        triage_notes: Union[Unset, AdvisoryTriageNotes]
        if isinstance(_triage_notes, Unset):
            triage_notes = UNSET
        else:
            triage_notes = AdvisoryTriageNotes.from_dict(_triage_notes)

        advisory_override_annotation = cls(
            cve_id=cve_id,
            reason=reason,
            snapshot=snapshot,
            triage_notes=triage_notes,
        )

        advisory_override_annotation.additional_properties = d
        return advisory_override_annotation

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

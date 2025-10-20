from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_kb import AdvisoryKb
    from ..models.advisory_kb_threat_description import AdvisoryKbThreatDescription


T = TypeVar("T", bound="AdvisoryMicrosoftKb")


@_attrs_define
class AdvisoryMicrosoftKb:
    """
    Attributes:
        cve (Union[Unset, str]):
        date_added (Union[Unset, str]):
        kbs (Union[Unset, list['AdvisoryKb']]):
        threat (Union[Unset, AdvisoryKbThreatDescription]):
        title (Union[Unset, str]):
    """

    cve: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    kbs: Union[Unset, list["AdvisoryKb"]] = UNSET
    threat: Union[Unset, "AdvisoryKbThreatDescription"] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve = self.cve

        date_added = self.date_added

        kbs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.kbs, Unset):
            kbs = []
            for kbs_item_data in self.kbs:
                kbs_item = kbs_item_data.to_dict()
                kbs.append(kbs_item)

        threat: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.threat, Unset):
            threat = self.threat.to_dict()

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if kbs is not UNSET:
            field_dict["kbs"] = kbs
        if threat is not UNSET:
            field_dict["threat"] = threat
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_kb import AdvisoryKb
        from ..models.advisory_kb_threat_description import AdvisoryKbThreatDescription

        d = dict(src_dict)
        cve = d.pop("cve", UNSET)

        date_added = d.pop("date_added", UNSET)

        kbs = []
        _kbs = d.pop("kbs", UNSET)
        for kbs_item_data in _kbs or []:
            kbs_item = AdvisoryKb.from_dict(kbs_item_data)

            kbs.append(kbs_item)

        _threat = d.pop("threat", UNSET)
        threat: Union[Unset, AdvisoryKbThreatDescription]
        if isinstance(_threat, Unset):
            threat = UNSET
        else:
            threat = AdvisoryKbThreatDescription.from_dict(_threat)

        title = d.pop("title", UNSET)

        advisory_microsoft_kb = cls(
            cve=cve,
            date_added=date_added,
            kbs=kbs,
            threat=threat,
            title=title,
        )

        advisory_microsoft_kb.additional_properties = d
        return advisory_microsoft_kb

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

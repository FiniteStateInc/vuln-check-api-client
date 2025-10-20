from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_reference_data_extended import ApiReferenceDataExtended


T = TypeVar("T", bound="ApiReferencesExtended")


@_attrs_define
class ApiReferencesExtended:
    """
    Attributes:
        reference_data (Union[Unset, list['ApiReferenceDataExtended']]): ExploitData     []NormalizedExploit
            `json:"exploit_data,omitempty"`
                            ThreatActorData []ThreatActorExtended     `json:"threat_actor_data,omitempty"`
                            RansomwareData  []RansomwareReferenceData `json:"ransomware_data,omitempty"`
                            AdvisoryData    []AdvisoryExtended        `json:"advisory_data,omitempty"`
                            IdentifierData  []IdentifierExtended      `json:"identifier_data,omitempty"`
    """

    reference_data: Union[Unset, list["ApiReferenceDataExtended"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference_data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.reference_data, Unset):
            reference_data = []
            for reference_data_item_data in self.reference_data:
                reference_data_item = reference_data_item_data.to_dict()
                reference_data.append(reference_data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_data is not UNSET:
            field_dict["reference_data"] = reference_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_reference_data_extended import ApiReferenceDataExtended

        d = dict(src_dict)
        reference_data = []
        _reference_data = d.pop("reference_data", UNSET)
        for reference_data_item_data in _reference_data or []:
            reference_data_item = ApiReferenceDataExtended.from_dict(reference_data_item_data)

            reference_data.append(reference_data_item)

        api_references_extended = cls(
            reference_data=reference_data,
        )

        api_references_extended.additional_properties = d
        return api_references_extended

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

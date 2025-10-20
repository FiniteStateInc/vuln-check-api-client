from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_adp import AdvisoryADP
    from ..models.advisory_m_cna import AdvisoryMCna


T = TypeVar("T", bound="AdvisoryVulnrichmentContainers")


@_attrs_define
class AdvisoryVulnrichmentContainers:
    """
    Attributes:
        adp (Union[Unset, list['AdvisoryADP']]):
        cna (Union[Unset, AdvisoryMCna]):
    """

    adp: Union[Unset, list["AdvisoryADP"]] = UNSET
    cna: Union[Unset, "AdvisoryMCna"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        adp: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.adp, Unset):
            adp = []
            for adp_item_data in self.adp:
                adp_item = adp_item_data.to_dict()
                adp.append(adp_item)

        cna: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cna, Unset):
            cna = self.cna.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if adp is not UNSET:
            field_dict["adp"] = adp
        if cna is not UNSET:
            field_dict["cna"] = cna

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_adp import AdvisoryADP
        from ..models.advisory_m_cna import AdvisoryMCna

        d = dict(src_dict)
        adp = []
        _adp = d.pop("adp", UNSET)
        for adp_item_data in _adp or []:
            adp_item = AdvisoryADP.from_dict(adp_item_data)

            adp.append(adp_item)

        _cna = d.pop("cna", UNSET)
        cna: Union[Unset, AdvisoryMCna]
        if isinstance(_cna, Unset):
            cna = UNSET
        else:
            cna = AdvisoryMCna.from_dict(_cna)

        advisory_vulnrichment_containers = cls(
            adp=adp,
            cna=cna,
        )

        advisory_vulnrichment_containers.additional_properties = d
        return advisory_vulnrichment_containers

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

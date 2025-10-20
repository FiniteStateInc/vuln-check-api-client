from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_mcpe_match import AdvisoryMCPEMatch


T = TypeVar("T", bound="AdvisoryMNodes")


@_attrs_define
class AdvisoryMNodes:
    """
    Attributes:
        cpe_match (Union[Unset, list['AdvisoryMCPEMatch']]):
        negate (Union[Unset, bool]):
        operator (Union[Unset, str]):
    """

    cpe_match: Union[Unset, list["AdvisoryMCPEMatch"]] = UNSET
    negate: Union[Unset, bool] = UNSET
    operator: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpe_match: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cpe_match, Unset):
            cpe_match = []
            for cpe_match_item_data in self.cpe_match:
                cpe_match_item = cpe_match_item_data.to_dict()
                cpe_match.append(cpe_match_item)

        negate = self.negate

        operator = self.operator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpe_match is not UNSET:
            field_dict["cpeMatch"] = cpe_match
        if negate is not UNSET:
            field_dict["negate"] = negate
        if operator is not UNSET:
            field_dict["operator"] = operator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_mcpe_match import AdvisoryMCPEMatch

        d = dict(src_dict)
        cpe_match = []
        _cpe_match = d.pop("cpeMatch", UNSET)
        for cpe_match_item_data in _cpe_match or []:
            cpe_match_item = AdvisoryMCPEMatch.from_dict(cpe_match_item_data)

            cpe_match.append(cpe_match_item)

        negate = d.pop("negate", UNSET)

        operator = d.pop("operator", UNSET)

        advisory_m_nodes = cls(
            cpe_match=cpe_match,
            negate=negate,
            operator=operator,
        )

        advisory_m_nodes.additional_properties = d
        return advisory_m_nodes

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

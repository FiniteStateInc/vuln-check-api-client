from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_nvd20_node import AdvisoryNVD20Node


T = TypeVar("T", bound="AdvisoryNVD20Configuration")


@_attrs_define
class AdvisoryNVD20Configuration:
    """
    Attributes:
        negate (Union[Unset, bool]):
        nodes (Union[Unset, list['AdvisoryNVD20Node']]):
        operator (Union[Unset, str]):
    """

    negate: Union[Unset, bool] = UNSET
    nodes: Union[Unset, list["AdvisoryNVD20Node"]] = UNSET
    operator: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        negate = self.negate

        nodes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()
                nodes.append(nodes_item)

        operator = self.operator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if negate is not UNSET:
            field_dict["negate"] = negate
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if operator is not UNSET:
            field_dict["operator"] = operator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_nvd20_node import AdvisoryNVD20Node

        d = dict(src_dict)
        negate = d.pop("negate", UNSET)

        nodes = []
        _nodes = d.pop("nodes", UNSET)
        for nodes_item_data in _nodes or []:
            nodes_item = AdvisoryNVD20Node.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        operator = d.pop("operator", UNSET)

        advisory_nvd20_configuration = cls(
            negate=negate,
            nodes=nodes,
            operator=operator,
        )

        advisory_nvd20_configuration.additional_properties = d
        return advisory_nvd20_configuration

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

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_cwe_node import AdvisoryCWENode


T = TypeVar("T", bound="AdvisoryCwes")


@_attrs_define
class AdvisoryCwes:
    """
    Attributes:
        nodes (Union[Unset, list['AdvisoryCWENode']]):
        total_count (Union[Unset, int]):
    """

    nodes: Union[Unset, list["AdvisoryCWENode"]] = UNSET
    total_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nodes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()
                nodes.append(nodes_item)

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_cwe_node import AdvisoryCWENode

        d = dict(src_dict)
        nodes = []
        _nodes = d.pop("nodes", UNSET)
        for nodes_item_data in _nodes or []:
            nodes_item = AdvisoryCWENode.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        total_count = d.pop("totalCount", UNSET)

        advisory_cwes = cls(
            nodes=nodes,
            total_count=total_count,
        )

        advisory_cwes.additional_properties = d
        return advisory_cwes

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

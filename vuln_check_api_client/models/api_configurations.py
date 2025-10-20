from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_nodes import ApiNodes


T = TypeVar("T", bound="ApiConfigurations")


@_attrs_define
class ApiConfigurations:
    """
    Attributes:
        cve_data_version (Union[Unset, str]):
        nodes (Union[Unset, list['ApiNodes']]):
    """

    cve_data_version: Union[Unset, str] = UNSET
    nodes: Union[Unset, list["ApiNodes"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve_data_version = self.cve_data_version

        nodes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()
                nodes.append(nodes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve_data_version is not UNSET:
            field_dict["CVE_data_version"] = cve_data_version
        if nodes is not UNSET:
            field_dict["nodes"] = nodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_nodes import ApiNodes

        d = dict(src_dict)
        cve_data_version = d.pop("CVE_data_version", UNSET)

        nodes = []
        _nodes = d.pop("nodes", UNSET)
        for nodes_item_data in _nodes or []:
            nodes_item = ApiNodes.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        api_configurations = cls(
            cve_data_version=cve_data_version,
            nodes=nodes,
        )

        api_configurations.additional_properties = d
        return api_configurations

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

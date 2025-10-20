from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_cpe_match import ApiCPEMatch


T = TypeVar("T", bound="ApiNodes")


@_attrs_define
class ApiNodes:
    """
    Attributes:
        children (Union[Unset, list['ApiNodes']]):
        cpe_match (Union[Unset, list['ApiCPEMatch']]):
        operator (Union[Unset, str]):
    """

    children: Union[Unset, list["ApiNodes"]] = UNSET
    cpe_match: Union[Unset, list["ApiCPEMatch"]] = UNSET
    operator: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        children: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        cpe_match: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cpe_match, Unset):
            cpe_match = []
            for cpe_match_item_data in self.cpe_match:
                cpe_match_item = cpe_match_item_data.to_dict()
                cpe_match.append(cpe_match_item)

        operator = self.operator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if children is not UNSET:
            field_dict["children"] = children
        if cpe_match is not UNSET:
            field_dict["cpe_match"] = cpe_match
        if operator is not UNSET:
            field_dict["operator"] = operator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_cpe_match import ApiCPEMatch

        d = dict(src_dict)
        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in _children or []:
            children_item = ApiNodes.from_dict(children_item_data)

            children.append(children_item)

        cpe_match = []
        _cpe_match = d.pop("cpe_match", UNSET)
        for cpe_match_item_data in _cpe_match or []:
            cpe_match_item = ApiCPEMatch.from_dict(cpe_match_item_data)

            cpe_match.append(cpe_match_item)

        operator = d.pop("operator", UNSET)

        api_nodes = cls(
            children=children,
            cpe_match=cpe_match,
            operator=operator,
        )

        api_nodes.additional_properties = d
        return api_nodes

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

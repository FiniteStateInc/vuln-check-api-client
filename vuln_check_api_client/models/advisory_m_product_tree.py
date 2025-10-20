from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_m_branch import AdvisoryMBranch
    from ..models.advisory_m_full_product_name import AdvisoryMFullProductName


T = TypeVar("T", bound="AdvisoryMProductTree")


@_attrs_define
class AdvisoryMProductTree:
    """
    Attributes:
        branch (Union[Unset, list['AdvisoryMBranch']]):
        full_product_name (Union[Unset, list['AdvisoryMFullProductName']]):
    """

    branch: Union[Unset, list["AdvisoryMBranch"]] = UNSET
    full_product_name: Union[Unset, list["AdvisoryMFullProductName"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branch: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.branch, Unset):
            branch = []
            for branch_item_data in self.branch:
                branch_item = branch_item_data.to_dict()
                branch.append(branch_item)

        full_product_name: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.full_product_name, Unset):
            full_product_name = []
            for full_product_name_item_data in self.full_product_name:
                full_product_name_item = full_product_name_item_data.to_dict()
                full_product_name.append(full_product_name_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branch is not UNSET:
            field_dict["Branch"] = branch
        if full_product_name is not UNSET:
            field_dict["FullProductName"] = full_product_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_m_branch import AdvisoryMBranch
        from ..models.advisory_m_full_product_name import AdvisoryMFullProductName

        d = dict(src_dict)
        branch = []
        _branch = d.pop("Branch", UNSET)
        for branch_item_data in _branch or []:
            branch_item = AdvisoryMBranch.from_dict(branch_item_data)

            branch.append(branch_item)

        full_product_name = []
        _full_product_name = d.pop("FullProductName", UNSET)
        for full_product_name_item_data in _full_product_name or []:
            full_product_name_item = AdvisoryMFullProductName.from_dict(full_product_name_item_data)

            full_product_name.append(full_product_name_item)

        advisory_m_product_tree = cls(
            branch=branch,
            full_product_name=full_product_name,
        )

        advisory_m_product_tree.additional_properties = d
        return advisory_m_product_tree

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

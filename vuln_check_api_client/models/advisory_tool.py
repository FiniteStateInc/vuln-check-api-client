from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_tool_ref import AdvisoryToolRef


T = TypeVar("T", bound="AdvisoryTool")


@_attrs_define
class AdvisoryTool:
    """
    Attributes:
        name (Union[Unset, str]):
        references (Union[Unset, list['AdvisoryToolRef']]):
    """

    name: Union[Unset, str] = UNSET
    references: Union[Unset, list["AdvisoryToolRef"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if references is not UNSET:
            field_dict["references"] = references

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_tool_ref import AdvisoryToolRef

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = AdvisoryToolRef.from_dict(references_item_data)

            references.append(references_item)

        advisory_tool = cls(
            name=name,
            references=references,
        )

        advisory_tool.additional_properties = d
        return advisory_tool

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

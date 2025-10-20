from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryMispRelatedItem")


@_attrs_define
class AdvisoryMispRelatedItem:
    """
    Attributes:
        dest_uuid (Union[Unset, str]):
        tags (Union[Unset, list[str]]):
        type_ (Union[Unset, str]):
    """

    dest_uuid: Union[Unset, str] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dest_uuid = self.dest_uuid

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dest_uuid is not UNSET:
            field_dict["dest-uuid"] = dest_uuid
        if tags is not UNSET:
            field_dict["tags"] = tags
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dest_uuid = d.pop("dest-uuid", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        type_ = d.pop("type", UNSET)

        advisory_misp_related_item = cls(
            dest_uuid=dest_uuid,
            tags=tags,
            type_=type_,
        )

        advisory_misp_related_item.additional_properties = d
        return advisory_misp_related_item

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

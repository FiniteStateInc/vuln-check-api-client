from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaginateParam")


@_attrs_define
class PaginateParam:
    """
    Attributes:
        filtering (Union[Unset, str]):
        format_ (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    filtering: Union[Unset, str] = UNSET
    format_: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filtering = self.filtering

        format_ = self.format_

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filtering is not UNSET:
            field_dict["filtering"] = filtering
        if format_ is not UNSET:
            field_dict["format"] = format_
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filtering = d.pop("filtering", UNSET)

        format_ = d.pop("format", UNSET)

        name = d.pop("name", UNSET)

        paginate_param = cls(
            filtering=filtering,
            format_=format_,
            name=name,
        )

        paginate_param.additional_properties = d
        return paginate_param

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

from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiNVD20Reference")


@_attrs_define
class ApiNVD20Reference:
    """
    Attributes:
        source (Union[Unset, str]):
        tags (Union[Unset, list[str]]):
        url (Union[Unset, str]):
    """

    source: Union[Unset, str] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if tags is not UNSET:
            field_dict["tags"] = tags
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        url = d.pop("url", UNSET)

        api_nvd20_reference = cls(
            source=source,
            tags=tags,
            url=url,
        )

        api_nvd20_reference.additional_properties = d
        return api_nvd20_reference

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

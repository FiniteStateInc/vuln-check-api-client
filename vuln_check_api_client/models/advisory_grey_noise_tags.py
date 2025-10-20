from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryGreyNoiseTags")


@_attrs_define
class AdvisoryGreyNoiseTags:
    """
    Attributes:
        category (Union[Unset, str]):
        id (Union[Unset, str]):
        intention (Union[Unset, str]):
        name (Union[Unset, str]):
        slug (Union[Unset, str]):
    """

    category: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    intention: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        id = self.id

        intention = self.intention

        name = self.name

        slug = self.slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if id is not UNSET:
            field_dict["id"] = id
        if intention is not UNSET:
            field_dict["intention"] = intention
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category", UNSET)

        id = d.pop("id", UNSET)

        intention = d.pop("intention", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        advisory_grey_noise_tags = cls(
            category=category,
            id=id,
            intention=intention,
            name=name,
            slug=slug,
        )

        advisory_grey_noise_tags.additional_properties = d
        return advisory_grey_noise_tags

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

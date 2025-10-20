from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryNodeAuthor")


@_attrs_define
class AdvisoryNodeAuthor:
    """
    Attributes:
        author (Union[Unset, str]):
        username (Union[Unset, str]):
        website (Union[Unset, str]):
    """

    author: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author = self.author

        username = self.username

        website = self.website

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if username is not UNSET:
            field_dict["username"] = username
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        author = d.pop("author", UNSET)

        username = d.pop("username", UNSET)

        website = d.pop("website", UNSET)

        advisory_node_author = cls(
            author=author,
            username=username,
            website=website,
        )

        advisory_node_author.additional_properties = d
        return advisory_node_author

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

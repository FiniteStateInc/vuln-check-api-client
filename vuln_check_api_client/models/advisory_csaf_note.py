from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCSAFNote")


@_attrs_define
class AdvisoryCSAFNote:
    """
    Attributes:
        audience (Union[Unset, str]):
        category (Union[Unset, str]):
        text (Union[Unset, str]):
        title (Union[Unset, str]):
    """

    audience: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audience = self.audience

        category = self.category

        text = self.text

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if audience is not UNSET:
            field_dict["audience"] = audience
        if category is not UNSET:
            field_dict["category"] = category
        if text is not UNSET:
            field_dict["text"] = text
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        audience = d.pop("audience", UNSET)

        category = d.pop("category", UNSET)

        text = d.pop("text", UNSET)

        title = d.pop("title", UNSET)

        advisory_csaf_note = cls(
            audience=audience,
            category=category,
            text=text,
            title=title,
        )

        advisory_csaf_note.additional_properties = d
        return advisory_csaf_note

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

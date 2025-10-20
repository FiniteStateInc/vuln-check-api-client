from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryRNote")


@_attrs_define
class AdvisoryRNote:
    """
    Attributes:
        audience (Union[Unset, str]):
        ordinal (Union[Unset, str]):
        text (Union[Unset, str]):
        title (Union[Unset, str]):
        type_ (Union[Unset, int]): diff between xml && json
    """

    audience: Union[Unset, str] = UNSET
    ordinal: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type_: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audience = self.audience

        ordinal = self.ordinal

        text = self.text

        title = self.title

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if audience is not UNSET:
            field_dict["audience"] = audience
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal
        if text is not UNSET:
            field_dict["text"] = text
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        audience = d.pop("audience", UNSET)

        ordinal = d.pop("ordinal", UNSET)

        text = d.pop("text", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        advisory_r_note = cls(
            audience=audience,
            ordinal=ordinal,
            text=text,
            title=title,
            type_=type_,
        )

        advisory_r_note.additional_properties = d
        return advisory_r_note

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

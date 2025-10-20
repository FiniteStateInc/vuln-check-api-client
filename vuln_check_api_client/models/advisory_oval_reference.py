from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryOvalReference")


@_attrs_define
class AdvisoryOvalReference:
    """
    Attributes:
        ref_id (Union[Unset, str]):
        ref_url (Union[Unset, str]):
        source (Union[Unset, str]):
    """

    ref_id: Union[Unset, str] = UNSET
    ref_url: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ref_id = self.ref_id

        ref_url = self.ref_url

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if ref_url is not UNSET:
            field_dict["ref_url"] = ref_url
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ref_id = d.pop("ref_id", UNSET)

        ref_url = d.pop("ref_url", UNSET)

        source = d.pop("source", UNSET)

        advisory_oval_reference = cls(
            ref_id=ref_id,
            ref_url=ref_url,
            source=source,
        )

        advisory_oval_reference.additional_properties = d
        return advisory_oval_reference

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

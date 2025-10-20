from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryPyPAReference")


@_attrs_define
class AdvisoryPyPAReference:
    """
    Attributes:
        refs_type (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    refs_type: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        refs_type = self.refs_type

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if refs_type is not UNSET:
            field_dict["refs_type"] = refs_type
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        refs_type = d.pop("refs_type", UNSET)

        url = d.pop("url", UNSET)

        advisory_py_pa_reference = cls(
            refs_type=refs_type,
            url=url,
        )

        advisory_py_pa_reference.additional_properties = d
        return advisory_py_pa_reference

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

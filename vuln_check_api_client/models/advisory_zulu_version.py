from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryZuluVersion")


@_attrs_define
class AdvisoryZuluVersion:
    """
    Attributes:
        jdk (Union[Unset, str]):
        type_ (Union[Unset, str]):
        zulu (Union[Unset, str]):
    """

    jdk: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    zulu: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jdk = self.jdk

        type_ = self.type_

        zulu = self.zulu

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if jdk is not UNSET:
            field_dict["jdk"] = jdk
        if type_ is not UNSET:
            field_dict["type"] = type_
        if zulu is not UNSET:
            field_dict["zulu"] = zulu

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        jdk = d.pop("jdk", UNSET)

        type_ = d.pop("type", UNSET)

        zulu = d.pop("zulu", UNSET)

        advisory_zulu_version = cls(
            jdk=jdk,
            type_=type_,
            zulu=zulu,
        )

        advisory_zulu_version.additional_properties = d
        return advisory_zulu_version

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

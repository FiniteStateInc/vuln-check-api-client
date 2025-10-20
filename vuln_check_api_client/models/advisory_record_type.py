from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryRecordType")


@_attrs_define
class AdvisoryRecordType:
    """
    Attributes:
        finding (Union[Unset, str]):
        id (Union[Unset, str]):
        kind (Union[Unset, str]):
    """

    finding: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    kind: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        finding = self.finding

        id = self.id

        kind = self.kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if finding is not UNSET:
            field_dict["finding"] = finding
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        finding = d.pop("finding", UNSET)

        id = d.pop("id", UNSET)

        kind = d.pop("kind", UNSET)

        advisory_record_type = cls(
            finding=finding,
            id=id,
            kind=kind,
        )

        advisory_record_type.additional_properties = d
        return advisory_record_type

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

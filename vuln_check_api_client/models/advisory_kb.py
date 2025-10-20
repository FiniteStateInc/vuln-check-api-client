from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryKb")


@_attrs_define
class AdvisoryKb:
    """
    Attributes:
        kb_url (Union[Unset, str]):
        ms_date_added (Union[Unset, str]):
        status (Union[Unset, str]):
        supercedence (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    kb_url: Union[Unset, str] = UNSET
    ms_date_added: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    supercedence: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kb_url = self.kb_url

        ms_date_added = self.ms_date_added

        status = self.status

        supercedence = self.supercedence

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kb_url is not UNSET:
            field_dict["kb_url"] = kb_url
        if ms_date_added is not UNSET:
            field_dict["ms_date_added"] = ms_date_added
        if status is not UNSET:
            field_dict["status"] = status
        if supercedence is not UNSET:
            field_dict["supercedence"] = supercedence
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kb_url = d.pop("kb_url", UNSET)

        ms_date_added = d.pop("ms_date_added", UNSET)

        status = d.pop("status", UNSET)

        supercedence = d.pop("supercedence", UNSET)

        value = d.pop("value", UNSET)

        advisory_kb = cls(
            kb_url=kb_url,
            ms_date_added=ms_date_added,
            status=status,
            supercedence=supercedence,
            value=value,
        )

        advisory_kb.additional_properties = d
        return advisory_kb

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

from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryXDB")


@_attrs_define
class AdvisoryXDB:
    """
    Attributes:
        clone_ssh_url (Union[Unset, str]):
        date_added (Union[Unset, str]):
        exploit_type (Union[Unset, str]):
        xdb_id (Union[Unset, str]):
        xdb_url (Union[Unset, str]):
    """

    clone_ssh_url: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    exploit_type: Union[Unset, str] = UNSET
    xdb_id: Union[Unset, str] = UNSET
    xdb_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clone_ssh_url = self.clone_ssh_url

        date_added = self.date_added

        exploit_type = self.exploit_type

        xdb_id = self.xdb_id

        xdb_url = self.xdb_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clone_ssh_url is not UNSET:
            field_dict["clone_ssh_url"] = clone_ssh_url
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if exploit_type is not UNSET:
            field_dict["exploit_type"] = exploit_type
        if xdb_id is not UNSET:
            field_dict["xdb_id"] = xdb_id
        if xdb_url is not UNSET:
            field_dict["xdb_url"] = xdb_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        clone_ssh_url = d.pop("clone_ssh_url", UNSET)

        date_added = d.pop("date_added", UNSET)

        exploit_type = d.pop("exploit_type", UNSET)

        xdb_id = d.pop("xdb_id", UNSET)

        xdb_url = d.pop("xdb_url", UNSET)

        advisory_xdb = cls(
            clone_ssh_url=clone_ssh_url,
            date_added=date_added,
            exploit_type=exploit_type,
            xdb_id=xdb_id,
            xdb_url=xdb_url,
        )

        advisory_xdb.additional_properties = d
        return advisory_xdb

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

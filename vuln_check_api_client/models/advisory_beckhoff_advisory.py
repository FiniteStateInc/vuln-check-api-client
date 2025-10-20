from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryBeckhoffAdvisory")


@_attrs_define
class AdvisoryBeckhoffAdvisory:
    """
    Attributes:
        beckhoff_id (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cwe (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        date_last_revised (Union[Unset, str]): if in the future we can delete this great - it's just a dupe to
            normalize the field names
        name (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
        vde (Union[Unset, list[str]]):
    """

    beckhoff_id: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cwe: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    date_last_revised: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    vde: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        beckhoff_id = self.beckhoff_id

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cwe: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cwe, Unset):
            cwe = self.cwe

        date_added = self.date_added

        date_last_revised = self.date_last_revised

        name = self.name

        updated_at = self.updated_at

        url = self.url

        vde: Union[Unset, list[str]] = UNSET
        if not isinstance(self.vde, Unset):
            vde = self.vde

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if beckhoff_id is not UNSET:
            field_dict["beckhoff_id"] = beckhoff_id
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cwe is not UNSET:
            field_dict["cwe"] = cwe
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_last_revised is not UNSET:
            field_dict["date_last_revised"] = date_last_revised
        if name is not UNSET:
            field_dict["name"] = name
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url
        if vde is not UNSET:
            field_dict["vde"] = vde

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        beckhoff_id = d.pop("beckhoff_id", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cwe = cast(list[str], d.pop("cwe", UNSET))

        date_added = d.pop("date_added", UNSET)

        date_last_revised = d.pop("date_last_revised", UNSET)

        name = d.pop("name", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        vde = cast(list[str], d.pop("vde", UNSET))

        advisory_beckhoff_advisory = cls(
            beckhoff_id=beckhoff_id,
            cve=cve,
            cwe=cwe,
            date_added=date_added,
            date_last_revised=date_last_revised,
            name=name,
            updated_at=updated_at,
            url=url,
            vde=vde,
        )

        advisory_beckhoff_advisory.additional_properties = d
        return advisory_beckhoff_advisory

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

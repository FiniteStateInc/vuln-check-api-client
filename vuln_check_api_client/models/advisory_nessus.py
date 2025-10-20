from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryNessus")


@_attrs_define
class AdvisoryNessus:
    """
    Attributes:
        cpe (Union[Unset, list[str]]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        exploitability_ease (Union[Unset, str]): seems like only 3 vals for this
        filename (Union[Unset, str]):
        iava (Union[Unset, list[str]]):
        name (Union[Unset, str]):
        script_id (Union[Unset, int]):
        updated (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cpe: Union[Unset, list[str]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    exploitability_ease: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    iava: Union[Unset, list[str]] = UNSET
    name: Union[Unset, str] = UNSET
    script_id: Union[Unset, int] = UNSET
    updated: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpe: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cpe, Unset):
            cpe = self.cpe

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        exploitability_ease = self.exploitability_ease

        filename = self.filename

        iava: Union[Unset, list[str]] = UNSET
        if not isinstance(self.iava, Unset):
            iava = self.iava

        name = self.name

        script_id = self.script_id

        updated = self.updated

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpe is not UNSET:
            field_dict["cpe"] = cpe
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if exploitability_ease is not UNSET:
            field_dict["exploitability_ease"] = exploitability_ease
        if filename is not UNSET:
            field_dict["filename"] = filename
        if iava is not UNSET:
            field_dict["iava"] = iava
        if name is not UNSET:
            field_dict["name"] = name
        if script_id is not UNSET:
            field_dict["script_id"] = script_id
        if updated is not UNSET:
            field_dict["updated"] = updated
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cpe = cast(list[str], d.pop("cpe", UNSET))

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        exploitability_ease = d.pop("exploitability_ease", UNSET)

        filename = d.pop("filename", UNSET)

        iava = cast(list[str], d.pop("iava", UNSET))

        name = d.pop("name", UNSET)

        script_id = d.pop("script_id", UNSET)

        updated = d.pop("updated", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        advisory_nessus = cls(
            cpe=cpe,
            cve=cve,
            date_added=date_added,
            exploitability_ease=exploitability_ease,
            filename=filename,
            iava=iava,
            name=name,
            script_id=script_id,
            updated=updated,
            updated_at=updated_at,
            url=url,
        )

        advisory_nessus.additional_properties = d
        return advisory_nessus

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

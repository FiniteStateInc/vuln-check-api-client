from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryHuaweiIPS")


@_attrs_define
class AdvisoryHuaweiIPS:
    """
    Attributes:
        cnnvd (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        date_updated (Union[Unset, str]):
        name (Union[Unset, str]):
        severity (Union[Unset, str]):
        threat_id (Union[Unset, int]):
        url (Union[Unset, str]):
        vendor (Union[Unset, str]):
    """

    cnnvd: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    date_updated: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    threat_id: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cnnvd = self.cnnvd

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        date_updated = self.date_updated

        name = self.name

        severity = self.severity

        threat_id = self.threat_id

        url = self.url

        vendor = self.vendor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cnnvd is not UNSET:
            field_dict["cnnvd"] = cnnvd
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_updated is not UNSET:
            field_dict["date_updated"] = date_updated
        if name is not UNSET:
            field_dict["name"] = name
        if severity is not UNSET:
            field_dict["severity"] = severity
        if threat_id is not UNSET:
            field_dict["threat_id"] = threat_id
        if url is not UNSET:
            field_dict["url"] = url
        if vendor is not UNSET:
            field_dict["vendor"] = vendor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cnnvd = d.pop("cnnvd", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        date_updated = d.pop("date_updated", UNSET)

        name = d.pop("name", UNSET)

        severity = d.pop("severity", UNSET)

        threat_id = d.pop("threat_id", UNSET)

        url = d.pop("url", UNSET)

        vendor = d.pop("vendor", UNSET)

        advisory_huawei_ips = cls(
            cnnvd=cnnvd,
            cve=cve,
            date_added=date_added,
            date_updated=date_updated,
            name=name,
            severity=severity,
            threat_id=threat_id,
            url=url,
            vendor=vendor,
        )

        advisory_huawei_ips.additional_properties = d
        return advisory_huawei_ips

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

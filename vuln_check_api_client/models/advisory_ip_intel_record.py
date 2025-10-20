from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_record_type import AdvisoryRecordType


T = TypeVar("T", bound="AdvisoryIpIntelRecord")


@_attrs_define
class AdvisoryIpIntelRecord:
    """
    Attributes:
        asn (Union[Unset, str]):
        city (Union[Unset, str]):
        country (Union[Unset, str]):
        country_code (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        feed_ids (Union[Unset, list[str]]):
        hostnames (Union[Unset, list[str]]):
        ip (Union[Unset, str]):
        last_seen (Union[Unset, str]):
        matches (Union[Unset, list[str]]):
        port (Union[Unset, int]):
        ssl (Union[Unset, bool]):
        type_ (Union[Unset, AdvisoryRecordType]):
    """

    asn: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    feed_ids: Union[Unset, list[str]] = UNSET
    hostnames: Union[Unset, list[str]] = UNSET
    ip: Union[Unset, str] = UNSET
    last_seen: Union[Unset, str] = UNSET
    matches: Union[Unset, list[str]] = UNSET
    port: Union[Unset, int] = UNSET
    ssl: Union[Unset, bool] = UNSET
    type_: Union[Unset, "AdvisoryRecordType"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asn = self.asn

        city = self.city

        country = self.country

        country_code = self.country_code

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        feed_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.feed_ids, Unset):
            feed_ids = self.feed_ids

        hostnames: Union[Unset, list[str]] = UNSET
        if not isinstance(self.hostnames, Unset):
            hostnames = self.hostnames

        ip = self.ip

        last_seen = self.last_seen

        matches: Union[Unset, list[str]] = UNSET
        if not isinstance(self.matches, Unset):
            matches = self.matches

        port = self.port

        ssl = self.ssl

        type_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asn is not UNSET:
            field_dict["asn"] = asn
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if cve is not UNSET:
            field_dict["cve"] = cve
        if feed_ids is not UNSET:
            field_dict["feed_ids"] = feed_ids
        if hostnames is not UNSET:
            field_dict["hostnames"] = hostnames
        if ip is not UNSET:
            field_dict["ip"] = ip
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if matches is not UNSET:
            field_dict["matches"] = matches
        if port is not UNSET:
            field_dict["port"] = port
        if ssl is not UNSET:
            field_dict["ssl"] = ssl
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_record_type import AdvisoryRecordType

        d = dict(src_dict)
        asn = d.pop("asn", UNSET)

        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        country_code = d.pop("country_code", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        feed_ids = cast(list[str], d.pop("feed_ids", UNSET))

        hostnames = cast(list[str], d.pop("hostnames", UNSET))

        ip = d.pop("ip", UNSET)

        last_seen = d.pop("lastSeen", UNSET)

        matches = cast(list[str], d.pop("matches", UNSET))

        port = d.pop("port", UNSET)

        ssl = d.pop("ssl", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, AdvisoryRecordType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AdvisoryRecordType.from_dict(_type_)

        advisory_ip_intel_record = cls(
            asn=asn,
            city=city,
            country=country,
            country_code=country_code,
            cve=cve,
            feed_ids=feed_ids,
            hostnames=hostnames,
            ip=ip,
            last_seen=last_seen,
            matches=matches,
            port=port,
            ssl=ssl,
            type_=type_,
        )

        advisory_ip_intel_record.additional_properties = d
        return advisory_ip_intel_record

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

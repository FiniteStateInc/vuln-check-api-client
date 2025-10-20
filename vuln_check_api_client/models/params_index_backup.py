from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ParamsIndexBackup")


@_attrs_define
class ParamsIndexBackup:
    """
    Attributes:
        date_added (Union[Unset, str]):
        filename (Union[Unset, str]):
        sha256 (Union[Unset, str]):
        url (Union[Unset, str]):
        url_ap_southeast_2 (Union[Unset, str]):
        url_eu_west_2 (Union[Unset, str]):
        url_expires (Union[Unset, str]):
        url_mrap (Union[Unset, str]):
        url_ttl_minutes (Union[Unset, int]):
        url_us_east_1 (Union[Unset, str]):
        url_us_west_2 (Union[Unset, str]):
    """

    date_added: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    sha256: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    url_ap_southeast_2: Union[Unset, str] = UNSET
    url_eu_west_2: Union[Unset, str] = UNSET
    url_expires: Union[Unset, str] = UNSET
    url_mrap: Union[Unset, str] = UNSET
    url_ttl_minutes: Union[Unset, int] = UNSET
    url_us_east_1: Union[Unset, str] = UNSET
    url_us_west_2: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_added = self.date_added

        filename = self.filename

        sha256 = self.sha256

        url = self.url

        url_ap_southeast_2 = self.url_ap_southeast_2

        url_eu_west_2 = self.url_eu_west_2

        url_expires = self.url_expires

        url_mrap = self.url_mrap

        url_ttl_minutes = self.url_ttl_minutes

        url_us_east_1 = self.url_us_east_1

        url_us_west_2 = self.url_us_west_2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if filename is not UNSET:
            field_dict["filename"] = filename
        if sha256 is not UNSET:
            field_dict["sha256"] = sha256
        if url is not UNSET:
            field_dict["url"] = url
        if url_ap_southeast_2 is not UNSET:
            field_dict["url_ap-southeast-2"] = url_ap_southeast_2
        if url_eu_west_2 is not UNSET:
            field_dict["url_eu-west-2"] = url_eu_west_2
        if url_expires is not UNSET:
            field_dict["url_expires"] = url_expires
        if url_mrap is not UNSET:
            field_dict["url_mrap"] = url_mrap
        if url_ttl_minutes is not UNSET:
            field_dict["url_ttl_minutes"] = url_ttl_minutes
        if url_us_east_1 is not UNSET:
            field_dict["url_us-east-1"] = url_us_east_1
        if url_us_west_2 is not UNSET:
            field_dict["url_us-west-2"] = url_us_west_2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date_added = d.pop("date_added", UNSET)

        filename = d.pop("filename", UNSET)

        sha256 = d.pop("sha256", UNSET)

        url = d.pop("url", UNSET)

        url_ap_southeast_2 = d.pop("url_ap-southeast-2", UNSET)

        url_eu_west_2 = d.pop("url_eu-west-2", UNSET)

        url_expires = d.pop("url_expires", UNSET)

        url_mrap = d.pop("url_mrap", UNSET)

        url_ttl_minutes = d.pop("url_ttl_minutes", UNSET)

        url_us_east_1 = d.pop("url_us-east-1", UNSET)

        url_us_west_2 = d.pop("url_us-west-2", UNSET)

        params_index_backup = cls(
            date_added=date_added,
            filename=filename,
            sha256=sha256,
            url=url,
            url_ap_southeast_2=url_ap_southeast_2,
            url_eu_west_2=url_eu_west_2,
            url_expires=url_expires,
            url_mrap=url_mrap,
            url_ttl_minutes=url_ttl_minutes,
            url_us_east_1=url_us_east_1,
            url_us_west_2=url_us_west_2,
        )

        params_index_backup.additional_properties = d
        return params_index_backup

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

from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryEOLAlibaba")


@_attrs_define
class AdvisoryEOLAlibaba:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        eol_date (Union[Unset, str]):
        eol_name (Union[Unset, str]):
        product (Union[Unset, str]):
        release_date (Union[Unset, str]):
        url (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    eol_date: Union[Unset, str] = UNSET
    eol_name: Union[Unset, str] = UNSET
    product: Union[Unset, str] = UNSET
    release_date: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        eol_date = self.eol_date

        eol_name = self.eol_name

        product = self.product

        release_date = self.release_date

        url = self.url

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if eol_date is not UNSET:
            field_dict["eol_date"] = eol_date
        if eol_name is not UNSET:
            field_dict["eol_name"] = eol_name
        if product is not UNSET:
            field_dict["product"] = product
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if url is not UNSET:
            field_dict["url"] = url
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        eol_date = d.pop("eol_date", UNSET)

        eol_name = d.pop("eol_name", UNSET)

        product = d.pop("product", UNSET)

        release_date = d.pop("release_date", UNSET)

        url = d.pop("url", UNSET)

        version = d.pop("version", UNSET)

        advisory_eol_alibaba = cls(
            cve=cve,
            eol_date=eol_date,
            eol_name=eol_name,
            product=product,
            release_date=release_date,
            url=url,
            version=version,
        )

        advisory_eol_alibaba.additional_properties = d
        return advisory_eol_alibaba

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

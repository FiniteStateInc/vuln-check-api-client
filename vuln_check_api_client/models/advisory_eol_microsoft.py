from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryEOLMicrosoft")


@_attrs_define
class AdvisoryEOLMicrosoft:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        edition (Union[Unset, str]):
        extended_end_date (Union[Unset, str]):
        mainstream_date (Union[Unset, str]):
        product (Union[Unset, str]):
        release (Union[Unset, str]):
        release_end_date (Union[Unset, str]):
        release_start_date (Union[Unset, str]):
        retirement_date (Union[Unset, str]):
        start_date (Union[Unset, str]):
        support_policy (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    edition: Union[Unset, str] = UNSET
    extended_end_date: Union[Unset, str] = UNSET
    mainstream_date: Union[Unset, str] = UNSET
    product: Union[Unset, str] = UNSET
    release: Union[Unset, str] = UNSET
    release_end_date: Union[Unset, str] = UNSET
    release_start_date: Union[Unset, str] = UNSET
    retirement_date: Union[Unset, str] = UNSET
    start_date: Union[Unset, str] = UNSET
    support_policy: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        edition = self.edition

        extended_end_date = self.extended_end_date

        mainstream_date = self.mainstream_date

        product = self.product

        release = self.release

        release_end_date = self.release_end_date

        release_start_date = self.release_start_date

        retirement_date = self.retirement_date

        start_date = self.start_date

        support_policy = self.support_policy

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if edition is not UNSET:
            field_dict["edition"] = edition
        if extended_end_date is not UNSET:
            field_dict["extended_end_date"] = extended_end_date
        if mainstream_date is not UNSET:
            field_dict["mainstream_date"] = mainstream_date
        if product is not UNSET:
            field_dict["product"] = product
        if release is not UNSET:
            field_dict["release"] = release
        if release_end_date is not UNSET:
            field_dict["release_end_date"] = release_end_date
        if release_start_date is not UNSET:
            field_dict["release_start_date"] = release_start_date
        if retirement_date is not UNSET:
            field_dict["retirement_date"] = retirement_date
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if support_policy is not UNSET:
            field_dict["support_policy"] = support_policy
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        edition = d.pop("edition", UNSET)

        extended_end_date = d.pop("extended_end_date", UNSET)

        mainstream_date = d.pop("mainstream_date", UNSET)

        product = d.pop("product", UNSET)

        release = d.pop("release", UNSET)

        release_end_date = d.pop("release_end_date", UNSET)

        release_start_date = d.pop("release_start_date", UNSET)

        retirement_date = d.pop("retirement_date", UNSET)

        start_date = d.pop("start_date", UNSET)

        support_policy = d.pop("support_policy", UNSET)

        url = d.pop("url", UNSET)

        advisory_eol_microsoft = cls(
            cve=cve,
            edition=edition,
            extended_end_date=extended_end_date,
            mainstream_date=mainstream_date,
            product=product,
            release=release,
            release_end_date=release_end_date,
            release_start_date=release_start_date,
            retirement_date=retirement_date,
            start_date=start_date,
            support_policy=support_policy,
            url=url,
        )

        advisory_eol_microsoft.additional_properties = d
        return advisory_eol_microsoft

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

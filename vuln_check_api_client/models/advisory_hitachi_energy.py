from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryHitachiEnergy")


@_attrs_define
class AdvisoryHitachiEnergy:
    """
    Attributes:
        advisory_id (Union[Unset, str]):
        csaf_url (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        exploited (Union[Unset, bool]):
        products (Union[Unset, list[str]]):
        title (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    advisory_id: Union[Unset, str] = UNSET
    csaf_url: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    exploited: Union[Unset, bool] = UNSET
    products: Union[Unset, list[str]] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advisory_id = self.advisory_id

        csaf_url = self.csaf_url

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        exploited = self.exploited

        products: Union[Unset, list[str]] = UNSET
        if not isinstance(self.products, Unset):
            products = self.products

        title = self.title

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advisory_id is not UNSET:
            field_dict["advisory_id"] = advisory_id
        if csaf_url is not UNSET:
            field_dict["csaf_url"] = csaf_url
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if exploited is not UNSET:
            field_dict["exploited"] = exploited
        if products is not UNSET:
            field_dict["products"] = products
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        advisory_id = d.pop("advisory_id", UNSET)

        csaf_url = d.pop("csaf_url", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        exploited = d.pop("exploited", UNSET)

        products = cast(list[str], d.pop("products", UNSET))

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        advisory_hitachi_energy = cls(
            advisory_id=advisory_id,
            csaf_url=csaf_url,
            cve=cve,
            date_added=date_added,
            exploited=exploited,
            products=products,
            title=title,
            updated_at=updated_at,
            url=url,
        )

        advisory_hitachi_energy.additional_properties = d
        return advisory_hitachi_energy

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

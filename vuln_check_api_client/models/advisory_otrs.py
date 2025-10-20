from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryOTRS")


@_attrs_define
class AdvisoryOTRS:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        fixed (Union[Unset, str]):
        id (Union[Unset, str]):
        product (Union[Unset, str]):
        release (Union[Unset, str]):
        risk (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    fixed: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    product: Union[Unset, str] = UNSET
    release: Union[Unset, str] = UNSET
    risk: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        fixed = self.fixed

        id = self.id

        product = self.product

        release = self.release

        risk = self.risk

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if fixed is not UNSET:
            field_dict["fixed"] = fixed
        if id is not UNSET:
            field_dict["id"] = id
        if product is not UNSET:
            field_dict["product"] = product
        if release is not UNSET:
            field_dict["release"] = release
        if risk is not UNSET:
            field_dict["risk"] = risk
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        fixed = d.pop("fixed", UNSET)

        id = d.pop("id", UNSET)

        product = d.pop("product", UNSET)

        release = d.pop("release", UNSET)

        risk = d.pop("risk", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_otrs = cls(
            cve=cve,
            date_added=date_added,
            fixed=fixed,
            id=id,
            product=product,
            release=release,
            risk=risk,
            title=title,
            url=url,
        )

        advisory_otrs.additional_properties = d
        return advisory_otrs

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

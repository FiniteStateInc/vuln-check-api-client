from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisorySiemensRemediation")


@_attrs_define
class AdvisorySiemensRemediation:
    """
    Attributes:
        category (Union[Unset, str]):
        details (Union[Unset, str]):
        product_ids (Union[Unset, list[str]]):
        url (Union[Unset, str]):
    """

    category: Union[Unset, str] = UNSET
    details: Union[Unset, str] = UNSET
    product_ids: Union[Unset, list[str]] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        details = self.details

        product_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.product_ids, Unset):
            product_ids = self.product_ids

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if details is not UNSET:
            field_dict["details"] = details
        if product_ids is not UNSET:
            field_dict["product_ids"] = product_ids
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category", UNSET)

        details = d.pop("details", UNSET)

        product_ids = cast(list[str], d.pop("product_ids", UNSET))

        url = d.pop("url", UNSET)

        advisory_siemens_remediation = cls(
            category=category,
            details=details,
            product_ids=product_ids,
            url=url,
        )

        advisory_siemens_remediation.additional_properties = d
        return advisory_siemens_remediation

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

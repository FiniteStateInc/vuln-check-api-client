from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryJetBrains")


@_attrs_define
class AdvisoryJetBrains:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        cwe (Union[Unset, str]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        product (Union[Unset, str]):
        resolved_in (Union[Unset, list[str]]):
        severity (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    cwe: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    product: Union[Unset, str] = UNSET
    resolved_in: Union[Unset, list[str]] = UNSET
    severity: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cwe = self.cwe

        date_added = self.date_added

        description = self.description

        product = self.product

        resolved_in: Union[Unset, list[str]] = UNSET
        if not isinstance(self.resolved_in, Unset):
            resolved_in = self.resolved_in

        severity = self.severity

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cwe is not UNSET:
            field_dict["cwe"] = cwe
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if product is not UNSET:
            field_dict["product"] = product
        if resolved_in is not UNSET:
            field_dict["resolved_in"] = resolved_in
        if severity is not UNSET:
            field_dict["severity"] = severity
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        cwe = d.pop("cwe", UNSET)

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        product = d.pop("product", UNSET)

        resolved_in = cast(list[str], d.pop("resolved_in", UNSET))

        severity = d.pop("severity", UNSET)

        url = d.pop("url", UNSET)

        advisory_jet_brains = cls(
            cve=cve,
            cwe=cwe,
            date_added=date_added,
            description=description,
            product=product,
            resolved_in=resolved_in,
            severity=severity,
            url=url,
        )

        advisory_jet_brains.additional_properties = d
        return advisory_jet_brains

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

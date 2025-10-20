from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryDeltaAdvisory")


@_attrs_define
class AdvisoryDeltaAdvisory:
    """
    Attributes:
        affected_products (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cvss (Union[Unset, str]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        link (Union[Unset, str]):
        recommended_action (Union[Unset, str]):
        title (Union[Unset, str]):
    """

    affected_products: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvss: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    recommended_action: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_products = self.affected_products

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvss = self.cvss

        date_added = self.date_added

        description = self.description

        link = self.link

        recommended_action = self.recommended_action

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_products is not UNSET:
            field_dict["affectedProducts"] = affected_products
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss is not UNSET:
            field_dict["cvss"] = cvss
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if link is not UNSET:
            field_dict["link"] = link
        if recommended_action is not UNSET:
            field_dict["recommendedAction"] = recommended_action
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_products = d.pop("affectedProducts", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cvss = d.pop("cvss", UNSET)

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        link = d.pop("link", UNSET)

        recommended_action = d.pop("recommendedAction", UNSET)

        title = d.pop("title", UNSET)

        advisory_delta_advisory = cls(
            affected_products=affected_products,
            cve=cve,
            cvss=cvss,
            date_added=date_added,
            description=description,
            link=link,
            recommended_action=recommended_action,
            title=title,
        )

        advisory_delta_advisory.additional_properties = d
        return advisory_delta_advisory

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

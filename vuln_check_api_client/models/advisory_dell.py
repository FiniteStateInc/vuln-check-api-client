from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_dell_cve import AdvisoryDellCVE


T = TypeVar("T", bound="AdvisoryDell")


@_attrs_define
class AdvisoryDell:
    """
    Attributes:
        article_number (Union[Unset, str]):
        combined_product_list (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        dell_cves (Union[Unset, list['AdvisoryDellCVE']]):
        severity (Union[Unset, str]):
        title (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    article_number: Union[Unset, str] = UNSET
    combined_product_list: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    dell_cves: Union[Unset, list["AdvisoryDellCVE"]] = UNSET
    severity: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        article_number = self.article_number

        combined_product_list = self.combined_product_list

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        dell_cves: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.dell_cves, Unset):
            dell_cves = []
            for dell_cves_item_data in self.dell_cves:
                dell_cves_item = dell_cves_item_data.to_dict()
                dell_cves.append(dell_cves_item)

        severity = self.severity

        title = self.title

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if article_number is not UNSET:
            field_dict["articleNumber"] = article_number
        if combined_product_list is not UNSET:
            field_dict["combinedProductList"] = combined_product_list
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if dell_cves is not UNSET:
            field_dict["dell_cves"] = dell_cves
        if severity is not UNSET:
            field_dict["severity"] = severity
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_dell_cve import AdvisoryDellCVE

        d = dict(src_dict)
        article_number = d.pop("articleNumber", UNSET)

        combined_product_list = d.pop("combinedProductList", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        dell_cves = []
        _dell_cves = d.pop("dell_cves", UNSET)
        for dell_cves_item_data in _dell_cves or []:
            dell_cves_item = AdvisoryDellCVE.from_dict(dell_cves_item_data)

            dell_cves.append(dell_cves_item)

        severity = d.pop("severity", UNSET)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        advisory_dell = cls(
            article_number=article_number,
            combined_product_list=combined_product_list,
            cve=cve,
            date_added=date_added,
            dell_cves=dell_cves,
            severity=severity,
            title=title,
            updated_at=updated_at,
            url=url,
        )

        advisory_dell.additional_properties = d
        return advisory_dell

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

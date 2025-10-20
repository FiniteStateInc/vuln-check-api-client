from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCISAAlert")


@_attrs_define
class AdvisoryCISAAlert:
    """
    Attributes:
        affected_products (Union[Unset, str]):
        alert_id (Union[Unset, str]):
        archived (Union[Unset, bool]):
        cve (Union[Unset, list[str]]):
        cveexploited_itw (Union[Unset, bool]):
        cvss (Union[Unset, str]):
        date_added (Union[Unset, str]):
        icsa (Union[Unset, bool]):
        icsma (Union[Unset, bool]):
        mitigations (Union[Unset, str]):
        release_date (Union[Unset, str]):
        title (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
        vendor (Union[Unset, str]):
    """

    affected_products: Union[Unset, str] = UNSET
    alert_id: Union[Unset, str] = UNSET
    archived: Union[Unset, bool] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cveexploited_itw: Union[Unset, bool] = UNSET
    cvss: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    icsa: Union[Unset, bool] = UNSET
    icsma: Union[Unset, bool] = UNSET
    mitigations: Union[Unset, str] = UNSET
    release_date: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_products = self.affected_products

        alert_id = self.alert_id

        archived = self.archived

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cveexploited_itw = self.cveexploited_itw

        cvss = self.cvss

        date_added = self.date_added

        icsa = self.icsa

        icsma = self.icsma

        mitigations = self.mitigations

        release_date = self.release_date

        title = self.title

        updated_at = self.updated_at

        url = self.url

        vendor = self.vendor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_products is not UNSET:
            field_dict["affectedProducts"] = affected_products
        if alert_id is not UNSET:
            field_dict["alertID"] = alert_id
        if archived is not UNSET:
            field_dict["archived"] = archived
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cveexploited_itw is not UNSET:
            field_dict["cveexploitedITW"] = cveexploited_itw
        if cvss is not UNSET:
            field_dict["cvss"] = cvss
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if icsa is not UNSET:
            field_dict["icsa"] = icsa
        if icsma is not UNSET:
            field_dict["icsma"] = icsma
        if mitigations is not UNSET:
            field_dict["mitigations"] = mitigations
        if release_date is not UNSET:
            field_dict["releaseDate"] = release_date
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url
        if vendor is not UNSET:
            field_dict["vendor"] = vendor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_products = d.pop("affectedProducts", UNSET)

        alert_id = d.pop("alertID", UNSET)

        archived = d.pop("archived", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cveexploited_itw = d.pop("cveexploitedITW", UNSET)

        cvss = d.pop("cvss", UNSET)

        date_added = d.pop("date_added", UNSET)

        icsa = d.pop("icsa", UNSET)

        icsma = d.pop("icsma", UNSET)

        mitigations = d.pop("mitigations", UNSET)

        release_date = d.pop("releaseDate", UNSET)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        vendor = d.pop("vendor", UNSET)

        advisory_cisa_alert = cls(
            affected_products=affected_products,
            alert_id=alert_id,
            archived=archived,
            cve=cve,
            cveexploited_itw=cveexploited_itw,
            cvss=cvss,
            date_added=date_added,
            icsa=icsa,
            icsma=icsma,
            mitigations=mitigations,
            release_date=release_date,
            title=title,
            updated_at=updated_at,
            url=url,
            vendor=vendor,
        )

        advisory_cisa_alert.additional_properties = d
        return advisory_cisa_alert

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

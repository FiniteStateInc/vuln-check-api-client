from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_schneider_cve import AdvisorySchneiderCVE


T = TypeVar("T", bound="AdvisorySchneiderElectricAdvisory")


@_attrs_define
class AdvisorySchneiderElectricAdvisory:
    """
    Attributes:
        csaf_url (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cwe (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        pdf_url (Union[Unset, str]):
        schneider_cves (Union[Unset, list['AdvisorySchneiderCVE']]):
        schneider_electric_id (Union[Unset, str]):
        title (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    csaf_url: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cwe: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    pdf_url: Union[Unset, str] = UNSET
    schneider_cves: Union[Unset, list["AdvisorySchneiderCVE"]] = UNSET
    schneider_electric_id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        csaf_url = self.csaf_url

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cwe: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cwe, Unset):
            cwe = self.cwe

        date_added = self.date_added

        pdf_url = self.pdf_url

        schneider_cves: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.schneider_cves, Unset):
            schneider_cves = []
            for schneider_cves_item_data in self.schneider_cves:
                schneider_cves_item = schneider_cves_item_data.to_dict()
                schneider_cves.append(schneider_cves_item)

        schneider_electric_id = self.schneider_electric_id

        title = self.title

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if csaf_url is not UNSET:
            field_dict["csaf_url"] = csaf_url
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cwe is not UNSET:
            field_dict["cwe"] = cwe
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if pdf_url is not UNSET:
            field_dict["pdf_url"] = pdf_url
        if schneider_cves is not UNSET:
            field_dict["schneider_cves"] = schneider_cves
        if schneider_electric_id is not UNSET:
            field_dict["schneider_electric_id"] = schneider_electric_id
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_schneider_cve import AdvisorySchneiderCVE

        d = dict(src_dict)
        csaf_url = d.pop("csaf_url", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cwe = cast(list[str], d.pop("cwe", UNSET))

        date_added = d.pop("date_added", UNSET)

        pdf_url = d.pop("pdf_url", UNSET)

        schneider_cves = []
        _schneider_cves = d.pop("schneider_cves", UNSET)
        for schneider_cves_item_data in _schneider_cves or []:
            schneider_cves_item = AdvisorySchneiderCVE.from_dict(schneider_cves_item_data)

            schneider_cves.append(schneider_cves_item)

        schneider_electric_id = d.pop("schneider_electric_id", UNSET)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        advisory_schneider_electric_advisory = cls(
            csaf_url=csaf_url,
            cve=cve,
            cwe=cwe,
            date_added=date_added,
            pdf_url=pdf_url,
            schneider_cves=schneider_cves,
            schneider_electric_id=schneider_electric_id,
            title=title,
            updated_at=updated_at,
            url=url,
        )

        advisory_schneider_electric_advisory.additional_properties = d
        return advisory_schneider_electric_advisory

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

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_affected_product import AdvisoryAffectedProduct


T = TypeVar("T", bound="AdvisoryLexmarkAdvisory")


@_attrs_define
class AdvisoryLexmarkAdvisory:
    """
    Attributes:
        affected_products (Union[Unset, list['AdvisoryAffectedProduct']]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        details (Union[Unset, str]):
        impact (Union[Unset, str]):
        last_update (Union[Unset, str]):
        link (Union[Unset, str]):
        public_release_date (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        revision (Union[Unset, str]):
        summary (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        workarounds (Union[Unset, str]):
    """

    affected_products: Union[Unset, list["AdvisoryAffectedProduct"]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    details: Union[Unset, str] = UNSET
    impact: Union[Unset, str] = UNSET
    last_update: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    public_release_date: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    revision: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    workarounds: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_products: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.affected_products, Unset):
            affected_products = []
            for affected_products_item_data in self.affected_products:
                affected_products_item = affected_products_item_data.to_dict()
                affected_products.append(affected_products_item)

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        details = self.details

        impact = self.impact

        last_update = self.last_update

        link = self.link

        public_release_date = self.public_release_date

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        revision = self.revision

        summary = self.summary

        updated_at = self.updated_at

        workarounds = self.workarounds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_products is not UNSET:
            field_dict["affectedProducts"] = affected_products
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if details is not UNSET:
            field_dict["details"] = details
        if impact is not UNSET:
            field_dict["impact"] = impact
        if last_update is not UNSET:
            field_dict["lastUpdate"] = last_update
        if link is not UNSET:
            field_dict["link"] = link
        if public_release_date is not UNSET:
            field_dict["publicReleaseDate"] = public_release_date
        if references is not UNSET:
            field_dict["references"] = references
        if revision is not UNSET:
            field_dict["revision"] = revision
        if summary is not UNSET:
            field_dict["summary"] = summary
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workarounds is not UNSET:
            field_dict["workarounds"] = workarounds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_affected_product import AdvisoryAffectedProduct

        d = dict(src_dict)
        affected_products = []
        _affected_products = d.pop("affectedProducts", UNSET)
        for affected_products_item_data in _affected_products or []:
            affected_products_item = AdvisoryAffectedProduct.from_dict(affected_products_item_data)

            affected_products.append(affected_products_item)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        details = d.pop("details", UNSET)

        impact = d.pop("impact", UNSET)

        last_update = d.pop("lastUpdate", UNSET)

        link = d.pop("link", UNSET)

        public_release_date = d.pop("publicReleaseDate", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        revision = d.pop("revision", UNSET)

        summary = d.pop("summary", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        workarounds = d.pop("workarounds", UNSET)

        advisory_lexmark_advisory = cls(
            affected_products=affected_products,
            cve=cve,
            date_added=date_added,
            details=details,
            impact=impact,
            last_update=last_update,
            link=link,
            public_release_date=public_release_date,
            references=references,
            revision=revision,
            summary=summary,
            updated_at=updated_at,
            workarounds=workarounds,
        )

        advisory_lexmark_advisory.additional_properties = d
        return advisory_lexmark_advisory

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

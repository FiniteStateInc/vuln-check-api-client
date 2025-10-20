from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_mozilla_component import AdvisoryMozillaComponent


T = TypeVar("T", bound="AdvisoryMozillaAdvisory")


@_attrs_define
class AdvisoryMozillaAdvisory:
    """
    Attributes:
        affected_components (Union[Unset, list['AdvisoryMozillaComponent']]):
        bugzilla (Union[Unset, list[str]]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        fixed_in (Union[Unset, list[str]]):
        impact (Union[Unset, str]):
        products (Union[Unset, list[str]]):
        reporter (Union[Unset, str]):
        risk (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    affected_components: Union[Unset, list["AdvisoryMozillaComponent"]] = UNSET
    bugzilla: Union[Unset, list[str]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    fixed_in: Union[Unset, list[str]] = UNSET
    impact: Union[Unset, str] = UNSET
    products: Union[Unset, list[str]] = UNSET
    reporter: Union[Unset, str] = UNSET
    risk: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_components: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.affected_components, Unset):
            affected_components = []
            for affected_components_item_data in self.affected_components:
                affected_components_item = affected_components_item_data.to_dict()
                affected_components.append(affected_components_item)

        bugzilla: Union[Unset, list[str]] = UNSET
        if not isinstance(self.bugzilla, Unset):
            bugzilla = self.bugzilla

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        description = self.description

        fixed_in: Union[Unset, list[str]] = UNSET
        if not isinstance(self.fixed_in, Unset):
            fixed_in = self.fixed_in

        impact = self.impact

        products: Union[Unset, list[str]] = UNSET
        if not isinstance(self.products, Unset):
            products = self.products

        reporter = self.reporter

        risk = self.risk

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_components is not UNSET:
            field_dict["affected_components"] = affected_components
        if bugzilla is not UNSET:
            field_dict["bugzilla"] = bugzilla
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if fixed_in is not UNSET:
            field_dict["fixed_in"] = fixed_in
        if impact is not UNSET:
            field_dict["impact"] = impact
        if products is not UNSET:
            field_dict["products"] = products
        if reporter is not UNSET:
            field_dict["reporter"] = reporter
        if risk is not UNSET:
            field_dict["risk"] = risk
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_mozilla_component import AdvisoryMozillaComponent

        d = dict(src_dict)
        affected_components = []
        _affected_components = d.pop("affected_components", UNSET)
        for affected_components_item_data in _affected_components or []:
            affected_components_item = AdvisoryMozillaComponent.from_dict(affected_components_item_data)

            affected_components.append(affected_components_item)

        bugzilla = cast(list[str], d.pop("bugzilla", UNSET))

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        fixed_in = cast(list[str], d.pop("fixed_in", UNSET))

        impact = d.pop("impact", UNSET)

        products = cast(list[str], d.pop("products", UNSET))

        reporter = d.pop("reporter", UNSET)

        risk = d.pop("risk", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_mozilla_advisory = cls(
            affected_components=affected_components,
            bugzilla=bugzilla,
            cve=cve,
            date_added=date_added,
            description=description,
            fixed_in=fixed_in,
            impact=impact,
            products=products,
            reporter=reporter,
            risk=risk,
            title=title,
            url=url,
        )

        advisory_mozilla_advisory.additional_properties = d
        return advisory_mozilla_advisory

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

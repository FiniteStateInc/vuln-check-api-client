from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_adobe_affected import AdvisoryAdobeAffected
    from ..models.advisory_adobe_cve import AdvisoryAdobeCVE
    from ..models.advisory_adobe_solution import AdvisoryAdobeSolution


T = TypeVar("T", bound="AdvisoryAdobeAdvisory")


@_attrs_define
class AdvisoryAdobeAdvisory:
    """
    Attributes:
        adobe_cves (Union[Unset, list['AdvisoryAdobeCVE']]):
        affected (Union[Unset, list['AdvisoryAdobeAffected']]):
        bulletin_id (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        link (Union[Unset, str]):
        solutions (Union[Unset, list['AdvisoryAdobeSolution']]):
        updated_at (Union[Unset, str]):
    """

    adobe_cves: Union[Unset, list["AdvisoryAdobeCVE"]] = UNSET
    affected: Union[Unset, list["AdvisoryAdobeAffected"]] = UNSET
    bulletin_id: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    solutions: Union[Unset, list["AdvisoryAdobeSolution"]] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        adobe_cves: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.adobe_cves, Unset):
            adobe_cves = []
            for adobe_cves_item_data in self.adobe_cves:
                adobe_cves_item = adobe_cves_item_data.to_dict()
                adobe_cves.append(adobe_cves_item)

        affected: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.affected, Unset):
            affected = []
            for affected_item_data in self.affected:
                affected_item = affected_item_data.to_dict()
                affected.append(affected_item)

        bulletin_id = self.bulletin_id

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        link = self.link

        solutions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.solutions, Unset):
            solutions = []
            for solutions_item_data in self.solutions:
                solutions_item = solutions_item_data.to_dict()
                solutions.append(solutions_item)

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if adobe_cves is not UNSET:
            field_dict["adobe_cves"] = adobe_cves
        if affected is not UNSET:
            field_dict["affected"] = affected
        if bulletin_id is not UNSET:
            field_dict["bulletinId"] = bulletin_id
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if link is not UNSET:
            field_dict["link"] = link
        if solutions is not UNSET:
            field_dict["solutions"] = solutions
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_adobe_affected import AdvisoryAdobeAffected
        from ..models.advisory_adobe_cve import AdvisoryAdobeCVE
        from ..models.advisory_adobe_solution import AdvisoryAdobeSolution

        d = dict(src_dict)
        adobe_cves = []
        _adobe_cves = d.pop("adobe_cves", UNSET)
        for adobe_cves_item_data in _adobe_cves or []:
            adobe_cves_item = AdvisoryAdobeCVE.from_dict(adobe_cves_item_data)

            adobe_cves.append(adobe_cves_item)

        affected = []
        _affected = d.pop("affected", UNSET)
        for affected_item_data in _affected or []:
            affected_item = AdvisoryAdobeAffected.from_dict(affected_item_data)

            affected.append(affected_item)

        bulletin_id = d.pop("bulletinId", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        link = d.pop("link", UNSET)

        solutions = []
        _solutions = d.pop("solutions", UNSET)
        for solutions_item_data in _solutions or []:
            solutions_item = AdvisoryAdobeSolution.from_dict(solutions_item_data)

            solutions.append(solutions_item)

        updated_at = d.pop("updated_at", UNSET)

        advisory_adobe_advisory = cls(
            adobe_cves=adobe_cves,
            affected=affected,
            bulletin_id=bulletin_id,
            cve=cve,
            date_added=date_added,
            link=link,
            solutions=solutions,
            updated_at=updated_at,
        )

        advisory_adobe_advisory.additional_properties = d
        return advisory_adobe_advisory

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

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_rocky_cve import AdvisoryRockyCve
    from ..models.advisory_rocky_fix import AdvisoryRockyFix
    from ..models.advisory_rocky_rpms import AdvisoryRockyRpms


T = TypeVar("T", bound="AdvisoryRockyAdvisory")


@_attrs_define
class AdvisoryRockyAdvisory:
    """
    Attributes:
        affected_products (Union[Unset, list[str]]):
        build_references (Union[Unset, list[str]]):
        cves (Union[Unset, list['AdvisoryRockyCve']]):
        description (Union[Unset, str]):
        fixes (Union[Unset, list['AdvisoryRockyFix']]):
        name (Union[Unset, str]):
        published_at (Union[Unset, str]):
        reboot_suggested (Union[Unset, bool]):
        references (Union[Unset, list[str]]):
        rpms (Union[Unset, AdvisoryRockyRpms]):
        severity (Union[Unset, str]):
        short_code (Union[Unset, str]):
        solution (Union[Unset, str]):
        synopsis (Union[Unset, str]):
        topic (Union[Unset, str]):
        type_ (Union[Unset, str]):
    """

    affected_products: Union[Unset, list[str]] = UNSET
    build_references: Union[Unset, list[str]] = UNSET
    cves: Union[Unset, list["AdvisoryRockyCve"]] = UNSET
    description: Union[Unset, str] = UNSET
    fixes: Union[Unset, list["AdvisoryRockyFix"]] = UNSET
    name: Union[Unset, str] = UNSET
    published_at: Union[Unset, str] = UNSET
    reboot_suggested: Union[Unset, bool] = UNSET
    references: Union[Unset, list[str]] = UNSET
    rpms: Union[Unset, "AdvisoryRockyRpms"] = UNSET
    severity: Union[Unset, str] = UNSET
    short_code: Union[Unset, str] = UNSET
    solution: Union[Unset, str] = UNSET
    synopsis: Union[Unset, str] = UNSET
    topic: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_products: Union[Unset, list[str]] = UNSET
        if not isinstance(self.affected_products, Unset):
            affected_products = self.affected_products

        build_references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.build_references, Unset):
            build_references = self.build_references

        cves: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cves, Unset):
            cves = []
            for cves_item_data in self.cves:
                cves_item = cves_item_data.to_dict()
                cves.append(cves_item)

        description = self.description

        fixes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fixes, Unset):
            fixes = []
            for fixes_item_data in self.fixes:
                fixes_item = fixes_item_data.to_dict()
                fixes.append(fixes_item)

        name = self.name

        published_at = self.published_at

        reboot_suggested = self.reboot_suggested

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        rpms: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rpms, Unset):
            rpms = self.rpms.to_dict()

        severity = self.severity

        short_code = self.short_code

        solution = self.solution

        synopsis = self.synopsis

        topic = self.topic

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_products is not UNSET:
            field_dict["affectedProducts"] = affected_products
        if build_references is not UNSET:
            field_dict["buildReferences"] = build_references
        if cves is not UNSET:
            field_dict["cves"] = cves
        if description is not UNSET:
            field_dict["description"] = description
        if fixes is not UNSET:
            field_dict["fixes"] = fixes
        if name is not UNSET:
            field_dict["name"] = name
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at
        if reboot_suggested is not UNSET:
            field_dict["rebootSuggested"] = reboot_suggested
        if references is not UNSET:
            field_dict["references"] = references
        if rpms is not UNSET:
            field_dict["rpms"] = rpms
        if severity is not UNSET:
            field_dict["severity"] = severity
        if short_code is not UNSET:
            field_dict["shortCode"] = short_code
        if solution is not UNSET:
            field_dict["solution"] = solution
        if synopsis is not UNSET:
            field_dict["synopsis"] = synopsis
        if topic is not UNSET:
            field_dict["topic"] = topic
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_rocky_cve import AdvisoryRockyCve
        from ..models.advisory_rocky_fix import AdvisoryRockyFix
        from ..models.advisory_rocky_rpms import AdvisoryRockyRpms

        d = dict(src_dict)
        affected_products = cast(list[str], d.pop("affectedProducts", UNSET))

        build_references = cast(list[str], d.pop("buildReferences", UNSET))

        cves = []
        _cves = d.pop("cves", UNSET)
        for cves_item_data in _cves or []:
            cves_item = AdvisoryRockyCve.from_dict(cves_item_data)

            cves.append(cves_item)

        description = d.pop("description", UNSET)

        fixes = []
        _fixes = d.pop("fixes", UNSET)
        for fixes_item_data in _fixes or []:
            fixes_item = AdvisoryRockyFix.from_dict(fixes_item_data)

            fixes.append(fixes_item)

        name = d.pop("name", UNSET)

        published_at = d.pop("publishedAt", UNSET)

        reboot_suggested = d.pop("rebootSuggested", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        _rpms = d.pop("rpms", UNSET)
        rpms: Union[Unset, AdvisoryRockyRpms]
        if isinstance(_rpms, Unset):
            rpms = UNSET
        else:
            rpms = AdvisoryRockyRpms.from_dict(_rpms)

        severity = d.pop("severity", UNSET)

        short_code = d.pop("shortCode", UNSET)

        solution = d.pop("solution", UNSET)

        synopsis = d.pop("synopsis", UNSET)

        topic = d.pop("topic", UNSET)

        type_ = d.pop("type", UNSET)

        advisory_rocky_advisory = cls(
            affected_products=affected_products,
            build_references=build_references,
            cves=cves,
            description=description,
            fixes=fixes,
            name=name,
            published_at=published_at,
            reboot_suggested=reboot_suggested,
            references=references,
            rpms=rpms,
            severity=severity,
            short_code=short_code,
            solution=solution,
            synopsis=synopsis,
            topic=topic,
            type_=type_,
        )

        advisory_rocky_advisory.additional_properties = d
        return advisory_rocky_advisory

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

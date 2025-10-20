from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_go_vuln_database_specific import AdvisoryGoVulnDatabaseSpecific
    from ..models.advisory_go_vuln_ecosystem_specific import AdvisoryGoVulnEcosystemSpecific
    from ..models.advisory_go_vuln_package import AdvisoryGoVulnPackage
    from ..models.advisory_go_vuln_ranges import AdvisoryGoVulnRanges


T = TypeVar("T", bound="AdvisoryGoVulnAffected")


@_attrs_define
class AdvisoryGoVulnAffected:
    """
    Attributes:
        database_specific (Union[Unset, AdvisoryGoVulnDatabaseSpecific]):
        ecosystem_specific (Union[Unset, AdvisoryGoVulnEcosystemSpecific]):
        package (Union[Unset, AdvisoryGoVulnPackage]):
        ranges (Union[Unset, list['AdvisoryGoVulnRanges']]):
    """

    database_specific: Union[Unset, "AdvisoryGoVulnDatabaseSpecific"] = UNSET
    ecosystem_specific: Union[Unset, "AdvisoryGoVulnEcosystemSpecific"] = UNSET
    package: Union[Unset, "AdvisoryGoVulnPackage"] = UNSET
    ranges: Union[Unset, list["AdvisoryGoVulnRanges"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        database_specific: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.database_specific, Unset):
            database_specific = self.database_specific.to_dict()

        ecosystem_specific: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ecosystem_specific, Unset):
            ecosystem_specific = self.ecosystem_specific.to_dict()

        package: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.package, Unset):
            package = self.package.to_dict()

        ranges: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ranges, Unset):
            ranges = []
            for ranges_item_data in self.ranges:
                ranges_item = ranges_item_data.to_dict()
                ranges.append(ranges_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if database_specific is not UNSET:
            field_dict["database_specific"] = database_specific
        if ecosystem_specific is not UNSET:
            field_dict["ecosystem_specific"] = ecosystem_specific
        if package is not UNSET:
            field_dict["package"] = package
        if ranges is not UNSET:
            field_dict["ranges"] = ranges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_go_vuln_database_specific import AdvisoryGoVulnDatabaseSpecific
        from ..models.advisory_go_vuln_ecosystem_specific import AdvisoryGoVulnEcosystemSpecific
        from ..models.advisory_go_vuln_package import AdvisoryGoVulnPackage
        from ..models.advisory_go_vuln_ranges import AdvisoryGoVulnRanges

        d = dict(src_dict)
        _database_specific = d.pop("database_specific", UNSET)
        database_specific: Union[Unset, AdvisoryGoVulnDatabaseSpecific]
        if isinstance(_database_specific, Unset):
            database_specific = UNSET
        else:
            database_specific = AdvisoryGoVulnDatabaseSpecific.from_dict(_database_specific)

        _ecosystem_specific = d.pop("ecosystem_specific", UNSET)
        ecosystem_specific: Union[Unset, AdvisoryGoVulnEcosystemSpecific]
        if isinstance(_ecosystem_specific, Unset):
            ecosystem_specific = UNSET
        else:
            ecosystem_specific = AdvisoryGoVulnEcosystemSpecific.from_dict(_ecosystem_specific)

        _package = d.pop("package", UNSET)
        package: Union[Unset, AdvisoryGoVulnPackage]
        if isinstance(_package, Unset):
            package = UNSET
        else:
            package = AdvisoryGoVulnPackage.from_dict(_package)

        ranges = []
        _ranges = d.pop("ranges", UNSET)
        for ranges_item_data in _ranges or []:
            ranges_item = AdvisoryGoVulnRanges.from_dict(ranges_item_data)

            ranges.append(ranges_item)

        advisory_go_vuln_affected = cls(
            database_specific=database_specific,
            ecosystem_specific=ecosystem_specific,
            package=package,
            ranges=ranges,
        )

        advisory_go_vuln_affected.additional_properties = d
        return advisory_go_vuln_affected

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

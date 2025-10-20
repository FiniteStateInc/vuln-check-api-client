from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_affected_database_specific import AdvisoryAffectedDatabaseSpecific
    from ..models.advisory_affected_ecosystem_specific import AdvisoryAffectedEcosystemSpecific
    from ..models.advisory_osv_package import AdvisoryOSVPackage
    from ..models.advisory_range import AdvisoryRange
    from ..models.advisory_severity import AdvisorySeverity


T = TypeVar("T", bound="AdvisoryAffected")


@_attrs_define
class AdvisoryAffected:
    """
    Attributes:
        database_specific (Union[Unset, AdvisoryAffectedDatabaseSpecific]): The meaning of the values within the object
            is entirely defined by the database
        ecosystem_specific (Union[Unset, AdvisoryAffectedEcosystemSpecific]): The meaning of the values within the
            object is entirely defined by the ecosystem
        package (Union[Unset, AdvisoryOSVPackage]):
        ranges (Union[Unset, list['AdvisoryRange']]):
        severity (Union[Unset, list['AdvisorySeverity']]):
        versions (Union[Unset, list[str]]):
    """

    database_specific: Union[Unset, "AdvisoryAffectedDatabaseSpecific"] = UNSET
    ecosystem_specific: Union[Unset, "AdvisoryAffectedEcosystemSpecific"] = UNSET
    package: Union[Unset, "AdvisoryOSVPackage"] = UNSET
    ranges: Union[Unset, list["AdvisoryRange"]] = UNSET
    severity: Union[Unset, list["AdvisorySeverity"]] = UNSET
    versions: Union[Unset, list[str]] = UNSET
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

        severity: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.severity, Unset):
            severity = []
            for severity_item_data in self.severity:
                severity_item = severity_item_data.to_dict()
                severity.append(severity_item)

        versions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.versions, Unset):
            versions = self.versions

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
        if severity is not UNSET:
            field_dict["severity"] = severity
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_affected_database_specific import AdvisoryAffectedDatabaseSpecific
        from ..models.advisory_affected_ecosystem_specific import AdvisoryAffectedEcosystemSpecific
        from ..models.advisory_osv_package import AdvisoryOSVPackage
        from ..models.advisory_range import AdvisoryRange
        from ..models.advisory_severity import AdvisorySeverity

        d = dict(src_dict)
        _database_specific = d.pop("database_specific", UNSET)
        database_specific: Union[Unset, AdvisoryAffectedDatabaseSpecific]
        if isinstance(_database_specific, Unset):
            database_specific = UNSET
        else:
            database_specific = AdvisoryAffectedDatabaseSpecific.from_dict(_database_specific)

        _ecosystem_specific = d.pop("ecosystem_specific", UNSET)
        ecosystem_specific: Union[Unset, AdvisoryAffectedEcosystemSpecific]
        if isinstance(_ecosystem_specific, Unset):
            ecosystem_specific = UNSET
        else:
            ecosystem_specific = AdvisoryAffectedEcosystemSpecific.from_dict(_ecosystem_specific)

        _package = d.pop("package", UNSET)
        package: Union[Unset, AdvisoryOSVPackage]
        if isinstance(_package, Unset):
            package = UNSET
        else:
            package = AdvisoryOSVPackage.from_dict(_package)

        ranges = []
        _ranges = d.pop("ranges", UNSET)
        for ranges_item_data in _ranges or []:
            ranges_item = AdvisoryRange.from_dict(ranges_item_data)

            ranges.append(ranges_item)

        severity = []
        _severity = d.pop("severity", UNSET)
        for severity_item_data in _severity or []:
            severity_item = AdvisorySeverity.from_dict(severity_item_data)

            severity.append(severity_item)

        versions = cast(list[str], d.pop("versions", UNSET))

        advisory_affected = cls(
            database_specific=database_specific,
            ecosystem_specific=ecosystem_specific,
            package=package,
            ranges=ranges,
            severity=severity,
            versions=versions,
        )

        advisory_affected.additional_properties = d
        return advisory_affected

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

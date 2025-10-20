from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_cwe_acceptance_level import AdvisoryCweAcceptanceLevel
    from ..models.advisory_v3_acceptance_level import AdvisoryV3AcceptanceLevel


T = TypeVar("T", bound="AdvisoryNVD20Source")


@_attrs_define
class AdvisoryNVD20Source:
    """
    Attributes:
        contact_email (Union[Unset, str]):
        created (Union[Unset, str]):
        cwe_acceptance_level (Union[Unset, AdvisoryCweAcceptanceLevel]):
        last_modified (Union[Unset, str]):
        name (Union[Unset, str]):
        source_identifiers (Union[Unset, list[str]]):
        v_3_acceptance_level (Union[Unset, AdvisoryV3AcceptanceLevel]):
    """

    contact_email: Union[Unset, str] = UNSET
    created: Union[Unset, str] = UNSET
    cwe_acceptance_level: Union[Unset, "AdvisoryCweAcceptanceLevel"] = UNSET
    last_modified: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    source_identifiers: Union[Unset, list[str]] = UNSET
    v_3_acceptance_level: Union[Unset, "AdvisoryV3AcceptanceLevel"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact_email = self.contact_email

        created = self.created

        cwe_acceptance_level: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cwe_acceptance_level, Unset):
            cwe_acceptance_level = self.cwe_acceptance_level.to_dict()

        last_modified = self.last_modified

        name = self.name

        source_identifiers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.source_identifiers, Unset):
            source_identifiers = self.source_identifiers

        v_3_acceptance_level: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.v_3_acceptance_level, Unset):
            v_3_acceptance_level = self.v_3_acceptance_level.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact_email is not UNSET:
            field_dict["contactEmail"] = contact_email
        if created is not UNSET:
            field_dict["created"] = created
        if cwe_acceptance_level is not UNSET:
            field_dict["cweAcceptanceLevel"] = cwe_acceptance_level
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if name is not UNSET:
            field_dict["name"] = name
        if source_identifiers is not UNSET:
            field_dict["sourceIdentifiers"] = source_identifiers
        if v_3_acceptance_level is not UNSET:
            field_dict["v3AcceptanceLevel"] = v_3_acceptance_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_cwe_acceptance_level import AdvisoryCweAcceptanceLevel
        from ..models.advisory_v3_acceptance_level import AdvisoryV3AcceptanceLevel

        d = dict(src_dict)
        contact_email = d.pop("contactEmail", UNSET)

        created = d.pop("created", UNSET)

        _cwe_acceptance_level = d.pop("cweAcceptanceLevel", UNSET)
        cwe_acceptance_level: Union[Unset, AdvisoryCweAcceptanceLevel]
        if isinstance(_cwe_acceptance_level, Unset):
            cwe_acceptance_level = UNSET
        else:
            cwe_acceptance_level = AdvisoryCweAcceptanceLevel.from_dict(_cwe_acceptance_level)

        last_modified = d.pop("lastModified", UNSET)

        name = d.pop("name", UNSET)

        source_identifiers = cast(list[str], d.pop("sourceIdentifiers", UNSET))

        _v_3_acceptance_level = d.pop("v3AcceptanceLevel", UNSET)
        v_3_acceptance_level: Union[Unset, AdvisoryV3AcceptanceLevel]
        if isinstance(_v_3_acceptance_level, Unset):
            v_3_acceptance_level = UNSET
        else:
            v_3_acceptance_level = AdvisoryV3AcceptanceLevel.from_dict(_v_3_acceptance_level)

        advisory_nvd20_source = cls(
            contact_email=contact_email,
            created=created,
            cwe_acceptance_level=cwe_acceptance_level,
            last_modified=last_modified,
            name=name,
            source_identifiers=source_identifiers,
            v_3_acceptance_level=v_3_acceptance_level,
        )

        advisory_nvd20_source.additional_properties = d
        return advisory_nvd20_source

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

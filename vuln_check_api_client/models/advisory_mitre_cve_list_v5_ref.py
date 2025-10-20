from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_m_containers import AdvisoryMContainers
    from ..models.advisory_m_cve_metadata import AdvisoryMCveMetadata


T = TypeVar("T", bound="AdvisoryMitreCVEListV5Ref")


@_attrs_define
class AdvisoryMitreCVEListV5Ref:
    """
    Attributes:
        containers (Union[Unset, AdvisoryMContainers]):
        cve_metadata (Union[Unset, AdvisoryMCveMetadata]):
        data_type (Union[Unset, str]):
        data_version (Union[Unset, str]):
    """

    containers: Union[Unset, "AdvisoryMContainers"] = UNSET
    cve_metadata: Union[Unset, "AdvisoryMCveMetadata"] = UNSET
    data_type: Union[Unset, str] = UNSET
    data_version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        containers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.containers, Unset):
            containers = self.containers.to_dict()

        cve_metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cve_metadata, Unset):
            cve_metadata = self.cve_metadata.to_dict()

        data_type = self.data_type

        data_version = self.data_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if containers is not UNSET:
            field_dict["containers"] = containers
        if cve_metadata is not UNSET:
            field_dict["cveMetadata"] = cve_metadata
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if data_version is not UNSET:
            field_dict["dataVersion"] = data_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_m_containers import AdvisoryMContainers
        from ..models.advisory_m_cve_metadata import AdvisoryMCveMetadata

        d = dict(src_dict)
        _containers = d.pop("containers", UNSET)
        containers: Union[Unset, AdvisoryMContainers]
        if isinstance(_containers, Unset):
            containers = UNSET
        else:
            containers = AdvisoryMContainers.from_dict(_containers)

        _cve_metadata = d.pop("cveMetadata", UNSET)
        cve_metadata: Union[Unset, AdvisoryMCveMetadata]
        if isinstance(_cve_metadata, Unset):
            cve_metadata = UNSET
        else:
            cve_metadata = AdvisoryMCveMetadata.from_dict(_cve_metadata)

        data_type = d.pop("dataType", UNSET)

        data_version = d.pop("dataVersion", UNSET)

        advisory_mitre_cve_list_v5_ref = cls(
            containers=containers,
            cve_metadata=cve_metadata,
            data_type=data_type,
            data_version=data_version,
        )

        advisory_mitre_cve_list_v5_ref.additional_properties = d
        return advisory_mitre_cve_list_v5_ref

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

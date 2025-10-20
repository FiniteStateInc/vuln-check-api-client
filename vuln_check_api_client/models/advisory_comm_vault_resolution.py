from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_comm_vault_resolution_details import AdvisoryCommVaultResolutionDetails


T = TypeVar("T", bound="AdvisoryCommVaultResolution")


@_attrs_define
class AdvisoryCommVaultResolution:
    """
    Attributes:
        description (Union[Unset, str]):
        resolution_details (Union[Unset, list['AdvisoryCommVaultResolutionDetails']]):
    """

    description: Union[Unset, str] = UNSET
    resolution_details: Union[Unset, list["AdvisoryCommVaultResolutionDetails"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        resolution_details: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.resolution_details, Unset):
            resolution_details = []
            for resolution_details_item_data in self.resolution_details:
                resolution_details_item = resolution_details_item_data.to_dict()
                resolution_details.append(resolution_details_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if resolution_details is not UNSET:
            field_dict["resolution_details"] = resolution_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_comm_vault_resolution_details import AdvisoryCommVaultResolutionDetails

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        resolution_details = []
        _resolution_details = d.pop("resolution_details", UNSET)
        for resolution_details_item_data in _resolution_details or []:
            resolution_details_item = AdvisoryCommVaultResolutionDetails.from_dict(resolution_details_item_data)

            resolution_details.append(resolution_details_item)

        advisory_comm_vault_resolution = cls(
            description=description,
            resolution_details=resolution_details,
        )

        advisory_comm_vault_resolution.additional_properties = d
        return advisory_comm_vault_resolution

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

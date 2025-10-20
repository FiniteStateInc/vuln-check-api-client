from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_override_configuration import AdvisoryOverrideConfiguration


T = TypeVar("T", bound="AdvisoryOverrideCVE")


@_attrs_define
class AdvisoryOverrideCVE:
    """
    Attributes:
        configurations (Union[Unset, list['AdvisoryOverrideConfiguration']]):
    """

    configurations: Union[Unset, list["AdvisoryOverrideConfiguration"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configurations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.configurations, Unset):
            configurations = []
            for configurations_item_data in self.configurations:
                configurations_item = configurations_item_data.to_dict()
                configurations.append(configurations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configurations is not UNSET:
            field_dict["configurations"] = configurations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_override_configuration import AdvisoryOverrideConfiguration

        d = dict(src_dict)
        configurations = []
        _configurations = d.pop("configurations", UNSET)
        for configurations_item_data in _configurations or []:
            configurations_item = AdvisoryOverrideConfiguration.from_dict(configurations_item_data)

            configurations.append(configurations_item)

        advisory_override_cve = cls(
            configurations=configurations,
        )

        advisory_override_cve.additional_properties = d
        return advisory_override_cve

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

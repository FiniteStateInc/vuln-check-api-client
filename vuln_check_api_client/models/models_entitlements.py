from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_entitlements_entitlements import ModelsEntitlementsEntitlements


T = TypeVar("T", bound="ModelsEntitlements")


@_attrs_define
class ModelsEntitlements:
    """
    Attributes:
        entitlements (Union[Unset, ModelsEntitlementsEntitlements]): Entitlements provides a map of roles to a list of
            entitlements
    """

    entitlements: Union[Unset, "ModelsEntitlementsEntitlements"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entitlements: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entitlements, Unset):
            entitlements = self.entitlements.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entitlements is not UNSET:
            field_dict["entitlements"] = entitlements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_entitlements_entitlements import ModelsEntitlementsEntitlements

        d = dict(src_dict)
        _entitlements = d.pop("entitlements", UNSET)
        entitlements: Union[Unset, ModelsEntitlementsEntitlements]
        if isinstance(_entitlements, Unset):
            entitlements = UNSET
        else:
            entitlements = ModelsEntitlementsEntitlements.from_dict(_entitlements)

        models_entitlements = cls(
            entitlements=entitlements,
        )

        models_entitlements.additional_properties = d
        return models_entitlements

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

from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCOSUpdate")


@_attrs_define
class AdvisoryCOSUpdate:
    """
    Attributes:
        changed (Union[Unset, list[str]]):
        featured (Union[Unset, list[str]]):
        fixed (Union[Unset, list[str]]):
        id (Union[Unset, str]):
        reference (Union[Unset, str]):
        security (Union[Unset, list[str]]):
        updated (Union[Unset, str]):
    """

    changed: Union[Unset, list[str]] = UNSET
    featured: Union[Unset, list[str]] = UNSET
    fixed: Union[Unset, list[str]] = UNSET
    id: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    security: Union[Unset, list[str]] = UNSET
    updated: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changed: Union[Unset, list[str]] = UNSET
        if not isinstance(self.changed, Unset):
            changed = self.changed

        featured: Union[Unset, list[str]] = UNSET
        if not isinstance(self.featured, Unset):
            featured = self.featured

        fixed: Union[Unset, list[str]] = UNSET
        if not isinstance(self.fixed, Unset):
            fixed = self.fixed

        id = self.id

        reference = self.reference

        security: Union[Unset, list[str]] = UNSET
        if not isinstance(self.security, Unset):
            security = self.security

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if changed is not UNSET:
            field_dict["changed"] = changed
        if featured is not UNSET:
            field_dict["featured"] = featured
        if fixed is not UNSET:
            field_dict["fixed"] = fixed
        if id is not UNSET:
            field_dict["id"] = id
        if reference is not UNSET:
            field_dict["reference"] = reference
        if security is not UNSET:
            field_dict["security"] = security
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        changed = cast(list[str], d.pop("changed", UNSET))

        featured = cast(list[str], d.pop("featured", UNSET))

        fixed = cast(list[str], d.pop("fixed", UNSET))

        id = d.pop("id", UNSET)

        reference = d.pop("reference", UNSET)

        security = cast(list[str], d.pop("security", UNSET))

        updated = d.pop("updated", UNSET)

        advisory_cos_update = cls(
            changed=changed,
            featured=featured,
            fixed=fixed,
            id=id,
            reference=reference,
            security=security,
            updated=updated,
        )

        advisory_cos_update.additional_properties = d
        return advisory_cos_update

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

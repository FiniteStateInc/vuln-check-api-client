from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryPublisher")


@_attrs_define
class AdvisoryPublisher:
    """
    Attributes:
        category (Union[Unset, str]):
        contact_details (Union[Unset, str]):
        issuing_authority (Union[Unset, str]):
        name (Union[Unset, str]):
        namespace (Union[Unset, str]):
    """

    category: Union[Unset, str] = UNSET
    contact_details: Union[Unset, str] = UNSET
    issuing_authority: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    namespace: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        contact_details = self.contact_details

        issuing_authority = self.issuing_authority

        name = self.name

        namespace = self.namespace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if contact_details is not UNSET:
            field_dict["contact_details"] = contact_details
        if issuing_authority is not UNSET:
            field_dict["issuing_authority"] = issuing_authority
        if name is not UNSET:
            field_dict["name"] = name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category", UNSET)

        contact_details = d.pop("contact_details", UNSET)

        issuing_authority = d.pop("issuing_authority", UNSET)

        name = d.pop("name", UNSET)

        namespace = d.pop("namespace", UNSET)

        advisory_publisher = cls(
            category=category,
            contact_details=contact_details,
            issuing_authority=issuing_authority,
            name=name,
            namespace=namespace,
        )

        advisory_publisher.additional_properties = d
        return advisory_publisher

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

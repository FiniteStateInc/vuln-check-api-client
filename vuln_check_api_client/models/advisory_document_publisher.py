from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryDocumentPublisher")


@_attrs_define
class AdvisoryDocumentPublisher:
    """
    Attributes:
        contact_details (Union[Unset, str]):
        issuing_authority (Union[Unset, str]):
        type_ (Union[Unset, int]): the json for this is missing/broke
    """

    contact_details: Union[Unset, str] = UNSET
    issuing_authority: Union[Unset, str] = UNSET
    type_: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact_details = self.contact_details

        issuing_authority = self.issuing_authority

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact_details is not UNSET:
            field_dict["contact_details"] = contact_details
        if issuing_authority is not UNSET:
            field_dict["issuing_authority"] = issuing_authority
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contact_details = d.pop("contact_details", UNSET)

        issuing_authority = d.pop("issuing_authority", UNSET)

        type_ = d.pop("type", UNSET)

        advisory_document_publisher = cls(
            contact_details=contact_details,
            issuing_authority=issuing_authority,
            type_=type_,
        )

        advisory_document_publisher.additional_properties = d
        return advisory_document_publisher

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

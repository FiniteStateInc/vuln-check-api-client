from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_zdi_response_vendor import AdvisoryZDIResponseVendor


T = TypeVar("T", bound="AdvisoryZDIResponse")


@_attrs_define
class AdvisoryZDIResponse:
    """
    Attributes:
        text (Union[Unset, str]):
        uri (Union[Unset, str]):
        vendor (Union[Unset, AdvisoryZDIResponseVendor]):
    """

    text: Union[Unset, str] = UNSET
    uri: Union[Unset, str] = UNSET
    vendor: Union[Unset, "AdvisoryZDIResponseVendor"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        uri = self.uri

        vendor: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vendor, Unset):
            vendor = self.vendor.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if uri is not UNSET:
            field_dict["uri"] = uri
        if vendor is not UNSET:
            field_dict["vendor"] = vendor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_zdi_response_vendor import AdvisoryZDIResponseVendor

        d = dict(src_dict)
        text = d.pop("text", UNSET)

        uri = d.pop("uri", UNSET)

        _vendor = d.pop("vendor", UNSET)
        vendor: Union[Unset, AdvisoryZDIResponseVendor]
        if isinstance(_vendor, Unset):
            vendor = UNSET
        else:
            vendor = AdvisoryZDIResponseVendor.from_dict(_vendor)

        advisory_zdi_response = cls(
            text=text,
            uri=uri,
            vendor=vendor,
        )

        advisory_zdi_response.additional_properties = d
        return advisory_zdi_response

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

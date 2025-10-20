from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.purl_package_urljson import PurlPackageURLJSON


T = TypeVar("T", bound="V3ControllersPurlResponseMetadata")


@_attrs_define
class V3ControllersPurlResponseMetadata:
    """
    Attributes:
        purl_struct (Union[Unset, PurlPackageURLJSON]):
        timestamp (Union[Unset, str]): time of the transaction
        total_documents (Union[Unset, int]): number of results found
    """

    purl_struct: Union[Unset, "PurlPackageURLJSON"] = UNSET
    timestamp: Union[Unset, str] = UNSET
    total_documents: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        purl_struct: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.purl_struct, Unset):
            purl_struct = self.purl_struct.to_dict()

        timestamp = self.timestamp

        total_documents = self.total_documents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if purl_struct is not UNSET:
            field_dict["purl_struct"] = purl_struct
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if total_documents is not UNSET:
            field_dict["total_documents"] = total_documents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.purl_package_urljson import PurlPackageURLJSON

        d = dict(src_dict)
        _purl_struct = d.pop("purl_struct", UNSET)
        purl_struct: Union[Unset, PurlPackageURLJSON]
        if isinstance(_purl_struct, Unset):
            purl_struct = UNSET
        else:
            purl_struct = PurlPackageURLJSON.from_dict(_purl_struct)

        timestamp = d.pop("timestamp", UNSET)

        total_documents = d.pop("total_documents", UNSET)

        v3_controllers_purl_response_metadata = cls(
            purl_struct=purl_struct,
            timestamp=timestamp,
            total_documents=total_documents,
        )

        v3_controllers_purl_response_metadata.additional_properties = d
        return v3_controllers_purl_response_metadata

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

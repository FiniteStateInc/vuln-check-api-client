from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_cpe import ApiCPE


T = TypeVar("T", bound="V3ControllersResponseMetadata")


@_attrs_define
class V3ControllersResponseMetadata:
    """
    Attributes:
        cpe (Union[Unset, str]):
        cpe_struct (Union[Unset, ApiCPE]):
        timestamp (Union[Unset, str]):
        total_documents (Union[Unset, int]):
    """

    cpe: Union[Unset, str] = UNSET
    cpe_struct: Union[Unset, "ApiCPE"] = UNSET
    timestamp: Union[Unset, str] = UNSET
    total_documents: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpe = self.cpe

        cpe_struct: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cpe_struct, Unset):
            cpe_struct = self.cpe_struct.to_dict()

        timestamp = self.timestamp

        total_documents = self.total_documents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpe is not UNSET:
            field_dict["cpe"] = cpe
        if cpe_struct is not UNSET:
            field_dict["cpe_struct"] = cpe_struct
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if total_documents is not UNSET:
            field_dict["total_documents"] = total_documents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_cpe import ApiCPE

        d = dict(src_dict)
        cpe = d.pop("cpe", UNSET)

        _cpe_struct = d.pop("cpe_struct", UNSET)
        cpe_struct: Union[Unset, ApiCPE]
        if isinstance(_cpe_struct, Unset):
            cpe_struct = UNSET
        else:
            cpe_struct = ApiCPE.from_dict(_cpe_struct)

        timestamp = d.pop("timestamp", UNSET)

        total_documents = d.pop("total_documents", UNSET)

        v3_controllers_response_metadata = cls(
            cpe=cpe,
            cpe_struct=cpe_struct,
            timestamp=timestamp,
            total_documents=total_documents,
        )

        v3_controllers_response_metadata.additional_properties = d
        return v3_controllers_response_metadata

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

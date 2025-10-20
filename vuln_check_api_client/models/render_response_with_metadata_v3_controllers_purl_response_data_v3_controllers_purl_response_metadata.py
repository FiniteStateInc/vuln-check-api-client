from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.v3_controllers_purl_response_data import V3ControllersPurlResponseData
    from ..models.v3_controllers_purl_response_metadata import V3ControllersPurlResponseMetadata


T = TypeVar("T", bound="RenderResponseWithMetadataV3ControllersPurlResponseDataV3ControllersPurlResponseMetadata")


@_attrs_define
class RenderResponseWithMetadataV3ControllersPurlResponseDataV3ControllersPurlResponseMetadata:
    """
    Attributes:
        field_benchmark (Union[Unset, float]):
        field_meta (Union[Unset, V3ControllersPurlResponseMetadata]):
        data (Union[Unset, V3ControllersPurlResponseData]):
    """

    field_benchmark: Union[Unset, float] = UNSET
    field_meta: Union[Unset, "V3ControllersPurlResponseMetadata"] = UNSET
    data: Union[Unset, "V3ControllersPurlResponseData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_benchmark = self.field_benchmark

        field_meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_meta, Unset):
            field_meta = self.field_meta.to_dict()

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_benchmark is not UNSET:
            field_dict["_benchmark"] = field_benchmark
        if field_meta is not UNSET:
            field_dict["_meta"] = field_meta
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v3_controllers_purl_response_data import V3ControllersPurlResponseData
        from ..models.v3_controllers_purl_response_metadata import V3ControllersPurlResponseMetadata

        d = dict(src_dict)
        field_benchmark = d.pop("_benchmark", UNSET)

        _field_meta = d.pop("_meta", UNSET)
        field_meta: Union[Unset, V3ControllersPurlResponseMetadata]
        if isinstance(_field_meta, Unset):
            field_meta = UNSET
        else:
            field_meta = V3ControllersPurlResponseMetadata.from_dict(_field_meta)

        _data = d.pop("data", UNSET)
        data: Union[Unset, V3ControllersPurlResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = V3ControllersPurlResponseData.from_dict(_data)

        render_response_with_metadata_v3_controllers_purl_response_data_v3_controllers_purl_response_metadata = cls(
            field_benchmark=field_benchmark,
            field_meta=field_meta,
            data=data,
        )

        render_response_with_metadata_v3_controllers_purl_response_data_v3_controllers_purl_response_metadata.additional_properties = d
        return render_response_with_metadata_v3_controllers_purl_response_data_v3_controllers_purl_response_metadata

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

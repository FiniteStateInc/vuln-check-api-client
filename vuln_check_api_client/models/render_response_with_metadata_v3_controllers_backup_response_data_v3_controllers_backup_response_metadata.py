from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.params_index_backup import ParamsIndexBackup
    from ..models.v3_controllers_backup_response_metadata import V3ControllersBackupResponseMetadata


T = TypeVar("T", bound="RenderResponseWithMetadataV3ControllersBackupResponseDataV3ControllersBackupResponseMetadata")


@_attrs_define
class RenderResponseWithMetadataV3ControllersBackupResponseDataV3ControllersBackupResponseMetadata:
    """
    Attributes:
        field_benchmark (Union[Unset, float]):
        field_meta (Union[Unset, V3ControllersBackupResponseMetadata]):
        data (Union[Unset, list['ParamsIndexBackup']]):
    """

    field_benchmark: Union[Unset, float] = UNSET
    field_meta: Union[Unset, "V3ControllersBackupResponseMetadata"] = UNSET
    data: Union[Unset, list["ParamsIndexBackup"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_benchmark = self.field_benchmark

        field_meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_meta, Unset):
            field_meta = self.field_meta.to_dict()

        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

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
        from ..models.params_index_backup import ParamsIndexBackup
        from ..models.v3_controllers_backup_response_metadata import V3ControllersBackupResponseMetadata

        d = dict(src_dict)
        field_benchmark = d.pop("_benchmark", UNSET)

        _field_meta = d.pop("_meta", UNSET)
        field_meta: Union[Unset, V3ControllersBackupResponseMetadata]
        if isinstance(_field_meta, Unset):
            field_meta = UNSET
        else:
            field_meta = V3ControllersBackupResponseMetadata.from_dict(_field_meta)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = ParamsIndexBackup.from_dict(data_item_data)

            data.append(data_item)

        render_response_with_metadata_v3_controllers_backup_response_data_v3_controllers_backup_response_metadata = cls(
            field_benchmark=field_benchmark,
            field_meta=field_meta,
            data=data,
        )

        render_response_with_metadata_v3_controllers_backup_response_data_v3_controllers_backup_response_metadata.additional_properties = d
        return render_response_with_metadata_v3_controllers_backup_response_data_v3_controllers_backup_response_metadata

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

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_oss_package_download_info import ApiOSSPackageDownloadInfo


T = TypeVar("T", bound="ApiOSSPackageArtifacts")


@_attrs_define
class ApiOSSPackageArtifacts:
    """
    Attributes:
        binary (Union[Unset, list['ApiOSSPackageDownloadInfo']]):
        source (Union[Unset, list['ApiOSSPackageDownloadInfo']]):
    """

    binary: Union[Unset, list["ApiOSSPackageDownloadInfo"]] = UNSET
    source: Union[Unset, list["ApiOSSPackageDownloadInfo"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        binary: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.binary, Unset):
            binary = []
            for binary_item_data in self.binary:
                binary_item = binary_item_data.to_dict()
                binary.append(binary_item)

        source: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.source, Unset):
            source = []
            for source_item_data in self.source:
                source_item = source_item_data.to_dict()
                source.append(source_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if binary is not UNSET:
            field_dict["binary"] = binary
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_oss_package_download_info import ApiOSSPackageDownloadInfo

        d = dict(src_dict)
        binary = []
        _binary = d.pop("binary", UNSET)
        for binary_item_data in _binary or []:
            binary_item = ApiOSSPackageDownloadInfo.from_dict(binary_item_data)

            binary.append(binary_item)

        source = []
        _source = d.pop("source", UNSET)
        for source_item_data in _source or []:
            source_item = ApiOSSPackageDownloadInfo.from_dict(source_item_data)

            source.append(source_item)

        api_oss_package_artifacts = cls(
            binary=binary,
            source=source,
        )

        api_oss_package_artifacts.additional_properties = d
        return api_oss_package_artifacts

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

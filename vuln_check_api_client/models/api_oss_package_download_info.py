from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_oss_package_hash_info import ApiOSSPackageHashInfo


T = TypeVar("T", bound="ApiOSSPackageDownloadInfo")


@_attrs_define
class ApiOSSPackageDownloadInfo:
    """
    Attributes:
        hashes (Union[Unset, list['ApiOSSPackageHashInfo']]):
        reference (Union[Unset, str]):
        type_ (Union[Unset, str]): See OSSPackageDownloadInfoType* consts
        url (Union[Unset, str]):
    """

    hashes: Union[Unset, list["ApiOSSPackageHashInfo"]] = UNSET
    reference: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hashes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.hashes, Unset):
            hashes = []
            for hashes_item_data in self.hashes:
                hashes_item = hashes_item_data.to_dict()
                hashes.append(hashes_item)

        reference = self.reference

        type_ = self.type_

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hashes is not UNSET:
            field_dict["hashes"] = hashes
        if reference is not UNSET:
            field_dict["reference"] = reference
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_oss_package_hash_info import ApiOSSPackageHashInfo

        d = dict(src_dict)
        hashes = []
        _hashes = d.pop("hashes", UNSET)
        for hashes_item_data in _hashes or []:
            hashes_item = ApiOSSPackageHashInfo.from_dict(hashes_item_data)

            hashes.append(hashes_item)

        reference = d.pop("reference", UNSET)

        type_ = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        api_oss_package_download_info = cls(
            hashes=hashes,
            reference=reference,
            type_=type_,
            url=url,
        )

        api_oss_package_download_info.additional_properties = d
        return api_oss_package_download_info

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

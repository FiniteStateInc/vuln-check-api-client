from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_cpe_name import ApiCPEName


T = TypeVar("T", bound="ApiCPEMatch")


@_attrs_define
class ApiCPEMatch:
    """
    Attributes:
        cpe_22_uri (Union[Unset, str]):
        cpe_23_uri (Union[Unset, str]):
        cpe_name (Union[Unset, list['ApiCPEName']]):
        version_end_excluding (Union[Unset, str]):
        version_end_including (Union[Unset, str]):
        version_start_excluding (Union[Unset, str]):
        version_start_including (Union[Unset, str]):
        vulnerable (Union[Unset, bool]):
    """

    cpe_22_uri: Union[Unset, str] = UNSET
    cpe_23_uri: Union[Unset, str] = UNSET
    cpe_name: Union[Unset, list["ApiCPEName"]] = UNSET
    version_end_excluding: Union[Unset, str] = UNSET
    version_end_including: Union[Unset, str] = UNSET
    version_start_excluding: Union[Unset, str] = UNSET
    version_start_including: Union[Unset, str] = UNSET
    vulnerable: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpe_22_uri = self.cpe_22_uri

        cpe_23_uri = self.cpe_23_uri

        cpe_name: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cpe_name, Unset):
            cpe_name = []
            for cpe_name_item_data in self.cpe_name:
                cpe_name_item = cpe_name_item_data.to_dict()
                cpe_name.append(cpe_name_item)

        version_end_excluding = self.version_end_excluding

        version_end_including = self.version_end_including

        version_start_excluding = self.version_start_excluding

        version_start_including = self.version_start_including

        vulnerable = self.vulnerable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpe_22_uri is not UNSET:
            field_dict["cpe22Uri"] = cpe_22_uri
        if cpe_23_uri is not UNSET:
            field_dict["cpe23Uri"] = cpe_23_uri
        if cpe_name is not UNSET:
            field_dict["cpe_name"] = cpe_name
        if version_end_excluding is not UNSET:
            field_dict["versionEndExcluding"] = version_end_excluding
        if version_end_including is not UNSET:
            field_dict["versionEndIncluding"] = version_end_including
        if version_start_excluding is not UNSET:
            field_dict["versionStartExcluding"] = version_start_excluding
        if version_start_including is not UNSET:
            field_dict["versionStartIncluding"] = version_start_including
        if vulnerable is not UNSET:
            field_dict["vulnerable"] = vulnerable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_cpe_name import ApiCPEName

        d = dict(src_dict)
        cpe_22_uri = d.pop("cpe22Uri", UNSET)

        cpe_23_uri = d.pop("cpe23Uri", UNSET)

        cpe_name = []
        _cpe_name = d.pop("cpe_name", UNSET)
        for cpe_name_item_data in _cpe_name or []:
            cpe_name_item = ApiCPEName.from_dict(cpe_name_item_data)

            cpe_name.append(cpe_name_item)

        version_end_excluding = d.pop("versionEndExcluding", UNSET)

        version_end_including = d.pop("versionEndIncluding", UNSET)

        version_start_excluding = d.pop("versionStartExcluding", UNSET)

        version_start_including = d.pop("versionStartIncluding", UNSET)

        vulnerable = d.pop("vulnerable", UNSET)

        api_cpe_match = cls(
            cpe_22_uri=cpe_22_uri,
            cpe_23_uri=cpe_23_uri,
            cpe_name=cpe_name,
            version_end_excluding=version_end_excluding,
            version_end_including=version_end_including,
            version_start_excluding=version_start_excluding,
            version_start_including=version_start_including,
            vulnerable=vulnerable,
        )

        api_cpe_match.additional_properties = d
        return api_cpe_match

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

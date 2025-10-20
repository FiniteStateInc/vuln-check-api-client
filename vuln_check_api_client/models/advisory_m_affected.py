from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_m_version import AdvisoryMVersion


T = TypeVar("T", bound="AdvisoryMAffected")


@_attrs_define
class AdvisoryMAffected:
    """
    Attributes:
        collection_url (Union[Unset, str]):
        cpes (Union[Unset, list[str]]):
        default_status (Union[Unset, str]):
        package_name (Union[Unset, str]):
        platforms (Union[Unset, list[str]]):
        product (Union[Unset, str]):
        repos (Union[Unset, str]):
        vendor (Union[Unset, str]):
        versions (Union[Unset, list['AdvisoryMVersion']]):
    """

    collection_url: Union[Unset, str] = UNSET
    cpes: Union[Unset, list[str]] = UNSET
    default_status: Union[Unset, str] = UNSET
    package_name: Union[Unset, str] = UNSET
    platforms: Union[Unset, list[str]] = UNSET
    product: Union[Unset, str] = UNSET
    repos: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    versions: Union[Unset, list["AdvisoryMVersion"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_url = self.collection_url

        cpes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cpes, Unset):
            cpes = self.cpes

        default_status = self.default_status

        package_name = self.package_name

        platforms: Union[Unset, list[str]] = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = self.platforms

        product = self.product

        repos = self.repos

        vendor = self.vendor

        versions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()
                versions.append(versions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collection_url is not UNSET:
            field_dict["collectionURL"] = collection_url
        if cpes is not UNSET:
            field_dict["cpes"] = cpes
        if default_status is not UNSET:
            field_dict["defaultStatus"] = default_status
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if platforms is not UNSET:
            field_dict["platforms"] = platforms
        if product is not UNSET:
            field_dict["product"] = product
        if repos is not UNSET:
            field_dict["repos"] = repos
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_m_version import AdvisoryMVersion

        d = dict(src_dict)
        collection_url = d.pop("collectionURL", UNSET)

        cpes = cast(list[str], d.pop("cpes", UNSET))

        default_status = d.pop("defaultStatus", UNSET)

        package_name = d.pop("packageName", UNSET)

        platforms = cast(list[str], d.pop("platforms", UNSET))

        product = d.pop("product", UNSET)

        repos = d.pop("repos", UNSET)

        vendor = d.pop("vendor", UNSET)

        versions = []
        _versions = d.pop("versions", UNSET)
        for versions_item_data in _versions or []:
            versions_item = AdvisoryMVersion.from_dict(versions_item_data)

            versions.append(versions_item)

        advisory_m_affected = cls(
            collection_url=collection_url,
            cpes=cpes,
            default_status=default_status,
            package_name=package_name,
            platforms=platforms,
            product=product,
            repos=repos,
            vendor=vendor,
            versions=versions,
        )

        advisory_m_affected.additional_properties = d
        return advisory_m_affected

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

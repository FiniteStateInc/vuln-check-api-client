from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_ubuntu_package_release_status import AdvisoryUbuntuPackageReleaseStatus


T = TypeVar("T", bound="AdvisoryAffectedUbuntuPackage")


@_attrs_define
class AdvisoryAffectedUbuntuPackage:
    """
    Attributes:
        break_commit_url (Union[Unset, list[str]]):
        fix_commit_url (Union[Unset, list[str]]):
        package_name (Union[Unset, str]):
        package_release_status (Union[Unset, list['AdvisoryUbuntuPackageReleaseStatus']]):
        upstream_fix_url (Union[Unset, list[str]]):
    """

    break_commit_url: Union[Unset, list[str]] = UNSET
    fix_commit_url: Union[Unset, list[str]] = UNSET
    package_name: Union[Unset, str] = UNSET
    package_release_status: Union[Unset, list["AdvisoryUbuntuPackageReleaseStatus"]] = UNSET
    upstream_fix_url: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        break_commit_url: Union[Unset, list[str]] = UNSET
        if not isinstance(self.break_commit_url, Unset):
            break_commit_url = self.break_commit_url

        fix_commit_url: Union[Unset, list[str]] = UNSET
        if not isinstance(self.fix_commit_url, Unset):
            fix_commit_url = self.fix_commit_url

        package_name = self.package_name

        package_release_status: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.package_release_status, Unset):
            package_release_status = []
            for package_release_status_item_data in self.package_release_status:
                package_release_status_item = package_release_status_item_data.to_dict()
                package_release_status.append(package_release_status_item)

        upstream_fix_url: Union[Unset, list[str]] = UNSET
        if not isinstance(self.upstream_fix_url, Unset):
            upstream_fix_url = self.upstream_fix_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if break_commit_url is not UNSET:
            field_dict["break_commit_url"] = break_commit_url
        if fix_commit_url is not UNSET:
            field_dict["fix_commit_url"] = fix_commit_url
        if package_name is not UNSET:
            field_dict["package_name"] = package_name
        if package_release_status is not UNSET:
            field_dict["package_release_status"] = package_release_status
        if upstream_fix_url is not UNSET:
            field_dict["upstream_fix_url"] = upstream_fix_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_ubuntu_package_release_status import AdvisoryUbuntuPackageReleaseStatus

        d = dict(src_dict)
        break_commit_url = cast(list[str], d.pop("break_commit_url", UNSET))

        fix_commit_url = cast(list[str], d.pop("fix_commit_url", UNSET))

        package_name = d.pop("package_name", UNSET)

        package_release_status = []
        _package_release_status = d.pop("package_release_status", UNSET)
        for package_release_status_item_data in _package_release_status or []:
            package_release_status_item = AdvisoryUbuntuPackageReleaseStatus.from_dict(package_release_status_item_data)

            package_release_status.append(package_release_status_item)

        upstream_fix_url = cast(list[str], d.pop("upstream_fix_url", UNSET))

        advisory_affected_ubuntu_package = cls(
            break_commit_url=break_commit_url,
            fix_commit_url=fix_commit_url,
            package_name=package_name,
            package_release_status=package_release_status,
            upstream_fix_url=upstream_fix_url,
        )

        advisory_affected_ubuntu_package.additional_properties = d
        return advisory_affected_ubuntu_package

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

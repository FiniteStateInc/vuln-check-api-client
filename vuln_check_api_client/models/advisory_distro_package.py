from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_distro_version import AdvisoryDistroVersion
    from ..models.advisory_sec_fix import AdvisorySecFix


T = TypeVar("T", bound="AdvisoryDistroPackage")


@_attrs_define
class AdvisoryDistroPackage:
    """
    Attributes:
        binary (Union[Unset, bool]):
        cve (Union[Unset, list[str]]):
        license_ (Union[Unset, list[str]]):
        name (Union[Unset, str]):
        sec_fixes (Union[Unset, list['AdvisorySecFix']]):
        versions (Union[Unset, list['AdvisoryDistroVersion']]):
    """

    binary: Union[Unset, bool] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    license_: Union[Unset, list[str]] = UNSET
    name: Union[Unset, str] = UNSET
    sec_fixes: Union[Unset, list["AdvisorySecFix"]] = UNSET
    versions: Union[Unset, list["AdvisoryDistroVersion"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        binary = self.binary

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        license_: Union[Unset, list[str]] = UNSET
        if not isinstance(self.license_, Unset):
            license_ = self.license_

        name = self.name

        sec_fixes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sec_fixes, Unset):
            sec_fixes = []
            for sec_fixes_item_data in self.sec_fixes:
                sec_fixes_item = sec_fixes_item_data.to_dict()
                sec_fixes.append(sec_fixes_item)

        versions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()
                versions.append(versions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if binary is not UNSET:
            field_dict["binary"] = binary
        if cve is not UNSET:
            field_dict["cve"] = cve
        if license_ is not UNSET:
            field_dict["license"] = license_
        if name is not UNSET:
            field_dict["name"] = name
        if sec_fixes is not UNSET:
            field_dict["secFixes"] = sec_fixes
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_distro_version import AdvisoryDistroVersion
        from ..models.advisory_sec_fix import AdvisorySecFix

        d = dict(src_dict)
        binary = d.pop("binary", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        license_ = cast(list[str], d.pop("license", UNSET))

        name = d.pop("name", UNSET)

        sec_fixes = []
        _sec_fixes = d.pop("secFixes", UNSET)
        for sec_fixes_item_data in _sec_fixes or []:
            sec_fixes_item = AdvisorySecFix.from_dict(sec_fixes_item_data)

            sec_fixes.append(sec_fixes_item)

        versions = []
        _versions = d.pop("versions", UNSET)
        for versions_item_data in _versions or []:
            versions_item = AdvisoryDistroVersion.from_dict(versions_item_data)

            versions.append(versions_item)

        advisory_distro_package = cls(
            binary=binary,
            cve=cve,
            license_=license_,
            name=name,
            sec_fixes=sec_fixes,
            versions=versions,
        )

        advisory_distro_package.additional_properties = d
        return advisory_distro_package

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

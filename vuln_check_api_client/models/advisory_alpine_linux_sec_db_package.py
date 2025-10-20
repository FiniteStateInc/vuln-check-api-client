from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_alpine_linux_security_fix import AdvisoryAlpineLinuxSecurityFix


T = TypeVar("T", bound="AdvisoryAlpineLinuxSecDBPackage")


@_attrs_define
class AdvisoryAlpineLinuxSecDBPackage:
    """
    Attributes:
        package_name (Union[Unset, str]):
        secfixes (Union[Unset, list['AdvisoryAlpineLinuxSecurityFix']]):
    """

    package_name: Union[Unset, str] = UNSET
    secfixes: Union[Unset, list["AdvisoryAlpineLinuxSecurityFix"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_name = self.package_name

        secfixes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.secfixes, Unset):
            secfixes = []
            for secfixes_item_data in self.secfixes:
                secfixes_item = secfixes_item_data.to_dict()
                secfixes.append(secfixes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package_name is not UNSET:
            field_dict["package_name"] = package_name
        if secfixes is not UNSET:
            field_dict["secfixes"] = secfixes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_alpine_linux_security_fix import AdvisoryAlpineLinuxSecurityFix

        d = dict(src_dict)
        package_name = d.pop("package_name", UNSET)

        secfixes = []
        _secfixes = d.pop("secfixes", UNSET)
        for secfixes_item_data in _secfixes or []:
            secfixes_item = AdvisoryAlpineLinuxSecurityFix.from_dict(secfixes_item_data)

            secfixes.append(secfixes_item)

        advisory_alpine_linux_sec_db_package = cls(
            package_name=package_name,
            secfixes=secfixes,
        )

        advisory_alpine_linux_sec_db_package.additional_properties = d
        return advisory_alpine_linux_sec_db_package

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

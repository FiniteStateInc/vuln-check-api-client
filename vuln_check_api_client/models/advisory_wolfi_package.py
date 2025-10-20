from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_wolfi_sec_fix import AdvisoryWolfiSecFix


T = TypeVar("T", bound="AdvisoryWolfiPackage")


@_attrs_define
class AdvisoryWolfiPackage:
    """
    Attributes:
        name (Union[Unset, str]):
        secfixes (Union[Unset, list['AdvisoryWolfiSecFix']]):
    """

    name: Union[Unset, str] = UNSET
    secfixes: Union[Unset, list["AdvisoryWolfiSecFix"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        secfixes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.secfixes, Unset):
            secfixes = []
            for secfixes_item_data in self.secfixes:
                secfixes_item = secfixes_item_data.to_dict()
                secfixes.append(secfixes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if secfixes is not UNSET:
            field_dict["secfixes"] = secfixes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_wolfi_sec_fix import AdvisoryWolfiSecFix

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        secfixes = []
        _secfixes = d.pop("secfixes", UNSET)
        for secfixes_item_data in _secfixes or []:
            secfixes_item = AdvisoryWolfiSecFix.from_dict(secfixes_item_data)

            secfixes.append(secfixes_item)

        advisory_wolfi_package = cls(
            name=name,
            secfixes=secfixes,
        )

        advisory_wolfi_package.additional_properties = d
        return advisory_wolfi_package

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

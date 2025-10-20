from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_nvd20_weakness_desc_extended import ApiNVD20WeaknessDescExtended


T = TypeVar("T", bound="ApiNVD20WeaknessExtended")


@_attrs_define
class ApiNVD20WeaknessExtended:
    """
    Attributes:
        description (Union[Unset, list['ApiNVD20WeaknessDescExtended']]):
        source (Union[Unset, str]):
        type_ (Union[Unset, str]):
    """

    description: Union[Unset, list["ApiNVD20WeaknessDescExtended"]] = UNSET
    source: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.description, Unset):
            description = []
            for description_item_data in self.description:
                description_item = description_item_data.to_dict()
                description.append(description_item)

        source = self.source

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if source is not UNSET:
            field_dict["source"] = source
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_nvd20_weakness_desc_extended import ApiNVD20WeaknessDescExtended

        d = dict(src_dict)
        description = []
        _description = d.pop("description", UNSET)
        for description_item_data in _description or []:
            description_item = ApiNVD20WeaknessDescExtended.from_dict(description_item_data)

            description.append(description_item)

        source = d.pop("source", UNSET)

        type_ = d.pop("type", UNSET)

        api_nvd20_weakness_extended = cls(
            description=description,
            source=source,
            type_=type_,
        )

        api_nvd20_weakness_extended.additional_properties = d
        return api_nvd20_weakness_extended

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

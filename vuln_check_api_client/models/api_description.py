from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_description_data import ApiDescriptionData


T = TypeVar("T", bound="ApiDescription")


@_attrs_define
class ApiDescription:
    """
    Attributes:
        description_data (Union[Unset, list['ApiDescriptionData']]):
    """

    description_data: Union[Unset, list["ApiDescriptionData"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description_data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.description_data, Unset):
            description_data = []
            for description_data_item_data in self.description_data:
                description_data_item = description_data_item_data.to_dict()
                description_data.append(description_data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description_data is not UNSET:
            field_dict["description_data"] = description_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_description_data import ApiDescriptionData

        d = dict(src_dict)
        description_data = []
        _description_data = d.pop("description_data", UNSET)
        for description_data_item_data in _description_data or []:
            description_data_item = ApiDescriptionData.from_dict(description_data_item_data)

            description_data.append(description_data_item)

        api_description = cls(
            description_data=description_data,
        )

        api_description.additional_properties = d
        return api_description

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

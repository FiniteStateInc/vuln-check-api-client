from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_problem_type_description import ApiProblemTypeDescription


T = TypeVar("T", bound="ApiProblemTypeData")


@_attrs_define
class ApiProblemTypeData:
    """
    Attributes:
        description (Union[Unset, list['ApiProblemTypeDescription']]):
    """

    description: Union[Unset, list["ApiProblemTypeDescription"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.description, Unset):
            description = []
            for description_item_data in self.description:
                description_item = description_item_data.to_dict()
                description.append(description_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_problem_type_description import ApiProblemTypeDescription

        d = dict(src_dict)
        description = []
        _description = d.pop("description", UNSET)
        for description_item_data in _description or []:
            description_item = ApiProblemTypeDescription.from_dict(description_item_data)

            description.append(description_item)

        api_problem_type_data = cls(
            description=description,
        )

        api_problem_type_data.additional_properties = d
        return api_problem_type_data

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

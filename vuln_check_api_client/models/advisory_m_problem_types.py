from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_ptm_descriptions import AdvisoryPTMDescriptions


T = TypeVar("T", bound="AdvisoryMProblemTypes")


@_attrs_define
class AdvisoryMProblemTypes:
    """
    Attributes:
        descriptions (Union[Unset, list['AdvisoryPTMDescriptions']]):
    """

    descriptions: Union[Unset, list["AdvisoryPTMDescriptions"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        descriptions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.descriptions, Unset):
            descriptions = []
            for descriptions_item_data in self.descriptions:
                descriptions_item = descriptions_item_data.to_dict()
                descriptions.append(descriptions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_ptm_descriptions import AdvisoryPTMDescriptions

        d = dict(src_dict)
        descriptions = []
        _descriptions = d.pop("descriptions", UNSET)
        for descriptions_item_data in _descriptions or []:
            descriptions_item = AdvisoryPTMDescriptions.from_dict(descriptions_item_data)

            descriptions.append(descriptions_item)

        advisory_m_problem_types = cls(
            descriptions=descriptions,
        )

        advisory_m_problem_types.additional_properties = d
        return advisory_m_problem_types

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

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_m_descriptions import AdvisoryMDescriptions


T = TypeVar("T", bound="AdvisoryImpact")


@_attrs_define
class AdvisoryImpact:
    """
    Attributes:
        capec_id (Union[Unset, str]):
        descriptions (Union[Unset, list['AdvisoryMDescriptions']]):
    """

    capec_id: Union[Unset, str] = UNSET
    descriptions: Union[Unset, list["AdvisoryMDescriptions"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        capec_id = self.capec_id

        descriptions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.descriptions, Unset):
            descriptions = []
            for descriptions_item_data in self.descriptions:
                descriptions_item = descriptions_item_data.to_dict()
                descriptions.append(descriptions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if capec_id is not UNSET:
            field_dict["capecId"] = capec_id
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_m_descriptions import AdvisoryMDescriptions

        d = dict(src_dict)
        capec_id = d.pop("capecId", UNSET)

        descriptions = []
        _descriptions = d.pop("descriptions", UNSET)
        for descriptions_item_data in _descriptions or []:
            descriptions_item = AdvisoryMDescriptions.from_dict(descriptions_item_data)

            descriptions.append(descriptions_item)

        advisory_impact = cls(
            capec_id=capec_id,
            descriptions=descriptions,
        )

        advisory_impact.additional_properties = d
        return advisory_impact

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

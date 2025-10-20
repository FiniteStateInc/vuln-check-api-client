from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_i_val import AdvisoryIVal


T = TypeVar("T", bound="AdvisoryMIdentification")


@_attrs_define
class AdvisoryMIdentification:
    """
    Attributes:
        alias (Union[Unset, AdvisoryIVal]):
        id (Union[Unset, AdvisoryIVal]):
    """

    alias: Union[Unset, "AdvisoryIVal"] = UNSET
    id: Union[Unset, "AdvisoryIVal"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alias: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.alias, Unset):
            alias = self.alias.to_dict()

        id: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alias is not UNSET:
            field_dict["alias"] = alias
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_i_val import AdvisoryIVal

        d = dict(src_dict)
        _alias = d.pop("alias", UNSET)
        alias: Union[Unset, AdvisoryIVal]
        if isinstance(_alias, Unset):
            alias = UNSET
        else:
            alias = AdvisoryIVal.from_dict(_alias)

        _id = d.pop("id", UNSET)
        id: Union[Unset, AdvisoryIVal]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = AdvisoryIVal.from_dict(_id)

        advisory_m_identification = cls(
            alias=alias,
            id=id,
        )

        advisory_m_identification.additional_properties = d
        return advisory_m_identification

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

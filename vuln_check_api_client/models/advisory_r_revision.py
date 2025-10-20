from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_r_description import AdvisoryRDescription


T = TypeVar("T", bound="AdvisoryRRevision")


@_attrs_define
class AdvisoryRRevision:
    """
    Attributes:
        date (Union[Unset, str]):
        description (Union[Unset, AdvisoryRDescription]):
        number (Union[Unset, str]):
    """

    date: Union[Unset, str] = UNSET
    description: Union[Unset, "AdvisoryRDescription"] = UNSET
    number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        description: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        number = self.number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_r_description import AdvisoryRDescription

        d = dict(src_dict)
        date = d.pop("date", UNSET)

        _description = d.pop("description", UNSET)
        description: Union[Unset, AdvisoryRDescription]
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = AdvisoryRDescription.from_dict(_description)

        number = d.pop("number", UNSET)

        advisory_r_revision = cls(
            date=date,
            description=description,
            number=number,
        )

        advisory_r_revision.additional_properties = d
        return advisory_r_revision

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

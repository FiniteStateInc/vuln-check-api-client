from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_i_val import AdvisoryIVal


T = TypeVar("T", bound="AdvisoryRThreat")


@_attrs_define
class AdvisoryRThreat:
    """
    Attributes:
        date (Union[Unset, str]):
        date_specified (Union[Unset, bool]):
        description (Union[Unset, AdvisoryIVal]):
        product_id (Union[Unset, list[str]]):
        type_ (Union[Unset, int]): diff
    """

    date: Union[Unset, str] = UNSET
    date_specified: Union[Unset, bool] = UNSET
    description: Union[Unset, "AdvisoryIVal"] = UNSET
    product_id: Union[Unset, list[str]] = UNSET
    type_: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        date_specified = self.date_specified

        description: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        product_id: Union[Unset, list[str]] = UNSET
        if not isinstance(self.product_id, Unset):
            product_id = self.product_id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["Date"] = date
        if date_specified is not UNSET:
            field_dict["DateSpecified"] = date_specified
        if description is not UNSET:
            field_dict["Description"] = description
        if product_id is not UNSET:
            field_dict["ProductID"] = product_id
        if type_ is not UNSET:
            field_dict["Type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_i_val import AdvisoryIVal

        d = dict(src_dict)
        date = d.pop("Date", UNSET)

        date_specified = d.pop("DateSpecified", UNSET)

        _description = d.pop("Description", UNSET)
        description: Union[Unset, AdvisoryIVal]
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = AdvisoryIVal.from_dict(_description)

        product_id = cast(list[str], d.pop("ProductID", UNSET))

        type_ = d.pop("Type", UNSET)

        advisory_r_threat = cls(
            date=date,
            date_specified=date_specified,
            description=description,
            product_id=product_id,
            type_=type_,
        )

        advisory_r_threat.additional_properties = d
        return advisory_r_threat

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

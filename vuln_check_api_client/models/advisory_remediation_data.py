from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_restart_data import AdvisoryRestartData


T = TypeVar("T", bound="AdvisoryRemediationData")


@_attrs_define
class AdvisoryRemediationData:
    """
    Attributes:
        category (Union[Unset, str]):
        date (Union[Unset, str]):
        details (Union[Unset, str]):
        entitlements (Union[Unset, list[str]]):
        group_ids (Union[Unset, list[str]]):
        product_ids (Union[Unset, list[str]]):
        restart_required (Union[Unset, AdvisoryRestartData]):
    """

    category: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    details: Union[Unset, str] = UNSET
    entitlements: Union[Unset, list[str]] = UNSET
    group_ids: Union[Unset, list[str]] = UNSET
    product_ids: Union[Unset, list[str]] = UNSET
    restart_required: Union[Unset, "AdvisoryRestartData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        date = self.date

        details = self.details

        entitlements: Union[Unset, list[str]] = UNSET
        if not isinstance(self.entitlements, Unset):
            entitlements = self.entitlements

        group_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        product_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.product_ids, Unset):
            product_ids = self.product_ids

        restart_required: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.restart_required, Unset):
            restart_required = self.restart_required.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if date is not UNSET:
            field_dict["date"] = date
        if details is not UNSET:
            field_dict["details"] = details
        if entitlements is not UNSET:
            field_dict["entitlements"] = entitlements
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if product_ids is not UNSET:
            field_dict["product_ids"] = product_ids
        if restart_required is not UNSET:
            field_dict["restart_required"] = restart_required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_restart_data import AdvisoryRestartData

        d = dict(src_dict)
        category = d.pop("category", UNSET)

        date = d.pop("date", UNSET)

        details = d.pop("details", UNSET)

        entitlements = cast(list[str], d.pop("entitlements", UNSET))

        group_ids = cast(list[str], d.pop("group_ids", UNSET))

        product_ids = cast(list[str], d.pop("product_ids", UNSET))

        _restart_required = d.pop("restart_required", UNSET)
        restart_required: Union[Unset, AdvisoryRestartData]
        if isinstance(_restart_required, Unset):
            restart_required = UNSET
        else:
            restart_required = AdvisoryRestartData.from_dict(_restart_required)

        advisory_remediation_data = cls(
            category=category,
            date=date,
            details=details,
            entitlements=entitlements,
            group_ids=group_ids,
            product_ids=product_ids,
            restart_required=restart_required,
        )

        advisory_remediation_data.additional_properties = d
        return advisory_remediation_data

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

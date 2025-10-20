from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_cis_control import AdvisoryCISControl


T = TypeVar("T", bound="AdvisoryNISTControl")


@_attrs_define
class AdvisoryNISTControl:
    """
    Attributes:
        cis_controls (Union[Unset, list['AdvisoryCISControl']]):
        nist_control_family (Union[Unset, str]):
        nist_control_id (Union[Unset, str]):
        nist_control_name (Union[Unset, str]):
    """

    cis_controls: Union[Unset, list["AdvisoryCISControl"]] = UNSET
    nist_control_family: Union[Unset, str] = UNSET
    nist_control_id: Union[Unset, str] = UNSET
    nist_control_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cis_controls: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cis_controls, Unset):
            cis_controls = []
            for cis_controls_item_data in self.cis_controls:
                cis_controls_item = cis_controls_item_data.to_dict()
                cis_controls.append(cis_controls_item)

        nist_control_family = self.nist_control_family

        nist_control_id = self.nist_control_id

        nist_control_name = self.nist_control_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cis_controls is not UNSET:
            field_dict["cis_controls"] = cis_controls
        if nist_control_family is not UNSET:
            field_dict["nist_control_family"] = nist_control_family
        if nist_control_id is not UNSET:
            field_dict["nist_control_id"] = nist_control_id
        if nist_control_name is not UNSET:
            field_dict["nist_control_name"] = nist_control_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_cis_control import AdvisoryCISControl

        d = dict(src_dict)
        cis_controls = []
        _cis_controls = d.pop("cis_controls", UNSET)
        for cis_controls_item_data in _cis_controls or []:
            cis_controls_item = AdvisoryCISControl.from_dict(cis_controls_item_data)

            cis_controls.append(cis_controls_item)

        nist_control_family = d.pop("nist_control_family", UNSET)

        nist_control_id = d.pop("nist_control_id", UNSET)

        nist_control_name = d.pop("nist_control_name", UNSET)

        advisory_nist_control = cls(
            cis_controls=cis_controls,
            nist_control_family=nist_control_family,
            nist_control_id=nist_control_id,
            nist_control_name=nist_control_name,
        )

        advisory_nist_control.additional_properties = d
        return advisory_nist_control

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

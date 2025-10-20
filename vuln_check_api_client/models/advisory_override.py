from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_override_annotation import AdvisoryOverrideAnnotation
    from ..models.advisory_override_cve import AdvisoryOverrideCVE


T = TypeVar("T", bound="AdvisoryOverride")


@_attrs_define
class AdvisoryOverride:
    """
    Attributes:
        field_annotation (Union[Unset, AdvisoryOverrideAnnotation]):
        cve (Union[Unset, AdvisoryOverrideCVE]):
    """

    field_annotation: Union[Unset, "AdvisoryOverrideAnnotation"] = UNSET
    cve: Union[Unset, "AdvisoryOverrideCVE"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_annotation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_annotation, Unset):
            field_annotation = self.field_annotation.to_dict()

        cve: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_annotation is not UNSET:
            field_dict["_annotation"] = field_annotation
        if cve is not UNSET:
            field_dict["cve"] = cve

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_override_annotation import AdvisoryOverrideAnnotation
        from ..models.advisory_override_cve import AdvisoryOverrideCVE

        d = dict(src_dict)
        _field_annotation = d.pop("_annotation", UNSET)
        field_annotation: Union[Unset, AdvisoryOverrideAnnotation]
        if isinstance(_field_annotation, Unset):
            field_annotation = UNSET
        else:
            field_annotation = AdvisoryOverrideAnnotation.from_dict(_field_annotation)

        _cve = d.pop("cve", UNSET)
        cve: Union[Unset, AdvisoryOverrideCVE]
        if isinstance(_cve, Unset):
            cve = UNSET
        else:
            cve = AdvisoryOverrideCVE.from_dict(_cve)

        advisory_override = cls(
            field_annotation=field_annotation,
            cve=cve,
        )

        advisory_override.additional_properties = d
        return advisory_override

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

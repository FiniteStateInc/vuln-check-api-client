from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_siemens_engine import AdvisorySiemensEngine


T = TypeVar("T", bound="AdvisorySiemensGenerator")


@_attrs_define
class AdvisorySiemensGenerator:
    """
    Attributes:
        engine (Union[Unset, AdvisorySiemensEngine]):
    """

    engine: Union[Unset, "AdvisorySiemensEngine"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        engine: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.engine, Unset):
            engine = self.engine.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if engine is not UNSET:
            field_dict["engine"] = engine

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_siemens_engine import AdvisorySiemensEngine

        d = dict(src_dict)
        _engine = d.pop("engine", UNSET)
        engine: Union[Unset, AdvisorySiemensEngine]
        if isinstance(_engine, Unset):
            engine = UNSET
        else:
            engine = AdvisorySiemensEngine.from_dict(_engine)

        advisory_siemens_generator = cls(
            engine=engine,
        )

        advisory_siemens_generator.additional_properties = d
        return advisory_siemens_generator

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

from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiMitreDetectionTech")


@_attrs_define
class ApiMitreDetectionTech:
    """
    Attributes:
        datacomponent (Union[Unset, str]):
        datasource (Union[Unset, str]):
        detects (Union[Unset, str]):
        id (Union[Unset, str]):
    """

    datacomponent: Union[Unset, str] = UNSET
    datasource: Union[Unset, str] = UNSET
    detects: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datacomponent = self.datacomponent

        datasource = self.datasource

        detects = self.detects

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if datacomponent is not UNSET:
            field_dict["datacomponent"] = datacomponent
        if datasource is not UNSET:
            field_dict["datasource"] = datasource
        if detects is not UNSET:
            field_dict["detects"] = detects
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        datacomponent = d.pop("datacomponent", UNSET)

        datasource = d.pop("datasource", UNSET)

        detects = d.pop("detects", UNSET)

        id = d.pop("id", UNSET)

        api_mitre_detection_tech = cls(
            datacomponent=datacomponent,
            datasource=datasource,
            detects=detects,
            id=id,
        )

        api_mitre_detection_tech.additional_properties = d
        return api_mitre_detection_tech

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

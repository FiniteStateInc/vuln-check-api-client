from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_mitre_d3_fend_technique import ApiMitreD3FendTechnique


T = TypeVar("T", bound="ApiMitreMitigation2D3FendMapping")


@_attrs_define
class ApiMitreMitigation2D3FendMapping:
    """
    Attributes:
        d3fendtechniques (Union[Unset, list['ApiMitreD3FendTechnique']]):
        id (Union[Unset, str]):
    """

    d3fendtechniques: Union[Unset, list["ApiMitreD3FendTechnique"]] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        d3fendtechniques: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.d3fendtechniques, Unset):
            d3fendtechniques = []
            for d3fendtechniques_item_data in self.d3fendtechniques:
                d3fendtechniques_item = d3fendtechniques_item_data.to_dict()
                d3fendtechniques.append(d3fendtechniques_item)

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if d3fendtechniques is not UNSET:
            field_dict["d3fendtechniques"] = d3fendtechniques
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_mitre_d3_fend_technique import ApiMitreD3FendTechnique

        d = dict(src_dict)
        d3fendtechniques = []
        _d3fendtechniques = d.pop("d3fendtechniques", UNSET)
        for d3fendtechniques_item_data in _d3fendtechniques or []:
            d3fendtechniques_item = ApiMitreD3FendTechnique.from_dict(d3fendtechniques_item_data)

            d3fendtechniques.append(d3fendtechniques_item)

        id = d.pop("id", UNSET)

        api_mitre_mitigation_2d3_fend_mapping = cls(
            d3fendtechniques=d3fendtechniques,
            id=id,
        )

        api_mitre_mitigation_2d3_fend_mapping.additional_properties = d
        return api_mitre_mitigation_2d3_fend_mapping

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

from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiCWE")


@_attrs_define
class ApiCWE:
    """
    Attributes:
        abstraction (Union[Unset, str]):
        description (Union[Unset, str]):
        kev_count (Union[Unset, int]):
        status (Union[Unset, str]):
        structure (Union[Unset, str]):
        vulncheck_nvd_count (Union[Unset, int]):
        weakness_id (Union[Unset, str]):
        weakness_name (Union[Unset, str]):
        weighted_score (Union[Unset, float]):
    """

    abstraction: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    kev_count: Union[Unset, int] = UNSET
    status: Union[Unset, str] = UNSET
    structure: Union[Unset, str] = UNSET
    vulncheck_nvd_count: Union[Unset, int] = UNSET
    weakness_id: Union[Unset, str] = UNSET
    weakness_name: Union[Unset, str] = UNSET
    weighted_score: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        abstraction = self.abstraction

        description = self.description

        kev_count = self.kev_count

        status = self.status

        structure = self.structure

        vulncheck_nvd_count = self.vulncheck_nvd_count

        weakness_id = self.weakness_id

        weakness_name = self.weakness_name

        weighted_score = self.weighted_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if abstraction is not UNSET:
            field_dict["abstraction"] = abstraction
        if description is not UNSET:
            field_dict["description"] = description
        if kev_count is not UNSET:
            field_dict["kev_count"] = kev_count
        if status is not UNSET:
            field_dict["status"] = status
        if structure is not UNSET:
            field_dict["structure"] = structure
        if vulncheck_nvd_count is not UNSET:
            field_dict["vulncheck_nvd_count"] = vulncheck_nvd_count
        if weakness_id is not UNSET:
            field_dict["weakness_id"] = weakness_id
        if weakness_name is not UNSET:
            field_dict["weakness_name"] = weakness_name
        if weighted_score is not UNSET:
            field_dict["weighted_score"] = weighted_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        abstraction = d.pop("abstraction", UNSET)

        description = d.pop("description", UNSET)

        kev_count = d.pop("kev_count", UNSET)

        status = d.pop("status", UNSET)

        structure = d.pop("structure", UNSET)

        vulncheck_nvd_count = d.pop("vulncheck_nvd_count", UNSET)

        weakness_id = d.pop("weakness_id", UNSET)

        weakness_name = d.pop("weakness_name", UNSET)

        weighted_score = d.pop("weighted_score", UNSET)

        api_cwe = cls(
            abstraction=abstraction,
            description=description,
            kev_count=kev_count,
            status=status,
            structure=structure,
            vulncheck_nvd_count=vulncheck_nvd_count,
            weakness_id=weakness_id,
            weakness_name=weakness_name,
            weighted_score=weighted_score,
        )

        api_cwe.additional_properties = d
        return api_cwe

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

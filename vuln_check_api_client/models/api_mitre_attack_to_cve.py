from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_mitre_attack_tech import ApiMitreAttackTech


T = TypeVar("T", bound="ApiMitreAttackToCVE")


@_attrs_define
class ApiMitreAttackToCVE:
    """
    Attributes:
        cve_list (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        technique_id (Union[Unset, ApiMitreAttackTech]):
    """

    cve_list: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    technique_id: Union[Unset, "ApiMitreAttackTech"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve_list, Unset):
            cve_list = self.cve_list

        date_added = self.date_added

        technique_id: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.technique_id, Unset):
            technique_id = self.technique_id.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve_list is not UNSET:
            field_dict["cve_list"] = cve_list
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if technique_id is not UNSET:
            field_dict["technique_id"] = technique_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_mitre_attack_tech import ApiMitreAttackTech

        d = dict(src_dict)
        cve_list = cast(list[str], d.pop("cve_list", UNSET))

        date_added = d.pop("date_added", UNSET)

        _technique_id = d.pop("technique_id", UNSET)
        technique_id: Union[Unset, ApiMitreAttackTech]
        if isinstance(_technique_id, Unset):
            technique_id = UNSET
        else:
            technique_id = ApiMitreAttackTech.from_dict(_technique_id)

        api_mitre_attack_to_cve = cls(
            cve_list=cve_list,
            date_added=date_added,
            technique_id=technique_id,
        )

        api_mitre_attack_to_cve.additional_properties = d
        return api_mitre_attack_to_cve

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

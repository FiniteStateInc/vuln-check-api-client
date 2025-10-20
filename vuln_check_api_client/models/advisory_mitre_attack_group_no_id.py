from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_mitre_attack_technique import AdvisoryMitreAttackTechnique


T = TypeVar("T", bound="AdvisoryMITREAttackGroupNoID")


@_attrs_define
class AdvisoryMITREAttackGroupNoID:
    """
    Attributes:
        aliases (Union[Unset, list[str]]):
        description (Union[Unset, str]):
        name (Union[Unset, str]):
        techniques (Union[Unset, list['AdvisoryMitreAttackTechnique']]):
    """

    aliases: Union[Unset, list[str]] = UNSET
    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    techniques: Union[Unset, list["AdvisoryMitreAttackTechnique"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aliases: Union[Unset, list[str]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        description = self.description

        name = self.name

        techniques: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.techniques, Unset):
            techniques = []
            for techniques_item_data in self.techniques:
                techniques_item = techniques_item_data.to_dict()
                techniques.append(techniques_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if techniques is not UNSET:
            field_dict["techniques"] = techniques

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_mitre_attack_technique import AdvisoryMitreAttackTechnique

        d = dict(src_dict)
        aliases = cast(list[str], d.pop("aliases", UNSET))

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        techniques = []
        _techniques = d.pop("techniques", UNSET)
        for techniques_item_data in _techniques or []:
            techniques_item = AdvisoryMitreAttackTechnique.from_dict(techniques_item_data)

            techniques.append(techniques_item)

        advisory_mitre_attack_group_no_id = cls(
            aliases=aliases,
            description=description,
            name=name,
            techniques=techniques,
        )

        advisory_mitre_attack_group_no_id.additional_properties = d
        return advisory_mitre_attack_group_no_id

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

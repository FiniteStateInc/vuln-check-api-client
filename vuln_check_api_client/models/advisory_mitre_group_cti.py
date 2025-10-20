from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_external_references import AdvisoryExternalReferences


T = TypeVar("T", bound="AdvisoryMitreGroupCTI")


@_attrs_define
class AdvisoryMitreGroupCTI:
    """
    Attributes:
        aliases (Union[Unset, list[str]]):
        description (Union[Unset, str]):
        id (Union[Unset, str]):
        references (Union[Unset, list['AdvisoryExternalReferences']]):
    """

    aliases: Union[Unset, list[str]] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    references: Union[Unset, list["AdvisoryExternalReferences"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aliases: Union[Unset, list[str]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        description = self.description

        id = self.id

        references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if references is not UNSET:
            field_dict["references"] = references

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_external_references import AdvisoryExternalReferences

        d = dict(src_dict)
        aliases = cast(list[str], d.pop("aliases", UNSET))

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = AdvisoryExternalReferences.from_dict(references_item_data)

            references.append(references_item)

        advisory_mitre_group_cti = cls(
            aliases=aliases,
            description=description,
            id=id,
            references=references,
        )

        advisory_mitre_group_cti.additional_properties = d
        return advisory_mitre_group_cti

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

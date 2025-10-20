from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryMispMeta")


@_attrs_define
class AdvisoryMispMeta:
    """
    Attributes:
        attribution_confidence (Union[Unset, str]):
        cfr_suspected_state_sponsor (Union[Unset, str]):
        cfr_suspected_victims (Union[Unset, list[str]]):
        cfr_target_category (Union[Unset, list[str]]):
        cfr_type_of_incident (Union[Unset, list[str]]):
        country (Union[Unset, str]):
        refs (Union[Unset, list[str]]):
        synonyms (Union[Unset, list[str]]):
    """

    attribution_confidence: Union[Unset, str] = UNSET
    cfr_suspected_state_sponsor: Union[Unset, str] = UNSET
    cfr_suspected_victims: Union[Unset, list[str]] = UNSET
    cfr_target_category: Union[Unset, list[str]] = UNSET
    cfr_type_of_incident: Union[Unset, list[str]] = UNSET
    country: Union[Unset, str] = UNSET
    refs: Union[Unset, list[str]] = UNSET
    synonyms: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribution_confidence = self.attribution_confidence

        cfr_suspected_state_sponsor = self.cfr_suspected_state_sponsor

        cfr_suspected_victims: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cfr_suspected_victims, Unset):
            cfr_suspected_victims = self.cfr_suspected_victims

        cfr_target_category: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cfr_target_category, Unset):
            cfr_target_category = self.cfr_target_category

        cfr_type_of_incident: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cfr_type_of_incident, Unset):
            cfr_type_of_incident = self.cfr_type_of_incident

        country = self.country

        refs: Union[Unset, list[str]] = UNSET
        if not isinstance(self.refs, Unset):
            refs = self.refs

        synonyms: Union[Unset, list[str]] = UNSET
        if not isinstance(self.synonyms, Unset):
            synonyms = self.synonyms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribution_confidence is not UNSET:
            field_dict["attribution-confidence"] = attribution_confidence
        if cfr_suspected_state_sponsor is not UNSET:
            field_dict["cfr-suspected-state-sponsor"] = cfr_suspected_state_sponsor
        if cfr_suspected_victims is not UNSET:
            field_dict["cfr-suspected-victims"] = cfr_suspected_victims
        if cfr_target_category is not UNSET:
            field_dict["cfr-target-category"] = cfr_target_category
        if cfr_type_of_incident is not UNSET:
            field_dict["cfr-type-of-incident"] = cfr_type_of_incident
        if country is not UNSET:
            field_dict["country"] = country
        if refs is not UNSET:
            field_dict["refs"] = refs
        if synonyms is not UNSET:
            field_dict["synonyms"] = synonyms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attribution_confidence = d.pop("attribution-confidence", UNSET)

        cfr_suspected_state_sponsor = d.pop("cfr-suspected-state-sponsor", UNSET)

        cfr_suspected_victims = cast(list[str], d.pop("cfr-suspected-victims", UNSET))

        cfr_target_category = cast(list[str], d.pop("cfr-target-category", UNSET))

        cfr_type_of_incident = cast(list[str], d.pop("cfr-type-of-incident", UNSET))

        country = d.pop("country", UNSET)

        refs = cast(list[str], d.pop("refs", UNSET))

        synonyms = cast(list[str], d.pop("synonyms", UNSET))

        advisory_misp_meta = cls(
            attribution_confidence=attribution_confidence,
            cfr_suspected_state_sponsor=cfr_suspected_state_sponsor,
            cfr_suspected_victims=cfr_suspected_victims,
            cfr_target_category=cfr_target_category,
            cfr_type_of_incident=cfr_type_of_incident,
            country=country,
            refs=refs,
            synonyms=synonyms,
        )

        advisory_misp_meta.additional_properties = d
        return advisory_misp_meta

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

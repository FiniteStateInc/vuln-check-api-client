from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryUSOMAdvisory")


@_attrs_define
class AdvisoryUSOMAdvisory:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        effect_tr (Union[Unset, str]):
        general_information_tr (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        solution_tr (Union[Unset, str]):
        title_tr (Union[Unset, str]):
        trid (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    effect_tr: Union[Unset, str] = UNSET
    general_information_tr: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    solution_tr: Union[Unset, str] = UNSET
    title_tr: Union[Unset, str] = UNSET
    trid: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        effect_tr = self.effect_tr

        general_information_tr = self.general_information_tr

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        solution_tr = self.solution_tr

        title_tr = self.title_tr

        trid = self.trid

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if effect_tr is not UNSET:
            field_dict["effect_tr"] = effect_tr
        if general_information_tr is not UNSET:
            field_dict["general_information_tr"] = general_information_tr
        if references is not UNSET:
            field_dict["references"] = references
        if solution_tr is not UNSET:
            field_dict["solution_tr"] = solution_tr
        if title_tr is not UNSET:
            field_dict["title_tr"] = title_tr
        if trid is not UNSET:
            field_dict["trid"] = trid
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        effect_tr = d.pop("effect_tr", UNSET)

        general_information_tr = d.pop("general_information_tr", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        solution_tr = d.pop("solution_tr", UNSET)

        title_tr = d.pop("title_tr", UNSET)

        trid = d.pop("trid", UNSET)

        url = d.pop("url", UNSET)

        advisory_usom_advisory = cls(
            cve=cve,
            date_added=date_added,
            effect_tr=effect_tr,
            general_information_tr=general_information_tr,
            references=references,
            solution_tr=solution_tr,
            title_tr=title_tr,
            trid=trid,
            url=url,
        )

        advisory_usom_advisory.additional_properties = d
        return advisory_usom_advisory

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

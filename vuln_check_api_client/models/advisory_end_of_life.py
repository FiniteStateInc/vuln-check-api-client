from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_cycle import AdvisoryCycle


T = TypeVar("T", bound="AdvisoryEndOfLife")


@_attrs_define
class AdvisoryEndOfLife:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        cycles (Union[Unset, list['AdvisoryCycle']]):
        date_added (Union[Unset, str]):
        name (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    cycles: Union[Unset, list["AdvisoryCycle"]] = UNSET
    date_added: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cycles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cycles, Unset):
            cycles = []
            for cycles_item_data in self.cycles:
                cycles_item = cycles_item_data.to_dict()
                cycles.append(cycles_item)

        date_added = self.date_added

        name = self.name

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cycles is not UNSET:
            field_dict["cycles"] = cycles
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_cycle import AdvisoryCycle

        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        cycles = []
        _cycles = d.pop("cycles", UNSET)
        for cycles_item_data in _cycles or []:
            cycles_item = AdvisoryCycle.from_dict(cycles_item_data)

            cycles.append(cycles_item)

        date_added = d.pop("date_added", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        advisory_end_of_life = cls(
            cve=cve,
            cycles=cycles,
            date_added=date_added,
            name=name,
            url=url,
        )

        advisory_end_of_life.additional_properties = d
        return advisory_end_of_life

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

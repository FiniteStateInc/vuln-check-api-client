from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_cycle_discontinued import AdvisoryCycleDiscontinued
    from ..models.advisory_cycle_eol import AdvisoryCycleEol
    from ..models.advisory_cycle_extended_support import AdvisoryCycleExtendedSupport
    from ..models.advisory_cycle_lts import AdvisoryCycleLts
    from ..models.advisory_cycle_support import AdvisoryCycleSupport


T = TypeVar("T", bound="AdvisoryCycle")


@_attrs_define
class AdvisoryCycle:
    """
    Attributes:
        codename (Union[Unset, str]):
        cycle (Union[Unset, str]):
        discontinued (Union[Unset, AdvisoryCycleDiscontinued]):
        eol (Union[Unset, AdvisoryCycleEol]):
        extended_support (Union[Unset, AdvisoryCycleExtendedSupport]):
        latest (Union[Unset, str]):
        latest_release_date (Union[Unset, str]):
        link (Union[Unset, str]):
        lts (Union[Unset, AdvisoryCycleLts]):
        release_date (Union[Unset, str]):
        release_label (Union[Unset, str]):
        support (Union[Unset, AdvisoryCycleSupport]):
    """

    codename: Union[Unset, str] = UNSET
    cycle: Union[Unset, str] = UNSET
    discontinued: Union[Unset, "AdvisoryCycleDiscontinued"] = UNSET
    eol: Union[Unset, "AdvisoryCycleEol"] = UNSET
    extended_support: Union[Unset, "AdvisoryCycleExtendedSupport"] = UNSET
    latest: Union[Unset, str] = UNSET
    latest_release_date: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    lts: Union[Unset, "AdvisoryCycleLts"] = UNSET
    release_date: Union[Unset, str] = UNSET
    release_label: Union[Unset, str] = UNSET
    support: Union[Unset, "AdvisoryCycleSupport"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        codename = self.codename

        cycle = self.cycle

        discontinued: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.discontinued, Unset):
            discontinued = self.discontinued.to_dict()

        eol: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.eol, Unset):
            eol = self.eol.to_dict()

        extended_support: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.extended_support, Unset):
            extended_support = self.extended_support.to_dict()

        latest = self.latest

        latest_release_date = self.latest_release_date

        link = self.link

        lts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.lts, Unset):
            lts = self.lts.to_dict()

        release_date = self.release_date

        release_label = self.release_label

        support: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.support, Unset):
            support = self.support.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if codename is not UNSET:
            field_dict["codename"] = codename
        if cycle is not UNSET:
            field_dict["cycle"] = cycle
        if discontinued is not UNSET:
            field_dict["discontinued"] = discontinued
        if eol is not UNSET:
            field_dict["eol"] = eol
        if extended_support is not UNSET:
            field_dict["extendedSupport"] = extended_support
        if latest is not UNSET:
            field_dict["latest"] = latest
        if latest_release_date is not UNSET:
            field_dict["latestReleaseDate"] = latest_release_date
        if link is not UNSET:
            field_dict["link"] = link
        if lts is not UNSET:
            field_dict["lts"] = lts
        if release_date is not UNSET:
            field_dict["releaseDate"] = release_date
        if release_label is not UNSET:
            field_dict["releaseLabel"] = release_label
        if support is not UNSET:
            field_dict["support"] = support

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_cycle_discontinued import AdvisoryCycleDiscontinued
        from ..models.advisory_cycle_eol import AdvisoryCycleEol
        from ..models.advisory_cycle_extended_support import AdvisoryCycleExtendedSupport
        from ..models.advisory_cycle_lts import AdvisoryCycleLts
        from ..models.advisory_cycle_support import AdvisoryCycleSupport

        d = dict(src_dict)
        codename = d.pop("codename", UNSET)

        cycle = d.pop("cycle", UNSET)

        _discontinued = d.pop("discontinued", UNSET)
        discontinued: Union[Unset, AdvisoryCycleDiscontinued]
        if isinstance(_discontinued, Unset):
            discontinued = UNSET
        else:
            discontinued = AdvisoryCycleDiscontinued.from_dict(_discontinued)

        _eol = d.pop("eol", UNSET)
        eol: Union[Unset, AdvisoryCycleEol]
        if isinstance(_eol, Unset):
            eol = UNSET
        else:
            eol = AdvisoryCycleEol.from_dict(_eol)

        _extended_support = d.pop("extendedSupport", UNSET)
        extended_support: Union[Unset, AdvisoryCycleExtendedSupport]
        if isinstance(_extended_support, Unset):
            extended_support = UNSET
        else:
            extended_support = AdvisoryCycleExtendedSupport.from_dict(_extended_support)

        latest = d.pop("latest", UNSET)

        latest_release_date = d.pop("latestReleaseDate", UNSET)

        link = d.pop("link", UNSET)

        _lts = d.pop("lts", UNSET)
        lts: Union[Unset, AdvisoryCycleLts]
        if isinstance(_lts, Unset):
            lts = UNSET
        else:
            lts = AdvisoryCycleLts.from_dict(_lts)

        release_date = d.pop("releaseDate", UNSET)

        release_label = d.pop("releaseLabel", UNSET)

        _support = d.pop("support", UNSET)
        support: Union[Unset, AdvisoryCycleSupport]
        if isinstance(_support, Unset):
            support = UNSET
        else:
            support = AdvisoryCycleSupport.from_dict(_support)

        advisory_cycle = cls(
            codename=codename,
            cycle=cycle,
            discontinued=discontinued,
            eol=eol,
            extended_support=extended_support,
            latest=latest,
            latest_release_date=latest_release_date,
            link=link,
            lts=lts,
            release_date=release_date,
            release_label=release_label,
            support=support,
        )

        advisory_cycle.additional_properties = d
        return advisory_cycle

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

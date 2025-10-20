from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_override import AdvisoryOverride


T = TypeVar("T", bound="AdvisoryAnchoreNVDOverride")


@_attrs_define
class AdvisoryAnchoreNVDOverride:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        override (Union[Unset, AdvisoryOverride]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    override: Union[Unset, "AdvisoryOverride"] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        override: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.override, Unset):
            override = self.override.to_dict()

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if override is not UNSET:
            field_dict["override"] = override
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_override import AdvisoryOverride

        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        _override = d.pop("override", UNSET)
        override: Union[Unset, AdvisoryOverride]
        if isinstance(_override, Unset):
            override = UNSET
        else:
            override = AdvisoryOverride.from_dict(_override)

        url = d.pop("url", UNSET)

        advisory_anchore_nvd_override = cls(
            cve=cve,
            date_added=date_added,
            override=override,
            url=url,
        )

        advisory_anchore_nvd_override.additional_properties = d
        return advisory_anchore_nvd_override

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

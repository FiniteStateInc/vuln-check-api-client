from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiNormalizedReportV3Entry")


@_attrs_define
class ApiNormalizedReportV3Entry:
    """
    Attributes:
        date_added (Union[Unset, str]):
        name (Union[Unset, str]):
        refsource (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    date_added: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    refsource: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_added = self.date_added

        name = self.name

        refsource = self.refsource

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if name is not UNSET:
            field_dict["name"] = name
        if refsource is not UNSET:
            field_dict["refsource"] = refsource
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date_added = d.pop("date_added", UNSET)

        name = d.pop("name", UNSET)

        refsource = d.pop("refsource", UNSET)

        url = d.pop("url", UNSET)

        api_normalized_report_v3_entry = cls(
            date_added=date_added,
            name=name,
            refsource=refsource,
            url=url,
        )

        api_normalized_report_v3_entry.additional_properties = d
        return api_normalized_report_v3_entry

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

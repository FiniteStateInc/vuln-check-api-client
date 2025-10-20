from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_cos_update import AdvisoryCOSUpdate


T = TypeVar("T", bound="AdvisoryContainerOS")


@_attrs_define
class AdvisoryContainerOS:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        title (Union[Unset, str]):
        updates (Union[Unset, list['AdvisoryCOSUpdate']]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    updates: Union[Unset, list["AdvisoryCOSUpdate"]] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        title = self.title

        updates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.updates, Unset):
            updates = []
            for updates_item_data in self.updates:
                updates_item = updates_item_data.to_dict()
                updates.append(updates_item)

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if title is not UNSET:
            field_dict["title"] = title
        if updates is not UNSET:
            field_dict["updates"] = updates
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_cos_update import AdvisoryCOSUpdate

        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        title = d.pop("title", UNSET)

        updates = []
        _updates = d.pop("updates", UNSET)
        for updates_item_data in _updates or []:
            updates_item = AdvisoryCOSUpdate.from_dict(updates_item_data)

            updates.append(updates_item)

        url = d.pop("url", UNSET)

        advisory_container_os = cls(
            cve=cve,
            date_added=date_added,
            title=title,
            updates=updates,
            url=url,
        )

        advisory_container_os.additional_properties = d
        return advisory_container_os

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

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_android_event import AdvisoryAndroidEvent


T = TypeVar("T", bound="AdvisoryAndroidRange")


@_attrs_define
class AdvisoryAndroidRange:
    """
    Attributes:
        events (Union[Unset, list['AdvisoryAndroidEvent']]):
        type_ (Union[Unset, str]):
    """

    events: Union[Unset, list["AdvisoryAndroidEvent"]] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_android_event import AdvisoryAndroidEvent

        d = dict(src_dict)
        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = AdvisoryAndroidEvent.from_dict(events_item_data)

            events.append(events_item)

        type_ = d.pop("type", UNSET)

        advisory_android_range = cls(
            events=events,
            type_=type_,
        )

        advisory_android_range.additional_properties = d
        return advisory_android_range

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

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_py_pa_event import AdvisoryPyPAEvent


T = TypeVar("T", bound="AdvisoryPyPARange")


@_attrs_define
class AdvisoryPyPARange:
    """
    Attributes:
        events (Union[Unset, list['AdvisoryPyPAEvent']]):
        ranges_type (Union[Unset, str]):
    """

    events: Union[Unset, list["AdvisoryPyPAEvent"]] = UNSET
    ranges_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        ranges_type = self.ranges_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events
        if ranges_type is not UNSET:
            field_dict["ranges_type"] = ranges_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_py_pa_event import AdvisoryPyPAEvent

        d = dict(src_dict)
        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = AdvisoryPyPAEvent.from_dict(events_item_data)

            events.append(events_item)

        ranges_type = d.pop("ranges_type", UNSET)

        advisory_py_pa_range = cls(
            events=events,
            ranges_type=ranges_type,
        )

        advisory_py_pa_range.additional_properties = d
        return advisory_py_pa_range

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

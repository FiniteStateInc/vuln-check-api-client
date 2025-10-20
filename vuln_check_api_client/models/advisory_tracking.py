from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_revision_history import AdvisoryRevisionHistory


T = TypeVar("T", bound="AdvisoryTracking")


@_attrs_define
class AdvisoryTracking:
    """
    Attributes:
        current_release_date (Union[Unset, str]):
        id (Union[Unset, str]):
        initial_release_date (Union[Unset, str]):
        revision_history (Union[Unset, list['AdvisoryRevisionHistory']]):
        status (Union[Unset, str]):
        version (Union[Unset, str]): should match last 'number' in []RevisionHistory
    """

    current_release_date: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    initial_release_date: Union[Unset, str] = UNSET
    revision_history: Union[Unset, list["AdvisoryRevisionHistory"]] = UNSET
    status: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_release_date = self.current_release_date

        id = self.id

        initial_release_date = self.initial_release_date

        revision_history: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.revision_history, Unset):
            revision_history = []
            for revision_history_item_data in self.revision_history:
                revision_history_item = revision_history_item_data.to_dict()
                revision_history.append(revision_history_item)

        status = self.status

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_release_date is not UNSET:
            field_dict["current_release_date"] = current_release_date
        if id is not UNSET:
            field_dict["id"] = id
        if initial_release_date is not UNSET:
            field_dict["initial_release_date"] = initial_release_date
        if revision_history is not UNSET:
            field_dict["revision_history"] = revision_history
        if status is not UNSET:
            field_dict["status"] = status
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_revision_history import AdvisoryRevisionHistory

        d = dict(src_dict)
        current_release_date = d.pop("current_release_date", UNSET)

        id = d.pop("id", UNSET)

        initial_release_date = d.pop("initial_release_date", UNSET)

        revision_history = []
        _revision_history = d.pop("revision_history", UNSET)
        for revision_history_item_data in _revision_history or []:
            revision_history_item = AdvisoryRevisionHistory.from_dict(revision_history_item_data)

            revision_history.append(revision_history_item)

        status = d.pop("status", UNSET)

        version = d.pop("version", UNSET)

        advisory_tracking = cls(
            current_release_date=current_release_date,
            id=id,
            initial_release_date=initial_release_date,
            revision_history=revision_history,
            status=status,
            version=version,
        )

        advisory_tracking.additional_properties = d
        return advisory_tracking

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

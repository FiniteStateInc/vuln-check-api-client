from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_i_val import AdvisoryIVal


T = TypeVar("T", bound="AdvisoryAcknowledgement")


@_attrs_define
class AdvisoryAcknowledgement:
    """
    Attributes:
        name (Union[Unset, list['AdvisoryIVal']]):
        url (Union[Unset, list[str]]):
    """

    name: Union[Unset, list["AdvisoryIVal"]] = UNSET
    url: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.name, Unset):
            name = []
            for name_item_data in self.name:
                name_item = name_item_data.to_dict()
                name.append(name_item)

        url: Union[Unset, list[str]] = UNSET
        if not isinstance(self.url, Unset):
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_i_val import AdvisoryIVal

        d = dict(src_dict)
        name = []
        _name = d.pop("name", UNSET)
        for name_item_data in _name or []:
            name_item = AdvisoryIVal.from_dict(name_item_data)

            name.append(name_item)

        url = cast(list[str], d.pop("url", UNSET))

        advisory_acknowledgement = cls(
            name=name,
            url=url,
        )

        advisory_acknowledgement.additional_properties = d
        return advisory_acknowledgement

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

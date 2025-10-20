from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_apple_component import AdvisoryAppleComponent


T = TypeVar("T", bound="AdvisoryAppleAdvisory")


@_attrs_define
class AdvisoryAppleAdvisory:
    """
    Attributes:
        components (Union[Unset, list['AdvisoryAppleComponent']]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        name (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    components: Union[Unset, list["AdvisoryAppleComponent"]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        components: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.components, Unset):
            components = []
            for components_item_data in self.components:
                components_item = components_item_data.to_dict()
                components.append(components_item)

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        name = self.name

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if components is not UNSET:
            field_dict["components"] = components
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_apple_component import AdvisoryAppleComponent

        d = dict(src_dict)
        components = []
        _components = d.pop("components", UNSET)
        for components_item_data in _components or []:
            components_item = AdvisoryAppleComponent.from_dict(components_item_data)

            components.append(components_item)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        advisory_apple_advisory = cls(
            components=components,
            cve=cve,
            date_added=date_added,
            name=name,
            url=url,
        )

        advisory_apple_advisory.additional_properties = d
        return advisory_apple_advisory

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

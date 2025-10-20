from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_vulnrichment_option import AdvisoryVulnrichmentOption


T = TypeVar("T", bound="AdvisoryVulnrichmentContent")


@_attrs_define
class AdvisoryVulnrichmentContent:
    """
    Attributes:
        id (Union[Unset, str]):
        options (Union[Unset, list['AdvisoryVulnrichmentOption']]):
        role (Union[Unset, str]):
        timestamp (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    options: Union[Unset, list["AdvisoryVulnrichmentOption"]] = UNSET
    role: Union[Unset, str] = UNSET
    timestamp: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        options: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        role = self.role

        timestamp = self.timestamp

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if options is not UNSET:
            field_dict["options"] = options
        if role is not UNSET:
            field_dict["role"] = role
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_vulnrichment_option import AdvisoryVulnrichmentOption

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = AdvisoryVulnrichmentOption.from_dict(options_item_data)

            options.append(options_item)

        role = d.pop("role", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        version = d.pop("version", UNSET)

        advisory_vulnrichment_content = cls(
            id=id,
            options=options,
            role=role,
            timestamp=timestamp,
            version=version,
        )

        advisory_vulnrichment_content.additional_properties = d
        return advisory_vulnrichment_content

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

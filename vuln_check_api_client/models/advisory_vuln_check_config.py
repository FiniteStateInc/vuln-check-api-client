from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_nvd20_configuration import AdvisoryNVD20Configuration


T = TypeVar("T", bound="AdvisoryVulnCheckConfig")


@_attrs_define
class AdvisoryVulnCheckConfig:
    """
    Attributes:
        config (Union[Unset, list['AdvisoryNVD20Configuration']]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
    """

    config: Union[Unset, list["AdvisoryNVD20Configuration"]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.config, Unset):
            config = []
            for config_item_data in self.config:
                config_item = config_item_data.to_dict()
                config.append(config_item)

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_nvd20_configuration import AdvisoryNVD20Configuration

        d = dict(src_dict)
        config = []
        _config = d.pop("config", UNSET)
        for config_item_data in _config or []:
            config_item = AdvisoryNVD20Configuration.from_dict(config_item_data)

            config.append(config_item)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        advisory_vuln_check_config = cls(
            config=config,
            cve=cve,
            date_added=date_added,
        )

        advisory_vuln_check_config.additional_properties = d
        return advisory_vuln_check_config

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

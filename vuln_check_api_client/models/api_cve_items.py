from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_configurations import ApiConfigurations
    from ..models.api_cve import ApiCVE
    from ..models.api_impact import ApiImpact


T = TypeVar("T", bound="ApiCveItems")


@_attrs_define
class ApiCveItems:
    """
    Attributes:
        configurations (Union[Unset, ApiConfigurations]):
        cve (Union[Unset, ApiCVE]):
        impact (Union[Unset, ApiImpact]):
        last_modified_date (Union[Unset, str]):
        published_date (Union[Unset, str]):
        vc_configurations (Union[Unset, ApiConfigurations]):
        vc_vulnerable_cp_es (Union[Unset, list[str]]):
    """

    configurations: Union[Unset, "ApiConfigurations"] = UNSET
    cve: Union[Unset, "ApiCVE"] = UNSET
    impact: Union[Unset, "ApiImpact"] = UNSET
    last_modified_date: Union[Unset, str] = UNSET
    published_date: Union[Unset, str] = UNSET
    vc_configurations: Union[Unset, "ApiConfigurations"] = UNSET
    vc_vulnerable_cp_es: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configurations: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.configurations, Unset):
            configurations = self.configurations.to_dict()

        cve: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve.to_dict()

        impact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.impact, Unset):
            impact = self.impact.to_dict()

        last_modified_date = self.last_modified_date

        published_date = self.published_date

        vc_configurations: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vc_configurations, Unset):
            vc_configurations = self.vc_configurations.to_dict()

        vc_vulnerable_cp_es: Union[Unset, list[str]] = UNSET
        if not isinstance(self.vc_vulnerable_cp_es, Unset):
            vc_vulnerable_cp_es = self.vc_vulnerable_cp_es

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configurations is not UNSET:
            field_dict["configurations"] = configurations
        if cve is not UNSET:
            field_dict["cve"] = cve
        if impact is not UNSET:
            field_dict["impact"] = impact
        if last_modified_date is not UNSET:
            field_dict["lastModifiedDate"] = last_modified_date
        if published_date is not UNSET:
            field_dict["publishedDate"] = published_date
        if vc_configurations is not UNSET:
            field_dict["vcConfigurations"] = vc_configurations
        if vc_vulnerable_cp_es is not UNSET:
            field_dict["vcVulnerableCPEs"] = vc_vulnerable_cp_es

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_configurations import ApiConfigurations
        from ..models.api_cve import ApiCVE
        from ..models.api_impact import ApiImpact

        d = dict(src_dict)
        _configurations = d.pop("configurations", UNSET)
        configurations: Union[Unset, ApiConfigurations]
        if isinstance(_configurations, Unset):
            configurations = UNSET
        else:
            configurations = ApiConfigurations.from_dict(_configurations)

        _cve = d.pop("cve", UNSET)
        cve: Union[Unset, ApiCVE]
        if isinstance(_cve, Unset):
            cve = UNSET
        else:
            cve = ApiCVE.from_dict(_cve)

        _impact = d.pop("impact", UNSET)
        impact: Union[Unset, ApiImpact]
        if isinstance(_impact, Unset):
            impact = UNSET
        else:
            impact = ApiImpact.from_dict(_impact)

        last_modified_date = d.pop("lastModifiedDate", UNSET)

        published_date = d.pop("publishedDate", UNSET)

        _vc_configurations = d.pop("vcConfigurations", UNSET)
        vc_configurations: Union[Unset, ApiConfigurations]
        if isinstance(_vc_configurations, Unset):
            vc_configurations = UNSET
        else:
            vc_configurations = ApiConfigurations.from_dict(_vc_configurations)

        vc_vulnerable_cp_es = cast(list[str], d.pop("vcVulnerableCPEs", UNSET))

        api_cve_items = cls(
            configurations=configurations,
            cve=cve,
            impact=impact,
            last_modified_date=last_modified_date,
            published_date=published_date,
            vc_configurations=vc_configurations,
            vc_vulnerable_cp_es=vc_vulnerable_cp_es,
        )

        api_cve_items.additional_properties = d
        return api_cve_items

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

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_sigma_rule_rule import AdvisorySigmaRuleRule


T = TypeVar("T", bound="AdvisorySigmaRule")


@_attrs_define
class AdvisorySigmaRule:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        mitre_attack_techniques (Union[Unset, list[str]]):
        sigma_rule (Union[Unset, AdvisorySigmaRuleRule]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    mitre_attack_techniques: Union[Unset, list[str]] = UNSET
    sigma_rule: Union[Unset, "AdvisorySigmaRuleRule"] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        mitre_attack_techniques: Union[Unset, list[str]] = UNSET
        if not isinstance(self.mitre_attack_techniques, Unset):
            mitre_attack_techniques = self.mitre_attack_techniques

        sigma_rule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sigma_rule, Unset):
            sigma_rule = self.sigma_rule.to_dict()

        summary = self.summary

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if mitre_attack_techniques is not UNSET:
            field_dict["mitre_attack_techniques"] = mitre_attack_techniques
        if sigma_rule is not UNSET:
            field_dict["sigma_rule"] = sigma_rule
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_sigma_rule_rule import AdvisorySigmaRuleRule

        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        mitre_attack_techniques = cast(list[str], d.pop("mitre_attack_techniques", UNSET))

        _sigma_rule = d.pop("sigma_rule", UNSET)
        sigma_rule: Union[Unset, AdvisorySigmaRuleRule]
        if isinstance(_sigma_rule, Unset):
            sigma_rule = UNSET
        else:
            sigma_rule = AdvisorySigmaRuleRule.from_dict(_sigma_rule)

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_sigma_rule = cls(
            cve=cve,
            date_added=date_added,
            mitre_attack_techniques=mitre_attack_techniques,
            sigma_rule=sigma_rule,
            summary=summary,
            title=title,
            url=url,
        )

        advisory_sigma_rule.additional_properties = d
        return advisory_sigma_rule

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

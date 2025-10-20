from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_nvd20_cvss_data_v2 import ApiNVD20CvssDataV2


T = TypeVar("T", bound="ApiNVD20CvssMetricV2")


@_attrs_define
class ApiNVD20CvssMetricV2:
    """
    Attributes:
        ac_insuf_info (Union[Unset, bool]):
        base_severity (Union[Unset, str]):
        cvss_data (Union[Unset, ApiNVD20CvssDataV2]):
        exploitability_score (Union[Unset, float]):
        impact_score (Union[Unset, float]):
        obtain_all_privilege (Union[Unset, bool]):
        obtain_other_privilege (Union[Unset, bool]):
        obtain_user_privilege (Union[Unset, bool]):
        source (Union[Unset, str]):
        type_ (Union[Unset, str]):
        user_interaction_required (Union[Unset, bool]):
    """

    ac_insuf_info: Union[Unset, bool] = UNSET
    base_severity: Union[Unset, str] = UNSET
    cvss_data: Union[Unset, "ApiNVD20CvssDataV2"] = UNSET
    exploitability_score: Union[Unset, float] = UNSET
    impact_score: Union[Unset, float] = UNSET
    obtain_all_privilege: Union[Unset, bool] = UNSET
    obtain_other_privilege: Union[Unset, bool] = UNSET
    obtain_user_privilege: Union[Unset, bool] = UNSET
    source: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    user_interaction_required: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ac_insuf_info = self.ac_insuf_info

        base_severity = self.base_severity

        cvss_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cvss_data, Unset):
            cvss_data = self.cvss_data.to_dict()

        exploitability_score = self.exploitability_score

        impact_score = self.impact_score

        obtain_all_privilege = self.obtain_all_privilege

        obtain_other_privilege = self.obtain_other_privilege

        obtain_user_privilege = self.obtain_user_privilege

        source = self.source

        type_ = self.type_

        user_interaction_required = self.user_interaction_required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ac_insuf_info is not UNSET:
            field_dict["acInsufInfo"] = ac_insuf_info
        if base_severity is not UNSET:
            field_dict["baseSeverity"] = base_severity
        if cvss_data is not UNSET:
            field_dict["cvssData"] = cvss_data
        if exploitability_score is not UNSET:
            field_dict["exploitabilityScore"] = exploitability_score
        if impact_score is not UNSET:
            field_dict["impactScore"] = impact_score
        if obtain_all_privilege is not UNSET:
            field_dict["obtainAllPrivilege"] = obtain_all_privilege
        if obtain_other_privilege is not UNSET:
            field_dict["obtainOtherPrivilege"] = obtain_other_privilege
        if obtain_user_privilege is not UNSET:
            field_dict["obtainUserPrivilege"] = obtain_user_privilege
        if source is not UNSET:
            field_dict["source"] = source
        if type_ is not UNSET:
            field_dict["type"] = type_
        if user_interaction_required is not UNSET:
            field_dict["userInteractionRequired"] = user_interaction_required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_nvd20_cvss_data_v2 import ApiNVD20CvssDataV2

        d = dict(src_dict)
        ac_insuf_info = d.pop("acInsufInfo", UNSET)

        base_severity = d.pop("baseSeverity", UNSET)

        _cvss_data = d.pop("cvssData", UNSET)
        cvss_data: Union[Unset, ApiNVD20CvssDataV2]
        if isinstance(_cvss_data, Unset):
            cvss_data = UNSET
        else:
            cvss_data = ApiNVD20CvssDataV2.from_dict(_cvss_data)

        exploitability_score = d.pop("exploitabilityScore", UNSET)

        impact_score = d.pop("impactScore", UNSET)

        obtain_all_privilege = d.pop("obtainAllPrivilege", UNSET)

        obtain_other_privilege = d.pop("obtainOtherPrivilege", UNSET)

        obtain_user_privilege = d.pop("obtainUserPrivilege", UNSET)

        source = d.pop("source", UNSET)

        type_ = d.pop("type", UNSET)

        user_interaction_required = d.pop("userInteractionRequired", UNSET)

        api_nvd20_cvss_metric_v2 = cls(
            ac_insuf_info=ac_insuf_info,
            base_severity=base_severity,
            cvss_data=cvss_data,
            exploitability_score=exploitability_score,
            impact_score=impact_score,
            obtain_all_privilege=obtain_all_privilege,
            obtain_other_privilege=obtain_other_privilege,
            obtain_user_privilege=obtain_user_privilege,
            source=source,
            type_=type_,
            user_interaction_required=user_interaction_required,
        )

        api_nvd20_cvss_metric_v2.additional_properties = d
        return api_nvd20_cvss_metric_v2

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

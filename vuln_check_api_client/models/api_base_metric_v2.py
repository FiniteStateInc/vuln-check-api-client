from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_cvssv2 import ApiCVSSV2


T = TypeVar("T", bound="ApiBaseMetricV2")


@_attrs_define
class ApiBaseMetricV2:
    """
    Attributes:
        ac_insuf_info (Union[Unset, bool]):
        cvss_v2 (Union[Unset, ApiCVSSV2]):
        exploitability_score (Union[Unset, float]):
        impact_score (Union[Unset, float]):
        obtain_all_privilege (Union[Unset, bool]):
        obtain_other_privilege (Union[Unset, bool]):
        obtain_user_privilege (Union[Unset, bool]):
        severity (Union[Unset, str]):
        user_interaction_required (Union[Unset, bool]):
    """

    ac_insuf_info: Union[Unset, bool] = UNSET
    cvss_v2: Union[Unset, "ApiCVSSV2"] = UNSET
    exploitability_score: Union[Unset, float] = UNSET
    impact_score: Union[Unset, float] = UNSET
    obtain_all_privilege: Union[Unset, bool] = UNSET
    obtain_other_privilege: Union[Unset, bool] = UNSET
    obtain_user_privilege: Union[Unset, bool] = UNSET
    severity: Union[Unset, str] = UNSET
    user_interaction_required: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ac_insuf_info = self.ac_insuf_info

        cvss_v2: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cvss_v2, Unset):
            cvss_v2 = self.cvss_v2.to_dict()

        exploitability_score = self.exploitability_score

        impact_score = self.impact_score

        obtain_all_privilege = self.obtain_all_privilege

        obtain_other_privilege = self.obtain_other_privilege

        obtain_user_privilege = self.obtain_user_privilege

        severity = self.severity

        user_interaction_required = self.user_interaction_required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ac_insuf_info is not UNSET:
            field_dict["acInsufInfo"] = ac_insuf_info
        if cvss_v2 is not UNSET:
            field_dict["cvssV2"] = cvss_v2
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
        if severity is not UNSET:
            field_dict["severity"] = severity
        if user_interaction_required is not UNSET:
            field_dict["userInteractionRequired"] = user_interaction_required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_cvssv2 import ApiCVSSV2

        d = dict(src_dict)
        ac_insuf_info = d.pop("acInsufInfo", UNSET)

        _cvss_v2 = d.pop("cvssV2", UNSET)
        cvss_v2: Union[Unset, ApiCVSSV2]
        if isinstance(_cvss_v2, Unset):
            cvss_v2 = UNSET
        else:
            cvss_v2 = ApiCVSSV2.from_dict(_cvss_v2)

        exploitability_score = d.pop("exploitabilityScore", UNSET)

        impact_score = d.pop("impactScore", UNSET)

        obtain_all_privilege = d.pop("obtainAllPrivilege", UNSET)

        obtain_other_privilege = d.pop("obtainOtherPrivilege", UNSET)

        obtain_user_privilege = d.pop("obtainUserPrivilege", UNSET)

        severity = d.pop("severity", UNSET)

        user_interaction_required = d.pop("userInteractionRequired", UNSET)

        api_base_metric_v2 = cls(
            ac_insuf_info=ac_insuf_info,
            cvss_v2=cvss_v2,
            exploitability_score=exploitability_score,
            impact_score=impact_score,
            obtain_all_privilege=obtain_all_privilege,
            obtain_other_privilege=obtain_other_privilege,
            obtain_user_privilege=obtain_user_privilege,
            severity=severity,
            user_interaction_required=user_interaction_required,
        )

        api_base_metric_v2.additional_properties = d
        return api_base_metric_v2

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

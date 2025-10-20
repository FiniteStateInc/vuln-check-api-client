from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_initial_access_artifact import ApiInitialAccessArtifact


T = TypeVar("T", bound="ApiInitialAccess")


@_attrs_define
class ApiInitialAccess:
    """
    Attributes:
        artifacts (Union[Unset, list['ApiInitialAccessArtifact']]): Artifacts holds the set of available artifacts for
            this vulnerability, such as exploit, shodan queries, PCAP traces, and others.
        cve (Union[Unset, str]): CVE identifier for the given initial access record.
        in_kev (Union[Unset, bool]): InKEV is true if this artifact is in CISA's Known Exploited Vulnerabilities (KEV)
            data set; otherwise, false.
        in_vckev (Union[Unset, bool]): InVCKEV is true if this artifact is in VulnCheck's Known Exploited
            Vulnerabilities (VCKEV) data set; otherwise, false.
        vulnerable_cpes (Union[Unset, list[str]]): VulnerableCPEs is the list of vulnerable CPE strings associated with
            this CVE and artifact(s).
    """

    artifacts: Union[Unset, list["ApiInitialAccessArtifact"]] = UNSET
    cve: Union[Unset, str] = UNSET
    in_kev: Union[Unset, bool] = UNSET
    in_vckev: Union[Unset, bool] = UNSET
    vulnerable_cpes: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        artifacts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.artifacts, Unset):
            artifacts = []
            for artifacts_item_data in self.artifacts:
                artifacts_item = artifacts_item_data.to_dict()
                artifacts.append(artifacts_item)

        cve = self.cve

        in_kev = self.in_kev

        in_vckev = self.in_vckev

        vulnerable_cpes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.vulnerable_cpes, Unset):
            vulnerable_cpes = self.vulnerable_cpes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if artifacts is not UNSET:
            field_dict["artifacts"] = artifacts
        if cve is not UNSET:
            field_dict["cve"] = cve
        if in_kev is not UNSET:
            field_dict["inKEV"] = in_kev
        if in_vckev is not UNSET:
            field_dict["inVCKEV"] = in_vckev
        if vulnerable_cpes is not UNSET:
            field_dict["vulnerable_cpes"] = vulnerable_cpes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_initial_access_artifact import ApiInitialAccessArtifact

        d = dict(src_dict)
        artifacts = []
        _artifacts = d.pop("artifacts", UNSET)
        for artifacts_item_data in _artifacts or []:
            artifacts_item = ApiInitialAccessArtifact.from_dict(artifacts_item_data)

            artifacts.append(artifacts_item)

        cve = d.pop("cve", UNSET)

        in_kev = d.pop("inKEV", UNSET)

        in_vckev = d.pop("inVCKEV", UNSET)

        vulnerable_cpes = cast(list[str], d.pop("vulnerable_cpes", UNSET))

        api_initial_access = cls(
            artifacts=artifacts,
            cve=cve,
            in_kev=in_kev,
            in_vckev=in_vckev,
            vulnerable_cpes=vulnerable_cpes,
        )

        api_initial_access.additional_properties = d
        return api_initial_access

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

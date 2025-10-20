from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_oss_package_vulnerability import ApiOSSPackageVulnerability


T = TypeVar("T", bound="V3ControllersPurlResponseData")


@_attrs_define
class V3ControllersPurlResponseData:
    """
    Attributes:
        cves (Union[Unset, list[str]]): list of associated CVE 's
        vulnerabilities (Union[Unset, list['ApiOSSPackageVulnerability']]): list of associated vulnerabilities
    """

    cves: Union[Unset, list[str]] = UNSET
    vulnerabilities: Union[Unset, list["ApiOSSPackageVulnerability"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cves: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cves, Unset):
            cves = self.cves

        vulnerabilities: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vulnerabilities, Unset):
            vulnerabilities = []
            for vulnerabilities_item_data in self.vulnerabilities:
                vulnerabilities_item = vulnerabilities_item_data.to_dict()
                vulnerabilities.append(vulnerabilities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cves is not UNSET:
            field_dict["cves"] = cves
        if vulnerabilities is not UNSET:
            field_dict["vulnerabilities"] = vulnerabilities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_oss_package_vulnerability import ApiOSSPackageVulnerability

        d = dict(src_dict)
        cves = cast(list[str], d.pop("cves", UNSET))

        vulnerabilities = []
        _vulnerabilities = d.pop("vulnerabilities", UNSET)
        for vulnerabilities_item_data in _vulnerabilities or []:
            vulnerabilities_item = ApiOSSPackageVulnerability.from_dict(vulnerabilities_item_data)

            vulnerabilities.append(vulnerabilities_item)

        v3_controllers_purl_response_data = cls(
            cves=cves,
            vulnerabilities=vulnerabilities,
        )

        v3_controllers_purl_response_data.additional_properties = d
        return v3_controllers_purl_response_data

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

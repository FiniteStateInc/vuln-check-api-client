from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_award import AdvisoryAward
    from ..models.advisory_curl_cwe import AdvisoryCurlCWE


T = TypeVar("T", bound="AdvisoryDBSpecific")


@_attrs_define
class AdvisoryDBSpecific:
    """
    Attributes:
        cwe (Union[Unset, AdvisoryCurlCWE]):
        award (Union[Unset, AdvisoryAward]):
        last_affected (Union[Unset, str]):
        package (Union[Unset, str]):
        severity (Union[Unset, str]):
        url (Union[Unset, str]):
        www (Union[Unset, str]):
    """

    cwe: Union[Unset, "AdvisoryCurlCWE"] = UNSET
    award: Union[Unset, "AdvisoryAward"] = UNSET
    last_affected: Union[Unset, str] = UNSET
    package: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    www: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cwe: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cwe, Unset):
            cwe = self.cwe.to_dict()

        award: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.award, Unset):
            award = self.award.to_dict()

        last_affected = self.last_affected

        package = self.package

        severity = self.severity

        url = self.url

        www = self.www

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cwe is not UNSET:
            field_dict["CWE"] = cwe
        if award is not UNSET:
            field_dict["award"] = award
        if last_affected is not UNSET:
            field_dict["last_affected"] = last_affected
        if package is not UNSET:
            field_dict["package"] = package
        if severity is not UNSET:
            field_dict["severity"] = severity
        if url is not UNSET:
            field_dict["url"] = url
        if www is not UNSET:
            field_dict["www"] = www

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_award import AdvisoryAward
        from ..models.advisory_curl_cwe import AdvisoryCurlCWE

        d = dict(src_dict)
        _cwe = d.pop("CWE", UNSET)
        cwe: Union[Unset, AdvisoryCurlCWE]
        if isinstance(_cwe, Unset):
            cwe = UNSET
        else:
            cwe = AdvisoryCurlCWE.from_dict(_cwe)

        _award = d.pop("award", UNSET)
        award: Union[Unset, AdvisoryAward]
        if isinstance(_award, Unset):
            award = UNSET
        else:
            award = AdvisoryAward.from_dict(_award)

        last_affected = d.pop("last_affected", UNSET)

        package = d.pop("package", UNSET)

        severity = d.pop("severity", UNSET)

        url = d.pop("url", UNSET)

        www = d.pop("www", UNSET)

        advisory_db_specific = cls(
            cwe=cwe,
            award=award,
            last_affected=last_affected,
            package=package,
            severity=severity,
            url=url,
            www=www,
        )

        advisory_db_specific.additional_properties = d
        return advisory_db_specific

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

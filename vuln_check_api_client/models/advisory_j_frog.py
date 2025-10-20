from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_nvd20cvecpe_match import AdvisoryNVD20CVECPEMatch


T = TypeVar("T", bound="AdvisoryJFrog")


@_attrs_define
class AdvisoryJFrog:
    """
    Attributes:
        cpes (Union[Unset, list['AdvisoryNVD20CVECPEMatch']]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        product (Union[Unset, str]):
        severity (Union[Unset, str]):
        summary (Union[Unset, str]):
        url (Union[Unset, str]):
        versions (Union[Unset, list[str]]):
    """

    cpes: Union[Unset, list["AdvisoryNVD20CVECPEMatch"]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    product: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    versions: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cpes, Unset):
            cpes = []
            for cpes_item_data in self.cpes:
                cpes_item = cpes_item_data.to_dict()
                cpes.append(cpes_item)

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        product = self.product

        severity = self.severity

        summary = self.summary

        url = self.url

        versions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.versions, Unset):
            versions = self.versions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpes is not UNSET:
            field_dict["cpes"] = cpes
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if product is not UNSET:
            field_dict["product"] = product
        if severity is not UNSET:
            field_dict["severity"] = severity
        if summary is not UNSET:
            field_dict["summary"] = summary
        if url is not UNSET:
            field_dict["url"] = url
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_nvd20cvecpe_match import AdvisoryNVD20CVECPEMatch

        d = dict(src_dict)
        cpes = []
        _cpes = d.pop("cpes", UNSET)
        for cpes_item_data in _cpes or []:
            cpes_item = AdvisoryNVD20CVECPEMatch.from_dict(cpes_item_data)

            cpes.append(cpes_item)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        product = d.pop("product", UNSET)

        severity = d.pop("severity", UNSET)

        summary = d.pop("summary", UNSET)

        url = d.pop("url", UNSET)

        versions = cast(list[str], d.pop("versions", UNSET))

        advisory_j_frog = cls(
            cpes=cpes,
            cve=cve,
            date_added=date_added,
            product=product,
            severity=severity,
            summary=summary,
            url=url,
            versions=versions,
        )

        advisory_j_frog.additional_properties = d
        return advisory_j_frog

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

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_affected_ubuntu_package import AdvisoryAffectedUbuntuPackage


T = TypeVar("T", bound="AdvisoryUbuntuCVE")


@_attrs_define
class AdvisoryUbuntuCVE:
    """
    Attributes:
        affected_packages (Union[Unset, list['AdvisoryAffectedUbuntuPackage']]):
        cve (Union[Unset, list[str]]): Candidate
        date_added (Union[Unset, str]): PublicDate
        reference_urls (Union[Unset, list[str]]): References
        source_url (Union[Unset, str]):
        status (Union[Unset, str]): active || retired
        ubuntu_url (Union[Unset, str]):
        usn (Union[Unset, list[str]]):
    """

    affected_packages: Union[Unset, list["AdvisoryAffectedUbuntuPackage"]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    reference_urls: Union[Unset, list[str]] = UNSET
    source_url: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    ubuntu_url: Union[Unset, str] = UNSET
    usn: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_packages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.affected_packages, Unset):
            affected_packages = []
            for affected_packages_item_data in self.affected_packages:
                affected_packages_item = affected_packages_item_data.to_dict()
                affected_packages.append(affected_packages_item)

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        reference_urls: Union[Unset, list[str]] = UNSET
        if not isinstance(self.reference_urls, Unset):
            reference_urls = self.reference_urls

        source_url = self.source_url

        status = self.status

        ubuntu_url = self.ubuntu_url

        usn: Union[Unset, list[str]] = UNSET
        if not isinstance(self.usn, Unset):
            usn = self.usn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_packages is not UNSET:
            field_dict["affected_packages"] = affected_packages
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if reference_urls is not UNSET:
            field_dict["reference_urls"] = reference_urls
        if source_url is not UNSET:
            field_dict["source_url"] = source_url
        if status is not UNSET:
            field_dict["status"] = status
        if ubuntu_url is not UNSET:
            field_dict["ubuntu_url"] = ubuntu_url
        if usn is not UNSET:
            field_dict["usn"] = usn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_affected_ubuntu_package import AdvisoryAffectedUbuntuPackage

        d = dict(src_dict)
        affected_packages = []
        _affected_packages = d.pop("affected_packages", UNSET)
        for affected_packages_item_data in _affected_packages or []:
            affected_packages_item = AdvisoryAffectedUbuntuPackage.from_dict(affected_packages_item_data)

            affected_packages.append(affected_packages_item)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        reference_urls = cast(list[str], d.pop("reference_urls", UNSET))

        source_url = d.pop("source_url", UNSET)

        status = d.pop("status", UNSET)

        ubuntu_url = d.pop("ubuntu_url", UNSET)

        usn = cast(list[str], d.pop("usn", UNSET))

        advisory_ubuntu_cve = cls(
            affected_packages=affected_packages,
            cve=cve,
            date_added=date_added,
            reference_urls=reference_urls,
            source_url=source_url,
            status=status,
            ubuntu_url=ubuntu_url,
            usn=usn,
        )

        advisory_ubuntu_cve.additional_properties = d
        return advisory_ubuntu_cve

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

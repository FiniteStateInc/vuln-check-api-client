from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_affected_debian_package import AdvisoryAffectedDebianPackage


T = TypeVar("T", bound="AdvisoryDebianSecurityAdvisory")


@_attrs_define
class AdvisoryDebianSecurityAdvisory:
    """
    Attributes:
        affected_packages (Union[Unset, list['AdvisoryAffectedDebianPackage']]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        dsa (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    affected_packages: Union[Unset, list["AdvisoryAffectedDebianPackage"]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    dsa: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
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

        dsa = self.dsa

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_packages is not UNSET:
            field_dict["affected_packages"] = affected_packages
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if dsa is not UNSET:
            field_dict["dsa"] = dsa
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_affected_debian_package import AdvisoryAffectedDebianPackage

        d = dict(src_dict)
        affected_packages = []
        _affected_packages = d.pop("affected_packages", UNSET)
        for affected_packages_item_data in _affected_packages or []:
            affected_packages_item = AdvisoryAffectedDebianPackage.from_dict(affected_packages_item_data)

            affected_packages.append(affected_packages_item)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        dsa = d.pop("dsa", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_debian_security_advisory = cls(
            affected_packages=affected_packages,
            cve=cve,
            date_added=date_added,
            dsa=dsa,
            title=title,
            url=url,
        )

        advisory_debian_security_advisory.additional_properties = d
        return advisory_debian_security_advisory

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

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_affected_debian_release import AdvisoryAffectedDebianRelease


T = TypeVar("T", bound="AdvisoryDebianCVE")


@_attrs_define
class AdvisoryDebianCVE:
    """
    Attributes:
        cve (Union[Unset, str]):
        debianbug (Union[Unset, int]):
        description (Union[Unset, str]):
        releases (Union[Unset, list['AdvisoryAffectedDebianRelease']]):
        scope (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, str] = UNSET
    debianbug: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    releases: Union[Unset, list["AdvisoryAffectedDebianRelease"]] = UNSET
    scope: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve = self.cve

        debianbug = self.debianbug

        description = self.description

        releases: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.releases, Unset):
            releases = []
            for releases_item_data in self.releases:
                releases_item = releases_item_data.to_dict()
                releases.append(releases_item)

        scope = self.scope

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if debianbug is not UNSET:
            field_dict["debianbug"] = debianbug
        if description is not UNSET:
            field_dict["description"] = description
        if releases is not UNSET:
            field_dict["releases"] = releases
        if scope is not UNSET:
            field_dict["scope"] = scope
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_affected_debian_release import AdvisoryAffectedDebianRelease

        d = dict(src_dict)
        cve = d.pop("cve", UNSET)

        debianbug = d.pop("debianbug", UNSET)

        description = d.pop("description", UNSET)

        releases = []
        _releases = d.pop("releases", UNSET)
        for releases_item_data in _releases or []:
            releases_item = AdvisoryAffectedDebianRelease.from_dict(releases_item_data)

            releases.append(releases_item)

        scope = d.pop("scope", UNSET)

        url = d.pop("url", UNSET)

        advisory_debian_cve = cls(
            cve=cve,
            debianbug=debianbug,
            description=description,
            releases=releases,
            scope=scope,
            url=url,
        )

        advisory_debian_cve.additional_properties = d
        return advisory_debian_cve

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

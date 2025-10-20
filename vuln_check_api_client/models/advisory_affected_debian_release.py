from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_affected_debian_repository import AdvisoryAffectedDebianRepository


T = TypeVar("T", bound="AdvisoryAffectedDebianRelease")


@_attrs_define
class AdvisoryAffectedDebianRelease:
    """
    Attributes:
        fixed_version (Union[Unset, str]):
        nodsa (Union[Unset, str]):
        nodsa_reason (Union[Unset, str]):
        release_name (Union[Unset, str]):
        repositories (Union[Unset, list['AdvisoryAffectedDebianRepository']]):
        status (Union[Unset, str]):
        urgency (Union[Unset, str]):
    """

    fixed_version: Union[Unset, str] = UNSET
    nodsa: Union[Unset, str] = UNSET
    nodsa_reason: Union[Unset, str] = UNSET
    release_name: Union[Unset, str] = UNSET
    repositories: Union[Unset, list["AdvisoryAffectedDebianRepository"]] = UNSET
    status: Union[Unset, str] = UNSET
    urgency: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fixed_version = self.fixed_version

        nodsa = self.nodsa

        nodsa_reason = self.nodsa_reason

        release_name = self.release_name

        repositories: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.repositories, Unset):
            repositories = []
            for repositories_item_data in self.repositories:
                repositories_item = repositories_item_data.to_dict()
                repositories.append(repositories_item)

        status = self.status

        urgency = self.urgency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fixed_version is not UNSET:
            field_dict["fixed_version"] = fixed_version
        if nodsa is not UNSET:
            field_dict["nodsa"] = nodsa
        if nodsa_reason is not UNSET:
            field_dict["nodsa_reason"] = nodsa_reason
        if release_name is not UNSET:
            field_dict["release_name"] = release_name
        if repositories is not UNSET:
            field_dict["repositories"] = repositories
        if status is not UNSET:
            field_dict["status"] = status
        if urgency is not UNSET:
            field_dict["urgency"] = urgency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_affected_debian_repository import AdvisoryAffectedDebianRepository

        d = dict(src_dict)
        fixed_version = d.pop("fixed_version", UNSET)

        nodsa = d.pop("nodsa", UNSET)

        nodsa_reason = d.pop("nodsa_reason", UNSET)

        release_name = d.pop("release_name", UNSET)

        repositories = []
        _repositories = d.pop("repositories", UNSET)
        for repositories_item_data in _repositories or []:
            repositories_item = AdvisoryAffectedDebianRepository.from_dict(repositories_item_data)

            repositories.append(repositories_item)

        status = d.pop("status", UNSET)

        urgency = d.pop("urgency", UNSET)

        advisory_affected_debian_release = cls(
            fixed_version=fixed_version,
            nodsa=nodsa,
            nodsa_reason=nodsa_reason,
            release_name=release_name,
            repositories=repositories,
            status=status,
            urgency=urgency,
        )

        advisory_affected_debian_release.additional_properties = d
        return advisory_affected_debian_release

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

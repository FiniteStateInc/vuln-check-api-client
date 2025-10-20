from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_centos_package import AdvisoryCentosPackage


T = TypeVar("T", bound="AdvisoryCESA")


@_attrs_define
class AdvisoryCESA:
    """
    Attributes:
        arch (Union[Unset, list[str]]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        id (Union[Unset, str]):
        issue_date (Union[Unset, str]):
        os_release (Union[Unset, str]):
        packages (Union[Unset, list['AdvisoryCentosPackage']]):
        references (Union[Unset, list[str]]):
        title (Union[Unset, str]):
    """

    arch: Union[Unset, list[str]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    issue_date: Union[Unset, str] = UNSET
    os_release: Union[Unset, str] = UNSET
    packages: Union[Unset, list["AdvisoryCentosPackage"]] = UNSET
    references: Union[Unset, list[str]] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arch: Union[Unset, list[str]] = UNSET
        if not isinstance(self.arch, Unset):
            arch = self.arch

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        id = self.id

        issue_date = self.issue_date

        os_release = self.os_release

        packages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.packages, Unset):
            packages = []
            for packages_item_data in self.packages:
                packages_item = packages_item_data.to_dict()
                packages.append(packages_item)

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arch is not UNSET:
            field_dict["arch"] = arch
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if id is not UNSET:
            field_dict["id"] = id
        if issue_date is not UNSET:
            field_dict["issueDate"] = issue_date
        if os_release is not UNSET:
            field_dict["osRelease"] = os_release
        if packages is not UNSET:
            field_dict["packages"] = packages
        if references is not UNSET:
            field_dict["references"] = references
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_centos_package import AdvisoryCentosPackage

        d = dict(src_dict)
        arch = cast(list[str], d.pop("arch", UNSET))

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        id = d.pop("id", UNSET)

        issue_date = d.pop("issueDate", UNSET)

        os_release = d.pop("osRelease", UNSET)

        packages = []
        _packages = d.pop("packages", UNSET)
        for packages_item_data in _packages or []:
            packages_item = AdvisoryCentosPackage.from_dict(packages_item_data)

            packages.append(packages_item)

        references = cast(list[str], d.pop("references", UNSET))

        title = d.pop("title", UNSET)

        advisory_cesa = cls(
            arch=arch,
            cve=cve,
            date_added=date_added,
            id=id,
            issue_date=issue_date,
            os_release=os_release,
            packages=packages,
            references=references,
            title=title,
        )

        advisory_cesa.additional_properties = d
        return advisory_cesa

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

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_advisory_details import AdvisoryAdvisoryDetails
    from ..models.advisory_oval_reference import AdvisoryOvalReference
    from ..models.advisory_vuln_check_package import AdvisoryVulnCheckPackage


T = TypeVar("T", bound="AdvisoryMetaData")


@_attrs_define
class AdvisoryMetaData:
    """
    Attributes:
        advisory (Union[Unset, AdvisoryAdvisoryDetails]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        packages (Union[Unset, list['AdvisoryVulnCheckPackage']]):
        references (Union[Unset, list['AdvisoryOvalReference']]):
        title (Union[Unset, str]):
    """

    advisory: Union[Unset, "AdvisoryAdvisoryDetails"] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    packages: Union[Unset, list["AdvisoryVulnCheckPackage"]] = UNSET
    references: Union[Unset, list["AdvisoryOvalReference"]] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advisory: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.advisory, Unset):
            advisory = self.advisory.to_dict()

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        description = self.description

        packages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.packages, Unset):
            packages = []
            for packages_item_data in self.packages:
                packages_item = packages_item_data.to_dict()
                packages.append(packages_item)

        references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advisory is not UNSET:
            field_dict["advisory"] = advisory
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if packages is not UNSET:
            field_dict["packages"] = packages
        if references is not UNSET:
            field_dict["references"] = references
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_advisory_details import AdvisoryAdvisoryDetails
        from ..models.advisory_oval_reference import AdvisoryOvalReference
        from ..models.advisory_vuln_check_package import AdvisoryVulnCheckPackage

        d = dict(src_dict)
        _advisory = d.pop("advisory", UNSET)
        advisory: Union[Unset, AdvisoryAdvisoryDetails]
        if isinstance(_advisory, Unset):
            advisory = UNSET
        else:
            advisory = AdvisoryAdvisoryDetails.from_dict(_advisory)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        packages = []
        _packages = d.pop("packages", UNSET)
        for packages_item_data in _packages or []:
            packages_item = AdvisoryVulnCheckPackage.from_dict(packages_item_data)

            packages.append(packages_item)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = AdvisoryOvalReference.from_dict(references_item_data)

            references.append(references_item)

        title = d.pop("title", UNSET)

        advisory_meta_data = cls(
            advisory=advisory,
            cve=cve,
            date_added=date_added,
            description=description,
            packages=packages,
            references=references,
            title=title,
        )

        advisory_meta_data.additional_properties = d
        return advisory_meta_data

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

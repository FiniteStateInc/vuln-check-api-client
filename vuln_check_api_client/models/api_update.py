from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_date_time import ApiDateTime
    from ..models.api_package import ApiPackage
    from ..models.api_reference import ApiReference


T = TypeVar("T", bound="ApiUpdate")


@_attrs_define
class ApiUpdate:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        id (Union[Unset, str]): sort // key
        issued (Union[Unset, ApiDateTime]):
        os_arch (Union[Unset, str]):
        os_version (Union[Unset, str]):
        packages (Union[Unset, list['ApiPackage']]):
        references (Union[Unset, list['ApiReference']]):
        severity (Union[Unset, str]):
        title (Union[Unset, str]):
        type_ (Union[Unset, str]):
        updated (Union[Unset, ApiDateTime]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    issued: Union[Unset, "ApiDateTime"] = UNSET
    os_arch: Union[Unset, str] = UNSET
    os_version: Union[Unset, str] = UNSET
    packages: Union[Unset, list["ApiPackage"]] = UNSET
    references: Union[Unset, list["ApiReference"]] = UNSET
    severity: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    updated: Union[Unset, "ApiDateTime"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        description = self.description

        id = self.id

        issued: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.issued, Unset):
            issued = self.issued.to_dict()

        os_arch = self.os_arch

        os_version = self.os_version

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

        severity = self.severity

        title = self.title

        type_ = self.type_

        updated: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if issued is not UNSET:
            field_dict["issued"] = issued
        if os_arch is not UNSET:
            field_dict["os_arch"] = os_arch
        if os_version is not UNSET:
            field_dict["os_version"] = os_version
        if packages is not UNSET:
            field_dict["packages"] = packages
        if references is not UNSET:
            field_dict["references"] = references
        if severity is not UNSET:
            field_dict["severity"] = severity
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_date_time import ApiDateTime
        from ..models.api_package import ApiPackage
        from ..models.api_reference import ApiReference

        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        _issued = d.pop("issued", UNSET)
        issued: Union[Unset, ApiDateTime]
        if isinstance(_issued, Unset):
            issued = UNSET
        else:
            issued = ApiDateTime.from_dict(_issued)

        os_arch = d.pop("os_arch", UNSET)

        os_version = d.pop("os_version", UNSET)

        packages = []
        _packages = d.pop("packages", UNSET)
        for packages_item_data in _packages or []:
            packages_item = ApiPackage.from_dict(packages_item_data)

            packages.append(packages_item)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = ApiReference.from_dict(references_item_data)

            references.append(references_item)

        severity = d.pop("severity", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, ApiDateTime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = ApiDateTime.from_dict(_updated)

        api_update = cls(
            cve=cve,
            date_added=date_added,
            description=description,
            id=id,
            issued=issued,
            os_arch=os_arch,
            os_version=os_version,
            packages=packages,
            references=references,
            severity=severity,
            title=title,
            type_=type_,
            updated=updated,
        )

        api_update.additional_properties = d
        return api_update

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

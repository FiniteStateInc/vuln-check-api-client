from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_alma_date import AdvisoryAlmaDate
    from ..models.advisory_alma_object_id import AdvisoryAlmaObjectID
    from ..models.advisory_alma_package_list import AdvisoryAlmaPackageList
    from ..models.advisory_alma_reference import AdvisoryAlmaReference


T = TypeVar("T", bound="AdvisoryAlmaLinuxUpdate")


@_attrs_define
class AdvisoryAlmaLinuxUpdate:
    """
    Attributes:
        bs_repo_id (Union[Unset, AdvisoryAlmaObjectID]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        fromstr (Union[Unset, str]):
        id (Union[Unset, AdvisoryAlmaObjectID]):
        issued_date (Union[Unset, AdvisoryAlmaDate]):
        pkglist (Union[Unset, AdvisoryAlmaPackageList]):
        pushcount (Union[Unset, str]):
        references (Union[Unset, list['AdvisoryAlmaReference']]):
        release (Union[Unset, str]):
        rights (Union[Unset, str]):
        severity (Union[Unset, str]):
        solution (Union[Unset, str]):
        status (Union[Unset, str]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
        type_ (Union[Unset, str]):
        update_url (Union[Unset, str]):
        updated_date (Union[Unset, AdvisoryAlmaDate]):
        updateinfo_id (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    bs_repo_id: Union[Unset, "AdvisoryAlmaObjectID"] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    fromstr: Union[Unset, str] = UNSET
    id: Union[Unset, "AdvisoryAlmaObjectID"] = UNSET
    issued_date: Union[Unset, "AdvisoryAlmaDate"] = UNSET
    pkglist: Union[Unset, "AdvisoryAlmaPackageList"] = UNSET
    pushcount: Union[Unset, str] = UNSET
    references: Union[Unset, list["AdvisoryAlmaReference"]] = UNSET
    release: Union[Unset, str] = UNSET
    rights: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    solution: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    update_url: Union[Unset, str] = UNSET
    updated_date: Union[Unset, "AdvisoryAlmaDate"] = UNSET
    updateinfo_id: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bs_repo_id: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bs_repo_id, Unset):
            bs_repo_id = self.bs_repo_id.to_dict()

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        description = self.description

        fromstr = self.fromstr

        id: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        issued_date: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.issued_date, Unset):
            issued_date = self.issued_date.to_dict()

        pkglist: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pkglist, Unset):
            pkglist = self.pkglist.to_dict()

        pushcount = self.pushcount

        references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        release = self.release

        rights = self.rights

        severity = self.severity

        solution = self.solution

        status = self.status

        summary = self.summary

        title = self.title

        type_ = self.type_

        update_url = self.update_url

        updated_date: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.updated_date, Unset):
            updated_date = self.updated_date.to_dict()

        updateinfo_id = self.updateinfo_id

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bs_repo_id is not UNSET:
            field_dict["bs_repo_id"] = bs_repo_id
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if fromstr is not UNSET:
            field_dict["fromstr"] = fromstr
        if id is not UNSET:
            field_dict["id"] = id
        if issued_date is not UNSET:
            field_dict["issued_date"] = issued_date
        if pkglist is not UNSET:
            field_dict["pkglist"] = pkglist
        if pushcount is not UNSET:
            field_dict["pushcount"] = pushcount
        if references is not UNSET:
            field_dict["references"] = references
        if release is not UNSET:
            field_dict["release"] = release
        if rights is not UNSET:
            field_dict["rights"] = rights
        if severity is not UNSET:
            field_dict["severity"] = severity
        if solution is not UNSET:
            field_dict["solution"] = solution
        if status is not UNSET:
            field_dict["status"] = status
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if update_url is not UNSET:
            field_dict["update_url"] = update_url
        if updated_date is not UNSET:
            field_dict["updated_date"] = updated_date
        if updateinfo_id is not UNSET:
            field_dict["updateinfo_id"] = updateinfo_id
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_alma_date import AdvisoryAlmaDate
        from ..models.advisory_alma_object_id import AdvisoryAlmaObjectID
        from ..models.advisory_alma_package_list import AdvisoryAlmaPackageList
        from ..models.advisory_alma_reference import AdvisoryAlmaReference

        d = dict(src_dict)
        _bs_repo_id = d.pop("bs_repo_id", UNSET)
        bs_repo_id: Union[Unset, AdvisoryAlmaObjectID]
        if isinstance(_bs_repo_id, Unset):
            bs_repo_id = UNSET
        else:
            bs_repo_id = AdvisoryAlmaObjectID.from_dict(_bs_repo_id)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        fromstr = d.pop("fromstr", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, AdvisoryAlmaObjectID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = AdvisoryAlmaObjectID.from_dict(_id)

        _issued_date = d.pop("issued_date", UNSET)
        issued_date: Union[Unset, AdvisoryAlmaDate]
        if isinstance(_issued_date, Unset):
            issued_date = UNSET
        else:
            issued_date = AdvisoryAlmaDate.from_dict(_issued_date)

        _pkglist = d.pop("pkglist", UNSET)
        pkglist: Union[Unset, AdvisoryAlmaPackageList]
        if isinstance(_pkglist, Unset):
            pkglist = UNSET
        else:
            pkglist = AdvisoryAlmaPackageList.from_dict(_pkglist)

        pushcount = d.pop("pushcount", UNSET)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = AdvisoryAlmaReference.from_dict(references_item_data)

            references.append(references_item)

        release = d.pop("release", UNSET)

        rights = d.pop("rights", UNSET)

        severity = d.pop("severity", UNSET)

        solution = d.pop("solution", UNSET)

        status = d.pop("status", UNSET)

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        update_url = d.pop("update_url", UNSET)

        _updated_date = d.pop("updated_date", UNSET)
        updated_date: Union[Unset, AdvisoryAlmaDate]
        if isinstance(_updated_date, Unset):
            updated_date = UNSET
        else:
            updated_date = AdvisoryAlmaDate.from_dict(_updated_date)

        updateinfo_id = d.pop("updateinfo_id", UNSET)

        version = d.pop("version", UNSET)

        advisory_alma_linux_update = cls(
            bs_repo_id=bs_repo_id,
            cve=cve,
            date_added=date_added,
            description=description,
            fromstr=fromstr,
            id=id,
            issued_date=issued_date,
            pkglist=pkglist,
            pushcount=pushcount,
            references=references,
            release=release,
            rights=rights,
            severity=severity,
            solution=solution,
            status=status,
            summary=summary,
            title=title,
            type_=type_,
            update_url=update_url,
            updated_date=updated_date,
            updateinfo_id=updateinfo_id,
            version=version,
        )

        advisory_alma_linux_update.additional_properties = d
        return advisory_alma_linux_update

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
